import re
import regex
from MySerializer import Serializer
from MyParser.Parser import Parser
from MyParser import nonetype
from MyParser.JsonParser import TRUE_LITERAL, FALSE_LITERAL, NULL_LITERAL, INT_PATTERN, FLOAT_PATTERN, BOOL_PATTERN, \
    STRING_PATTERN, NULL_PATTERN, VALUE_PATTERN


class Json:
    def dumps(self, obj) -> str:
        pass

    def loads(self, obj: str):
        pass
