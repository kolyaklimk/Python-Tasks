from enum import Enum

from MyParser.XmlParser.Xml import Xml
from MyParser.JsonParser.Json import Json


class SerializerType(Enum):
    JSON = "json"
    XML = "xml"


class Factory:
    @staticmethod
    def create_serializer(st: SerializerType):

        if st == SerializerType.JSON:
            return Json()

        elif st == SerializerType.XML:
            return Xml()

        else:
            raise Exception("Unknown type")
