from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Industrial Optical Inspection"
PROJECT_NAME_FULL: str = "Weakly Supervised Learning for Industrial Optical Inspection"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Domain.Industrial(),
    Domain.ComputerAidedQualityControl(),
]
CATEGORY: Category = Category.Manufacturing()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2007-09-14"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://zenodo.org/record/8086136"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1698282
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/industrial-optical-inspection"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Class1.zip": "https://zenodo.org/record/8086136/files/Class1.zip?download=1",
    "Class2.zip": "https://zenodo.org/record/8086136/files/Class2.zip?download=1",
    "Class3.zip": "https://zenodo.org/record/8086136/files/Class3.zip?download=1",
    "Class4.zip": "https://zenodo.org/record/8086136/files/Class4.zip?download=1",
    "Class5.zip": "https://zenodo.org/record/8086136/files/Class5.zip?download=1",
    "Class6.zip": "https://zenodo.org/record/8086136/files/Class6.zip?download=1",
    "Class7.zip": "https://zenodo.org/record/8086136/files/Class7.zip?download=1",
    "Class8.zip": "https://zenodo.org/record/8086136/files/Class8.zip?download=1",
    "Class9.zip": "https://zenodo.org/record/8086136/files/Class9.zip?download=1",
    "Class10.zip": "https://zenodo.org/record/8086136/files/Class10.zip?download=1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
PAPER: Optional[Union[str, List[str]]] = None
CITATION_URL: Optional[str] = "https://zenodo.org/record/8086136/export/hx"
AUTHORS: Optional[List[str]] = ["Wieler, Matthias", "Hahn, Tobias", "Hamprecht, Fred A."]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Bosch Research, Germany"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.bosch.com/research/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
