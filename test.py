import xml.etree.ElementTree as ET
events = ET.parse('test1.xml').getroot()

for event in events:
    print(event[1][18].text.replace("{","").replace("}",""))