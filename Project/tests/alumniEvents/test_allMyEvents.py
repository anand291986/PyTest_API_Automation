import pytest
import logging as logger
from Project.src.utilities.requestsUtility import RequestsUtility
from Project.src.utilities.assertionUtility import AssertionUtility
from Project.src.dao.alumniEvents_dao import AlumniEventsDao
from Project.tests.alumniEvents.data import Data
from sqlalchemy.orm import sessionmaker


pytestmark = [pytest.mark.alumni_regression, pytest.mark.myevents_tip]

@pytest.fixture(scope='function')
def session(connection):
    Session = sessionmaker()
    session = Session(bind=connection)
    logger.debug("Database session has been established")
    yield session
    session.close()
    logger.debug("Database session has been closed")


@pytest.fixture(scope='module')
def response():
    request_helper = RequestsUtility()
    headers = Data['myEvents']['fixtures']['headers']
    endpoint = Data['myEvents']['fixtures']['endpoint']
    response = request_helper.get(endpoint=endpoint, headers=headers, expected_status_code=200)
    yield response


@pytest.mark.myevents
def test_get_all_my_events_response_check_tc001(response):
    """Checking if API response is not blank"""
    assert response, f"No events in the response"


@pytest.mark.myevents
def test_get_all_my_events_json_schema_validation_tc002(response):
    """Checking if Json response Schema matches defined API Json Schema"""
    endpoint = Data['myEvents']['tc002']['endpoint']
    AssertionUtility.schema_assertion_json(endpoint, response)


@pytest.mark.myevents
def test_get_all_my_events_xml_schema_validation_tc003():
    """Checking if XML response Schema matches defined API XSD"""
    headers = Data['myEvents']['tc003']['headers']
    endpoint = Data['myEvents']['tc003']['endpoint']
    AssertionUtility.schema_assertion_xml(endpoint, headers)


@pytest.mark.myevents
def test_get_all_my_events_validate_eventid_in_database_tc004(session, response):
    """Checking if event ID in response is found in database"""
    response_eventId = response[0]["eventId"]
    result = AlumniEventsDao.get_eventid(session, response_eventId)
    assert response_eventId == result["event_id"]
    logger.debug(f"Event in Database response is {result}")
