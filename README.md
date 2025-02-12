# Dewarping Document Image
Dewarping Document Image By Displacement Flow Estimation with Fully Convolutional Network.

Please browse 90_paper.pdf




# Dewarping Process
![image](https://github.com/gwxie/Dewarping-Document-Image-By-Displacement-Flow-Estimation/blob/main/rectitify_image.jpg)
We predict the displacement and the categories (foreground or background) at pixellevel by applying two tasks in FCN, and then remove the background of the input
image, and mapped the foreground pixels to rectified image by interpolation according to the predicted displacements. The cracks maybe emerge in rectified image when using a forward mapping interpolation. Therefore, we construct Delaunay triangulations in all scattered pixels and then using interpolation.

# Compare
![image](https://github.com/gwxie/Dewarping-Document-Image-By-Displacement-Flow-Estimation/blob/main/compare.jpg)

# Notice
- 2020.11.10 update the result file, including 6-25_11_52_54-49-rgb_ and 6-25_11_52_54-49_.

- 2022.2.17 update the Release Code.

- 2022.4.14 update Source file.

# Release Code
The source code is open, please download from Source. 

Please send an email to xieguowang2018@ia.ac.cn.

# Dataset
The training dataset can be synthesised using the [scripts](https://github.com/phonhay103/DFE/tree/main/Distorted-Image-With-Flow).

