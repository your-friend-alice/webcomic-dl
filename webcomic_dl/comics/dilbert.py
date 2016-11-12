#Copyright 2016 Devon Sawatzky

#This file is part of webcomic-dl.

#webcomic-dl is free software: you can redistribute it and/or modify it under
#the terms of the GNU General Public License as published by the Free Software
#Foundation, either version 3 of the License, or (at your option) any later
#version.

#webcomic-dl is distributed in the hope that it will be useful, but WITHOUT ANY
#WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#PARTICULAR PURPOSE.  See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with
#webcomic-dl.  If not, see <http://www.gnu.org/licenses/>.

from webcomic_dl import Comic
import re

class DilbertComic(Comic):
    nextSelector='.nav-right a[title="Next Strip"]'
    """the CSS selector for the "next" link"""
    titleSelector='.comic-title-name'
    """the CSS selector for the comic title"""
    imgSelector='.img-comic'
    """the CSS selector for the comic img"""
    siteTitle='Dilbert'
    """The Site's Title"""
    directory='dilbert'
    """the default directory name to download into"""
    urlRegex="^https?://(?:www\.)?dilbert\.com(?:/|$)"
    """the regex for matching the URL to the Comic"""
    name="dilbert"
    """Name of the comic"""
    first="http://dilbert.com/strip/1989-04-16"
    """URL of first comic"""
    extension="gif"