import ofjustpy as oj
from py_tailwind_utils import *
from addict_tracking_changes import Dict
import page_style_editor as pse


# res = tt.styClause.to_json(
#     *hover(*focus(bg/green/400), *focus(*placeholder(noop/fw.bold), fc/pink/100))
# )


span_hc = oj.PC.Span(text="aspan",
           twsty_tags=[bg/green/1, fc/blue/8,
                       *hover(*focus(bg/green/400),
                              *focus(*placeholder(noop/fw.bold),
                                     fc/pink/100))
                       ]
           )



with oj.uictx("ActiveComps"): 
    ti_hc = oj.AC.TextInput(key="ati",
                            placeholder="enter name",
                            twsty_tags=[*hover(*focus(bg/green/4),
                                               *focus(*placeholder(bg/pink/2),
                                                      fc/pink/1)
                                               ),
                                        fc/green/1,
                                        bg/green/1
                                        ]
                            )
stackh = oj.PC.StackH(childs = [span_hc, ti_hc])
with oj.uictx("MutableComps"):    

    btn_ht = oj.Mutable.Button(key="abtn", text="Click Me", twsty_tags=[bg/green/3])

    
app = oj.load_app()
wp_endpoint_test = oj.create_endpoint(key="test_page",
                                    childs = [stackh,  btn_ht],
                                    title="Guinea pig"
                                    )





# ========================== hinav of a page =========================
from addict_tracking_changes import Dict
import ofjustpy_components as ojx
import json


def build_styeditor_endpoint(target_wp):
    DOM_hierarchy = pse.build_component_hierarchy(target_wp)
    def terminal_node_callback(spath):
        print ('terminal node selected', spath)
        pass

    hinav = ojx.HierarchyNavigator(DOM_hierarchy, terminal_node_callback, key="myhinav")
    hinav_depth_selector = oj.HCCMutable.StackH(childs = hinav.steps, twsty_tags=[space/x/4])

    tlc = oj.Mutable.Container(key="tlc", 
        childs = [hinav_depth_selector,
                                   oj.Halign(hinav.childpanel, content_type="mutable"),
                                   hinav
                                   ]

                         )

    wp_template = oj.Mutable.WebPage(
        key="editor",
        childs=[tlc],
        cookie_state_attr_names=oj.aci.the_starlette_app.cookie_state_attr_names,
        title="editor"
    )
    return oj.create_endpoint_impl(wp_template)




def wrapped_endpoint(request, *args, **kwargs):
    global target_wp

    wp = wp_endpoint_test(request, *args, **kwargs)
    session_manager = oj.get_session_manager(request)
    with oj.sessionctx(session_manager):
        styeditor_endpoint = build_styeditor_endpoint(wp)
        app.add_jproute("/styedit", styeditor_endpoint)
        # append a hyperlink to wp
        print ("comps = ", wp.components)
        oj.PC.A(
            href="/styedit",
            text="Style Editor",
            target="_blank").stub()(wp)
        print ("comps = ", wp.components)
    wp.styeditor_endpoint = styeditor_endpoint
    return wp

app.add_jproute("/", wrapped_endpoint)    
# request = Dict()
# request.session_id = "abc"
# wp = wrapped_endpoint(request)

# # wp_sty_json = pse.to_sty_json(wp)
# # print (wp_sty_json)

# import jsbeautifier
# opts = jsbeautifier.default_options()
# # res = jsbeautifier.beautify(json.dumps(wp_sty_json), opts)

# # print (res)
# DOM_hierarchy = pse.build_component_hierarchy(wp)
# res = jsbeautifier.beautify(json.dumps(DOM_hierarchy), opts)
# print (res)



