#import ofjustpy as oj
from py_tailwind_utils import *
from addict_tracking_changes import Dict

#app = oj.load_app()

#specimen = oj.AC.Button(key="abtn", text="labeltext", twsty_tags=[bg/blue/3])

def build_childs(oj):
    si = oj.AC.Select(key="select",
                      childs=[                                       ]
                 )
    pdiv = oj.PC.Div(childs = [si])
    
    wp_childs = [pdiv]
    return wp_childs


