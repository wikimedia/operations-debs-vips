# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('vdisplaymodule', [dirname(__file__)])
        except ImportError:
            import vdisplaymodule
            return vdisplaymodule
        if fp is not None:
            try:
                _mod = imp.load_module('vdisplaymodule', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    vdisplaymodule = swig_import_helper()
    del swig_import_helper
else:
    import vdisplaymodule
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


import VError
class VDisplay(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VDisplay, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VDisplay, name)
    __repr__ = _swig_repr
    BARCO = vdisplaymodule.VDisplay_BARCO
    DUMB = vdisplaymodule.VDisplay_DUMB
    def __init__(self, *args): 
        this = vdisplaymodule.new_VDisplay(*args)
        try: self.this.append(this)
        except: self.this = this
    def __assign__(self, *args): return vdisplaymodule.VDisplay___assign__(self, *args)
    __swig_destroy__ = vdisplaymodule.delete_VDisplay
    __del__ = lambda self : None;
    def disp(self): return vdisplaymodule.VDisplay_disp(self)
    def luts(self): return vdisplaymodule.VDisplay_luts(self)
VDisplay_swigregister = vdisplaymodule.VDisplay_swigregister
VDisplay_swigregister(VDisplay)

# This file is compatible with both classic and new-style classes.


