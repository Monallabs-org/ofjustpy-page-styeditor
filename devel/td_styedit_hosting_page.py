import page_style_editor as pse
import json
import jsbeautifier

from py_tailwind_utils import *
wp_endpoint_test = pse.create_endpoint('wp_hosting_components',
                                       key="test_page",
                                       title="Python-Powered Web Services and Solutions",
                                       twsty_tags = [bg/yellow/"100/30"]

                                       )
import ofjustpy as oj
app = oj.load_app()
    
app.add_jproute("/", wp_endpoint_test)
