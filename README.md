# neural_imaging

An image classifier and a 3D image reconstructor for drone imagery of utility poles. Utilizes [Transfer learning with TensorFlow Hub](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/transfer_learning_with_hub.ipynb#scrollTo=PWUmcKKjtwXL) by The TensorFlow Authors, [Neural Radiance Fields](https://github.com/bmild/nerf) developed by UC Berkeley/Google Research/UC San Diego, and [Local Light Field Fusion](https://github.com/Fyusion/LLFF) developed by UC Berkeley/Fyusion Inc/Texas A&M/UC San Diego. 

# Description

The image classifier was sourced from Transfer learning with TensorFlow Hub and uses pretrained models from TensorFlow Hub. The model was then fine-tuned through transfer learning to recognize utility poles. Instructions on how to use original imagery are below. 
3D reconstruction uses LLFF to generate poses to be used by NERF, which constructs a 3D representation. LLFF also outputs videos to illustrate its stitching capability and 3D field rendering capacity. NeRF requires a GPU to run and can be found in Google Colab. 

# Installation

Transfer learning with TensorFlow Hub requires Python 3 and TensorFlow 2 (the full list of requirements are in requirements.txt under the TF_Transfer_Learning subdirectory of this repository). 
The LLFF subdirectory, on the other hand, requires Python 2 and TensorFlow 1 (requirements.txt in the LLFF subdirectory). A virtual environment is suggested for the unique requirements of the subdirectory.
NeRF requires GPU support to process 3D models in a timely manner (see Colab). The Google Colab requires an input file (analogous to tiny_nerf_data.npz in the Colab example) that contains image data, poses, and focal data. An original .npz file can be outputted for use in Colab by doing _____ . 
Images to be 3D reconstructed within the LLFF subdirectory at a maximum view of 180 degrees should be taken in a grid format (see LLFF instructions on GitHub). For 360 degree 3D reconstruction, refer to the NeRF instructions on GitHub. Output geometry can be found in the NeRF repository under ___ after the model is successfully reconstructed. 

# File Import 

For image classification: the initial image to be classified should be in a directory called “image_identifier” within the neural_imaging repository and all images to be tested should be called “image0” starting with 0 and counting upwards by whole positive integers. For entire directories of images to be run through the classifier, save the directory as a tarfile and in the neural_imaging repository. Adjust the code accordingly to the name of the directory of images on line 179 in TF_Transfer_Learn/TF_Transfer_Learning.py. 
Images to be processed with the LLFF repository must be saved in a new directory in the neural_imaging repository named scenedir in a folder within called images. Ensure that these images are saved as JPEG files. 
The directory of images to be 3D reconstructed with NeRF should be ______ and the .npz file containing image/pose/focal information that can be easily imported in the Colab will be outputted for use _____ . 

# Instructions For Use

Once images are properly stored in a image_identifier directory using proper nomenclature (see above), run the pole_classifer_classify function of entrypoints.py, which is connected to TF_Transfer_Learning/TF_Transfer_Learning.py. To train the image classifer on a batch of photos, run the pole_classifier_train function in entrypoints.py, which takes the path to a directory of images as an argument and is also connected to TF_Transfer_Learning/TF_Transfer_Learning.py. 
