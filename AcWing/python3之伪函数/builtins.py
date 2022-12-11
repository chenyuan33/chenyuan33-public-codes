'''
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
'''
import builtins, sys
class object:
    '''
    The base class of the class hierarchy.
    
    When called, it accepts no arguments and returns a new featureless
    instance that has no instance attributes and cannot be given any.
    
    '''
    def __delattr__(self, name):
        '''
        Implement delattr(self, name).
        '''
        delattr(self, name)
    def __dir__(self):
        return [
                '__new__',
                '__repr__',
                '__hash__',
                '__str__',
                '__getattribute__',
                '__setattr__',
                '__delattr__',
                '__lt__',
                '__le__',
                '__eq__',
                '__ne__',
                '__gt__',
                '__ge__',
                '__init__',
                '__reduce_ex__',
                '__reduce__',
                '__subclasshook__',
                '__init_subclass__',
                '__format__',
                '__sizeof__',
                '__dir__',
                '__class__',
                '__doc__'
               ]
    def __eq__(self, value):
        '''
        Return self==value.
        '''
        return self is value
    def __format__(self, format_spec):
        '''
        Default object formatter.
        '''
        return format_spec % self
    def __ge__(self, value):
        '''
        Return self>=value.
        '''
        raise TypeError("'>=' not supported between instances of 'object' and 'object'")
    def __getattribute__(self, name):
        '''
        Return getattr(self, name).
        '''
        if name in dir(self):
            return eval('self.' + name)
        else:
            raise AttributeError("'object' object has no attribute " + repr(name))
    def __gt__(self, value):
        '''
        Return self>value.
        '''
        raise TypeError("'>' not supported between instances of 'object' and 'object'")
    def __hash__(self):
        '''
        Return hash(self).
        '''
        return hash(id(self))
    def __init__(self):
        '''
        Initialize self.  See help(type(self)) for accurate signature.
        '''
    def __le__(self, value):
        '''
        Return self<=value.
        '''
        raise TypeError("'<=' not supported between instances of 'object' and 'object'")
    def __lt__(self, value):
        '''
        Return self<value.
        '''
        raise TypeError("'<' not supported between instances of 'object' and 'object'")
    def __ne__(self, value):
        '''
        Return self!=value.
        '''
        return not(self == value)
    def __reduce__(self):
        '''
        Helper for pickle.
        '''
        def _reconstructor(cls, base, state):
            if base is object:
                obj = object.__new__(cls)
            else:
                obj = base.__new__(cls, state)
                if base.__init__ != object.__init__:
                    base.__init__(obj, state)
            return obj
        return _reconstructor, (object, object, None)
    def __reduce_ex__(self, protocol):
        '''
        Helper for pickle.
        '''
        return self.__reduce__()
    def __repr__(self):
        '''
        Return repr(self).
        '''
        return f'<object object as {hex(id(self))}>'
    def __setattr__(self, name, value):
        '''
        Implement setattr(self, name, value).
        '''
        eval(f'self.{name} = {value}')
    def __sizeof__(self):
        '''
        Size of object in memory, in bytes.
        '''
        return 16
    def __str__(self):
        '''
        Return str(self).
        '''
        return repr(self)
def __import__(name, globals = None, locals = None, fromlist = (), level = 0) -> type(__builtins__):
    '''
    __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module

    Import a module. Because this function is meant for use by the Python
    interpreter and not for general use, it is better to use
    importlib.import_module() to programmatically import a module.

    The globals argument is only used to determine the context;
    they are not modified.  The locals argument is unused.  The fromlist
    should be a list of names to emulate ``from name import ...'', or an
    empty list to emulate ``import name''.
    When importing a module from a package, note that __import__('A.B', ...)
    returns package A when fromlist is empty, but its submodule B when
    fromlist is not empty.  The level argument is used to determine whether to
    perform absolute or relative imports: 0 is absolute, while a positive number
    is the number of parent directories to search relative to the current module.
    '''
    return eval(f'import {name}' if fromlist in [(), [], set(), '', {}] else f'from {name} import {', '.join(fromlist)}')
def input(*prompt):
    '''
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
    '''
    if len(prompt) > 1:
        raise TypeError('input() takes no keyword arguments') from None
    if prompt != ():
        print(prompt)
    for i in sys.stdin:
        return i[:-1]
def print(*value, sep = ' ', end = '\n', file = sys.stdout, flush = False):
    '''
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    '''
    file.write(sep.join(value) + end)
__builtins__ = builtins
copyright = _sitebuiltins._Printer('', '''\
Copyright (c) 2001-2022 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.\
''')
credits = _sitebuiltins._Printer('', '''\
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.\
''')
exit = _sitebuiltins.Quitter('exit', 'Ctrl-D (end-of-file)')
help = _sitebuiltins._Helper()
