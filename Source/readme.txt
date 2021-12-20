# Train
python train.py --data_path_train=./dataset/train/data1024_greyV2/color/ --data_path_validate=./dataset/train/data1024_greyV2/color/ --data_path_test=./dataset/train/data1024_greyV2/png/ --batch_size=1

# Test
python test.py --data_path_test=./dataset/test/images_padded/ --resume="./flat/2021-10-27/2021-10-27 20_18_47 @2021-10-26/100/2021-10-26@2021-10-27 20_18_47Dewarping-Document-Image-By-Displacement-Flow-Estimation-v5.pkl"