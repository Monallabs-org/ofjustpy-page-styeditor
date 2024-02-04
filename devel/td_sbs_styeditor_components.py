import page_style_editor as pse

import json
import jsbeautifier

wp_endpoint_test = pse.create_endpoint('wp_components', key="test_page",
                                       
                                    title="Guinea pig"
                                    )

from addict_tracking_changes import Dict

request = Dict()
request.session_id = "abc"
wp = wp_endpoint_test(request)
wp_styeditor = wp.styeditor_endpoint(request)

