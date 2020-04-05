from pytube import YouTube
from bs4 import BeautifulSoup as bs
import requests
import os
import random
import csv
from itertools import chain
import pandas
import pytube
import time
from ftplib import FTP 
from pathlib import Path
import ffmpeg
import subprocess
import os
import os.path  
import re


## set working directory 
os.chdir("C:/Users/wooki/Desktop/videopython/list")

#read data
import pandas
colnames = ['title', 'keywords', 'url']
data = pandas.read_csv('channel_videos.csv', names=colnames)

#function to covert video using ffmpeg
def convert_video(video_input, video_output):
    cmds = ['ffmpeg', '-i', video_input, video_output, 'shell=True']
    os.system(cmds)

#start the iteration
for i, row in data.iterrows():
    try:
        #If video of the url is dead, skip to next
        item1 = data['url'][i]
        item = str(item1)
        yt = YouTube(item)

        #download
        stream = yt.streams.first()
        down = stream.download("C:/Users/wooki/Desktop/videopython/videos_new")
        stream.download("C:/Users/wooki/Desktop/videopython/videos_new")
        
        #ready to convert
        first_file=os.listdir("C:/Users/wooki/Desktop/videopython/videos_new")[0]
        new_filename = Path(first_file).stem + ".mp4"

        #convert and remove original video
        convert_video(first_file,new_filename)
        os.chdir("C:/Users/wooki/Desktop/videopython/videos_new")
        os.remove(first_file)
        
        #clean file name to prevent errors
        name_1 =str(first_file)
        name=re.sub('[^.A-Za-z0-9]+', ' ', name_1)
        os.chdir("C:/Users/wooki/Desktop/videopython/videos_new")
        conv_first_file=os.listdir("C:/Users/wooki/Desktop/videopython/videos_new")[0]
        
        #upload video
        ftp = FTP('ftp.box.com')  
        ftp.login('hyunwoolim@wustl.edu', 'Qq1047921!') 
        ftp.cwd("Videos_master/videos")

        with open(conv_first_file, 'rb') as f:  
            ftp.storbinary('STOR %s' % name, f)
        ftp.quit()
        
        #delete video in local drive
        os.chdir("C:/Users/wooki/Desktop/videopython/videos_new")
        delete_file = os.listdir("C:/Users/wooki/Desktop/videopython/videos_new")[0]
        os.remove(delete_file)

        try:
            #if the video does not offer captions, skip to next
            yt.captions.all()
            caption = yt.captions.get_by_language_code('en')
            text=caption.generate_srt_captions()
            os.chdir("C:/Users/wooki/Desktop/videopython/captions")

            #save the caption as text file
            file_name= name +".txt"
            text_file = open(file_name, "w")
            text_file.write(text)
            text_file.close()

            #upload caption
            os.chdir("C:/Users/wooki/Desktop/videopython/captions")
            cap=os.listdir("C:/Users/wooki/Desktop/videopython/captions")[0]

            #clean file name to prevent errors
            capname_1 =str(cap)
            capname=re.sub('[^.A-Za-z0-9]+', ' ', capname_1)
            
            ftp = FTP('ftp.box.com')  
            ftp.login('hyunwoolim@wustl.edu', 'Qq1047921!') 
            ftp.cwd("Videos_master/captions")

            with open(cap,'rb') as t:
                ftp.storbinary('STOR %s' % capname, t)
            ftp.quit()

            #delete the caption in local drive
            os.chdir("C:/Users/wooki/Desktop/videopython/captions")
            delete_cap = os.listdir("C:/Users/wooki/Desktop/videopython/captions")[0]
            os.remove(delete_cap)
        except:
            pass

        #time sleep for next item
        time.sleep(5)
    except:
        pass