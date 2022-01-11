from xml.etree import ElementTree as ET
from xml.dom import minidom

# Assume that we have an existing XML document with one "data" child
fle=open("file_notes.xml","w")
fle.close()
doc = ET.parse("file_notes.xml")
root = doc.getroot()

# Create 2 new "data" elements
data1 = ET.Element("data", {"a_version": "something_v001.0002.ma",
                            "b_user": "You",
                            "c_comment": "minor save"})
data2 = ET.Element("data", {"a_version": "something_v001.0003.ma",
                            "b_user": "Them",
                            "c_comment": "major save"})

# Append the new "data" elements to the root element of the XML document
root.append(data1)
root.append(data2)

# Now we have a new well-formed XML document. It is not very nicely formatted...
out = ET.tostring(root)

# ...so we'll use minidom to make the output a little prettier
dom = minidom.parseString(out)
print (dom.toprettyxml())
