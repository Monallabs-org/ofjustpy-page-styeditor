from py_tailwind_utils import *
from addict_tracking_changes import Dict

#def build_childs(oj):
import ofjustpy as oj
mbtn = oj.Mutable.Button(key="abtn", text="mutable button", twsty_tags=[bg/blue/3])
# mdiv = oj.Mutable.Div(key="mdiv", childs = [mbtn], twsty_tags=[W/64, H/64, bg/green/1])

print("--------------------------------------------------------------____<<<<<<<<<<<<<<<<<")
hccmutable = oj.HCCMutable.Div(childs=[mbtn], twsty_tags=[W/"1/2", H/16, bg/red/4])
print ("Done")
pspan = oj.PC.Span(text="Passive span", twsty_tags=[bg/blue/3, W/8, H/8, bg/blue/1])
pdiv = oj.PC.Div(childs = [pspan], twsty_tags=[W/64, H/64, bg/green/1])

hccstatic = oj.HCCStatic.Div(key="hccstatic",
                             childs = [pdiv],
                             twsty_tags=[W/"2/3", H/"2/3", bg/pink/1]
                             )

wp_childs = [hccmutable,
             hccstatic
             ]
#return wp_childs
