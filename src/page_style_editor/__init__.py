import functools


#from . import styeditor_sbs as styeditor
#from .styeditor_sbs import build_styeditor_endpoint

from unittest.mock import patch
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


def f_decorator(f):
    def wrapper(*args, **kwargs):
        print ("captured the id call of stub : ", args[0])
        assert False
        return None

    return wrapper

from .mutable_wrapper import (wrapper_is_static,
                              wrapper_id,
                              PassiveJsonMixin,
                              ActiveJsonMixin,
                              StaticCore,
                              get_styedit_A,
                              HCCPassiveJsonMixin
                              
                              )
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

def on_mouseenter(dbref, msg, to_ms):
    print ("ME", dbref.key)
    pass

def on_mouseleave(dbref, msg, to_ms):
    print ("ML ", dbref.key)
    pass


def create_endpoint(wp_comp_mod, **kwargs):
    """
    """
    #
    # ========== create the template; with patched JsonMixin =========
    with patch('ofjustpy_engine.SHC_types_mixin.PassiveJsonMixin',
               new=PassiveJsonMixin), patch('ofjustpy_engine.SHC_types_mixin.ActiveJsonMixin',
               new=ActiveJsonMixin), patch('ofjustpy_engine.SHC_types_mixin.HCCPassiveJsonMixin',
               new=HCCPassiveJsonMixin), patch('ofjustpy_engine.SHC_types_mixin.StaticCore',
          new = StaticCore
          ):
        import ofjustpy as oj
        wp_comp_mod = importlib.import_module(wp_comp_mod)
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

        for hc in wp_comp_mod.wp_childs:
            for comp in scan_childs(hc):
                comp.on('mouseenter', on_mouseenter)
                comp.on('mouseleave', on_mouseleave)
                print(comp.event_handlers)
                
            
        wp_template = oj.Mutable.ResponsiveStatic_CSR_WebPage(childs=wp_comp_mod.wp_childs,
                                                              cookie_state_attr_names=oj.aci.the_starlette_app.cookie_state_attr_names,
                                                              **kwargs,
                                                              )

    @oj.webpage_cache(wp_template.id)
    def endpoint(request, *args, **kwargs):
        # create wp within the patched context
        with patch.object(oj.TF_impl.Stub_HCPassive,
                          'id',
                          property(wrapper_id)
                          ), patch.object(oj.TF_impl.Stub_HCPassive,
                                          'is_static',
                                          wrapper_is_static):
            sm = oj.tracker.get_session_manager(request)
            with oj.tracker.sessionctx(sm):
                wp_ = wp_template.stub()
                wp = wp_(request, *args, **kwargs)
                wp.to_json_optimized = True
                wp.head_html = """<script src="https://cdn.tailwindcss.com"></script> 
                """
        with oj.tracker.sessionctx(sm):
            
            from . import styeditor_sbs
            styeditor_sbs.debug_oj_patch_reset()
            #importlib.reload(styeditor_sbs)
            styeditor_endpoint = styeditor_sbs.build_styeditor_endpoint(wp
                                                                        )
            oj.add_jproute("/styedit", styeditor_endpoint)
            a = get_styedit_A()
            a.stub()(wp)
            wp.styeditor_endpoint = styeditor_endpoint
            pass

        return wp
    return endpoint
            
            
        

    
