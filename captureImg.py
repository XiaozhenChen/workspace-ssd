import cv2
import os




videos_src_path  = os.path.join(os.path.abspath('.'), 'mp4')


#videos_src_path = r'./mov'#提取图片的视频文件夹


#videos_save_path = r'./images'#保存图片的路径

videos_save_path = os.path.join(os.path.abspath('.'), 'images_mp4')



videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith('mp4'), videos)

print(videos_save_path)

 
for each_video in videos:
    frame_count = 1
    # 得到每个文件夹的名字, 并指定每一帧的保存路径
    each_video_name, _ = each_video.split('.')
    os.mkdir(videos_save_path + '/' + each_video_name)
    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'
 
    # 得到完整的视频路径
    each_video_full_path = os.path.join(videos_src_path, each_video)
    # 用OpenCV一帧一帧读取出来
    cap = cv2.VideoCapture(each_video_full_path)
    
    success = True
    while (success):
        success, frame = cap.read()
        print('Read a new frame: ', success)
        params = []
        params.append(1)
        #if len(frame) > 0:
        #if success:
        if frame is not None and frame_count%20==0:#每？帧取一帧图片保存下来，可以自己修改
            cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_count, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            print(frame_count)
        frame_count = frame_count + 1
    cap.release()