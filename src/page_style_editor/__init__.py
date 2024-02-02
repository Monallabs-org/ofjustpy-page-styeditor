import functools


#from . import styeditor_sbs as styeditor
#from .styeditor_sbs import build_styeditor_endpoint
from py_tailwind_utils import *
from unittest.mock import patch
from . import actions
ui_app_trmap = [ ('/mouseenter_hcobj', '/update_sty_hcobj/selected_hcobj', None),
                 ('/mousexit_hcobj', '/update_sty_hcobj/deselected_hcobj', None),
                 ('/mouseclick_hcobj', '/update_sty_hcobj/clicked_hcobj', None),
                 ('/resume_selection', '/update_sty_hcobj/resume_selection', None)
    ]

# # yes This is global; only one wp edit at a time is feasible
# session_manager = None

# def wp_editor(request):
#     pass
# def enableStyEdit(app):
#     def f(func):
#         """
#         register the stub in _hcs/stubStore
#         """
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             global session_manager
#             wp = func(*args, **kwargs)
#             styeditor.target_wp = wp
#             app.add_jproute("/styedit", styeditor.wp_index)
            

#             # put href url to twstyconfig on target_wp under its own session manager
#             session_manager = oj.get_session_manager("enableStyEdit")
#             with oj.sessionctx(session_manager):
#                 PC.A(
#                       href="/styedit",
#                       text="Style Editor",
#                       target="_blank").stub()(wp)
#             return wp

#         return wrapper
#     return f

def post_init(session_manager=None):
    assert session_manager is not None
    session_manager.appstate.update_sty_hcobj.prev_selected_hcobj = None
    #session_manager.appstate.update_sty_hcobj.pause_selection = False
    #session_manager.appstate.pause_selection = False
    # print ("appstate, update_sty_hcobj, pause_selection == > ",
    #        id(session_manager.appstate), ' ', 
    #        id(session_manager.appstate.update_sty_hcobj), ' ', 
    #        id(session_manager.appstate.update_sty_hcobj.pause_selection), ' '
    #        )
    # print ("pause selection id = ", id(session_manager.appstate.pause_selection))
    # print (" In post init == ", id(session_manager.appstate.update_sty_hcobj.pause_selection),
    #        session_manager.appstate.update_sty_hcobj.pause_selection
    #        )
    session_manager.pause_selection = False
    pass
    
def f_decorator(f):
    def wrapper(*args, **kwargs):
        print ("captured the id call of stub : ", args[0])
        assert False
        return None

    return wrapper

from .mutable_wrapper import (#wrapper_is_static,
                              wrapper_id,
                              PassiveJsonMixin,
                              ActiveJsonMixin,
                              #StaticCore,
                              get_styedit_A,
                              HCCPassiveJsonMixin,
                              )

#from .HC_TF import gen_HC_type
from . import HC_TF
from . import Div_TF
from .TF_impl import gen_Stub_HCPassive

import importlib




# def wrapper(request, *args, **kwargs):
#     with patch.object(oj.TF_impl.Stub_HCPassive,
#                       'id',
#                       property(wrapper_id)
#                       ), patch.object(oj.TF_impl.Stub_HCPassive,
#                                       'is_static',
#                                       wrapper_is_static), patch.object(ofjustpy_engine.SHC_types_mixin.JsonMixin,
#                                                                        'build_json',
#                                                                        wrapper_build_json(ofjustpy_engine.SHC_types_mixin.JsonMixin.build_json) ):
#     wp = wp_endpoint(request, *args, **kwargs)
#     styeditor_editor_endpoint = build_styeditor_endpoint(wp)
#     app.add_jproute("/styedit", styeditor_editor_endpoint)
#     session_manager = oj.get_session_manager(request)
#     with oj.sessionctx(session_manager):
#         # append a hyperlink to wp
#         oj.PC.A(
#             href="/styedit",
#             text="Style Editor",
#             target="_blank").stub()(wp)
#     return wp



# patch('ofjustpy_engine.SHC_types_mixin.StaticCore',
#                new = StaticCore
#                )
def create_endpoint(wp_comp_mod, **kwargs):
    """
    """
    #
    # ========== create the template; with patched JsonMixin =========
    with  patch('ofjustpy.Div_TF.gen_Div_type', new=Div_TF.gen_Div_type), patch('ofjustpy.HC_TF.gen_HC_type', new=HC_TF.gen_HC_type), patch('ofjustpy_engine.SHC_types_mixin.PassiveJsonMixin',
               new=PassiveJsonMixin), patch('ofjustpy_engine.SHC_types_mixin.ActiveJsonMixin',
               new=ActiveJsonMixin), patch('ofjustpy_engine.SHC_types_mixin.HCCPassiveJsonMixin',
               new=HCCPassiveJsonMixin):
        
        #import ofjustpy as oj
        oj = importlib.import_module('ofjustpy')
        importlib.reload(oj.SHC_types)
        importlib.reload(oj.MHC_types)
        importlib.reload(oj.htmlcomponents)
        importlib.reload(oj)
        oje = importlib.import_module('ofjustpy_engine')
        importlib.reload(HC_TF.SCmixin)
        importlib.reload(HC_TF)
        importlib.reload(oje.SHC_types_mixin)
        # print (oj.SHC_types.PassiveComponents.Span)
        # print (oj.htmlcomponents.PassiveComponents.Span)
        # print (oj.AC.TextInput)
        # print (oj.PC.Span)
        
        
        wp_comp_mod = importlib.import_module(wp_comp_mod)
        #reloading wp_comp_mod in hopes that our own staticCore gets hooked

        wp_childs = wp_comp_mod.wp_childs #build_childs(oj)
        
        #oj = wp_comp_mod.oj
        # using default page builder for now
        # pjm = wp_comp_mod.pspan
        # pjm.build_json()
        # print (pjm.obj_json)
        def scan_childs(hc):
            has_childs =  hasattr(hc, 'childs')
            has_components = hasattr(hc, 'components')
            # hccMutable hccomponents are marked as being static
            # but they have attribute components
            # so we cannot use is_static as marker.
            # we will try both has_childs and has_components
            # whichever is available go with that. 
            
            # if hc.stub().is_static():
            #     if has_childs:
            #         print ("passive div has childs attribute")
            #         assert False
            # else:
            #     if has_components:
            #         print ("mutable div-staticCore has components attribute")
            #         assert False


            if has_childs and has_components:
                assert False
                
            elif has_childs:
                for cc in hc.childs:
                    yield from scan_childs(cc)
                    
            elif has_components:
                for cc in hc.components:
                    yield from scan_childs(cc)
            else:
                pass
            yield(hc)

        # we are importing ojr here
        # because we don't want ojr to import oj
        # outside of the patching context
        
        import ofjustpy_react as ojr
        @ojr.ReactDomino
        def on_mouseenter(dbref, msg, to_ms):
            print ("ME", dbref.key)
            #dbref.add_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
            return "/mouseenter_hcobj", dbref

        @ojr.ReactDomino
        def on_mouseleave(dbref, msg, to_ms):
            print ("ML ", dbref.key)
            #dbref.remove_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
            return "/mousexit_hcobj", dbref



        @ojr.ReactDomino
        def on_mouseleave(dbref, msg, to_ms):
            print ("ML ", dbref.key)
            #dbref.remove_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
            return "/mousexit_hcobj", dbref



        @ojr.ReactDomino
        def on_click(dbref, msg, to_ms):

            return "/mouseclick_hcobj", dbref

        # attach mouseenter, mouseleave event handler to all the page
        # components
        for hc in wp_childs:
            for comp in scan_childs(hc):
                # Note: browser/HTMLComponents.svelte is not cooperating
                # It is invoking mouseleave on both the nested and outercomponents
                #comp.on('mouseenter', on_mouseenter)
                comp.on('mouseout', on_mouseleave)
                comp.on('mouseenter', on_mouseenter)
                comp.on('click', on_click)
                # comp.on('dblclick', on_keydown)
                # comp.on('submit', on_keydown)

        app = oj.load_app()
        # wp_template = oj.Mutable.ResponsiveStatic_CSR_WebPage(childs=wp_childs,
        #                                                       cookie_state_attr_names=oj.aci.the_starlette_app.cookie_state_attr_names,
        #                                                       **kwargs,
        #                                                       )
        
        @ojr.ReactDomino
        def on_resume_selection(dbref, msg, to_ms):
            print ("ML ", dbref.key)
            #dbref.remove_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
            return "/resume_selection", True
        
        # resume_selection_btn = oj.AC.Button(key="reset_button",
        #                                     text="Resume Selection",
        #                                     twsty_tags=[mr/4, pd/4],
        #                                     on_click=on_resume_selection)

        # [oj.Mutable.StackV(key="axy",
        #                                                       childs = [oj.Mutable.Div(key="tt",
        #                                                                                childs=wp_childs),
        #                                                                 resume_selection_btn
        #                                                                 ]
        #                                                       )
        #                                     ]
        
        wp_template = ojr.WebPage(childs = wp_childs,
                    cookie_state_attr_names=oj.aci.the_starlette_app.cookie_state_attr_names,
                    ui_app_trmap_iter = ui_app_trmap,
                    action_module = actions,
                                  post_init = post_init,
                                  **kwargs
                    )
    @oj.webpage_cache(wp_template.id)
    def endpoint(request, *args, **kwargs):
        # create wp within the patched context
        with patch.object(oj.HC_TF, 'gen_Stub_HCPassive', gen_Stub_HCPassive):
            sm = oj.tracker.get_session_manager(request)
            with oj.tracker.sessionctx(sm):
                wp_ = wp_template.stub()
                wp = wp_(request, *args, **kwargs)
                wp.to_json_optimized = True
                wp.post_init(session_manager=sm)
                wp.session_manager = sm
                wp.head_html = """<script src="https://cdn.tailwindcss.com"></script> 
                """
        with oj.tracker.sessionctx(sm):
            
            from . import styeditor_sbs
            oj.set_style("un")
            styeditor_sbs.debug_oj_patch_reset()
            #importlib.reload(styeditor_sbs)
            styeditor_endpoint = styeditor_sbs.build_styeditor_endpoint(wp
                                                                        )
            oj.add_jproute("/styedit", styeditor_endpoint)
            a, resume_selection_btn = get_styedit_A()
            @ojr.ReactDomino
            def on_resume_selection(dbref, msg, to_ms):
                print ("resume selection  ", dbref.key)
                #dbref.remove_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
                return "/resume_selection", True
            resume_selection_btn.on('click', on_resume_selection)
            # add the href for styeditor to the webpage.
            a.stub()(wp)
            resume_selection_btn.stub()(wp)

            wp.styeditor_endpoint = styeditor_endpoint
            pass

        return wp
    return endpoint
            
            
        

    
