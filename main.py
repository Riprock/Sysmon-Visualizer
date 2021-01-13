from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
import logging

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
    app = App("bolt://localhost:7687", "neo4j", "sysmon")
    app.proc_start("crss.exe", "2")
    app.close()