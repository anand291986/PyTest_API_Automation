class SchemaSelect(object):
    """SchemaSelect class supports schema definition & further scheme selection for comparison"""

    @classmethod
    def select(cls, endpoint, *args):
        schema = getattr(cls, f"_select_{endpoint}")(*args)
        return schema

    @classmethod
    def _select_allMyEvents(cls):
        """Schema select method
        :arg None
        :return dict
        Schema dictionary gets returned
        """
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "eventId": {
                            "type": "integer"
                        },
                        "cventId": {
                            "type": "string"
                        },
                        "eventTitle": {
                            "type": "string"
                        },
                        "eventDescription": {
                            "type": "string"
                        },
                        "eventCategoryCode": {
                            "type": "null"
                        },
                        "eventTypeCode": {
                            "type": "null"
                        },
                        "eventCategoryDesc": {
                            "type": "null"
                        },
                        "location": {
                            "type": "string"
                        },
                        "locationCode": {
                            "type": "null"
                        },
                        "locationDesc": {
                            "type": "null"
                        },
                        "streetLine1": {
                            "type": "null"
                        },
                        "streetLine2": {
                            "type": "null"
                        },
                        "streetLine3": {
                            "type": "null"
                        },
                        "city": {
                            "type": "null"
                        },
                        "stateCode": {
                            "type": "null"
                        },
                        "countryCode": {
                            "type": "null"
                        },
                        "eventStatusCode": {
                            "type": "null"
                        },
                        "eventCode": {
                            "type": "null"
                        },
                        "categoryCode": {
                            "type": "null"
                        },
                        "categoryDescription": {
                            "type": "null"
                        },
                        "eventStartDate": {
                            "type": "string"
                        },
                        "eventEndDate": {
                            "type": "string"
                        },
                        "rsvpByDate": {
                            "type": "null"
                        },
                        "eventDisplayStartDate": {
                            "type": "string"
                        },
                        "eventDisplayEndDate": {
                            "type": "string"
                        },
                        "timeZone": {
                            "type": "string"
                        },
                        "clubURL": {
                            "type": "string"
                        },
                        "clubCode": {
                            "type": "string"
                        },
                        "clubDesc": {
                            "type": "string"
                        },
                        "inviteeStatusCode": {
                            "type": "string"
                        },
                        "participantFlag": {
                            "type": "null"
                        },
                        "inviteeStatusCodeDescription": {
                            "type": "null"
                        },
                        "inviteeOriginalResponseDate": {
                            "type": "null"
                        },
                        "inviteeLastModifiedDate": {
                            "type": "string"
                        },
                        "displayStartDateTime": {
                            "type": "null"
                        },
                        "displayEndDateTime": {
                            "type": "null"
                        },
                        "eventSpeakers": {
                            "type": "array",
                            "items": {}
                        },
                        "eventURLs": {
                            "type": "array",
                            "items": {}
                        },
                        "eventTags": {
                            "type": "array",
                            "items": {}
                        },
                        "attendeeList": {
                            "type": "array",
                            "items": {}
                        },
                        "inviteeList": {
                            "type": "array",
                            "items": {}
                        }
                    },
                    "required": [
                        "eventId",
                        "cventId",
                        "eventTitle",
                        "eventDescription",
                        "eventCategoryCode",
                        "eventTypeCode",
                        "eventCategoryDesc",
                        "location",
                        "locationCode",
                        "locationDesc",
                        "streetLine1",
                        "streetLine2",
                        "streetLine3",
                        "city",
                        "stateCode",
                        "countryCode",
                        "eventStatusCode",
                        "eventCode",
                        "categoryCode",
                        "categoryDescription",
                        "eventStartDate",
                        "eventEndDate",
                        "rsvpByDate",
                        "eventDisplayStartDate",
                        "eventDisplayEndDate",
                        "timeZone",
                        "clubURL",
                        "clubCode",
                        "clubDesc",
                        "inviteeStatusCode",
                        "participantFlag",
                        "inviteeStatusCodeDescription",
                        "inviteeOriginalResponseDate",
                        "inviteeLastModifiedDate",
                        "displayStartDateTime",
                        "displayEndDateTime",
                        "eventSpeakers",
                        "eventURLs",
                        "eventTags",
                        "attendeeList",
                        "inviteeList"
                    ]
                }
            ]
        }
        return schema

    @classmethod
    def _select_allMyEvents_xml(cls):
        """Schema select method
        :arg None
        :return str
        Schema string gets returned
        """
        schema = """<?xml version="1.0" encoding="utf-8"?>
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="list">
    <xs:complexType>
      <xs:sequence>
        <xs:element maxOccurs="unbounded" name="events">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="eventId" type="xs:unsignedShort" />
              <xs:element name="cventId" type="xs:string" />
              <xs:element name="eventTitle" type="xs:string" />
              <xs:element name="eventDescription" type="xs:string" />
              <xs:element minOccurs="0" name="eventCategoryCode" type="xs:string" />
              <xs:element minOccurs="0" name="eventCategoryDesc" type="xs:string" />
              <xs:element name="location" type="xs:string" />
              <xs:element minOccurs="0" name="streetLine1" type="xs:string" />
              <xs:element minOccurs="0" name="city" type="xs:string" />
              <xs:element minOccurs="0" name="stateCode" type="xs:string" />
              <xs:element minOccurs="0" name="countryCode" type="xs:string" />
              <xs:element name="eventStartDate" type="xs:dateTime" />
              <xs:element name="eventEndDate" type="xs:dateTime" />
              <xs:element name="eventDisplayStartDate" type="xs:string" />
              <xs:element name="eventDisplayEndDate" type="xs:string" />
              <xs:element name="timeZone" type="xs:string" />
              <xs:element minOccurs="0" name="clubURL" type="xs:string" />
              <xs:element minOccurs="0" name="clubCode" type="xs:string" />
              <xs:element minOccurs="0" name="clubDesc" type="xs:string" />
              <xs:element name="inviteeStatusCode" type="xs:string" />
              <xs:element minOccurs="0" name="inviteeLastModifiedDate" type="xs:dateTime" />
              <xs:element name="eventSpeakers" />
              <xs:element name="eventURLs" />
              <xs:element name="eventTags" />
              <xs:element name="attendeeList" />
              <xs:element name="inviteeList" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>"""

        return schema