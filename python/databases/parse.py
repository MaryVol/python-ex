import xml.etree.ElementTree as ET

fname = './tracks/Library.xml'
stuff = ET.parse(fname)
print(stuff)