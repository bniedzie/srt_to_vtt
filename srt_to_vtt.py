############################################################################
#This program converts an .srt file that uses commas for decimal points
#into a .vtt file.
#
#Author: Benjamin Niedzielski (bniedzie@ucla.edu)
#Last Modified: 2/20/2020
############################################################################
import re;
import sys;

readFile = '0_6q1bx6ol.srt'
writeFile = readFile[:-3] + '.vtt'
fp = open(readFile, 'r', encoding="utf-8");
fw = open(writeFile, 'w', encoding="utf-8");

fw.write("WEBVTT\n");
fw.write("Kind: captions\n\n");
line = fp.readline();
nextLine = True;
firstLine = True;

while line:
    #Special case the first line so commas get converted correctly
    if nextLine and not firstLine:
        line = re.sub(r',', '.', line);
        nextLine = False;
    elif firstLine:
        firstLine = False;
    else:
        #An integer means the next line will be a time stamp, whose commas must be converted
        try:
            if (line == "1\r"):
                nextLine = True;
            int(line)
            nextLine = True;
        except ValueError:
            line = line;
    fw.write(line);
    line = fp.readline();
fw.close();
fp.close();
