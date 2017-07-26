#!/bin/python2
#!-*- encoding: utf-8 -*-

from playsound import playsound
from time import sleep
import optparse
import sys
from os import path, chdir
#from urllib.request import urlopen
import random 

parser = optparse.OptionParser()
chdir(path.dirname(path.realpath(__file__)))

parser.add_option("--timer", dest = "GongoTimer", default = 3, type = 'int', action = 'store', help = 'Define the interval between the gongos {minutes}.')
parser.add_option("--count", dest = "GongoCount", default = 8, type = 'int', action = 'store', help = 'Define the total number of gongos.')
parser.add_option("--caos", dest = "Random", default = False, action = "store_true")

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
for GONGO in range(options.GongoCount):
    playsound(gong)

    time = 60
    #q=urlopen('http://random-ize.com/random-youtube/').read()

    if options.Random:
        time = time*random.randrange(5e7 , 15e7)/1e8
        time = int(round(time))
        print(time)

    for TIMER in range(time):
        sys.stdout.write("#")
        sys.stdout.flush()
        sleep(options.GongoTimer)
            
    print("\n\n")
playsound(endgong)
