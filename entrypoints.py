import os 
from TF_Transfer_Learning.TF_Transfer_Learning import *

def install():
	os.system('cd TF_Transfer_Learning && virtualenv venv-TFTL && . venv-TFTL/bin/activate && pip install -r requirements.txt')
	os.system('cd LLFF && virtualenv -p /usr/bin/python2.7 venv-LLFF && . venv-LLFF/bin/activate && pip install -r requirements.txt')
	os.system('cd nerf && virtualenv venv-nerf && . venv-nerf/bin/activate && pip install -r requirements.txt')

def nerf():
	os.system('. nerf/venv-nerf/bin/activate')
	llff_poses(scenedir)
	# 1. Relocate scenedir to nerf/data/nerf_llff_data
	# 2. Duplicate and rename nerf/config_fern.txt
	# 3. Within the above renamed file, rename expname and datadir
	os.system('python run_nerf.py --config nerf/config_fern.txt')
	return 'object geometry and visual representation'

def pole_classifier_train(training_images_folder):
	os.system('. TF_Transfer_Learning/venv-TFTL/bin/activate')
	transfer_learning(training_images_folder)
	return 'trained model'

def pole_classifier_classify(path_to_image_file, model=None):
	os.system('. TF_Transfer_Learning/venv-TFTL/bin/activate')
	image_classifier(path_to_image_file)
	return 'classification score(s)'

def llff_poses(scenedir_path):
	os.system('. LLFF/venv-LLFF/bin/activate && python2 LLFF/imgs2poses.py ' + scenedir_path)
	# os.system('python2 LLFF/imgs2poses.py ' + scenedir_path)
	return 'scenedir/poses_bounds.npy'

def llff_spiral_render():
	llff_poses('./LLFF/scenedir')
	os.system('. LLFF/venv-LLFF/bin/activate && python2 LLFF/imgs2mpis.py LLFF/scenedir LLFF/scenedir/mpis --height 360 && python2 LLFF/imgs2renderpath.py LLFF/scenedir LLFF/scenedir/spiral_path.txt --spiral && python2 LLFF/mpis2video.py LLFF/scenedir/mpis LLFF/scenedir/spiral_path.txt LLFF/scenedir/spiral_render.mp4 --crop_factor 0.8') 
	# os.system('python2 LLFF/imgs2mpis.py LLFF/scenedir LLFF/scenedir/mpis --height 360')
	# os.system('python2 LLFF/imgs2renderpath.py LLFF/scenedir LLFF/scenedir/spiral_path.txt --spiral')
	# os.system('python2 LLFF/mpis2video.py LLFF/scenedir/mpis LLFF/scenedir/spiral_path.txt LLFF/scenedir/spiral_render.mp4 --crop_factor 0.8')
	return 'LLFF/scenedir/spiral_render.mp4'

# install()
# nerf()
# pole_classifier_classify('TF_Transfer_Learning/image0.jpg')
# pole_classifier_train('../poles_photos')
# llff_poses('./LLFF/scenedir')
# llff_spiral_render()