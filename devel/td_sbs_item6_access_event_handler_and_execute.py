"""
in the rendered page grab hold of event handler and execute.
"""

# instantiate all the components of styeditor

import page_style_editor as pse

import json
import jsbeautifier


wp_endpoint_test = pse.create_endpoint('wp_components',
                                       key="test_page",
                                       
                                       title="Guinea pig"
                                    )
from addict import Dict
request = Dict()
request.session_id = "abc"
wp = wp_endpoint_test(request)
wp_styeditor = wp.styeditor_endpoint(request)

stubStore = wp_styeditor.session_manager.stubStore


# click_ev = stubStore.selection_panel.utilityClass_colorSelector.target.get_event_handler('click')
# print (click_ev)

# # call click_ev

# click_ev(color_selector_obj, msg, to_ms)
color_selector_obj = stubStore.selection_panel.utilityClass_colorSelector.target

import ofjustpy as oj
from ofjustpy_engine.jpcore.justpy_app import run_event_function
event_data = Dict()
event_data.page = wp_styeditor

import asyncio
asyncio.run(run_event_function(color_selector_obj, 'click', event_data, stubStore))
