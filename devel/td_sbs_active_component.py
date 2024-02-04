"""
one a single page is allowed to be edited at a time
"""

import page_style_editor as pse

import json
import jsbeautifier


wp_endpoint_test = pse.create_endpoint('wp_components', key="test_page",
                                       
                                    title="Guinea pig"
                                    )

import ofjustpy as oj
app = oj.load_app()
    
app.add_jproute("/x", wp_endpoint_test)

# ========================= devel/test/debug =========================
# from addict_tracking_changes import Dict

# request = Dict()
# request.session_id = "abc"
# wp = wp_endpoint_test(request)

# # # print("Calling JSON")
# wp_json = wp.build_json()
# opts = jsbeautifier.default_options()
# res = jsbeautifier.beautify(wp_json, opts)
# print(res)

# mbtn_ms = wp.components[0]
# ev_handler = mbtn_ms.get_event_handler("on_click")
# print(ev_handler)


# ev_handler(mbtn_ms, None, None)

# for _ in wp.get_changed_diff_patch():
#     res = jsbeautifier.beautify(_, opts)
#     print(res)

# ================================ end ===============================

# editor_wp = styeditor.wp_index(request)

# from starlette.testclient import TestClient
# testclient = TestClient(app)
# response = testclient.get(f'/x')
# response = testclient.get(f'/styedit')
# with patch.object(ofjustpy_engine.SHC_types_mixin.PassiveJsonMixin,
#                                                                                                                                                                     'get_changed_diff_patch',
#                                                                                                                                                                     return_value = wrapper_get_changed_diff_patch(ofjustpy_engine.SHC_types_mixin.PassiveJsonMixin.get_changed_diff_patch)
#                                                                                                                                                                     ):

# HOST="192.168.0.187"
# PORT=8000

# uvicorn_config = uvicorn.config.Config(
#                 app, host=HOST, port=PORT
#             )
# jp_server = uvicorn.Server(uvicorn_config)

# jp_server.run()
