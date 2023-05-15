import regex
from MySerializer import Serializer
from MyParser import Parser, nonetype
from MyParser.XmlParser import KEY_GROUP_NAME, VALUE_GROUP_NAME, XML_SCHEME_SOURCE, XML_ELEMENT_PATTERN, \
    FIRST_XML_ELEMENT_PATTERN


class Xml(Serializer):
    def dumps(self, obj) -> str:
        pass

    def loads(self, obj: str):
        pass
