import os 
from TF_Transfer_Learning.TF_Transfer_Learning import *

def install():
	os.system('cd TF_Transfer_Learning && virtualenv venv-TFTL')
	os.system('. venv-TFTL/bin/activate')
	os.system('pip install -r requirements.txt')
	os.system('deactivate && cd ..')

	os.system('cd LLFF && virtualenv -p /usr/bin/python2.7 venv-LLFF')
	os.system('. venv-LLFF/bin/activate')
	os.system('pip install -r requirements.txt')
	os.system('deactivate && cd ..')

	os.system('cd nerf && virtualenv venv-nerf')
	os.system('. venv-nerf/bin/activate')
	os.system('pip install -r requirements.txt')
	os.system('deactivate && cd ..')

def nerf(scene_folder):
	os.system('. nerf/venv-nerf/bin/activate')
	poses = llff_poses(scenedir)
	# probably want to have documentation on what a valid scene_folder is
	os.system('deactivate')
	return '3d model? video? many things?'

def pole_classifier_train(training_images_folder):
	os.system('. TF_Transfer_Learning/venv-TFTL/bin/activate')
	transfer_learning(training_images_folder)
	os.system('deactivate')
	return 'trained model'

def pole_classifier_classify(path_to_image_file, model=None):
	os.system('. TF_Transfer_Learning/venv-TFTL/bin/activate')
	image_classifier(path_to_image_file)
	os.system('deactivate')
	return 'classification score(s)'

def llff_poses(scenedir_path):
	os.system('. LLFF/venv-LLFF/bin/activate')
	os.system('python2 LLFF/imgs2poses.py ' + scenedir_path)
	os.system('deactivate')
	return "scenedir/poses_bounds.npy"

def llff_spiral_render():
	llff_poses('./LLFF/scenedir')
	os.system('. LLFF/venv-LLFF/bin/activate') 
	os.system('python2 LLFF/imgs2mpis.py LLFF/scenedir LLFF/scenedir/mpis --height 360')
	os.system('python2 LLFF/imgs2renderpath.py LLFF/scenedir LLFF/scenedir/spiral_path.txt --spiral')
	os.system('python2 LLFF/mpis2video.py LLFF/scenedir/mpis LLFF/scenedir/spiral_path.txt LLFF/scenedir/spiral_render.mp4 --crop_factor 0.8')
	os.system('deactivate')
	return 'LLFF/scenedir/spiral_render.mp4'

# install()
# pole_classifier_classify('TF_Transfer_Learning/image0.jpg')
# pole_classifier_train('../poles_photos')
# llff_poses('./LLFF/scenedir')
# llff_spiral_render()