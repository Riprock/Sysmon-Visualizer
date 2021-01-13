from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
import logging
import xml.etree.ElementTree as ET

class App:
    def __init__(self, url, user, password):
        self.driver = GraphDatabase.driver(url, auth=(user,password))
    
    def close(self):
        self.driver.close()
    
    def proc_start(self, procname, procid):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_proc_node, procname, procid)
            for row in result:
                print(f'Node {procname} was created')
        
    @staticmethod
    def _create_proc_node(tx, procname,procid):
        query = ("CREATE (n1:Process { procname: $procname, procid: $procid})"
                "RETURN n1")
        result = tx.run(query, procname=procname, procid=procid)
        try:
            return [{"n1": row["n1"]["procid"]} for row in result]        
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
            query=query, exception=exception))
            raise

if __name__ == "__main__":
    root = ET.parse('test1.xml').getroot()
    app = App("bolt://localhost:7687", "neo4j", "sysmon")
    app.proc_start("crss.exe", "2")
    app.close()
    UtcTime = root[1][1].text
    ProcessGuid = root[1][2].text
    ProcessId = root[1][3].text
    Image = root[1][4].text
    FileVersion = root[1][5].text
    Description = root[1][6].text
    Product = root[1][7].text
    Company = root[1][8].text
    OriginalFileName = root[1][9].text
    CommandLine = root[1][10].text
    CurrentDirectory = root[1][11].text
    User = root[1][12].text
    LogonGuid = root[1][13].text
    LogonId = root[1][14].text
    TerminalSessionId= root[1][15].text
    IntegrityLevel = root[1][16].text
    Hashes = root[1][17].text
    ParentProcessGuid = root[1][18].text
    ParentProcessId = root[1][19].text
    ParentImage = root[1][20].text
    ParentCommandLine = root[1][21].text