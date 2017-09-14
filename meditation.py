#!/bin/python
# -*- coding: utf-8 -*-

#from playsound import playsound
from time import sleep
import optparse
import sys
from os import path, chdir
#from urllib2 import urlopen
from urllib.request import urlopen
from bs4 import BeautifulSoup
from subprocess import call, Popen, PIPE
from threading import Thread
import random 
import os
from pytube import YouTube
parser = optparse.OptionParser()
chdir(path.dirname(path.realpath(__file__)))

parser.add_option("-t", "--timer", dest = "GongoTimer", default = 3, type = 'int', action = 'store', help = 'Define the interval between the gongos {minutes}.')
parser.add_option("-c", "--count", dest = "GongoCount", default = 8, type = 'int', action = 'store', help = 'Define the total number of gongos.')
parser.add_option("-@", "--caos", dest = "Random", default = False, action = "store_true")
parser.add_option("-s", "--silent", dest = "Radio", default= True, action="store_false")


def getRandomVideoAddr():
    URL ='http://www.randomvideogenerator.com/'
    Info = urlopen(URL).read()
    Info = BeautifulSoup(Info, "lxml")
    EmbedUrl = Info.find_all('iframe')[0].attrs['src']
    VideoUrl = EmbedUrl.replace('embed/', 'watch?v=')
    return VideoUrl

def downloadVideo(debug=False, showMusicNames-True, filename='HEIWA_MEDIT'):
    VideoUrl = getRandomVideoAddr()
    if debug:
        print(VideoUrl)
    VIDEO = YouTube(VideoUrl)
    if showMusicNames or debug:
        print(VIDEO.filename)
    VIDEO.set_filename(filename)
    v=VIDEO.get_videos()[0]
    if debug:
        print(v)
    try:        
        os.remove(filename+'.3gp')
        os.remove(filename+'.wav')
    except OSError:
        pass
    v.download('.')
    V = ['ffmpeg', '-i', 'HEIWA_MEDIT.3gp', '-af', "volume=0dB", 'HEIWA_MEDIT.wav']
    call(V, stdout=PIPE, stderr=PIPE)
    sleep(3)

def PlaySound(filename):
    C = ['play', filename]
    C = Popen(C, stdout=PIPE, stderr=PIPE)
    return C

    
# TODO: ADD RANDOM TIMER;
(options, args) = parser.parse_args()

gong = 'gong_hit.wav'
endgong = 'gong_hitjr.wav'

HEIWA = '''


   ▄█    █▄       ▄████████  ▄█   ▄█     █▄     ▄████████ 
  ███    ███     ███    ███ ███  ███     ███   ███    ███ 
  ███    ███     ███    █▀  ███▌ ███     ███   ███    ███ 
 ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███▌ ███     ███   ███    ███ 
▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███▌ ███     ███ ▀███████████ 
  ███    ███     ███    █▄  ███  ███     ███   ███    ███ 
  ███    ███     ███    ███ ███  ███ ▄█▄ ███   ███    ███ 
  ███    █▀      ██████████ █▀    ▀███▀███▀    ███    █▀  
                                                          

'''

print(HEIWA)
if options.Radio:
    downloadVideo()
for GONGO in range(options.GongoCount):
    PlaySound(gong)

    time = 60
    if options.Radio:          
        V = PlaySound('HEIWA_MEDIT.wav')
        nextDownload=Thread(target=downloadVideo, args=())
        nextDownload.start()
        
    if options.Random:
        time = time*random.randrange(5e7 , 15e7)/1e8
        time = int(round(time))
        print(time)

    for TIMER in range(time):
        sys.stdout.write("#")
        sys.stdout.flush()
        sleep(options.GongoTimer)
        
    if options.Radio:
        V.kill()
    print("\n\n")
    
PlaySound(endgong)
sleep(10)
