def main(events): 
    x = 1
    for event in events:
        data = {}
        if event[0][1].text == "1":
            proccreate(event,data,x)
        if event[0][1].text == "2":
            procfiletime(event,data,x)
        if event[0][1].text == "3":
            netcon(event,data,x)
        if event[0][1].text == "4":
            pass
        if event[0][1].text == "5":
            pass
        if event[0][1].text == "6":
            pass
        if event[0][1].text == "7":
            pass
        if event[0][1].text == "8":
            pass
        if event[0][1].text == "9":
            pass
        if event[0][1].text == "10":
            pass
        if event[0][1].text == "11":
            pass
        if event[0][1].text == "12":
            regevnt(event,data,x)
        if event[0][1].text == "13":
            pass
        if event[0][1].text == "14":
            pass
        if event[0][1].text == "15":
            pass
        if event[0][1].text == "16":
            pass
        if event[0][1].text == "17":
            pass
        if event[0][1].text == "18":
            pass
        if event[0][1].text == "19":
            pass
        if event[0][1].text == "20":
            pass
        if event[0][1].text == "21":
            pass
        if event[0][1].text == "22":
            dnsQuery(event,data,x)
        if event[0][1].text == "23":
            pass
        if event[0][1].text == "24":
            pass
        if event[0][1].text == "25":
            pass
        if event[0][1].text == "26":
            pass
                
def proccreate(event, data,x):
    #This is Event ID 1
    data["UtcTime"] = event[1][1].text
    data["ProcessGuid"] = event[1][2].text.replace("{","").replace("}","")
    data["ProcessId"] = event[1][3].text
    data["Image"] = event[1][4].text
    data["FileVersion"] = event[1][5].text  
    data["Description"] = event[1][6].text
    data["Product"] = event[1][7].text
    data["Company"] = event[1][8].text
    data["OriginalFileName"] = event[1][9].text
    data["CommandLine"] = event[1][10].text
    data["CurrentDirectory"] = event[1][11].text
    data["User"] = event[1][12].text
    data["LogonGuid"] = event[1][13].text
    data["LogonId"] = event[1][14].text
    data["TerminalSessionId"] = event[1][15].text
    data["IntegrityLevel"] = event[1][16].text
    data["Hashes"] = event[1][17].text
    data["ParentProcessGuid"] = event[1][18].text.replace("{","").replace("}","")
    data["ParentProcessId"] = event[1][19].text
    data["ParentImage"] = event[1][20].text
    data["ParentCommandLine"] = event[1][21].text
    x += 1

def procfiletime(event,data,x):
    #This is Event ID 2
    data["UtcTime"] = event[1][1].text
    data["ProcessGuid"] = event[1][2].text.replace("{","").replace("}","")
    data["ProcessId"] = event[1][3].text
    data["Image"] = event[1][4].text

def netcon(event,data,x):
    #This is Event ID 3
    data["UtcTime"] = event[1][1].text
    data["ProcessGuid"] = event[1][2].text
    data["ProcessId"] = event[1][3].text
    data["Image"] = event[1][4].text
    data["User"] = event[1][5].text
    data["Protocol"] = event[1][6].text
    data["Initiated"] = event[1][7].text
    data["SourceIsIpv6"] = event[1][8].text
    data["SourceIp"] = event[1][9].text
    data["SourceHostname"] = event[1][10].text
    data["SourcePort"] = event[1][11].text
    data["SourcePortName"] = event[1][12].text 
    data["DestinationIsIpv6"] = event[1][13].text
    data["DestinationIp"] = event[1][14].text
    data["DestinationHostname"] = event[1][15].text
    data["DestinationPort"] = event[1][16].text
    data["DestinationPortName"] = event[1][17].text


#This is Event ID 4

def procterm(event, data):
    #This is Event ID 5
    data["UtcTime"] = event[1][1].text
    data["ProcessGuid"] = event[1][2].text.replace("{","").replace("}","")
    data["ProcessId"] = event[1][3].text
    data["Image"] = event[1][4].text
    data["User"] = event[1][5].text
    
#This is Event ID 6
#This is Event ID 7
#This is Event ID 8
#This is Event ID 9
#This is Event ID 10
#This is Event ID 11
def regevnt(event,data,x):
    #This is Event ID 12
    data["UtcTime"] = event[1][1].text
    data["EventType"] = event[1][2].text
    data["ProcessGuid"] = event[1][3].text.replace("{","").replace("}","")
    data["ProcessId"] = event[1][4].text
    data["Image"] = event[1][5].text
    data["TargetObject"] = event[1][6].text
    data["User"] = event[1][7].text

#This is Event ID 13
#This is Event ID 14
#This is Event ID 15
#This is Event ID 16
#This is Event ID 17
#This is Event ID 18
#This is Event ID 19
#This is Event ID 20
#This is Event ID 21
def dnsQuery(event,data,x):
    #This is Event ID 22
    data["UtcTime"] = event[1][1].text
    data["ProcessGuid"] = event[1][2].text.replace("{","").replace("}","")
    data["ProcessId"] = event[1][3]
    data["QueryName"] = event[1][4]
    data["QueryStatus"] = event[1][5]
    data["QueryResults"] = event[1][6]
    data["Image"] = event[1][7]
    data["User"] = event[1][8]

    
#This is Event ID 23
#This is Event ID 24
#This is Event ID 25
#This is Event ID 26