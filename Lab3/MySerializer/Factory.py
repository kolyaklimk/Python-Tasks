from enum import Enum

from MyParser.XmlParser.Xml import Xml
from MyParser.JsonParser.Json import Json


class SerializerType(Enum):
    JSON = "json"
    XML = "xml"
