"""
in the rendered page grab hold of event handler and execute.
"""

# instantiate all the components of styeditor

import page_style_editor as pse
from py_tailwind_utils import *
import json
import jsbeautifier
from ofjustpy_engine.jpcore.justpy_app import run_event_function
from addict import Dict
import asyncio

import ofjustpy as oj
wp_endpoint_test = pse.create_endpoint('wp_components',
                                       key="test_page",
                                       
                                       title="Guinea pig"
                                    )

request = Dict()
request.session_id = "abc"
session_manager = oj.get_session_manager(request)
wp = wp_endpoint_test(request)
wp_styeditor = wp.styeditor_endpoint(request)

stubStore = wp_styeditor.session_manager.stubStore

hinav = stubStore.hccomp_selector.hinav.target

def to_ms(item):
    return dget(stubStore, item.id).target

# ================= Step 1: make abtn as selected hccomp object in hinav =================
child0_ms = to_ms(hinav.staticCore.childpanel.childs[0])
event_data = Dict()
event_data.page = wp_styeditor
asyncio.run(run_event_function(child0_ms, 'click', event_data, stubStore=stubStore))

child0_ms = to_ms(hinav.staticCore.childpanel.childs[0])
event_data = Dict()
event_data.page = wp_styeditor
asyncio.run(run_event_function(child0_ms, 'click', event_data, stubStore=stubStore))



# ================= Step 2: Choose a color =================
color_selector_obj = stubStore.selection_panel.utilityClass_colorSelector.target
color_selector_obj.mcs_value = "green"
color_selector_obj.scs_value = "5"
event_data = Dict()
event_data.page = wp_styeditor
asyncio.run(run_event_function(color_selector_obj, 'click', event_data, stubStore))

# ================= Step 3: Apply the color =================
color_apply_btn_obj = stubStore.selection_panel.color_apply_btn.target
event_data = Dict()
event_data.page = wp_styeditor

asyncio.run(run_event_function(color_apply_btn_obj, 'click', event_data, stubStore))
