# neural_imaging

An image classifier and a 3D image reconstructor for drone imagery of utility poles. Utilizes [Transfer learning with TensorFlow Hub](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/transfer_learning_with_hub.ipynb#scrollTo=PWUmcKKjtwXL) by The TensorFlow Authors, [Neural Radiance Fields](https://github.com/bmild/nerf) developed by UC Berkeley/Google Research/UC San Diego, and [Local Light Field Fusion](https://github.com/Fyusion/LLFF) developed by UC Berkeley/Fyusion Inc/Texas A&M/UC San Diego. 

# Description

The image classifier was sourced from Transfer learning with TensorFlow Hub and uses pretrained models from TensorFlow Hub. The model was then fine-tuned through transfer learning to recognize utility poles. Instructions on how to use original imagery are below. 
3D reconstruction uses LLFF to generate poses to be used by NERF, which constructs a 3D representation. LLFF also outputs videos to illustrate its stitching capability and 3D field rendering capacity. NeRF can be found in Google Colab. 

# Installation

To install virtual environments with the required components of each subdirectory to this repository, call the install() function of entrypoints.py. 
Transfer learning with TensorFlow Hub requires Python 3 and TensorFlow 2 (the full list of requirements are in requirements.txt under the TF_Transfer_Learning subdirectory of this repository). 
The LLFF subdirectory, on the other hand, requires Python 2 and TensorFlow 1 (requirements.txt in the LLFF subdirectory). 
NeRF requires GPU support to process 3D models in a timely manner. run_nerf.py requires a command line argument (analogous to config_fern.txt in the Colab example) that specicifies a data directory containing image data, poses, and focal data. This data is outputted under LLFF/scenedir by calling the llff_poses() function within entrypoints.py. 
Images to be 3D reconstructed within the LLFF subdirectory at a maximum view of 180 degrees should be taken in a grid format (see LLFF instructions on GitHub). For 360 degree 3D reconstruction, refer to the NeRF instructions on GitHub. NeRF outputs object geometry and a 3D rendering of the object. 

# File Import 

For image classification: Run the pole_classifier_classify() function in entrypoints.py, which requires command line arguments --file_path (file path here). To run entire directories of images through the classifier as training data, save the images in unique subdirectories under one directory and include command line arguments --dir_path (directory path here) when running the pole_classifier_train() function of entrypoints.py.  
Images to be processed with the LLFF repository must be saved in a new directory in the LLFF subdirectory named scenedir in a folder within called images. Ensure that these images are saved as JPEG files. To compute poses, call function llff_poses() in entrypoints.py. To output an MP4 of the spiral render, call function llff_spiral_render() in entrypoints.py. Include command line arguments --scenedirpath (scene directory path here) with both commands. 
After calculating poses for a directory of images (scenedir) using LLFF, the directory of images can be reconstructed using  NeRF.

# Instructions For Use

Call the pole_classifer_classify() function of entrypoints.py, which uses TF_Transfer_Learning/TF_Transfer_Learning.py, with the path to an image to classify that image on an untrained image classifier. To train the image classifer on a batch of photos, call the pole_classifier_train() function in entrypoints.py, which takes the path to a directory of images as a command line argument and also uses TF_Transfer_Learning/TF_Transfer_Learning.py. 
To compute poses for a directory of images saved as JPEG files (ex. LLFF/scenedir/images), call llff_poses() in entrypoints.py and include command line arguments (ex. --scenedirpath LLFF/scenedir). To output a spiral render MP4 of the image directory, call llff_spiral_render() in entrypoints.py and include the same command line arguments. 
Call nerf() to run NeRF on a directory of photos pre-processed with LLFF after completing the following steps: First, relocate scenedir to nerf/data/nerf_llff_data. Next, duplicate and rename nerf/config_fern.txt. Within the renamed config file, rename expname and datadir. 

# Single Image Classification Example

$ python3 entrypoints.py --filepath ../images/image1.jpg

# Batch Training and Classification Example

$ python3 entrypoints.py --dirpath ../images/folder1

# LLFF Poses and Spiral Render Example

$ python3 entrypoints.py --scenedir LLFF/scenedir
