# Description
`/models` contains model parameter. Pre-trained models are available [here](https://drive.google.com/file/d/17MtuXcgMqb5HjBRy4tNL9oLkEI5auLUT/view?usp=sharing).

`/dataset` contains dataset. We resized the image into 1024x960 (zooming in or out along the longest side and keeping the aspect ration, then filling zero for padding. )

`dataloader.py` is used to load data. 

`loss.py` is loss functions. 

`network.py` is network structure.

`test.py` is main program for testing.

`train.py` is main program for training.

`utils.py` is post-processing.



# Running
1、Download model parameter and source codes 

2、Resize the input image into 1024x960 (zooming in or out along the longest side and keeping the aspect ration, then filling zero for padding. )  

3、Run `python test.py --data_path_test=<DATA_TEST_PATH>`

# Training
- Please specify the path of the data. Run `python train.py --data_path_train=<DATA_TRAIN_PATH>  --data_path_validate=<DATA_VALID_PATH> --data_path_test=<DATA_TEST_PATH>`

# Dataset
- The training data is 6 dimensions, namely rgb image, pixel displacement and category.
- Synthesized images have same height and width (i.e., 1024 x 960). Moreover, our ground-truth flow has three channels. For the first two channels, we define the displacement (∆x, ∆y) at pixel-level which indicate how far each pixel have to move to reach its position in the undistorted image as the rectified Ground-truth. For the last channel, we represent the foreground or background by using the categories (1 or 0) at pixel-level.
