import inspect
from MyParser import nonetype, moduletype, codetype, celltype, \
    functype, smethodtype, cmethodtype, CODE_PROPS, UNIQUE_TYPES, \
    TYPE_KW, SOURCE_KW, CODE_KW, GLOBALS_KW, NAME_KW, DEFAULTS_KW, CLOSURE_KW, \
    BASES_KW, DICT_KW, CLASS_KW, OBJECT_KW


class Parser:
    @classmethod
    def to_dict(cls, obj, is_inner_func=False):
        pass

    @classmethod
    def from_dict(cls, obj, is_dict=False):
        pass
