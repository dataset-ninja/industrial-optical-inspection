Dataset **Industrial Optical Inspection** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/s/R/A4/ZsgbrqDqMEBCXK1WhyVpZkDikO1lnos3SyxBi5IZrRBHbk5G1Ct92YXxiVyB5BTazya5cndLaC8oSolUphhYuGZTJfknInlAaToOrVWmNfGQGwQfcUsALrXpXgow.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Industrial Optical Inspection', dst_path='~/dtools/datasets/Industrial Optical Inspection.tar')
```
The data in original format can be 🔗[downloaded here](https://zenodo.org/record/8086136)