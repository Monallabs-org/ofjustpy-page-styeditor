"""
one a single page is allowed to be edited at a time
"""

import page_style_editor as pse

import json
import jsbeautifier


wp_endpoint_test = pse.create_endpoint('wp_components',
                                       key="test_page",
                                       
                                       title="Guinea pig"
                                    )
# Caution: import oj after endpoint creation
import ofjustpy as oj
app = oj.load_app()
    
app.add_jproute("/x", wp_endpoint_test)

# ========================= devel/test/debug =========================
# from addict_tracking_changes import Dict

# request = Dict()
# request.session_id = "abc"
# wp = wp_endpoint_test(request)
# wp_styeditor = wp.styeditor_endpoint(request)
