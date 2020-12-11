import os 

# print('test')

def nerf(scene_folder):
	# code goes here
	# probably want to have documentation on what a valid scene_folder is
	return '3d model? video? many things?'

def pole_classifier_train(training_images_folder):
	# code goes here
	return 'trained model'

def pole_classifier_classify(path_to_image_file, model=None):
	# code goes here
	return 'classification score(s)'

def llff_poses(scenedir)
	os.system(python LLFF/imgs2poses.py scenedir)
	os.system(python imgs2mpis.py scenedir scenedir/mpis --height 360)
	os.system(python imgs2renderpath.py scenedir scenedir/spiral_path.txt --spiral)
	os.system(python mpis2video.py scenedir/mpis scenedir/spiral_path.txt scenedir/spiral_render.mp4 --crop_factor 0.8)
	return 'LLFF/scenedir/spiral_render.mp4'