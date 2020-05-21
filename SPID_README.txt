1. Create Anaconda (tested on Anaconda 4.7.12) environment (called tf_mobilenet) with the packages listed in anaconda_packages.txt

2. To prepare the dataset, run the Mobilenet_spid.ipynb notebook. The paths are set as follows:

	DATASET_PATH ="/PATH_TO_DATASET/SPID/Train" # Train folder contains the train data set00 to set04. set05 is not included as it contains only pedestrian with no background
    DATASET_PATH2 ="/PATH_TO_DATASET/SPID/Test" # Test folder contains set06 to set10
    GT_PATH = "/PATH_TO_DATASET/SPID/Train_GT/" # Train_GT folder contains train annotations folder
    GT_PATH2 = "/PATH_TO_DATASET/SPID/Test_GT/" # Test_GT folder contains test annotations folder

    Some images without annotations are not included in the final data set. The acceptable images are stored in images/train and images/test.

3. run python xml_to_csv.py  # this creates 2 csv files in dat folder.

4. run protoc models-spid/research/object_detection/protos/*.proto --python_out=.  

5. run export PYTHONPATH=$PYTHONPATH:'/PATH_TO/models-spid/research':'/PATH_TO/models-spid/research'/slim

6. run sudo /PATH_TO_CONDA/anaconda3/envs/tf_mobilenet/bin/python3 setup.py install # need to give path to python (python 3.7) in env, any other version might give issue

7. run /PATH_TO_CONDA/anaconda3/envs/tf_mobilenet/bin/python3 generate_tfrecord.py --csv_input=dat/train_labels.csv  --output_path=dat/train.record --image_dir=images/train/ # run from appropriate folder

   This creates train data in Tfrecord format

8. run /PATH_TO_CONDA/anaconda3/envs/tf_mobilenet/bin/python3 generate_tfrecord.py --csv_input=dat/test_labels.csv  --output_path=dat/test.record --image_dir=images/test/    # run from appropriate folder 

   This creates test data in Tfrecord format

9. Download ssd_mobilenet_v2_coco from https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

10. Unzip and store ssd_mobilenet_v2_coco_2018_03_29 in /PATH_TO/models-spid/research/object_detection 

11. Also store images into /PATH_TO/models-spid/research/object_detection 

12. Ensure there are the 2 Tfrecord in dat folder in  /PATH_TO/models-spid/research/object_detection

13. run /PATH_TO_CONDA/anaconda3/envs/tf_mobilenet/bin/python3 train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v2_coco.config


14. Checkpoints created in /PATH_TO/models-spid/research/object_detection/training

15.	from terminal run tensorboard --logdir='training'

16.	in browser got to 127.0.0.1:6006
