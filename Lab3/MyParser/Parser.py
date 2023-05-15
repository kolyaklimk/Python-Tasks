import inspect
from MyParser import nonetype, moduletype, codetype, celltype, \
    functype, smethodtype, cmethodtype, CODE_PROPS, UNIQUE_TYPES, \
    TYPE_KW, SOURCE_KW, CODE_KW, GLOBALS_KW, NAME_KW, DEFAULTS_KW, CLOSURE_KW, \
    BASES_KW, DICT_KW, CLASS_KW, OBJECT_KW


class Parser:
    @classmethod
    def to_dict(cls, obj, is_inner_func=False):
        if type(obj) in (int, float, bool, str, nonetype):
            return obj

        if type(obj) in (set, frozenset, tuple, bytes, bytearray):
            return {TYPE_KW: type(obj).__name__,
                    SOURCE_KW: cls.to_dict([*obj])}

        if type(obj) is complex:
            return {TYPE_KW: complex.__name__,
                    SOURCE_KW: {complex.real.__name__: obj.real, complex.imag.__name__: obj.imag}}

        if type(obj) is list:
            return [cls.to_dict(o) for o in obj]

        if type(obj) is dict:
            return {TYPE_KW: dict.__name__,
                    SOURCE_KW: [[cls.to_dict(item[0]), cls.to_dict(item[1])] for item in obj.items()]}

        if type(obj) is moduletype:
            return {TYPE_KW: moduletype.__name__,
                    SOURCE_KW: obj.__name__}

        if type(obj) is codetype:
            code = {TYPE_KW: codetype.__name__}
            source = {}

            for (key, value) in inspect.getmembers(obj):
                if key in CODE_PROPS:
                    source[key] = cls.to_dict(value)

            code.update({SOURCE_KW: source})
            return code

        if type(obj) is celltype:
            return {TYPE_KW: celltype.__name__,
                    SOURCE_KW: cls.to_dict(obj.cell_contents)}

        if type(obj) in (smethodtype, cmethodtype):
            return {TYPE_KW: type(obj).__name__,
                    SOURCE_KW: cls.to_dict(obj.__func__, is_inner_func)}

        

    @classmethod
    def from_dict(cls, obj, is_dict=False):
        pass
