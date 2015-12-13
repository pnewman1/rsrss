#!/usr/bin/env python

# by Patrick Nemwan (npbtracker@gmail.com)
# really simple rss
# take a list of static files and turn them into a static xml file
# served from an arbitrary location on disk
# seems to be at minimally compliant with rss standard

import commands
from time import strftime, localtime
import uuid
import xml.etree.ElementTree as ET

#variables for stuff we'll need later
link = "put your link here"
title = "put your title here"
rss_location = "location on disk" # eg "$DOCUMENT_ROOT/feed.xml"

#set up the basic rss file
root = ET.Element("rss", version="2.0")
channel = ET.SubElement(root, "channel")

ET.SubElement(channel, "title").text = title
ET.SubElement(channel, "description").text = "The finest collection of gifs known to humandkind."

ET.SubElement(channel, "link").text = link
ET.SubElement(channel, "lastBuildDate").text = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
ET.SubElement(channel, "pubDate").text = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
ET.SubElement(channel, "ttl").text = "60"

#get the last n files
searchdir = ""
lscmd = "ls -rt " + searchdir
files = commands.getoutput(searchdir)

fs = files.split("\n")

for fs in files.split("\n"):
  filename = fs.split("/")[4]
  url = link + filename
  item = ET.SubElement(channel, "item")
  ET.SubElement(item, "title").text = filename
  ET.SubElement(item, "link").text = url
  ET.SubElement(item, "description").text = "<img src=\'" + url + "\'>"
  ET.SubElement(item, "content").text = "<img src=\'" + url + "\'>"
  ET.SubElement(item, "guid").text = url
  
  print "added", filename

tree = ET.ElementTree(root)
tree.write(rss_location)
