import xml.etree.ElementTree as ET
events = ET.parse('sysmon.xml').getroot()
for event in events:
    if event[0][1].text == "5":
        print(event[1][2].attrib)
        print(event[1][2].text)
        break


