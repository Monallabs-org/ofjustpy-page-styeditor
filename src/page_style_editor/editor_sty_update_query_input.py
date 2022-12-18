"""
all components required to input user query for style update
"""
from py_tailwind_utils import *
from ofjustpy.SHC_types import  PassiveComponents as PC, ActiveComponents as AC
from ofjustpy.HC_wrappers import Halign, WithBanner
from ofjustpy.MHC_types import (StackD as MStackD,
                                TextInput as MTextInput,
                                Button as MButton,
                                HCCMutable
                                )
import ofjustpy_react as ojr

@ojr.ReactDomino
def click_updateStyBtn(dbref, msg, target_of):
    # print ("update style button clicked")
    # print(_compSelectCtx.pathExpr.target.value, " ",
    #       _stySelectCtx.pathExpr.target.value, " ",
    #       _styValueCtx.pathExpr.target.value)
    # return "/update_sty", ojr.make_opaque_dict({
    #     'comp_jpath': _compSelectCtx.pathExpr.target.value,
    #     'sty_jpath': _stySelectCtx.pathExpr.target.value,
    #     'mod_jpath': _modSelectCtx.queryExpr.target.value,
    #     'target_value': _styValueCtx.pathExpr.target.value
    # })
    print ("click_updateStyBtn")
    return "/update_sty", ojr.make_opaque_dict({
        'comp_jpath': "$..abtn",
        'sty_jpath': "fc",
        'mod_jpath': "[?_modifier_chain.`len`== 0]",
        'target_value': "green-100"
    })
        

    pass
def click_appendStyBtn(dbref, msg, target_of):
    # print ("update style button clicked")
    # print(_compSelectCtx.pathExpr.target.value, " ",
    #       _stySelectCtx.pathExpr.target.value, " ",
    #       _styValueCtx.pathExpr.target.value)
    # return "/update_sty", ojr.make_opaque_dict({
    #     'comp_jpath': _compSelectCtx.pathExpr.target.value,
    #     'sty_jpath': _stySelectCtx.pathExpr.target.value,
    #     'mod_jpath': _modSelectCtx.queryExpr.target.value,
    #     'target_value': _styValueCtx.pathExpr.target.value
    # })
    print ("click_appendStyBtn")
    pass

def click_removeStyBtn(dbref, msg, target_of):
    # print ("update style button clicked")
    # print(_compSelectCtx.pathExpr.target.value, " ",
    #       _stySelectCtx.pathExpr.target.value, " ",
    #       _styValueCtx.pathExpr.target.value)
    # return "/update_sty", ojr.make_opaque_dict({
    #     'comp_jpath': _compSelectCtx.pathExpr.target.value,
    #     'sty_jpath': _stySelectCtx.pathExpr.target.value,
    #     'mod_jpath': _modSelectCtx.queryExpr.target.value,
    #     'target_value': _styValueCtx.pathExpr.target.value
    # })
    print ("click_removeStyBtn")
    pass

def update_query_input_components():
    
    # expression to select components
    inp_component_selector_pathExpr = WithBanner("Component selector json query ",
                                    AC.TextInput(key="pathExpr",
                                     type="text",
                                     placeholder='$..mybtn',
                                     value='$..mybtn',
                                     )
                               )

    # pick which tw styles are going to be modified
    # mr, pd, bg, etc
    inp_style_tag_value = WithBanner("Style Key Selector",
                                    AC.TextInput(key = "pathExpr",
                                                 type="text",
                                                 placeholder="fc",
                                                 value="fc"
                                                 )
                                    )

    # the style value : append/update
    modifier_update_append = MStackD(key = "modify_update_tw_values",
                                     childs = [MTextInput(key = "queryExpr",
                                                          type="text",
                                                          placeholder="fc[?_modifier_chain.`len`== 0]",
                                                          value="[?_modifier_chain.`len`== 0]"
                                                          ),
                                               MTextInput(key = "appendExpr",
                                                          type="text",
                                                          placeholder="[]",
                                                          value="[]"
                                                          )
                                               ],
                                     height_anchor_key="queryExpr"
                                     
                                     )
    inp_modifier_selector_pathExpr = WithBanner("Style modifier clause",
                                   modifier_update_append,
                                   content_type="mutable"
                                   )
    inp_style_value = WithBanner("New Style Value", AC.TextInput(key="new_sty_value",
                                                          placeholder="pink/100",
                                                          value="pink/100"
                                                          )
                          )

    # ========================== the buttons =========================
    update_submit_btn = MButton(key = "updateBtn",
                                text="Submit",
                                value="Update",
                                twsty_tags=[pd/4, mr/4],
                                on_click = 
                                click_updateStyBtn
                                )
        
    append_submit_btn = MButton(key = "appendBtn",
                                text="Submit",
                                value="Append",
                                twsty_tags=[pd/4, mr/4],
                                on_click = click_appendStyBtn
                       )


    remove_submit_btn  = MButton(key = "removeBtn",
                             text="Submit",
                             value="Remove",
                             twsty_tags=[pd/4, mr/4],
                             on_click = click_removeStyBtn
                             )
    edit_submit_btn_deck = MStackD(key="btns",
                        childs = [update_submit_btn,
                                  append_submit_btn,
                                  remove_submit_btn
                                ]
                       )


    # ============================== end =============================

    # =================== edit type selection panel ==================
    def on_edit_type_choice(dbref, msg, target_of):
        pass
    
    choose_update_btn = AC.Button(key="choose_update_btn",
                                  text="Update",
                                  twsty_tags=[pd/4, mr/4],
                                  on_click = on_edit_type_choice
                                  )

    choose_append_btn = AC.Button(key="choose_append_btn",
                                  text="Append",
                                  twsty_tags=[pd/4, mr/4],
                                  on_click = on_edit_type_choice
                                  )
    
    choose_remove_btn = AC.Button(key="choose_remove_btn",
                                  text="Remove",
                                  twsty_tags=[pd/4, mr/4],
                                  on_click = on_edit_type_choice
                                  )

    edittype_choice_panel = PC.StackH(childs= [choose_update_btn,
                                           choose_append_btn,
                                           choose_remove_btn],
                                  twsty_tags=[space/x/4])
    
    input_panel = HCCMutable.Subsection(
                          "Bulk edit update/append styles using Json Paths",
                          HCCMutable.Halign(HCCMutable.StackV(key="inp_panel_core",
                                                            childs=[edittype_choice_panel,
                                                                    inp_component_selector_pathExpr,
                                                                    inp_style_tag_value ,
                                                                    inp_modifier_selector_pathExpr ,
                                                                inp_style_value,
                                                                    edit_submit_btn_deck
                                         ])
                                  )
                       )
    
    
    return input_panel

    # # expression to select the utility class

    # # select modifier chain


 

            

                   

    
