from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
import logging
import xml.etree.ElementTree as ET
import sys

class App:
    def __init__(self, url, user, password):
        self.driver = GraphDatabase.driver(url, auth=(user,password))
    
    def close(self):
        self.driver.close()
    
    def proc_start(self, data, num):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_proc_node, data)
            for row in result:
                print(f'Node {data["OriginalFileName"]} was created #{num}')
        
    @staticmethod
    def _create_proc_node(tx,data):
        query = ("CREATE (n1:Process { UtcTime: $UtcTime,ProcessGuid: $ProcessGuid,ProcessId: $ProcessId,Image: $Image,FileVersion: $FileVersion,Description: $Description,Product: $Product,Company: $Company,OriginalFileName: $OriginalFileName,CommandLine: $CommandLine,CurrentDirectory: $CurrentDirectory,User: $User,LogonGuid: $LogonGuid,LogonId: $LogonId, TerminalSessionId: $TerminalSessionId, IntegrityLevel: $IntegrityLevel, Hashes: $Hashes, ParentProcessGuid: $ParentProcessGuid, ParentProcessId: $ParentProcessId, ParentImage: $ParentImage, ParentCommandLine: $ParentCommandLine})"
                "RETURN n1")
        result = tx.run(query, UtcTime=data["UtcTime"],ProcessGuid=data["ProcessGuid"],ProcessId=data["ProcessId"],Image=data["Image"],FileVersion=data["FileVersion"],Description=data["Description"],Product=data["Product"],Company=data["Company"],OriginalFileName=data["OriginalFileName"],CommandLine=data["CommandLine"],CurrentDirectory=data["CurrentDirectory"],User=data["User"],LogonGuid=data["LogonGuid"],LogonId=data["LogonId"], TerminalSessionId=data["TerminalSessionId"], IntegrityLevel=data["IntegrityLevel"], Hashes=data["Hashes"], ParentProcessGuid=data["ParentProcessGuid"], ParentProcessId=data["ParentProcessId"], ParentImage=data["ParentImage"], ParentCommandLine=data["ParentCommandLine"])
        try:
            return [{"n1": row["n1"]["procid"]} for row in result]        
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
            query=query, exception=exception))
            raise
    
    def create_relationship(self, data):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_relationship, data)
            for row in result:
                print("Relationship made")
                #print(row)
                #print(f'Reationship was created from parent{data["ParentImage"]} to child {data["Image"]}')

    @staticmethod
    def _create_relationship(tx, procguid):
        query = (
               "MATCH (child:Process) WHERE child.ParentProcessGuid = $procguid "
                "MATCH (parent:Process) WHERE parent.ProcessGuid = $procguid "
                "CREATE (parent)-[:Spawns]->(child) "
                "Return child, parent"
                )
        result = tx.run(query, procguid=procguid)
        try:
            return [{"child": row["child"],"parent": row["parent"]} for row in result]        
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
            query=query, exception=exception))
            raise

def create_termination_nd(self, data):
    with self.driver.session() as session:
        result = session.write_transaction(self._create_termination_nd, data)
        for row in result:
            print(f'Termination Time was marked')

@staticmethod
def _create_termination_nd(tx, ):
    query = ("CREATE (n1:Process { UtcTime: $UtcTime,ProcessGuid: $ProcessGuid,ProcessId: $ProcessId,Image: $Image})"
                "RETURN n1")
    result = tx.run(query, UtcTime=data["UtcTime"],ProcessGuid=data["ProcessGuid"],ProcessId=data["ProcessId"],Image=data["Image"])
    try:
        return [{"n1": row["n1"]["procid"]} for row in result]        
    except ServiceUnavailable as exception:
        logging.error("{query} raised an error: \n {exception}".format(
        query=query, exception=exception))
        raise

def create(app):
    x = 1
    for event in events:
        if event[0][1].text == "1":
            data = {}
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
            app.proc_start(data, x)
            x += 1
            
def relate(app):
    guid = []
    for event in events:
        if event[0][1].text == "1":
            procguid = event[1][18].text.replace("{","").replace("}","")
            if procguid not in guid:
                guid.append(procguid)
                print(f'Added Guid {procguid}')
    for data in guid:
        app.create_relationship(data)

def terminations(app):
    for event in events:
        data = {}
        if event[0][1].text == "5":
            data["UtcTime"] = event[1][1].text
            data["ProcessGuid"] = event[1][2].text.replace("{","").replace("}","")
            data["ProcessId"] = event[1][3].text
            data["Image"] = event[1][4].text

if __name__ == "__main__":
    sysxml = sys.argv[1]
    events = ET.parse('sysmon.xml').getroot()
    app = App("bolt://localhost:7687", "neo4j", "sysmon")
    create(app)
    relate(app)
    app.close()

