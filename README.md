# README #

This program takes .srt subtitle files, such as those produced by Aegisub, and converts them to the .vtt format required by UCLA's Common Collaborative and Learning Environment (CCLE).

## Usage ##
This program was written using Python 3.8.  It will likely work with other versions of Python 3, but no guarantee is made.

To run this program:
1. Put the srt_to_vtt.py file in the same folder as the .srt file to convert.
2. Change the line readFile = '0_6q1bx6ol.srt' to contain the name of the .srt file to convert.
3. Run in Python.
4. The converted file will be in the same folder as the .srt file, with the same name, but with a .vtt extension.

## Reasons for Using ##
Occasionally, instructors want subtitles added to their videos on CCLE, but CCLE requires a rare format of .vtt.  Instructions on how to make .srt files and what to do with the .vtt files after converted can be found at https://humtech.atlassian.net/wiki/spaces/ITGIS/pages/214466565/Adding+Subtitles+to+Media.

## Credits ##

Written by Benjamin Niedzielski, a Research and Instructional Technology Consultant, on February 20, 2020.
This program may be edited as long as the original credits are maintained here.
