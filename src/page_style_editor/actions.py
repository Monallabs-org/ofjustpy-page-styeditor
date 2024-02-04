import traceback
import sys
from py_tailwind_utils import dget
import ofjustpy_react as ojr
import re
from py_tailwind_utils import (tstr,
                               styClause,
                               dget,
                               dnew
                               )
from py_tailwind_utils import *
import logging
import ofjustpy as oj


def on_enter_focus_hcobj(appstate, arg, wp):
    """
    appctx=/update_sty_hcobj/target_hcobj
    """
    # print ("WTF : pause_selection ===== ", id(appstate.update_sty_hcobj.pause_selection), " ",
    #        appstate.update_sty_hcobj.pause_selection)
    print("====Enter in-focus==========")
    #print("alt-approach on_enter_focus", wp.session_manager.pause_selection, id(wp.session_manager.pause_selection))
    if wp.session_manager.pause_selection == True:
        print("selection paused: no action taken ")
        return 
    print ("target_hcobj arg: = ", arg, " ", arg.id)


    if appstate.update_sty_hcobj.prev_target_hcobj:
        appstate.update_sty_hcobj.prev_target_hcobj.remove_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
        pass
    
    arg.add_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)    
    appstate.update_sty_hcobj.prev_target_hcobj = appstate.update_sty_hcobj.target_hcobj
    print("====Exit in-focus==========")
    pass


def on_exit_focus_hcobj(appstate, arg, wp):
    """
    appctx=/update_sty_hcobj/detarget_hcobj
    """

    if  wp.session_manager.pause_selection == True:
        print("on_exit_focus: selection paused: no action taken ")
        return
    
    try:
        arg.remove_twsty_tags(bds.double, bd/4, bd/red/6, outline/green/8)
    except:
        pass

    
    appstate.update_sty_hcobj.prev_target_hcobj = None
    pass

def on_mouseclick_hcobj(appstate, arg, wp):
    """
    appctx=/update_sty_hcobj/clicked_hcobj
    """

    print(f"================= Start on_mouseclick: {appstate.update_sty_hcobj.clicked_hcobj.id} ================+")
    if wp.session_manager.pause_selection:
        print("selection paused: no action taken ")
        pass
    # A click on already targeted component
    # will turn on the pause_selection flag
    
    if appstate.update_sty_hcobj.clicked_hcobj.id == appstate.update_sty_hcobj.target_hcobj.id:
        # toggle pause selection 
        if wp.session_manager.pause_selection == False:
            print("Pausing selection ")
            wp.session_manager.pause_selection = True
            appstate.update_sty_hcobj.selected_hcobj = appstate.update_sty_hcobj.clicked_hcobj
        else:
            # To resume selection click on reset button
            #wp.session_manager.pause_selection = False
            pass
            
    else:
        # First click on the component.
        #wp.session_manager.pause_selection = False
        # treat as selection
        appstate.update_sty_hcobj.target_hcobj = appstate.update_sty_hcobj.clicked_hcobj
        # no need : the change in appstate-storepath will trigger on_enter_focus
        on_enter_focus_hcobj(appstate, arg, wp)
        pass
    print("alt-approach mouseclick postchange ", wp.session_manager.pause_selection,
          id(appstate.pause_selection)
          )
    print ("===================END on_mouseclick=========================")
    
    pass

def on_resume_selection(appstate, arg, wp):
    """
    appctx=/update_sty_hcobj/resume_selection
    """
    print("reset the pause_selection to False")
    wp.session_manager.pause_selection = False
    pass

def apply_color_to_utility_class_on_selected_hcobj(appstate, arg, wp):
    """
    appctx=/update_sty_hcobj/apply_color_to_utility_class
    """
    try:
        the_utility_class = appstate.update_sty_hcobj.utility_class
        
        the_color = appstate.update_sty_hcobj.selected_color
        
        the_hc = appstate.update_sty_hcobj.selected_hcobj
        print ("applying color ", tstr(the_utility_class/the_color))
        print ("to ==> ", appstate.update_sty_hcobj.selected_hcobj)
        try:
            the_hc.add_twsty_tags(the_utility_class/the_color)
        except Exception as e:
            print("error in add_twsty_tags ", e)
        print ("new color ===> ", the_hc.classes)
        oj.run_task(appstate.target_wp.update())
        print("invoked:apply_color_to_utility_class_on_selected_hcobj ", appstate)
        # appstate.update_sty_hcobj.selected_color = None
        # appstate.update_sty_hcobj.selected_hcobj = None
        appstate.update_sty_hcobj.clear_changed_history()
        appstate.update_target_wp = True
        
    except Exception as e:
        logging.debug("HH")
        pass

    pass


from py_tailwind_utils.style_tags import styTagDict
def apply_attr_value_to_utility_class_on_selected_hcobj(appstate, arg, wp):
    """
    appctx=/update_sty_hcobj/apply_attr_value_to_utility_class
    """
    try:
        
        the_utility_class = appstate.update_sty_hcobj.utility_class
        
        the_attr = appstate.update_sty_hcobj.utility_class_attr
        
        the_value = appstate.update_sty_hcobj.utility_class_attr_value
        
        the_hc = appstate.update_sty_hcobj.selected_hcobj
        print ("=============> apply-attr-value ", the_utility_class, ":",
               the_attr, ":", the_value)

        the_expr = the_utility_class/the_attr/the_value
        print ("expr str ", tstr(the_expr))
        
        #print ("===================> ", styTagDict[the_attr])
        the_hc.add_twsty_tags(the_expr)
        oj.run_task(appstate.target_wp.update())

        # appstate.update_sty_hcobj.selected_color = None
        # appstate.update_sty_hcobj.selected_hcobj = None
        appstate.update_sty_hcobj.clear_changed_history()
        appstate.update_target_wp = True
        
    except Exception as e:
        logging.debug("HH")
        pass

    pass


def update_target_wp(appstate, arg, wp):
    """
    appctx=/update_target_wp
    """
    
    
    pass

# def update_sty_action(appstate, arg, wp):
#     """
#     appctx:/update_sty
#     """
#     styj = appstate.target_styj._asdict()
#     target_stubStore = appstate.target_wp.session_manager.stubStore
    
#     def update_sty(sty_xpath):
#         dnew(styj, sty_xpath + "/_val", arg.target_value)
#         component_path = re.sub(f"/_sty/{arg.sty_jpath}/\d", "/_sty", sty_xpath)
#         print ("Component_Path = ", component_path)
#         print ("Update sty at path = ", sty_xpath)
#         component_spath = dget(styj,   component_path + "/spath")
#         print("component_spath = ", component_spath)
#         component_stub_ref = dget(target_stubStore, component_spath)
#         print("component_spath_ref = ", component_stub_ref)
#         component_ref = component_stub_ref.target
#         print("component_target = ", component_ref)
#         print(type(component_ref))
#         if isinstance(component_ref, ojr.WebPage):
#             print ("updates to webpage itself not supported")
#         else:
#             component_styj = dget(styj,   component_path)
#             print ("component_styj = ", component_styj)
#             component_updated_twtags = styClause.to_clause(component_styj)
#             print ("tobe updated classes value = ", tstr(*component_updated_twtags))
#             print ("original classes = ", component_ref.domDict.classes)
#             component_ref.replace_twsty_tags(*component_updated_twtags)
#             print ("updated classes =", component_ref.classes)
    
#     pass

    
#     sty_jqpath = arg.comp_jpath + "._cref._sty" + "." + arg.sty_jpath + arg.mod_jpath
#     print ("X = ", sty_jqpath)
    
#     # sty_jqpath = "$..abtn._cref._sty.fc[?_modifier_chain.`len`== 0]"

#     # print ("Y = ", sty_jqpath)
#     for _ in matched_kpaths(sty_jqpath,  styj):
#         update_sty(_)
        
#     jp.run_task(appstate.target_wp.update())
#     #traceback.print_stack(file=sys.stdout)
#     print ("update_sty_action called as update_sty ")

 
