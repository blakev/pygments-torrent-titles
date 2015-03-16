# Copyright 2015 Blake VandeMerwe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Blake VandeMerwe'

import pygments
from pygments.lexer import RegexLexer, include
from pygments.token import *

__all__ = ['TvTorrentLexer']

class TvTorrentLexer(RegexLexer):
    name = 'TORRENT'

    tokens = {
        'root': [
            include('basics')
        ],

        'basics': [
            (r'^\s+', Text),
            (r'[sS](eason){0,1}[_\-\. ]*\d+', Text.Season, 'episode'),
            (r'(?:19|20)\d{2}[ \-\\\_\.]*(\d{2}[ \-\\\_\.]){2}', Number.YearFirstDate),
            (r'(\d{2}[ \-\\\_\.]*){2}(?:19|20)\d{2}', Number.YearLastDate),
            (r'(?:19|20)\d{2}', Number.Year),
            (r'(january|february|march|april|may|june|july|august|september|october|november|december)[_\-\. ]', Text.MonthFull, 'with_date'),
            (r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[_\-\. ]', Text.MonthShort, 'with_date'),
            (r'\d{3,4}\W*[pPiI]', Text.Quality),
            (r'[pP]art[\W\-,\.\_]*\d+', Text.ShowSegment),
            (r'(ntsc|pal)', Text.Region),
            (r'\W*(hdtv|hd)', Text.HDTV)
        ],

        'episode': [
            (r'([eE]|episode|d|day|dvd)', Text.Episode),
            (r'[_\-\. ]*(\d+)', Text.EpisodeNumber, '#pop')
        ],

        'with_date': [
            (r'[\W \-\_\.]\d{1,2}(st|nd|rd|th){0,1}', Text.Day, '#pop')
        ]
    }

building_name = True
the_torrent_name = ''

for token, value in pygments.lex('# the 2015 juno awards hdtv x264-crooks', TvTorrentLexer()):
    if token is not Error and building_name:
        building_name = False

    if token is Error:
        if building_name:
            the_torrent_name += value
    else:
        print(token, value.strip())

print(the_torrent_name)
