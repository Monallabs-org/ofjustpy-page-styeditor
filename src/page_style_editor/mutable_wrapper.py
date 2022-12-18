
# passive HC mixins:
# StaticCore, TR.PassiveKeyIdMixin, jsonMixinType, tagtype, TR.HCTextMixin
import json
from py_tailwind_utils import dget

# class MutableWrapper:
#     def __init__(self, passive_obj):
#         self.passive_obj = passive_obj


        
# class Wrapper_Stub_HCPassive:
#     def __init__(self, *args, **kwargs):
#         # The HC_Passive object
#         print ("The wrapper is the Stub")
#         self.target = kwargs.get("target")
#         assert False

#     def __call__(self, a):
#         assert False
        
#     @classmethod
#     def is_static(cls):
#         return False

#     @property
#     def key(self):
#         assert False

#     @property
#     def id(self):
#         assert False


# def passive_stub_cons_wrapper(stub_cons):
#     """
#     this function wrap/decorate passive stubs __call__ dunder func
#     """
#     def wrapper(*args, **kwargs):
#         print("captured the __init__ cons: replacing with mutable cons")
#         #passive_obj = stub_func(*args, **kwargs)
#         Wrapper_Stub_HCPassive(*args, **kwargs)
#     return wrapper


def wrapper_is_static(self):
    print("mock replace function: is_static is called")
    return False

def wrapper_id(self):

    return id(self.target)


# def wrapper_build_json(f):
#     """
#     attach id to the json being constructed
#     """
#     def wrapper(*args, **kwargs):
#         self = args[0]
#         self.domDict.id = id(self)
#         self.attrs.id = id(self)
#         print("mock replace function: build_json is called: ", f)
#         f(*args, **kwargs)
#         print ("obj_json = ", self.obj_json)
#     return wrapper


# def wrapper_get_changed_diff_patch(f):
#     def wrapper(*args, **kwargs):
#         print ("mock replace function = get_changed_diff_patch")
#         assert False
#         #yield from f(*args, **kwargs)
        
#     return wrapper

from ofjustpy_engine.HC_Div_type_mixins import (jpBaseComponentMixin,
                                                TwStyMixin,
                                                DOMEdgeMixin
                                                )

from addict_tracking_changes import Dict
import traceback
import sys
class StaticCore(
    jpBaseComponentMixin,
    TwStyMixin,
    DOMEdgeMixin
):
    """
    provides baseComponent (id, show, debounce, etc)
             divBase: (text, object_props)
             Label: label tag and label specific attributes
    """

    def __init__(self, *args, **kwargs):
        #print("===========================================================")
        
        #print ("initializing from mutable_wrapped Static core")
        #traceback.print_stack(file=sys.stdout)
        #print("===========================================================")
        self.domDict = Dict(track_changes=True)
        self.attrs = Dict(track_changes=True)
        jpBaseComponentMixin.__init__(
            self, domDict=self.domDict, attrs=self.attrs, **kwargs
        )
        DOMEdgeMixin.__init__(
            self, *args, domDict=self.domDict, attrs=self.attrs, **kwargs
        )
        TwStyMixin.__init__(
            self, *args, domDict=self.domDict, attrs=self.attrs, **kwargs
        )

        

class JsonMixin:
    """Mixin for static objects that have id/event handler attached to it."""

    def __init__(self, *args, **kwargs):
        self.obj_json = None
        pass

    def get_obj_props_json(self):
        return "[]"

    def build_json(self):
        print ("calling wrapped build_json")
        domDict_json = json.dumps(self.domDict, default=str)[1:-1]
        attrs_json = json.dumps(self.attrs, default=str)[1:-1]
        object_props_json = self.get_obj_props_json()

        self.obj_json = f"""{{ {domDict_json},  "attrs":{{ {attrs_json} }}, "object_props":{object_props_json} }}"""
        self.domDict.clear_changed_history()

    def convert_object_to_json(self, parent_hidden=False):
        return self.obj_json

    def get_obj_props_changed_diff_patch(self):
        return
        yield


    def get_mutable_shell_diff_patch(self):
        return
        yield
        
    def get_changed_diff_patch(self, parent_hidden=False):
        yield from self.get_mutable_shell_diff_patch()
        self.clear_changed_history()
        yield from self.get_obj_props_changed_diff_patch()


    def clear_changed_history(self):
        self.attrs.clear_changed_history()
        self.domDict.clear_changed_history()
        
class PassiveJsonMixin(JsonMixin):
    """
    passive items that do not have id/key
    """

    def __init__(self, *args, **kwargs):
        print ("From WrappedPassiveJsonMixin: init")
        JsonMixin.__init__(self, *args, **kwargs)
        self.domDict.id = id(self)
        self.attrs.id = id(self)
        # self.build_json()
        pass
    # def get_changed_diff_patch(self, parent_hidden=False):
        
    #     print ("From WrappedPassiveJsonMixin: get_changed_diff_patch")
    #     print ([_ for _ in self.domDict.get_changed_history()])
    #     return
    #     yield

    def get_mutable_shell_diff_patch(self):
        if not self.domDict.has_changed_history():
            return
            yield
        
        domDict_patch_kv = ""
        domDict_patch_kv = ",".join(
            [
                f""" "{k}":  {json.dumps(dget(self.domDict, k))} """
                for k in self.domDict.get_changed_history()
            ]
        )
        if domDict_patch_kv != "":
            domDict_patch_kv = f""" "domDict": {{ {domDict_patch_kv} }}"""
            
            yield f""" "{self.id}" : {{  {domDict_patch_kv} }} """

        else:
            return
            yield

            
def get_styedit_A():
    import importlib
    SHC_comp = importlib.import_module('ofjustpy.SHC_types')
    # The reload is crucial
    # it will reset all the patch done prior
    importlib.reload(SHC_comp)
    
    styedit_A = SHC_comp.PassiveComponents.A(href="/styedit",
                                 text="Style Editor",
                                 target="_blank"
                                 )
    print("Oring A = ", SHC_comp.PassiveComponents.A)
    return styedit_A
    
# class Stub_HCPassive:
#     def __init__(self, *args, **kwargs):
#         self.target = kwargs.get("target")

#     def register_childrens(self):
#         # HC are not div elements and do not
#         # contain childrens

#         pass

#     @classmethod
#     def is_static(cls):
#         print ("called wrapped is_static")
#         return False

#     def __call__(self, a, attach_to_parent=True):
#         """
#         if the both parent and child are static
#         then child is already attached at setup/initialized time

#         """
#         if attach_to_parent:
#             # if parent is static then childs are declared
#             # during setup/initialization
#             a.add_component(self.target)
#         self.register_childrens()

#         if not self.target.obj_json:
#             self.target.build_json()
#         return self.target

#     @property
#     def id(self):
#         print ("From Wrapped")
#         raise self
    
    
#     @property
#     def key(self):
#         print ("From Wrapped")
#         raise id(self)
        
#     pass
        
