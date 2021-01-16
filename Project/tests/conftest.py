import pytest
import logging as logger
from Project.src.utilities.credentialsUtility import CredentialsUtility
from sqlalchemy import create_engine


@pytest.fixture()
def connection():
    credential_helper = CredentialsUtility()
    credentials = credential_helper.get_db_credentials()
    engine = create_engine(
        f"oracle+cx_oracle://{credentials['username']}:{credentials['password']}"
        f"@{credentials['host']}:{credentials['port']}"
        f"/?service_name={credentials['servicename']}")
    connection = engine.connect()
    logger.debug("Database connection has been established")
    yield connection
    connection.close()
    logger.debug("Database connection has been closed")
