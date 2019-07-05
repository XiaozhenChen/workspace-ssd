
"""

在conda tensorflow 虚拟环境下
直接运行 python3 本文件
可以使用一张图片进行增广

下一步： 复制本文件
        确认在人像 数据集的增广方式， 参数，多10张 还是？
        初始实验， 增广后， 总图片数保持在 100 张
        然后开始训练
下一步： voc数据集制作

下一步： SSD 参数设置
"""
import os
from keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img

datagen=ImageDataGenerator(
      rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      rescale=1./255,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

'''
img=load_img('./test.jpg')
x=img_to_array(img)
x=x.reshape((1,)+x.shape)

i=0
for batch in datagen.flow(x,batch_size=1,
                         save_to_dir='1/clear',save_prefix='cucumber',save_format='jpg'):
    i+=1
    if i>10:
       break

'''

images_src_path  = os.path.join(os.path.abspath('.'), 'images_src')  # read jpg images dir


#videos_src_path = r'./mov'#提取图片的视频文件夹


#videos_save_path = r'./images'#保存图片的路径

images_save_path = os.path.join(os.path.abspath('.'), 'images_augment') # save augment images to the dir

images = os.listdir(images_src_path)
images = filter(lambda x: x.endswith('jpg'), images)
print(images_src_path)
print(images_save_path)


for image in images:
    
    image_name, _ = image.split('.')
  #  os.mkdir(images_save_path + '/' + image_name)
#    each_image_save_full_path = os.path.join(images_save_path, image_name)
    
    each_image_full_path = os.path.join(images_src_path, image)
    print('Read a new image:' + each_image_full_path)

    img = load_img(each_image_full_path)
    x = img_to_array(img)
    x = x.reshape((1,)+x.shape)

    i = 0
    for batch in datagen.flow(x, batch_size = 1, 
                               save_to_dir = images_save_path, save_prefix = image_name, save_format='jpg'):
        i +=1
        if i>2:
            break
    
