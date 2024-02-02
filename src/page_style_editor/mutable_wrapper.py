
# passive HC mixins:
# StaticCore, TR.PassiveKeyIdMixin, jsonMixinType, tagtype, TR.HCTextMixin
import json
from py_tailwind_utils import *

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


# this wrapper is no longer required
# keeping it around until everything is working again. 
def wrapper_is_static(self):
    print("mock replace function: is_static is called")
    return False

# this wrapper is no longer required
# keeping it around until everything is working again. 
def wrapper_id(self):
    
    return self.target.id


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
                                                DOMEdgeMixin,
                                                #EventMixin
                                                )

from addict_tracking_changes import Dict
import traceback
import sys

# class EventMixinBase:
#     """
#     for active components.
#     attach event handlers to HC;

#     :param event_modifiers: A dictionary to store event modifiers.
#     :type event_modifiers: dict, optional

#     :param transition: Stores transition information for the component.
#     :type transition: Any, optional

#     :param event_handlers: A dictionary that associates event types with their corresponding event handling functions.
#     :type event_handlers: dict, optional

#     :param event_prehook: A prehook function to be applied to all event handlers.
#     :type event_prehook: Callable, optional

#     :param allowed_events: A list of allowed event types.
#     :type allowed_events: list, optional

#     """

#     def __init__(self, *args, **kwargs):
#         self.domDict.event_modifiers = Dict()
#         self.domDict.transition = None

#         self.event_handlers = {}

#         # event_prehook applies to all the events
#         # get handler via event_prehook(func) and call
#         # that when invoked
#         self.event_prehook = kwargs.get("event_prehook", None)
#         self.set_keyword_events(**kwargs)
#         pass

#     def set_keyword_events(self, **kwargs):
#         for e in self.allowed_events:
#             for prefix in ["", "on", "on_"]:
#                 if prefix + e in kwargs.keys():
#                     fn = kwargs[prefix + e]
#                     self.on(e, fn)
#                     break

#     def on(
#         self,
#         event_type,
#         func,
#         *,
#         debounce=None,
#         throttle=None,
#         immediate=False,
#     ):
#         if event_type in self.allowed_events:
#             if not self.event_prehook:
#                 self.event_handlers["on_" + event_type] = func
#             else:
#                 self.event_handlers["on_" + event_type] = self.event_prehook(func)
#                 pass

#             if event_type not in self.domDict.events:
#                 self.domDict.events.append(event_type)
#             self.htmlRender_attr.append(f"""on{event_type}='eventHandler(event)'""")
            
#             # if debounce:
#             #     self.domDict.event_modifiers[event_type].debounce = {
#             #         "value": debounce,
#             #         "timeout": None,
#             #         "immediate": immediate,
#             #     }
#             # elif throttle:
#             #     self.domDict.event_modifiers[event_type].throttle = {
#             #         "value": throttle,
#             #         "timeout": None,
#             #     }
#         else:
#             raise Exception(f"No event of type {event_type} supported")
#         # events have changed: repare the htmlRenderer
#         self.prepare_htmlRender()

#     def add_prehook(self, prehook_func):
#         """
#         apply prehook to all the registered event handlers
#         """
#         for e in self.allowed_events:
#             if "on_" + e in self.event_handlers:
#                 ufunc = self.event_handlers["on_" + e]
#                 self.event_handlers["on_" + e] = prehook_func(ufunc)

#     def remove_event(self, event_type):
#         # if event_type in self.domDict.events:
#         #     self.domDict.events.remove(event_type)
#         # self.htmlRender_attr.remove(f"""on{event_type}='eventHandler(event)'""")
#         raise Exception("Implemented -- but to be tested")

#     def has_event_function(self, event_type):
#         if getattr(self, "on_" + event_type, None):
#             return True
#         else:
#             return False

#     def add_event(self, event_type):
#         if event_type not in self.domDict.allowed_events:
#             self.allowed_events.append(event_type)

#     def get_event_handler(self, event_type):
#         return self.event_handlers['on_' + event_type]

#     def add_allowed_event(self, event_type):
#         self.add_event(event_type)

#     @property
#     def events(self):
#         return self.domDict.events

#     @events.setter
#     def events(self, value):
#         self.domDict.events = value

#     # @property
#     # def event_modifiers(self):
#     #     return self.domDict.event_modifiers

#     # @event_modifiers.setter
#     # def event_modifiers(self, value):
#     #     self.domDict.event_modifiers = value

#     @property
#     def event_propagation(self):
#         return self.domDict.get("event_propagation", None)

#     @event_propagation.setter
#     def event_propagation(self, value):
#         if value is not None:
#             self.domDict["event_propagation"] = value


# class EventMixin(EventMixinBase):
#     """Mixin to associate event handlers with html components

#     :param on_click: handler for click event
#     :type event_modifiers: Callable, optional

#     :param on_mouseover: handler for mouseover event
#     :type event_modifiers: Callable, optional

#     :param on_mouseout: handler for mouseout event
#     :type event_modifiers: Callable, optional

#     :param on_mouseenter: handler for mouseenter event
#     :type event_modifiers: Callable, optional

#     :param on_mouseleave: handler for mouseleave event
#     :type event_modifiers: Callable, optional

#     :param on_input: handler for input event
#     :type event_modifiers: Callable, optional

#     :param on_change: handler for change event
#     :type event_modifiers: Callable, optional

#     :param on_after: handler for after event
#     :type event_modifiers: Callable, optional

#     :param on_before: handler for before event
#     :type event_modifiers: Callable, optional

#     :param on_keydown: handler for keydown event
#     :type event_modifiers: Callable, optional

#     :param on_keyup: handler for keyup event
#     :type event_modifiers: Callable, optional

#     :param on_keypress: handler for keypress event
#     :type event_modifiers: Callable, optional

#     :param on_focus: handler for focus event
#     :type event_modifiers: Callable, optional

#     :param on_blur: handler for blur event
#     :type event_modifiers: Callable, optional

#     :param on_submit: handler for submit event
#     :type event_modifiers: Callable, optional

#     :param on_dragstart: handler for dragstart event
#     :type event_modifiers: Callable, optional

#     :param on_dragover: handler for dragover event
#     :type event_modifiers: Callable, optional

#     :param on_drop: handler for drop event
#     :type event_modifiers: Callable, optional

#     :param on_click__out: handler for click__out event
#     :type event_modifiers: Callable, optional

#     """

#     allowed_events = [
#         "click",
#         "mouseover",
#         "mouseout",
#         "mouseenter",
#         "mouseleave",
#         "input",
#         "change",
#         "after",
#         "before",
#         "keydown",
#         "keyup",
#         "keypress",
#         "focus",
#         "blur",
#         "submit",
#         "dragstart",
#         "dragover",
#         "drop",
#         "click__out",
#     ]

#     def __init__(self, *args, **kwargs):
#         EventMixinBase.__init__(self, *args, **kwargs)
        
#         #self.htmlRender_attr.extend([f"""on{key}='eventHandler(event)'""" for key in map(lambda _: _.split("_")[1], self.event_handlers.keys())])
        

        
# class StaticCore(
#         jpBaseComponentMixin,
#         TwStyMixin,
#         DOMEdgeMixin,
#         EventMixin
# ):
#     """
#     provides baseComponent (id, show, debounce, etc)
#              divBase: (text, object_props)
#              Label: label tag and label specific attributes
#     """

#     def __init__(self, *args, **kwargs):
#         #print("===========================================================")
#         #traceback.print_stack(file=sys.stdout)
#         #print("===========================================================")
        
#         self.domDict = Dict(track_changes=True)
#         self.attrs = Dict(track_changes=True)
#         jpBaseComponentMixin.__init__(
#             self, domDict=self.domDict, attrs=self.attrs, **kwargs
#         )
#         DOMEdgeMixin.__init__(
#             self, *args, domDict=self.domDict, attrs=self.attrs, **kwargs
#         )
#         TwStyMixin.__init__(
#             self, *args, domDict=self.domDict, attrs=self.attrs, **kwargs
#         )
#         assert False
#         EventMixin.__init__(
#             self, *args, **kwargs
#             )

        

class JsonMixin:
    """Mixin for static objects that have id/event handler attached to it."""

    def __init__(self, *args, **kwargs):
        self.obj_json = None
        pass

    def get_obj_props_json(self):
        return "[]"

    def build_json(self):
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

        JsonMixin.__init__(self, *args, **kwargs)
        self.domDict.id = id(self)
        self.attrs.id = id(self)

        pass


class ActiveJsonMixin(JsonMixin):
    """
    passive items that do not have id/key
    """

    def __init__(self, *args, **kwargs):
        JsonMixin.__init__(self, *args, **kwargs)
        # no need to init id
        # id components already have ids
        

        pass
    

class HCCPassiveJsonMixin(PassiveJsonMixin):
    def __init__(self, *args, **kwargs):
        PassiveJsonMixin.__init__(self, *args, **kwargs)


    def get_obj_props_json(self):
        return (
            "[" + ",".join([_.convert_object_to_json() for _ in self.components]) + "]"
        )
    
    def get_obj_props_changed_diff_patch(self, parent_hidden=False):
        is_hidden = False  # "hidden" in self.classes
        if not parent_hidden:
            for obj in self.components:
                # no need to render hidden objects
                # save on comm and frontend rendering
                # if not "hidden" in self.classes:
                yield from obj.get_changed_diff_patch(parent_hidden=is_hidden)
        else:
            return
            yield

        
            
def get_styedit_A():
    """
    get the non-patched version A component
    that points to /styedit
    """
    import importlib
    SHC_comp = importlib.import_module('ofjustpy.SHC_types')
    # The reload is crucial
    # it will reset all the patch done prior
    importlib.reload(SHC_comp)

    styedit_A = SHC_comp.PassiveComponents.A(href="/styedit",
                                 text="Style Editor",
                                 target="_blank"
                                 )

    # need this roundabout way
    # to create a unpatched button 
    htmlcomponents_comp = importlib.import_module('ofjustpy.htmlcomponents')
    resume_selection_btn = htmlcomponents_comp.ActiveComponents.Button(key="reset_button",
                                        text="Resume Selection",
                                        twsty_tags=[mr/4, pd/4],
                                        )
    return styedit_A, resume_selection_btn
    
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

