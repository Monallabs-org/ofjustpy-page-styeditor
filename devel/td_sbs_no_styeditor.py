
import json
import jsbeautifier
import wp_components

import ofjustpy as oj
wp_endpoint_test = oj.create_endpoint(childs = wp_components.wp_childs,
                                       key="test_page",
                                       
                                       title="Guinea pig"
                                    )
# Caution: import oj after endpoint creation
app = oj.load_app()
    
app.add_jproute("/x", wp_endpoint_test)

# ========================= devel/test/debug =========================
# from addict_tracking_changes import Dict

# request = Dict()
# request.session_id = "abc"
# wp = wp_endpoint_test(request)

# for _ in wp.get_changed_diff_patch():
#     res = jsbeautifier.beautify(_, opts)
#     print(res)
