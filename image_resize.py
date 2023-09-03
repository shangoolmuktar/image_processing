import cv2 
import numpy as np 
import sys
import os
import fnmatch

def sharp(image):
    kernel= np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    new_img= cv2.filter2D(image, -1, kernel)
    cv2.imshow('sharpened', new_img)
    cv2.waitKey(0)
    return image

def blurr(image):
    kernels= [3,5,9,13]
    for idx, k in enumerate(kernels):
        blr_img= cv2.blur(image, ksize=(k,k))
        cv2.imshow(str(k),blr_img)
        cv2.waitKey(0)
    return

def resize(fname, width, height ):
    image=cv2.imread(fname)
    cv2.imshow('org_img', image)
    cv2.waitKey(0)
    org_height, org_width= image.shape[0:2]
    print("Width", org_width)
    print("height", org_height)

    if(org_width>= org_height):
        new_img= cv2.resize(image, (width, height))
    else:
        new_img=cv2.resize(image,(height,width))
    return fname, new_img

listOfFiles= os.listdir('.')
pattern= "*.jpg"
n= len(sys.argv)
if n==3:
    width= int(sys.argv[1])
    height = int(sys.argv[2])
else:
    width= 1280
    height=960
if not os.path.exists('new_folder'):
    os.makedirs('new_folder')

for filename in listOfFiles:
    if fnmatch.fnmatch(filename, pattern):
        filename, new_img= resize(filename, width, height)
        cv2.imwrite("new_folder\\"+ filename, new_img)


#filename, new_img= resize('bird.jpg',600,350)
#cv2.imshow('resized_img', new_img)
#cv2.waitKey(0)
#blurr(new_img)
#image=sharp(new_img)

