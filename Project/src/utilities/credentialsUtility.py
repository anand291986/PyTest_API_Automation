import os
from Project.src.configs.hosts_config import DB_HOST


class CredentialsUtility(object):
    """Credentials Utility fetches & initializes required credentials to make API & DB calls"""

    @staticmethod
    def get_wc_api_keys():
        pass

    @staticmethod
    def get_db_credentials():
        """
        Gets database credentials from config file
        :return: list
        List containing credentials
        """

        db_username = os.environ.get('db_username')
        db_password = os.environ.get('db_password')
        machine = os.environ.get('machine')
        assert machine, f"Environment variable 'machine' must be set."
        env = os.environ.get('env', 'test')
        host = DB_HOST[machine][env]['host']
        service_name = DB_HOST[machine][env]['servicename']
        port = DB_HOST[machine][env]['port']
        if not db_username or not db_password:
            raise Exception("The DB credentials in environment variables are missing or incomplete")
        else:
            return {'username': db_username, 'password': db_password, 'machine': machine,
                    'host': host, 'servicename': service_name, 'port': port}
