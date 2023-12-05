import ofjustpy as oj
from py_tailwind_utils import *
from addict_tracking_changes import Dict

app = oj.load_app()
pspan = oj.PC.Span(text="Passive span", twsty_tags=[bg/blue/3])
wp_childs = [pspan]


