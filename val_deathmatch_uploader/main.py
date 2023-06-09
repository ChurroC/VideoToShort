import glob
import os
import moviepy.editor as mp
import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

folder_path = "../clips"
for file in os.scandir(folder_path):
    print(file.name)

if __name__ == "__mains__":
    print("Hello World!")
    list_of_files = glob.glob(folder_path)
    print(list_of_files)
    if len(list_of_files) == 0:
        print("Could not find files")
        quit()
    latest_file = max(list_of_files, key=os.path.getctime)

    clip = mp.VideoFileClip(latest_file)
    print(clip.duration)
    for i in range(int(clip.duration / 60) + 1):
        print(i)
        clip1 = clip.cut(i * 60, (i + 1) * 60)
        clip1.ipython_display(width=360)
