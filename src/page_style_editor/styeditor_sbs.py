import jsbeautifier
import json

from py_tailwind_utils import dnew, dget
from py_tailwind_utils import *
from .styjson_utils import build_component_hierarchy, to_sty_json
from unittest.mock import patch
from .styeditor_components import build_tw_styValues_panel, build_tw_styTags_panel
from . import actions
ui_app_trmap = [('/color_choice', '/update_sty_hcobj/selected_color', None),
                ('/selected_hcobj', '/update_sty_hcobj/selected_hcobj', None),
                ('/apply_color_to_utility_class', '/update_sty_hcobj/apply_color_to_utility_class', None),
                ("/utility_class", "/update_sty_hcobj/utility_class", None),
                ("/utility_class_attr", "/update_sty_hcobj/utility_class_attr", None),
                ("/utility_class_attr_value",
                 "/update_sty_hcobj/utility_class_attr_value",
                 None
                 ),
                ("/apply_attr_value_to_utility_class",
                 "/update_sty_hcobj/apply_attr_value_to_utility_class",
                 None
                 )
                
                ]
import importlib

def debug_oj_patch_reset():
    oj = importlib.import_module('ofjustpy')
            
    # this should preceed the oj.htmlcomponents reload

    import ofjustpy_react as ojr
    importlib.reload(ojr)
    import ofjustpy_components as ojx
    importlib.reload(ojx)
    importlib.reload(oj.SHC_types)
    importlib.reload(oj.MHC_types)

    # Caution:Wisdom: importlib.reload(oj) will not have any effect
    # the oj.htmlcomponents needs to be reloaded
    importlib.reload(oj.htmlcomponents)

    # This line along with the above importlib.reload(oj.htmlcomponents) is crucial
    importlib.reload(oj)
    btn = oj.AC.Button(key="mybtn", text="A")
    btn.build_json()

        
def build_styeditor_endpoint(target_wp):

    # Have no idea why this works
    # Don't change anything here

    # We don't know which line below is responsible for
    # resetting the patches. Don't change anything

    oj = importlib.import_module('ofjustpy')

    # this should preceed the oj.htmlcomponents reload

    import ofjustpy_react as ojr
    importlib.reload(ojr)
    import ofjustpy_components as ojx
    importlib.reload(ojx)
    # make sure every module is reloaded
    # in order of the import hierarchy
    #importlib.reload(oj.TF_impl)
    importlib.reload(oj.SHC_types)
    importlib.reload(oj.MHC_types)
    importlib.reload(oj.Div_TF)
    importlib.reload(oj.HC_TF)
    
    # every submodule of oj needs to be reloaded
    importlib.reload(oj.HC_wrappers)
    importlib.reload(oj.MHC_types)
    # Caution:Wisdom: importlib.reload(oj) will not have any effect
    # the oj.htmlcomponents needs to be reloaded
    importlib.reload(oj.htmlcomponents)

    # This line along with the above importlib.reload(oj.htmlcomponents) is crucial
    # importlib.reload(oj)
    # btn = oj.AC.Button(key="mybtn", text="A")
    # print (type(btn))
    # btn.build_json()

    # logically moving after loading oj
    # logic didn't work
    # import ofjustpy_react as ojr
    # importlib.reload(ojr)
    # import ofjustpy_components as ojx
    # importlib.reload(ojx)
    # importlib.reload(oj.SHC_types)
        
    
    DOM_hierarchy = build_component_hierarchy(target_wp)

    # def fun_with_styj():
    #     styj = to_sty_json(target_wp)
    #     _ = "/test_page/abtn/_cref/_sty"
    #     styobj = dget(styj, _)
    #     all_rows = []
    #     for key, value in styobj.items():
    #         if key == 'spath':
    #             continue
    #         assert key not in ['hctype']
    #         print (key)
    #         for val_dict in value:
    #             #print (val_dict._val)
    #             #print (val_dict._modifier_chain)
    #             for kv, vv in val_dict.items():
    #                 vv._val
                    
    #                 #TODO: We need to do something about how to represent the modifier_chain
    #                 all_rows.append(oj.PC.Tr(childs = [oj.PC.Td(childs=[oj.PC.Span(text=key)]),
    #                                                oj.PC.Td(childs=[oj.PC.Span(text="".join(val_dict._modifier_chain))]),
    #                                                oj.PC.Td(childs=[oj.PC.Span(text=val_dict._val)])
    #                                ]
    #                      ))
    #     return oj.PC.Table(childs = all_rows)
        
                
                
                

    # sty_table = fun_with_styj()

    # ================================================================
    # ======================== selection panel =======================
    # ================================================================


    from py_tailwind_utils.colors import _tw_color_list, get_color_instance
    with oj.uictx("selection_panel"):
        @ojr.ReactDomino
        def on_utility_class_input(dbref, msg, to_ms):
            """
            the utility class selected: e.g. 
            """
            if msg.value in styTagDict:
                return "/utility_class", styTagDict.get(msg.value)

        
        input_utility_class = oj.HC_wrappers.WithBanner("utility class:",
                                                        oj.AC.TextInput(key="utility_class",
                                                                        placeholder="bg",
                                                                        on_change=on_utility_class_input
                                                                        ),
                                                        )

        @ojr.ReactDomino
        def on_color_selector_select(dbref, msg, to_ms):

            try:
                color_expr = get_color_instance(dbref.mcs_value)/int(dbref.scs_value)
                return "/color_choice", color_expr
            except:

                pass

            pass
    
        input_color = oj.HC_wrappers.WithBanner("select color:",
                                    oj.Mutable.ColorSelector(key="utilityClass_colorSelector",
                                                             on_change = on_color_selector_select,
                                                             on_click = on_color_selector_select
                                                             ),
                                    content_type="mutable",
                                    height_tag = H/8
                                    )

        @ojr.ReactDomino
        def on_color_apply(dbref, msg, to_ms):
            return "/apply_color_to_utility_class",  True

    
        color_apply_btn = oj.AC.Button(key="color_apply_btn",
                                       text="Apply",
                                       on_click=on_color_apply)

        
        @ojr.ReactDomino
        def on_attr_type_change(dbref, msg, to_ms):
            if msg.value in styTagDict:
                return "/utility_class_attr", styTagDict.get(msg.value)
            


        input_attribute_type = oj.WithBanner("enter attribute:",
                                           oj.AC.TextInput(key="attr",
                                                           placeholder="mr",
                                                           on_change=on_attr_type_change
                                                           )
                                           )
        @ojr.ReactDomino
        def on_attr_value_change(dbref, msg, to_ms):
            return "/utility_class_attr_value", msg.value

        input_attribute_value = oj.WithBanner("enter value:",
                                        oj.AC.TextInput(key="attr_value",
                                                     placeholder="3",
                                                     on_change=on_attr_value_change
                                                     )
                                        )

        @ojr.ReactDomino
        def on_attr_apply(dbref, msg, to_ms):
            return "/apply_attr_value_to_utility_class", True
        
        attr_apply_btn = oj.AC.Button(key="attr_apply_btn",
                                      text="Apply",
                                      on_click=on_attr_apply)


        selection_panel = oj.HCCMutable.Subsubsection("Input Panel",
                                          oj.HCCMutable.StackV(childs = [input_utility_class,
                                                              oj.HCCMutable.StackH(childs = [input_color,
                                                                                  color_apply_btn]),
                                                              oj.PC.StackH(childs = [input_attribute_type,
                                                                                  input_attribute_value,
                                                                                  attr_apply_btn 

                                                                                  ])

                                                              ]
                                                    )
                                          )
    # selection_panel = oj.HCCMutable.Subsubsection("Input Panel",
    #                                   oj.HCCMutable.StackV(childs = [
    #                                                       oj.HCCMutable.StackH(childs = [input_color,
    #                                                                           color_apply_btn])
                                                          
    #                                                       ]
    #                                             )
    #                                   )
    
    



    @ojr.ReactDomino
    def callback_hinav_terminal_selector(terminal_path, msg):
        selected_hcobj = dget(DOM_hierarchy, terminal_path)
        print ('terminal path: spath_or_self', terminal_path, " ", selected_hcobj)        
        selected_hcobj.add_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
        oj.run_task(target_wp.update())
        return "/selected_hcobj", selected_hcobj


    with oj.uictx("hccomp_selector"):
        hinav = ojx.HierarchyNavigator(DOM_hierarchy, callback_hinav_terminal_selector, key="hinav", max_depth=20)
        hinav_depth_selector = oj.HCCMutable.StackH(childs = hinav.steps, twsty_tags=[space/x/4])

    # try to see if we can freely import modules with "import ofjuspty stmts"
    # free import failed -- we have to create the components here only
    # from . import editor_components

    twstyle_panel = build_tw_styValues_panel(oj)
    twtags_panel  = build_tw_styTags_panel(oj)
    
    tlc = oj.Mutable.Container(key="tlc", 
                               childs = [hinav_depth_selector,
                                         oj.Halign(hinav.childpanel, content_type="mutable"),
                                         hinav,
                                         selection_panel, 
                                         twstyle_panel,
                                         twtags_panel
                                         ]

                               )
    def post_init(session_manager=None):
        assert session_manager is not None
        session_manager.appstate.target_wp = target_wp
        pass
    wp_template = ojr.WebPage(key="styeditor_wp",
                              childs=[tlc],
                              ui_app_trmap_iter = ui_app_trmap,
                              title="Style editor",
                              head_html =  """<script src="https://cdn.tailwindcss.com"></script> """,
                              action_module = actions,
                              post_init = post_init
                          )
    return oj.create_endpoint_impl(wp_template)




# ================================ end ===============================


