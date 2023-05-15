import inspect
from MyParser import nonetype, moduletype, codetype, celltype, \
    functype, smethodtype, cmethodtype, CODE_PROPS, UNIQUE_TYPES, \
    TYPE_KW, SOURCE_KW, CODE_KW, GLOBALS_KW, NAME_KW, DEFAULTS_KW, CLOSURE_KW, \
    BASES_KW, DICT_KW, CLASS_KW, OBJECT_KW


class Parser:
    @classmethod
    def to_dict(cls, obj, is_inner_func=False):
        def get_obj_dict(obj_dict):
            dct = {item[0]: item[1] for item in obj_dict.__dict__.items()}
            dct2 = {}

            for KEY, VALUE in dct.items():
                if type(VALUE) not in UNIQUE_TYPES:
                    if inspect.isroutine(VALUE):
                        dct2[cls.to_dict(KEY)] = cls.to_dict(VALUE, is_inner_func=True)
                    else:
                        dct2[cls.to_dict(KEY)] = cls.to_dict(VALUE)
            return dct2

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

        if inspect.isroutine(obj):
            source = {CODE_KW: cls.to_dict(obj.__code__)}

            name = obj.__name__
            gvars = {}
            for gvar_name in obj.__code__.co_names:
                if gvar_name in obj.__globals__:

                    if type(obj.__globals__[gvar_name]) is moduletype:
                        gvars[gvar_name] = obj.__globals__[gvar_name]

                    elif inspect.isclass(obj.__globals__[gvar_name]):
                        c = obj.__globals__[gvar_name]
                        if is_inner_func and name in c.__dict__ and obj == c.__dict__[name].__func__:
                            gvars[gvar_name] = c.__name__
                        else:
                            gvars[gvar_name] = c

                    elif gvar_name == obj.__code__.co_name:
                        gvars[gvar_name] = obj.__name__

                    else:
                        gvars[gvar_name] = obj.__globals__[gvar_name]
            source[GLOBALS_KW] = cls.to_dict(gvars)

            source[NAME_KW] = cls.to_dict(obj.__name__)

            source[DEFAULTS_KW] = cls.to_dict(obj.__defaults__)

            source[CLOSURE_KW] = cls.to_dict(obj.__closure__)

            return {TYPE_KW: functype.__name__, SOURCE_KW: source}

        elif inspect.isclass(obj):
            source = {NAME_KW: cls.to_dict(obj.__name__),
                      BASES_KW: cls.to_dict(tuple(b for b in obj.__bases__ if b != object)),
                      DICT_KW: get_obj_dict(obj)}

            return {TYPE_KW: type.__name__, SOURCE_KW: source}

        else:
            source = {CLASS_KW: cls.to_dict(obj.__class__), DICT_KW: get_obj_dict(obj)}

            return {TYPE_KW: OBJECT_KW, SOURCE_KW: source}

    @classmethod
    def from_dict(cls, obj, is_dict=False):
        if is_dict:
            return {cls.from_dict(item[0]): cls.from_dict(item[1]) for item in obj}

        if type(obj) not in (dict, list):
            return obj

        elif type(obj) is list:
            return [cls.from_dict(o) for o in obj]
