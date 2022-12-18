import jsbeautifier
import json

from py_tailwind_utils import dnew, dget
from py_tailwind_utils import *
from .styjson_utils import build_component_hierarchy

ui_app_trmap = []

def build_styeditor_endpoint(target_wp):
    import ofjustpy_react as ojr
    import ofjustpy as oj
    import ofjustpy_components as ojx
    DOM_hierarchy = build_component_hierarchy(target_wp)
    def callback_hinav_terminal_selector(terminal_path):
        selected_hcobj = dget(DOM_hierarchy, terminal_path)
        print ('terminal path: spath_or_self', terminal_path, " ", selected_hcobj)        
        selected_hcobj.add_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
        oj.run_task(target_wp.update())
        
        pass

    hinav = ojx.HierarchyNavigator(DOM_hierarchy, callback_hinav_terminal_selector, key="myhinav", max_depth=15)
    hinav_depth_selector = oj.HCCMutable.StackH(childs = hinav.steps, twsty_tags=[space/x/4])
    tlc = oj.Mutable.Container(key="tlc", 
                               childs = [hinav_depth_selector,
                                         oj.Halign(hinav.childpanel, content_type="mutable"),
                                         hinav
                                         ]

                               )

    wp_template = ojr.WebPage(key="styeditor_wp",
                              childs=[tlc],
                              ui_app_trmap_iter = ui_app_trmap,
                              title="Style editor"
                          )
    return oj.create_endpoint_impl(wp_template)




# ================================ end ===============================


