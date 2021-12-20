# Distorted-Image-With-Flow

- Synthesized images have same height and width (i.e., 1024 x 960). Moreover, our ground-truth flow has three channels. For the first two channels, we define the displacement (∆x, ∆y) at pixel-level which indicate how far each pixel have to move to reach its position in the undistorted image as the rectified Ground-truth. For the last channel, we represent the foreground or background by using the categories (1 or 0) at pixel-level.
- Run `python perturbed_images_generation_multiProcess.py --path=./scan/new/ --bg_path=./background/ --output_path=./output/`


# OTHER
For more information, please enter [url](https://github.com/gwxie/Dewarping-Document-Image-By-Displacement-Flow-Estimation).

Sorry for the late reply.
