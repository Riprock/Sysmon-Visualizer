import xml.etree.ElementTree as ET
#NOTE: As of right now this is only for one Event
#Once I get this to understand the structure of one event
#Just turns into an iteration of all Event in Events tag

root = ET.parse('test1.xml').getroot()
for i in root[1]:
    print(i.attrib)