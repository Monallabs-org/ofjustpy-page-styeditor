import traceback
import sys
import justpy as jp
from .styjson_utils import to_sty_json, matched_kpaths
from py_tailwind_utils import dget
import ofjustpy_react as ojr
import re
from py_tailwind_utils import (tstr,
                               styClause,
                               dget,
                               dnew
                               )
def update_sty_action(appstate, arg, wp):
    """
    appctx:/update_sty
    """
    styj = appstate.target_styj._asdict()
    target_stubStore = appstate.target_wp.session_manager.stubStore
    
    def update_sty(sty_xpath):
        dnew(styj, sty_xpath + "/_val", arg.target_value)
        component_path = re.sub(f"/_sty/{arg.sty_jpath}/\d", "/_sty", sty_xpath)
        print ("Component_Path = ", component_path)
        print ("Update sty at path = ", sty_xpath)
        component_spath = dget(styj,   component_path + "/spath")
        print("component_spath = ", component_spath)
        component_stub_ref = dget(target_stubStore, component_spath)
        print("component_spath_ref = ", component_stub_ref)
        component_ref = component_stub_ref.target
        print("component_target = ", component_ref)
        print(type(component_ref))
        if isinstance(component_ref, ojr.WebPage):
            print ("updates to webpage itself not supported")
        else:
            component_styj = dget(styj,   component_path)
            print ("component_styj = ", component_styj)
            component_updated_twtags = styClause.to_clause(component_styj)
            print ("tobe updated classes value = ", tstr(*component_updated_twtags))
            print ("original classes = ", component_ref.domDict.classes)
            component_ref.replace_twsty_tags(*component_updated_twtags)
            print ("updated classes =", component_ref.classes)
    
    pass

    
    sty_jqpath = arg.comp_jpath + "._cref._sty" + "." + arg.sty_jpath + arg.mod_jpath
    print ("X = ", sty_jqpath)
    
    # sty_jqpath = "$..abtn._cref._sty.fc[?_modifier_chain.`len`== 0]"

    # print ("Y = ", sty_jqpath)
    for _ in matched_kpaths(sty_jqpath,  styj):
        update_sty(_)
        
    jp.run_task(appstate.target_wp.update())
    #traceback.print_stack(file=sys.stdout)
    print ("update_sty_action called as update_sty ")
