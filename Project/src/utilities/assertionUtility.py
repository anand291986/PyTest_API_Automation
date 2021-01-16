from hamcrest import assert_that
from json_schema_matchers.common_matcher import matches_json_schema
from Project.tests.alumniEvents.schema import SchemaSelect
import xmlschema
from Project.src.utilities.requestsUtility import RequestsUtility


class AssertionUtility(object):
    """Assertion Utility class offers methods that help perform custom assertion on an api response"""

    def schema_assertion_xml(endpoint, headers):
        """Makes the API call and compares defined response schema & received response body
        :arg
        endpoint : str
        headers : dict
        :return bool
            Ture or False
        """
        request_helper = RequestsUtility()
        response = request_helper.get(endpoint, headers=headers)  # Makes API call & gets response body
        endpoint = endpoint + "_xml"
        xmlSchema = SchemaSelect.select(endpoint)  # Fetches correct XML schema for comparison
        xmlschema.validate(response, schema=xmlSchema)  # Schema comparison

    def schema_assertion_json(endpoint, response):
        """Compares defined response schema & received response body
        :arg
        endpoint : str
        response : dict
        :return bool
        Ture or False
        """
        apiSchema = SchemaSelect.select(endpoint)
        assert_that(response, matches_json_schema(apiSchema))  # Schema comparison
