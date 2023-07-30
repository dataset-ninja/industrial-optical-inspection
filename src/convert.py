import os
import shutil
from urllib.parse import unquote, urlparse

import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import dir_exists, file_exists, get_file_ext, get_file_name
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(desc=f"Downloading '{file_name_with_ext}' to buffer...", total=fsize) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    dataset_path = "/home/alex/DATASETS/TODO/Industrial Optical Inspection"
    batch_size = 30
    images_ext = ".PNG"
    masks_folder = "Label"
    ann_suffix = "_label"

    def create_ann(image_path):
        labels = []

        image_name = get_file_name(image_path)
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        mask_path = os.path.join(data_path, masks_folder, image_name + ann_suffix + images_ext)
        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
            mask = mask_np == 255
            ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
            for i in range(1, ret):
                obj_mask = curr_mask == i
                curr_bitmap = sly.Bitmap(obj_mask)
                curr_label = sly.Label(curr_bitmap, obj_class)
                labels.append(curr_label)

        tag_meta = subfolder_to_tag[subfolder]
        tag = sly.Tag(meta=tag_meta)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[tag])

    obj_class = sly.ObjClass("defect", sly.Bitmap)

    tag_train = sly.TagMeta("train", sly.TagValueType.NONE)
    tag_test = sly.TagMeta("test", sly.TagValueType.NONE)

    subfolder_to_tag = {"Train": tag_train, "Test": tag_test}

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=[tag_train, tag_test])
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in os.listdir(dataset_path):
        ds_path = os.path.join(dataset_path, ds_name)

        if dir_exists(ds_path):
            dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

            for subfolder in os.listdir(ds_path):
                data_path = os.path.join(ds_path, subfolder)

                images_names = [
                    im_name
                    for im_name in os.listdir(data_path)
                    if get_file_ext(im_name) == images_ext
                ]

                progress = sly.Progress(
                    "Create dataset {}, add {} images".format(ds_name, subfolder), len(images_names)
                )

                for images_names_batch in sly.batched(images_names, batch_size=batch_size):
                    img_pathes_batch = [
                        os.path.join(data_path, image_name) for image_name in images_names_batch
                    ]

                    img_infos = api.image.upload_paths(
                        dataset.id, images_names_batch, img_pathes_batch
                    )
                    img_ids = [im_info.id for im_info in img_infos]

                    anns = [create_ann(image_path) for image_path in img_pathes_batch]
                    api.annotation.upload_anns(img_ids, anns)

                    progress.iters_done_report(len(images_names_batch))

    return project
