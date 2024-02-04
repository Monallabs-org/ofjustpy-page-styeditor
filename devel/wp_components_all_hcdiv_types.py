from py_tailwind_utils import *
from addict_tracking_changes import Dict

def build_childs(oj):
    mbtn = oj.Mutable.Button(key="abtn", text="mutable button", twsty_tags=[bg/blue/3])
    mdiv = oj.Mutable.Div(key="mdiv", childs = [mbtn], twsty_tags=[W/64, H/64, bg/green/1])
    
    hccmutable = oj.HCCMutable.Div(childs=[mdiv])
    
    
    
    pspan = oj.PC.Span(text="Passive span", twsty_tags=[bg/blue/3])
    pdiv = oj.PC.Div(childs = [pspan])
    hccstatic = oj.HCCStatic.Div(key="hccstatic", childs = [pdiv])
    def on_input(dbref, msg, to_target):
        print ("input recieved")

    ti = oj.AC.TextInput(key = "ti", placeholder="abc", twsty_tags=[W/64, H/8, bg/pink/1],
                         on_change = on_input
                         )
    si = oj.AC.Select(key="select",
                 childs=[oj.PC.Option(text="hellow", twsty_tags=[bg/green/1])
                                       ]
                 )
    
    # def on_btn_click(dbref,  msg, to_target):
    #     print ("button clicked called")
    #     print (type(dbref))
    #     dbref.add_twsty_tags(outline._, outline/yellow/4)
    #     pspan.add_twsty_tags(outline._,  outline/yellow/4)
    #     pass

    # mbtn.on('click', on_btn_click)


    # do not modify or change order of the children
    # the test: /home/kabiraatmonallabs/to_githubcodes/org-ofjustpy/page-style-editor/devel/td_sbs_item4_hinav_selection.py
    # dependes on the order 

    wp_childs = [mbtn, pdiv, ti, si]
    return wp_childs
