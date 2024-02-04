"""
Check hcobj mouseover selection for mutable objs: 
"""
import logging
import os
if os:
    try:
        os.remove("td_sbs.log")
    except:
        pass


import sys
if sys:
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(filename="td_sbs.log",
                        level=logging.DEBUG, format=FORMAT)

    
import page_style_editor as pse
from addict import Dict
from py_tailwind_utils import *
wp_endpoint_test = pse.create_endpoint('wp_components_mutable_types',
                                       key="test_page",
                                       
                                       title="Guinea pig"
                                    )

import ofjustpy as oj
app = oj.load_app()
    
app.add_jproute("/x", wp_endpoint_test)
# performs test for hccmutable type
# request = Dict()
# request.session_id = "abc"
# session_manager = oj.get_session_manager(request)
# wp = wp_endpoint_test(request)
# hccmutable = wp.components[0]
# hccmutable.add_twsty_tags(bg/green/1)
# print ([_ for  _ in hccmutable.get_changed_diff_patch()])
# print (hccmutable.staticCore.classes)
