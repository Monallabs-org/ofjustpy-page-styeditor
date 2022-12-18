import jsbeautifier
import json

from py_tailwind_utils import dnew, dget
from py_tailwind_utils import *
from .styjson_utils import build_component_hierarchy
from unittest.mock import patch
from .styeditor_components import build_tw_styValues_panel, build_tw_styTags_panel
ui_app_trmap = []
import importlib

def debug_oj_patch_reset():
    oj = importlib.import_module('ofjustpy')
            
    # this should preceed the oj.htmlcomponents reload

    import ofjustpy_react as ojr
    importlib.reload(ojr)
    import ofjustpy_components as ojx
    importlib.reload(ojx)
    importlib.reload(oj.SHC_types)

    # Caution:Wisdom: importlib.reload(oj) will not have any effect
    # the oj.htmlcomponents needs to be reloaded
    importlib.reload(oj.htmlcomponents)

    # This line along with the above importlib.reload(oj.htmlcomponents) is crucial
    importlib.reload(oj)
    btn = oj.AC.Button(key="mybtn", text="A")
    print (type(btn))
    btn.build_json()

        
def build_styeditor_endpoint(target_wp):

    # Have no idea why this works
    # Don't change anything here

    # We don't know which line below is responsible for
    # resetting the patches. Don't change anything

    oj = importlib.import_module('ofjustpy')

    # this should preceed the oj.htmlcomponents reload

    import ofjustpy_react as ojr
    importlib.reload(ojr)
    import ofjustpy_components as ojx
    importlib.reload(ojx)
    importlib.reload(oj.SHC_types)
    # every submodule of oj needs to be reloaded
    importlib.reload(oj.HC_wrappers)

    # Caution:Wisdom: importlib.reload(oj) will not have any effect
    # the oj.htmlcomponents needs to be reloaded
    importlib.reload(oj.htmlcomponents)

    # This line along with the above importlib.reload(oj.htmlcomponents) is crucial
    # importlib.reload(oj)
    # btn = oj.AC.Button(key="mybtn", text="A")
    # print (type(btn))
    # btn.build_json()

    # logically moving after loading oj
    # logic didn't work
    # import ofjustpy_react as ojr
    # importlib.reload(ojr)
    # import ofjustpy_components as ojx
    # importlib.reload(ojx)
    # importlib.reload(oj.SHC_types)
        
    
    DOM_hierarchy = build_component_hierarchy(target_wp)

    def callback_hinav_terminal_selector(terminal_path):
        selected_hcobj = dget(DOM_hierarchy, terminal_path)
        print ('terminal path: spath_or_self', terminal_path, " ", selected_hcobj)        
        selected_hcobj.add_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
        oj.run_task(target_wp.update())
        
        pass

    hinav = ojx.HierarchyNavigator(DOM_hierarchy, callback_hinav_terminal_selector, key="myhinav", max_depth=15)
    hinav_depth_selector = oj.HCCMutable.StackH(childs = hinav.steps, twsty_tags=[space/x/4])

    # try to see if we can freely import modules with "import ofjuspty stmts"
    # free import failed -- we have to create the components here only
    # from . import editor_components

    twstyle_panel = build_tw_styValues_panel(oj)
    twtags_panel  = build_tw_styTags_panel(oj)
    
    tlc = oj.Mutable.Container(key="tlc", 
                               childs = [hinav_depth_selector,
                                         oj.Halign(hinav.childpanel, content_type="mutable"),
                                         hinav,
                                         twstyle_panel,
                                         twtags_panel
                                         ]

                               )

    wp_template = ojr.WebPage(key="styeditor_wp",
                              childs=[tlc],
                              ui_app_trmap_iter = ui_app_trmap,
                              title="Style editor",
                              head_html =  """<script src="https://cdn.tailwindcss.com"></script> """
                          )
    return oj.create_endpoint_impl(wp_template)




# ================================ end ===============================


