# -*- coding:utf8 -*-
#!/usr/bin/python2.7
import os

class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        self.path = '/home/xiaozhen/data/VOCdevkit/helmet_all/test/JPEGImages/'
	#self.path = '/home/chris/VOCdevkit/VOC2007/resize/'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0

        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
        	str1=str(i)
                dst = os.path.join(os.path.abspath(self.path), str1.zfill(5) + '.jpg')
                try:
                    os.rename(src, dst)
                    print 'converting %s to %s ...' % (src, dst)
                    i = i + 1
                except:
                    continue
        print 'total %d to rename & converted %d jpgs' % (total_num, i)

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
