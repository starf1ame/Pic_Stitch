# Pic_Stitch —— A generator for Panoramic image

## 1. Introduction

&emsp;&emsp;With the increasing popularity of cameras and mobile phones, more and more people are recording and shooting what they see in daily life. However, the scope of any shooting equipment is limited. It may only cover one corner or one side, which is difficult to meet people's needs for panorama. 

&emsp;&emsp;In this project, pic-stitch, a panoramic image splicing software, was designed. The algorithm was written in python, opencv was adopted to implement the algorithm, and pyqt was used to realize the interface. Users could select local images as input for splicing in a friendly interface, and the software would generate spliced panoramic images and save them to the local location.

## 2. Features

* Use PyQt-5 to design a user-friendly interface, which is easy to use and looks nice;
* Use SIFT and SURF algorithm to match feature point;
* Set several modes for different cases of using.

## 3. Usage

### 3.1 start with Pic_Stitch

#### Method 1: Run from source code

On terminal: $ python3 start.py

On IDE: just run start.py

#### Method 2: Run exe

Just click run.exe

### 3.2 Use different modes of Pic_Stitch

First, we come to Mainwindow like that:
![image](https://github.com/YZ-WANG/Pic_Stitch/raw/master/image/1.png)

Secondly, we can choose different modes, for example, run 1x2 stitch.Then, we choose target photos with algorithm and run stitching:
![image](https://github.com/YZ-WANG/Pic_Stitch/raw/master/image/2.png)

Fininally, we get the result we want:
![image](https://github.com/YZ-WANG/Pic_Stitch/raw/master/image/3.png)

show more test, like 2x2 stitch:
![image](https://github.com/YZ-WANG/Pic_Stitch/raw/master/image/4.png)
