'''
Generic (shallow and deep) copying operations.

Interface summary:

import copy

x = copy.copy(y)        # make a shallow copy of y
x = copy.deepcopy(y)    # make a deep copy of y

For module specific errors, copy.Error is raised.

The difference between shallow and deep copying is only relevant for
compound objects (objects that contain other objects, like lists or
class instances).

- A shallow copy constructs a new compound object and then (to the
extent possible) inserts *the same objects* into it that the
original contains.
- A deep copy constructs a new compound object and then, recursively,
inserts *copies* into it of the objects found in the original.

Two problems often exist with deep copy operations that don't exist
with shallow copy operations:

a) recursive objects (compound objects that, directly or indirectly,
contain a reference to themselves) may cause a recursive loop

b) because deep copy copies *everything* it may copy too much, e.g.
administrative data structures that should be shared even between
copies

Python's deep copy operation avoids these problems by:

a) keeping a table of objects already copied during the current
copying pass

b) letting user-defined classes override the copying operation or the
set of components copied\n\nThis version does not copy types like module, class, function, method,
nor stack trace, stack frame, nor file, socket, window, nor any\nsimilar types.

Classes can use the same interfaces to control copying that they use\nto control pickling: they can define methods called __getinitargs__(),
__getstate__() and __setstate__().  See the documentation for module
"pickle" for information on these methods.

'''
__all__ = ['Error', 'copy', 'deepcopy']
def copy(obj):
    '''
    Shallow copy operation on arbitrary Python objects.
    
    See the module's __doc__ string for more info.
    
    '''
    res = obj
    for i in range(len(obj)):
        res[i] = res[i]
    return res
def deepcopy(obj):
    '''
    Deep copy operation on arbitrary Python objects.
    
    See the module's __doc__ string for more info.
    
    '''
    res = obj
    for i in range(len(obj)):
        if all(map(lambda x: type(res[i]) == x, dict, list, set, str, tuple)):
            res[i] = deepcopy(res[i])
        else:
            res[i] = res[i]
    return res
