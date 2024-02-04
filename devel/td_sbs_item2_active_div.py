import page_style_editor as pse
from addict import Dict
from py_tailwind_utils import *
wp_endpoint_test = pse.create_endpoint('wp_components_active_div',
                                       key="test_page",
                                       
                                       title="Guinea pig"
                                    )

import ofjustpy as oj
request = Dict()
request.session_id = "abc"
session_manager = oj.get_session_manager(request)
wp = wp_endpoint_test(request)
wp_styeditor = wp.styeditor_endpoint(request)

active_div = session_manager.stubStore['select'].target

active_div.add_twsty_tags(bg/green/9)

# print (active_div.domDict)

# ===================== Milestone 1: Success: Active Div works ====================
for _ in wp.get_changed_diff_patch():
    print (_)

# ===================== Milestone 2: Success: Active Div within PC.Div ====================    
    
