"""
one a single page is allowed to be edited at a time
"""
import ofjustpy as oj
from py_tailwind_utils import *
from addict_tracking_changes import Dict
import page_style_editor as pse




app = oj.load_app()



specimen = oj.AC.Button(key="abtn", text="labeltext", twsty_tags=[bg/blue/3])

specimen = oj.Mutable.Button(key="abtn", text="labeltext", twsty_tags=[bg/blue/3])
specimen = oj.PC.Span(text="labeltext", twsty_tags=[bg/blue/3])

tlc = specimen

# @ojs.enableStyEdit(app)
# def wp_endpoint(request):
#     sm = oj.get_session_manager(request.session_id)
#     with oj.sessionctx(sm):
#         wp_ = oj.WebPage_("static_components",
#                           cgens=[
#                               label.stub()
#                           ]
#                           )
#         wp = wp_()
#         wp.to_json_optimized = True
#         return wp

# ========================== webworks index ==========================

# from  webworks_website.index import tlc

# ================================ end ===============================

wp_endpoint_test = pse.create_endpoint(key="test_page",
                                    childs = [tlc],
                                    title="Guinea pig"
                                    )

app.add_jproute("/x", wp_endpoint_test)

request = Dict()
request.session_id = "abc"
wp = wp_endpoint_test(request)


# editor_wp = styeditor.wp_index(request)

# from starlette.testclient import TestClient
# testclient = TestClient(app)
# response = testclient.get(f'/x')
# response = testclient.get(f'/styedit')
