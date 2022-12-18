import ofjustpy as oj
from py_tailwind_utils import *
from addict_tracking_changes import Dict

app = oj.load_app()

specimen = oj.AC.Button(key="abtn", text="labeltext", twsty_tags=[bg/blue/3])

mbtn = oj.Mutable.Button(key="abtn", text="mutable button", twsty_tags=[bg/blue/3])
pspan = oj.PC.Span(text="Passive span", twsty_tags=[bg/blue/3])


def on_btn_click(dbref,  msg, to_target):
    print ("button clicked called")
    print (type(dbref))
    dbref.add_twsty_tags(outline._, outline/yellow/4)
    pspan.add_twsty_tags(outline._,  outline/yellow/4)
    pass

mbtn.on('click', on_btn_click)

wp_childs = [mbtn, pspan] 

