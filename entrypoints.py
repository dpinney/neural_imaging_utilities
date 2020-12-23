import os 
from TF_Transfer_Learning.TF_Transfer_Learning import *

def nerf(scene_folder):
	poses = llff_poses(scenedir)
	# probably want to have documentation on what a valid scene_folder is
	return '3d model? video? many things?'

def pole_classifier_train(training_images_folder):
	transfer_learning(training_images_folder)
	return 'trained model'

def pole_classifier_classify(path_to_image_file, model=None):
	image_classifier(path_to_image_file)
	return 'classification score(s)'

def llff_poses(scenedir_path):
	os.system('python2 LLFF/imgs2poses.py ' + scenedir_path)
	return "scenedir/poses_bounds.npy"

def llff_spiral_render():
	# llff_poses('./LLFF/scenedir') 
	os.system('python2 LLFF/imgs2mpis.py LLFF/scenedir LLFF/scenedir/mpis --height 360')
	os.system('python2 LLFF/imgs2renderpath.py LLFF/scenedir LLFF/scenedir/spiral_path.txt --spiral')
	os.system('python2 LLFF/mpis2video.py LLFF/scenedir/mpis LLFF/scenedir/spiral_path.txt LLFF/scenedir/spiral_render.mp4 --crop_factor 0.8')
	return 'LLFF/scenedir/spiral_render.mp4'

# pole_classifier_classify('TF_Transfer_Learning/image0.jpg')
# pole_classifier_train('../poles_photos')
# llff_poses('./LLFF/scenedir')
llff_spiral_render()