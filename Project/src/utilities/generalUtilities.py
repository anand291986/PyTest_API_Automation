import xmltodict
import json
import xmlschema
import logging as logger
from lxml2json import convert


class GeneralUtilities(object):

    def xmltodict(xmlbody):
        xpars = xmltodict.parse(xmlbody)
        responsestring = json.dumps(xpars)
        responsejson = json.loads(responsestring)
        import pdb;
        pdb.set_trace()
        return responsejson

    def xmltojson(xmlbody):
        encoding = 'utf-8'
        responsestring = str(xmlbody, encoding)

        jsonbody = convert(responsestring)
        import pdb;
        pdb.set_trace()
        return jsonbody

    def xmlvalidator(xmlbody):
        # my_schema = xmlschema.XMLSchema('tests/alumniEvents/schemaxml.xsd')
        # import pdb;
        # pdb.set_trace()
        # my_schema.validate(xmlbody)
        # xml_file = 'tests/alumniEvents/xmlschema.xml'
        xsd_file = 'tests/alumniEvents/schemaxml.xsd'
        xmlschema.validate(xmlbody, schema=xsd_file)
        import pdb;
        pdb.set_trace()
        logger.info(xmlbody)
