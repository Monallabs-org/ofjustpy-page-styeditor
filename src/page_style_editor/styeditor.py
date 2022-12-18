import jsbeautifier
import json
import ofjustpy_react as ojr
import ofjustpy as oj
from .styjson_utils import to_sty_json, matched_kpaths
from addict_tracking_changes import Dict, walker as dictWalker
from py_tailwind_utils import dnew, dget
from .editor_sty_update_query_input import update_query_input_components
from . import actions

target_wp = None
# def walker(de, kpath="/"):
#     if de.components:
#         for ce in de.components:
#             yield from walker(ce, f"{kpath}{de.stub.key}/")
#             yield f"{kpath}{de.stub.key}/_cref", de
#     else:
#         yield f"{kpath}{de.stub.key}", de

def walker(de, kpath="/"):
    if getattr(de, 'components', None):
        if de.components:
            for ce in de.components:
                yield from walker(ce, f"{kpath}{de.key}/")
                yield f"{kpath}{de.key}/_cref", de
        elif getattr(de, "key", None):
            yield f"{kpath}{de.key}", de
            
    elif getattr(de, "key", None):
        yield f"{kpath}{de.key}", de
        
        
def build_component_hierarchy():
    component_hierarchy = Dict()
    for cpath, ce in walker(target_wp):
        #print ("walker ", cpath, " ", ce.stub.spath)
        dnew(component_hierarchy, cpath, ce.id)
    return component_hierarchy

# ================== uistate to appstate transitions =================

ui_app_trmap = [("/update_sty", "/update_sty", None),
                ("/append_sty", "/append_sty", None),
                ("/remove_sty", "/remove_sty", None)
    ]

# ================================ end ===============================
def wp_index(request):
    session_id = request.session_id
    session_manager = oj.get_session_manager(session_id)
    stubStore = session_manager.stubStore
    appstate = session_manager.appstate

    # input components to express update/add/remove styles to components
    # within the component hierarchy
    
    appstate.target_wp = target_wp
    target_styj = to_sty_json(target_wp)
    appstate.target_styj  = ojr.make_opaque_dict(target_styj) 
    appstate.component_hierarchy = ojr.make_opaque_dict(
                                                    build_component_hierarchy())
        

    # ==================== something about tables ====================
    def build_style_iter(dpath):
        """
        iterate over each style directive of the component
        """
        styobj = dget(target_styj, dpath+ "/_cref/_sty")
        for key, value in styobj.items():
            if key in [ "passthrough", "spath"]:
                continue
            #print("value = ", value)
            # works for {'_val': 'gray-600', '_modifier_chain': []}
            # TODO: but doesn't work for {'sr': {'_val': '1'}, '_modifier_chain': []}
            for val_dict in value:
                # skip attributes e.g. mr/sr/1; only deal with bg/green/1
                # the serialization fo mr/sr/1 is {'sr': {'_val': '1'}, '_modifier_chain': []}
                # while that of bg/green/1 is {'_val': 'gray-600', '_modifier_chain': []}
                if '_val' in val_dict:

                    yield [key, val_dict._modifier_chain, val_dict._val]
                else:
                    val_key = [_ for _ in val_dict.keys() if _ != "_modifier_chain"][0]
                    yield [key, val_dict._modifier_chain, f"{val_key}-{val_dict[val_key]._val}"]
                    pass
                
            pass
        pass
        
    for dpath, spath in dictWalker(appstate.component_hierarchy._asdict()):
        for _ in build_style_iter(dpath):
            #print(_)
            # There is no point is displaying all styles
            # for all components at once. 
            # Displaying only the selected component makes sense
            # selected via component hierarchy: Stopping here
            
            pass

    # ============================== end =============================

    # ================= the active/passive components ================
    input_panel = update_query_input_components()
    # ============================== end =============================
    with oj.sessionctx(session_manager) as tlctx:

        #opts = jsbeautifier.default_options()
        #res = jsbeautifier.beautify(json.dumps(appstate.target_styj._asdict()), opts)
   
        # The user input components
        # print ("sty Json : for target_webpage")
        # print ("=====================> ", res)
        # wp_ = oj.WebPage_("static_components",
        #                   cgens=[
        #                       input_panel.stub()
                              
        #                   ]
        #                   )
        wp = oj.WebPage_("wp_styeditor",
                         WPtype=ojr.WebPage,
                         cgens=[input_panel.stub()],
                         title="Style Editor",
                         action_module = actions,
                         ui_app_trmap_iter=ui_app_trmap
                         #session_manager=session_manager
                         )()
        
        #wp = wp_()
        wp.to_json_optimized = True
        return wp
        
