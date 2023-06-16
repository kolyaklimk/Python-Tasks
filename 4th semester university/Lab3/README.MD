## Create your own serializer.
In this lab you will create your own serializer:
- your serializer must correctly save/pack and load/unpack all objects and data passed into it;
- your serializer must correctly work with every built-in object of Python: 
  - default primitive types (int, bool, str, etc.);
  - default collections (list, set, dict, tuple);
  - functions (including wrappers, generators, iterators, closures, lambda, recursion);
  - classes (including inheritance, MRO, static and class methods, etc.);
  - object as an instance of class;
  - scopes (built-in, global, nonlocal, local);
  - imported libs for correct work of functions (math, re, etc.).

When it comes to innards of your program it should:
- contain factory method create_serializer() which gonna generate serializers for different formats: 
  - JSON;
  - XML;
  - YAML (optional);
  - TOML (optional);
- the architecture of an application must allow you to add new type without making any changes to existing code;
- your code must implement provided methods for each type of serializer:
  - dump(obj, fp) - serializes Python objects to file;
  - dumps(obj) - serializes Python objects to string;
  - load(fp) - deserializes Python objects from file;
  - loads(s) - deserializes Python objects from string;
  you can pass any additional parameters to these methods;
- you must be able to serialize objects from one format to another (e.g. save it to file in json and then serialize to yaml and then deserialize - and the code works correctly);
- you CAN NOT serialize an object by saving its source code.

When it comes to configuration and using of the application it must: 
- be configured with:
  - arguments from CLI (parse them with argparse);
  - config file with all arguments (if so, agrs from CLI must be ignored);
- work as:
  - library (from <my_lib> import json_serializer, etc.);
  - console util (my_util <arg1> <arg2> <arg3>, etc.);
- if it works as library - you must be able to install it to any other computer (pip install my_lib);
- it must be installed via setup.py file (in both variants);

Also:
- the application must be tested (at least 90% coverage);
- ANY LIBRARIES like pickle, json, etc. ARE BANNED!!!!
- eval(), exec() or saving the source code of the object to file ARE BANNED!!!!
