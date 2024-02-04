
import page_style_editor.redo_init as pse
import json
import jsbeautifier
import asyncio
from ofjustpy_engine.jpcore.justpy_app import run_event_function
from py_tailwind_utils import *
wp_endpoint_test = pse.create_endpoint('wp_components',
                                       key="test_page",
                                       
                                       title="Guinea pig"
                                       )
# from addict_tracking_changes import Dict

# request = Dict()
# request.session_id = "abc"
# wp = wp_endpoint_test(request)
# ss = wp.session_manager.stubStore



# print(ss.keys())
# event_data = Dict()
# event_data.page = wp
# pspan = wp.components[0]
# c = dget(ss, pspan.id).target
# print(pspan.id)
# print(ss)

# print(c)
# print(dget(ss, pspan.id))
# print (pspan.domDict)
# asyncio.run(run_event_function(pspan,
#                                'mouseenter',
#                                event_data,`
#                                stubStore=ss)
#             )
# print(ss)

# # print(wp.components)
import ofjustpy as oj
app = oj.load_app()
app.add_jproute("/x", wp_endpoint_test)

