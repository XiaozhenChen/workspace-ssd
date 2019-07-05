import cv2
import os

fullfilename=[]
# filepath = "/home/chris/darknet/scripts/VOCdevkit/VOC2007/JPEGImages" 
# filepath1 = "/home/chris/darknet/scripts/VOCdevkit/VOC2007/JPEGImages/JPEGImages"
filepath = "/home/chris/darknet/scripts/VOCdevkit/VOC2007/data-aug" 
filepath1 = "/home/chris/darknet/scripts/VOCdevkit/VOC2007/resize"
# filepath = "F:/input_img"                
# filepath1 = "F:/input_img"
for filename in os.listdir(filepath):
    print(filename)
    print(os.path.join(filepath, filename))
    filelist = os.path.join(filepath, filename)
    fullfilename.append(filelist)


i = 1
for imagename in fullfilename:
    img = cv2.imread(imagename)
    img = cv2.resize(img, (416, 416)) 
    resizename = str(i)+'.jpg'      
    isExists = os.path.exists(filepath1)
    if not isExists:
        os.makedirs(filepath1)
        print('mkdir resizename accomploshed')
    savename = filepath1+'/'+resizename
    cv2.imwrite(savename, img)
    print('{} is resized'.format(savename))
    i = i+1
