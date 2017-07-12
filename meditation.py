#!/bin/python2
#!-*- encoding: utf8 -*-

from playsound import playsound
from time import sleep
import optparse
import sys
parser = optparse.OptionParser()

parser.add_option("--timer", dest = "GongoTimer", default = 3, type = 'int', action = 'store', help = 'Define the interval between the gongos {minutes}.')
parser.add_option("--count", dest = "GongoCount", default = 8, type = 'int', action = 'store', help = 'Define the total number of gongos.')
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

    for TIMER in range(60):
        sys.stdout.write("#")
        sys.stdout.flush()
        sleep(options.GongoTimer)
            
    print("\n\n")
playsound(endgong)
