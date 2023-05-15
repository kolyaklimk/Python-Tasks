import re
import regex
from MySerializer import Serializer
from MyParser.Parser import Parser
from MyParser import nonetype
from MyParser.JsonParser import TRUE_LITERAL, FALSE_LITERAL, NULL_LITERAL, INT_PATTERN, FLOAT_PATTERN, BOOL_PATTERN, \
    STRING_PATTERN, NULL_PATTERN, VALUE_PATTERN


class Json(Serializer):
    def dumps(self, obj) -> str:
        def dumps_from_dict(string) -> str:
            if type(string) is nonetype:
                return NULL_LITERAL
            
            if type(string) is bool:
                return TRUE_LITERAL if string else FALSE_LITERAL

            if type(string) is str:
                return '"' + string.replace('\\', "\\\\").replace('"', r"\"").replace("'", r"\'") + '"'

            if type(string) in (int, float):
                return str(string)

            if type(string) is list:
                return '[' + ", ".join([dumps_from_dict(item) for item in string]) + ']'

            if type(string) is dict:
                return '{' + ", ".join([f"{dumps_from_dict(item[0])}: "
                                        f"{dumps_from_dict(item[1])}" for item in string.items()]) + '}'
            else:
                raise ValueError

        obj = Parser.to_dict(obj)
        return dumps_from_dict(obj)

    def loads(self, obj: str):
        pass
