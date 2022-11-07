import json
import mysql.connector
from datetime import datetime

class DatabaseInterface(object):

    def __init__(self):
        """
        This method is called when the class is instantiated.
        It create a connection to the database. 
        If cannot connect to the database, it raises an exception.
        Read database connection parameters from the config.json file.
        """

        f = open('/home/luca/Documents/rta-transient-receiver/comet/plugins/config.json')
        config = json.load(f)
        db_user = config['Database_user']
        db_password = config['Database_password']
        db_host = config['Database_host']
        db_port = config['Database_port']
        db_name = config['Database_name']
        
        try:
            self.cnx = mysql.connector.connect(user=db_user, password=db_password,
                            host=db_host, port=db_port, database=db_name)
            self.cursor = self.cnx.cursor()               
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password, please set the current parameter as env variable")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            raise err

    def insert_voevent(self, voevent):
        
        query = f"SELECT receivedsciencealertid FROM receivedsciencealert WHERE instrumentid = {voevent.instrument_id} AND triggerid = {voevent.trigger_id};"
        self.cursor.execute(query)
        check_rsa = self.cursor.fetchone()

        #insert in receivedsciencealert table if not already present
        #get id of the last row inserted
        if check_rsa is None:
            query = f'INSERT INTO receivedsciencealert (instrumentid, networkid, time, triggerid, ste) VALUES ({voevent.instrument_id}, {voevent.network_id}, {voevent.isoTime}, {voevent.trigger_id}, {voevent.is_ste});'
            self.cursor.execute(query)
            self.cnx.commit()

            receivedsciencealertid = self.cursor.lastrowid
        else:
            receivedsciencealertid = int(check_rsa[0])
            
        #seqnum handling
        query = f"SELECT seqnum FROM notice n join receivedsciencealert rsa ON (rsa.receivedsciencealertid = n.receivedsciencealertid) WHERE last = 1 AND rsa.instrumentid = {voevent.instrument_id} AND rsa.triggerid = {voevent.trigger_id}"
        self.cursor.execute(query)
        result_seqnum = self.cursor.fetchone()

        try:
            seqNum = int(result_seqnum[0]) + 1 
        except:
            seqNum = 0

        #last handling
        query = f"UPDATE notice SET last = 0 WHERE last = 1 AND receivedsciencealertid = {receivedsciencealertid};"
        self.cursor.execute(query)
        self.cnx.commit()

        #insert in notice table
        noticetime = datetime.utcnow().isoformat(timespec="seconds")
        query = f"INSERT INTO notice (receivedsciencealertid, seqnum, l, b, error, contour, `last`, `type`, configuration, noticetime, notice, tstart, tstop, url, `attributes`, afisscheck) VALUES ({receivedsciencealertid}, {seqNum}, {voevent.l}, {voevent.b}, {voevent.position_error}, '{voevent.contour}', {voevent.last}, {voevent.packet_type}, '{voevent.configuration}', '{noticetime}', '{voevent.notice}', {voevent.tstart}, {voevent.tstop}, '{voevent.url}', '{voevent.ligo_attributes}', 0);"
        self.cursor.execute(query)
        self.cnx.commit()

