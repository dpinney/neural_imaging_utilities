import os 
from TF_Transfer_Learning.TF_Transfer_Learning import *
import argparse

def file_path(string):
	if os.path.isfile(string):
		return string
	else:
		raise FileNotFoundError(string)

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def scenedir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser(description='Pass path to image file')
parser.add_argument('--filepath', type=file_path)
parser.add_argument('--dirpath', type=dir_path)
parser.add_argument('--scenedirpath', type=scenedir_path)
args = parser.parse_args()

def install():
	os.system('cd TF_Transfer_Learning; virtualenv venv-TFTL; . venv-TFTL/bin/activate; pip install -r requirements.txt')
	os.system('cd LLFF; virtualenv -p /usr/bin/python2.7 venv-LLFF; . venv-LLFF/bin/activate; pip install -r requirements.txt')
	os.system('cd nerf; virtualenv venv-nerf; . venv-nerf/bin/activate; pip install -r requirements.txt')

def nerf():
	# 1. call llff_poses(scenedir) according to README.md instructions 
	# 2. Relocate scenedir to nerf/data/nerf_llff_data
	# 3. Duplicate and rename nerf/config_fern.txt
	# 4. Within the above renamed file, rename expname and datadir
	os.system('. nerf/venv-nerf/bin/activate; python3 nerf/run_nerf.py --config nerf/config_fern.txt')
	return 'object geometry and visual representation'

def pole_classifier_train():
	os.system('. TF_Transfer_Learning/venv-TFTL/bin/activate; python3 -c "import TF_Transfer_Learning.TF_Transfer_Learning; TF_Transfer_Learning.TF_Transfer_Learning.transfer_learning(' + repr(str(args.dirpath)) + ')"')
	# transfer_learning(training_images_folder)
	return 'trained model'

def pole_classifier_classify(model=None):
	os.system('. TF_Transfer_Learning/venv-TFTL/bin/activate; python3 -c "import TF_Transfer_Learning.TF_Transfer_Learning; TF_Transfer_Learning.TF_Transfer_Learning.image_classifier(' + repr(str(args.filepath)) + ')"')
	# image_classifier(path_to_image_file)
	return 'classification score(s)'

def llff_poses():
	os.system('. LLFF/venv-LLFF/bin/activate; python2 LLFF/imgs2poses.py ' + args.scenedirpath)
	return 'scenedir/poses_bounds.npy'

def llff_spiral_render():
	llff_poses()
	os.system('. LLFF/venv-LLFF/bin/activate; python2 LLFF/imgs2mpis.py LLFF/scenedir LLFF/scenedir/mpis --height 360; python2 LLFF/imgs2renderpath.py LLFF/scenedir LLFF/scenedir/spiral_path.txt --spiral; python2 LLFF/mpis2video.py LLFF/scenedir/mpis LLFF/scenedir/spiral_path.txt LLFF/scenedir/spiral_render.mp4 --crop_factor 0.8') 
	return 'LLFF/scenedir/spiral_render.mp4'

# install()
# nerf()
# pole_classifier_classify()
# pole_classifier_train()
# llff_poses()
# llff_spiral_render()