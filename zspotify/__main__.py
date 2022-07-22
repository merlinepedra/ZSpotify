#! /usr/bin/env python3

"""
ZSpotify
It's like youtube-dl, but for Spotify.
Copyright (C) 2021 Deathmonger/Footsiefat and ZSpotify Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import argparse

from app import client
from config import CONFIG_VALUES

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='zspotify',
        description='A Spotify downloader needing only a python interpreter and ffmpeg.')
    parser.add_argument('-ns', '--no-splash',
                        action='store_true',
                        help='Suppress the splash screen when loading.')
    parser.add_argument('--config-location',
                        type=str,
                        help='Specify the zs_config.json location')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('urls',
                       type=str,
                       # action='extend',
                       default='',
                       nargs='*',
                       help='Downloads the track, album, playlist, podcast episode, or all albums by an artist from a url. Can take multiple urls.')
    group.add_argument('-ls', '--liked-songs',
                       dest='liked_songs',
                       action='store_true',
                       help='Downloads all the liked songs from your account.')
    group.add_argument('-p', '--playlist',
                       action='store_true',
                       help='Downloads a saved playlist from your account.')
    group.add_argument('-s', '--search',
                       dest='search_spotify',
                       action='store_true',
                       help='Loads search prompt to find then download a specific track, album or playlist')
    group.add_argument('-d', '--download',
                       type=str,
                       help='Downloads tracks, playlists and albums from the URLs written in the file passed.')

    for configkey in CONFIG_VALUES:
        parser.add_argument(CONFIG_VALUES[configkey]['arg'],
                            type=str,
                            default=None,
                            help='Specify the value of the ['+configkey+'] config value')

    parser.set_defaults(func=client)

    args = parser.parse_args()
    args.func(args)
