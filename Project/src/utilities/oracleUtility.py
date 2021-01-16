import os
from Project.src.utilities.credentialsUtility import CredentialsUtility
from Project.src.configs.hosts_config import DB_HOST
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.machine = os.environ.get('MACHINE')
        assert self.machine, f"Environment variable 'MACHINE' must be set."
        self.env = os.environ.get('ENV', 'test')
        self.host = DB_HOST[self.machine][self.env]['host']
        self.servicename = DB_HOST[self.machine][self.env]['servicename']
        self.port = DB_HOST[self.machine][self.env]['port']

    def create_connection(self):
        engine = create_engine(f"oracle+cx_oracle://{self.creds['username']}:{self.creds['password']}@{self.host}:{self.port}/?service_name={self.servicename}")
        connection = engine.connect()

        return connection

    def execute_select(self, sql):

        connection = self.create_connection()
        session = Session(bind=connection)
        results = session.execute(sql)
        output = results.fetchall()
        connection.close()
        return output