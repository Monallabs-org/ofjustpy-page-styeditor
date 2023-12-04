"""
one a single page is allowed to be edited at a time
"""

import page_style_editor as pse
import json
import jsbeautifier

wp_demo_advanced_components = pse.create_endpoint("demo_advanced_components_components",
                                                  key="demo_advanced_components",
                                                  title="Advanced components demo"
                                                  )

# wp_demo_advanced_components = pse.create_endpoint("wp_components",
#                                                   key="demo_advanced_components",
#                                                   title="Advanced components demo"
#                                                   )



import ofjustpy as oj
app = oj.load_app()
app.add_jproute("/", wp_demo_advanced_components)



