# neural_imaging

An image classifier and a 3D image reconstructor for drone imagery of utility poles. Utilizes [Transfer learning with TensorFlow Hub](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/transfer_learning_with_hub.ipynb#scrollTo=PWUmcKKjtwXL) by The TensorFlow Authors, [Neural Radiance Fields](https://github.com/bmild/nerf) developed by UC Berkeley/Google Research/UC San Diego, and [Local Light Field Fusion](https://github.com/Fyusion/LLFF) developed by UC Berkeley/Fyusion Inc/Texas A&M/UC San Diego. 

# Description

The image classifier was sourced from Transfer learning with TensorFlow Hub and uses pretrained models from TensorFlow Hub. The model was then fine-tuned through transfer learning to recognize utility poles. Instructions on how to use original imagery are below. 
3D reconstruction uses LLFF to generate poses to be used by NERF, which constructs a 3D representation. LLFF also outputs videos to illustrate its stitching capability and 3D field rendering capacity. NeRF can be found in Google Colab. 

# Installation

Transfer learning with TensorFlow Hub requires Python 3 and TensorFlow 2 (the full list of requirements are in requirements.txt under the TF_Transfer_Learning subdirectory of this repository). 
The LLFF subdirectory, on the other hand, requires Python 2 and TensorFlow 1 (requirements.txt in the LLFF subdirectory). A virtual environment is suggested for the unique requirements of the subdirectory.
NeRF requires GPU support to process 3D models in a timely manner (see Colab). The Google Colab requires a command line argument (analogous to config_fern.txt in the Colab example) that specicifies a data directory containing image data, poses, and focal data. 
Images to be 3D reconstructed within the LLFF subdirectory at a maximum view of 180 degrees should be taken in a grid format (see LLFF instructions on GitHub). For 360 degree 3D reconstruction, refer to the NeRF instructions on GitHub. NeRF outputs object geometry and a 3D rendering of the object. 

# File Import 

For image classification: entrypoints.py requires a path to a single image as a string argument to the pole_classifier_classify() function. For entire directories of images to be run through the classifier as training data, save the images under unique class names in subdirectories under one directory and feed the path as a string argument to the pole_classifier_train() function. This can be done directly in entrypoints.py. 
Images to be processed with the LLFF repository must be saved in a new directory in the LLFF subdirectory named scenedir in a folder within called images. Ensure that these images are saved as JPEG files. 
After calculating poses for a directory of images (scenedir) using LLFF, the directory may be uploaded to Google Colab to be reconstructed using NeRF. First, edit the config_fern.txt file to correspond accurately with original data. 

# Instructions For Use

Call the pole_classifer_classify() function of entrypoints.py, which calls TF_Transfer_Learning/TF_Transfer_Learning.py, with the path to an image to classify that image on an untrained image classifier. To train the image classifer on a batch of photos, call the pole_classifier_train() function in entrypoints.py, which takes the path to a directory of images as an argument and also calls TF_Transfer_Learning/TF_Transfer_Learning.py. 
