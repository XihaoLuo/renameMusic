# Xihao Luo
# Script for renaming album music
# Renames all the songs into '(track number).(artist name) - (song name)' format

import os
import sys
from albumMP3 import AlbumMP3


def main():
    # Information
    directory = input('Please enter album directory: ')
    try:
        os.listdir(directory)
    except OSError:
        print('Directory does not exist.')
        sys.exit(1)

    artist = input('Enter artist name: ')
    album = input('Enter album name: ')
    year = input('Enter album release year: ')
    names = [item for item in input("Enter the new names (in order - split by ; ): ").split(';')]
    ftype = input('Enter file type (flac/mp3/wav/m4a): ')

    fextension = ''
    if ftype in ['flac', 'mp3', 'wav', 'm4a']:
        fextension = '.' + ftype
    else:
        print('File type not recognized :(')
        sys.exit(1)

    if ftype == 'mp3':
        album = AlbumMP3(directory, artist, album, year, names, fextension)
        album.renameAlbumName()
        album.renameArtistName()
        album.renameAllSongs()
    elif ftype == 'flac':
        album = None


if __name__ == '__main__':
    main()