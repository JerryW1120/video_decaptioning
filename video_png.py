from __future__ import print_function, division
import os
import sys
from subprocess import call
import pdb

def class_process(dir_path, dst_dir_path, class_name):
  # class_path = os.path.join(dir_path, class_name)
  # if not os.path.isdir(class_path):
  #   return

  dst_class_path = os.path.join(dst_dir_path, class_name)
  if not os.path.exists(dst_class_path):
    os.mkdir(dst_class_path)
  for file_name in os.listdir(dir_path):
    if '.mp4' not in file_name:
      continue
    name, ext = os.path.splitext(file_name)
    dst_directory_path = os.path.join(dst_dir_path, name)

    video_file_path = os.path.join(dir_path, file_name)

    try:
      if os.path.exists(dst_directory_path): 
        if not os.path.exists(os.path.join(dst_directory_path, 'image_00001.png')):
          call('rm -r \"{}\"'.format(dst_directory_path), shell=True)
          print('remove {}'.format(dst_directory_path))
          os.mkdir(dst_directory_path)
        else:
          continue
      else:
        os.mkdir(dst_directory_path)
    except:
      print(dst_directory_path)
      continue
    cmd = 'ffmpeg.exe -i {} -vf scale=128:128 {}\image_%05d.png'.format(video_file_path, dst_directory_path)
    print(cmd)
    # call(cmd, shell=True)
    call(f'ffmpeg.exe -i {video_file_path} -vf scale=128:128 {dst_directory_path}\image_%05d.png')
    print('\n')

if __name__=="__main__":
  dir_path = 'F:\\train\Y'
  dst_dir_path = 'E:\software\\finalshell\\temp\edit\\train_png\Y'

  for class_name in os.listdir(dir_path):
    class_process(dir_path, dst_dir_path, class_name)

  # class_name = 'test'
  # class_process(dir_path, dst_dir_path, class_name)

  # /ssd2/vid_inpaint/Track2/dataset/train/X
  # /ssd2/vid_inpaint/Track2/dataset/train/Y
  # python utils/video_jpg_kinetics.py avi_video_directory jpg_video_directoryls
