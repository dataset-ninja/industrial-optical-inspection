**Weakly Supervised Learning for Industrial Optical Inspection** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the industrial and computer aided quality control domains. 

The dataset consists of 16100 images with 2120 labeled objects belonging to 1 single class (*defect*).

Images in the Industrial Optical Inspection dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 14000 (87% of the total) unlabeled images (i.e. without annotations). There are 20 splits in the dataset: *Class1-Train* (575 images), *Class1-Test* (575 images), *Class3-Train* (575 images), *Class4-Test* (575 images), *Class2-Train* (575 images), *Class3-Test* (575 images), *Class5-Train* (575 images), *Class7-Test* (1150 images), *Class8-Test* (1150 images), *Class9-Train* (1150 images), *Class9-Test* (1150 images), *Class5-Test* (575 images), *Class2-Test* (575 images), *Class4-Train* (575 images), *Class6-Test* (575 images), *Class6-Train* (575 images), *Class7-Train* (1150 images), *Class8-Train* (1150 images), *Class10-Test* (1150 images), and *Class10-Train* (1150 images)The dataset was released in 2007 by the Bosch Research, Germany.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/industrial-optical-inspection/raw/main/visualizations/horizontal_grid.webm)
