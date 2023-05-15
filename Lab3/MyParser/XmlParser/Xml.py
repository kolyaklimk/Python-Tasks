import regex
from MySerializer import Serializer
from MyParser import Parser, nonetype
from MyParser.XmlParser import KEY_GROUP_NAME, VALUE_GROUP_NAME, XML_SCHEME_SOURCE, XML_ELEMENT_PATTERN, \
    FIRST_XML_ELEMENT_PATTERN


class Xml(Serializer):
    def dumps(self, obj) -> str:
        def create_xml_element(name: str, data: str, is_first=False):
            if is_first:
                return f"<{name} {XML_SCHEME_SOURCE}>{data}</{name}>"
            else:
                return f"<{name}>{data}</{name}>"

        def dumps_from_dict(string, is_first=False) -> str:
            pass

        obj = Parser.to_dict(obj)
        return dumps_from_dict(obj, True)

    def loads(self, obj: str):
        pass
