"""
change the twstag of a active/passive component that is patched
and see if get_changed_diff_patch picks it pu
"""

# instantiate all the components of styeditor

import page_style_editor as pse
from addict import Dict
from py_tailwind_utils import *
wp_endpoint_test = pse.create_endpoint('wp_components',
                                       key="test_page",
                                       
                                       title="Guinea pig"
                                    )

import ofjustpy as oj
request = Dict()
request.session_id = "abc"
session_manager = oj.get_session_manager(request)
wp = wp_endpoint_test(request)

# get the active object with key 'ti'


# ============================ milestone 1 ===========================
# Success: Working:  get_changed_diff_patch()  on Active components
# text_input_object = session_manager.stubStore['ti'].target
# text_input_object.add_twsty_tags(bg/blue/400)
# for _ in text_input_object.get_changed_diff_patch():
#     print (_)

# ================================ end ===============================

# ============================ milestone 2 ===========================
# Success: Working:  get_changed_diff_patch()  on mutable component
# btn_object = session_manager.stubStore['abtn'].target
# btn_object.add_twsty_tags(bg/red/900)
# ================================ end ===============================

# ============================ milestone 3 ===========================
# Note: This test is hardwired to the order in which childs are added in wp_components:wp_childs# Success: Working: get_changed_diff_patch()  on passive component
passive_hc_key = list(session_manager.stubStore.keys())[3]
passive_hc = session_manager.stubStore[passive_hc_key].target
passive_hc.add_twsty_tags(bg/pink/9)
# for _ in passive_div.get_changed_diff_patch():
#     print (_)
# ================================ end ===============================

# ============================ milestone 4 ===========================
# passive hc which is child of passive div
# we can track changes from webpage
# ================================ end ===============================

# ============================ milestone 5 ===========================
# ====================== changes to passive div ======================
# Success : Working: get_changed_diff_patch on passive_div
print (session_manager.stubStore.keys())
passive_div_key = list(session_manager.stubStore.keys())[2]
passive_div = session_manager.stubStore[passive_div_key].target
passive_div.add_twsty_tags(bg/pink/1)
# for _ in passive_div.get_changed_diff_patch():
#     print (_)

for _ in wp.get_changed_diff_patch():
    print(_)
# for _ in text_input_object.get_changed_diff_patch():
#     print (_)

# ================================ end ===============================
# import asyncio
#from ofjustpy_engine.jpcore.justpy_app import run_event_function
# wp_styeditor = wp.styeditor_endpoint(request)

# stubStore = wp_styeditor.session_manager.stubStore

# hinav = stubStore.hccomp_selector.hinav.target

# def to_ms(item):
#     return dget(stubStore, item.id).target

# # ================= Step 1: make abtn as selected hccomp object in hinav =================
# child0_ms = to_ms(hinav.staticCore.childpanel.childs[0])
# event_data = Dict()
# event_data.page = wp_styeditor
# asyncio.run(run_event_function(child0_ms, 'click', event_data, stubStore=stubStore))

# child0_ms = to_ms(hinav.staticCore.childpanel.childs[0])
# event_data = Dict()
# event_data.page = wp_styeditor
# asyncio.run(run_event_function(child0_ms, 'click', event_data, stubStore=stubStore))

