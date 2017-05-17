import requests
import six
import lxml
from bs4 import BeautifulSoup
import argparse
import json
import os

def get_lyrics_from_url(artist, song):
    '''Looks up song_url, parses page for lyrics and returns the lyrics.'''
    base_url = 'http://www.genius.com/'
    artist = artist
    song = song
    artist = artist.replace(' ', '-')
    song = song.replace(' ', '-')
    song_url = base_url + artist + '-' + song + '-lyrics'
    get_url = requests.get(song_url)
    song_soup = BeautifulSoup(get_url.text, 'lxml')
    soup_lyrics = song_soup.lyrics.text
    for_removal = ['[Verse]', '[Verse 1]', '[verse]', '[Verse 1]', '[verse 1]', '[chorus]', '[Chorus]', '[Intro]', '[intro]', '[outro]', '[Outro]']
    for x in for_removal:
    	if x in soup_lyrics:
    		real_lyrics = soup_lyrics.replace(x, '')
    return real_lyrics

def save_to_file(data, filename):
    with open(filename, 'w') as fp:
        json.dump(data, fp)

# def get_speech_regions(path_to_song):
# 	'''finds speech regions based on ratio between speech band energy and total energy.
#         Output is array of window numbers and speech flags (1 - speech, 0 - nonspeech).'''
#     pass

# get_speech_regions('Music/Anderson .Paak - Put Me Thru.wav')
print(get_lyrics_from_url('santana', 'oye como va'))

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Analyze input wave-file and save detected speech interval to json file.')
#     parser.add_argument('inputfile', metavar='INPUTWAVE',
#                         help='the full path to input wave file')
#     parser.add_argument('outputfile', metavar='OUTPUTFILE',
#                         help='the full path to output json file to save detected speech intervals')
#     args = parser.parse_args()
    
