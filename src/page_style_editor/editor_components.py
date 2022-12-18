from ofjustpy.SHC_types import  PassiveComponents as PC, ActiveComponents as AC
from py_tailwind_utils import *
from py_tailwind_utils import style_values_noop as sv
from py_tailwind_utils.style_tags import styTagDict
from ofjustpy.HC_wrappers import Halign, WithBanner
def handle_twSty_select(dbref, msg):
    print ("stySelector: ",  dbref.name)
    print ("msg.value = ", msg.value)
    #styValueFeatureClass = sv.styValueDict.get(dbref.name)
    # msg.value is bi
    #featureValue_twtag = getattr(styValueFeatureClass, msg.value)
    #featureValue = tstr(featureValue_twtag)
    # print ("featureValue = ", featureValue)
    # #print ("styValue: msg-value ", msg.value)
    #print ("featureValue ", featureValue)

    # if FontWeight.semibold is selected
    # then this styvalue FontWeight
    # while semibold 
    # actions.update_bulkedit_form(stubStore.bulkedit,
    #                              "stySelector",
    #                              dbref.name
    #                              )

    # actions.update_bulkedit_form(stubStore.bulkedit,
    #                              "styValue",
    #                              msg.value
    #                              )
    pass
            
def styeditor_components():
    """
    components required to assit style edits
    """

    # ========================== twreference =========================

    def hc_enum_selector(attrClass):
        """Build selector htmlcomponent for enum class
        attrClass: enum type that describes a tailwind utility -- e.g. fw, fsz, etc.
        """
        twsty_tags = [noop/shadow.md, bg/gray/1]
        enum_class = attrClass._sv_class
        name = enum_class.__name__

        return WithBanner(name,
                          AC.Select(key=name,
                                    childs = [PC.Option(
                                                     text = _.value ,
                                                     value=_.name
                                                     )
                                          for _ in enum_class],
                                    on_change= handle_twSty_select
                                         ),
                                                    content_type="passive"
                          
                          )
            

    childs = [_ for _ in map(lambda kv: hc_enum_selector(kv[1]), sv.styValueDict.items())]
    
    twstyle_panel = PC.Subsubsection("Style Values",
                           PC.StackG(num_cols=3,  childs=childs)
                           )
    
    # ============================== end =============================
    # Tailwind tags defined in style tags
    
    def hc_twtag_info(tagC):
        """
        given a tag (e.g. bg, mr, pd) -- create a info box with description and label
        """
        return AC.StackH(key = tagC.__class__.__name__[1:],
                          childs=[PC.Span(#"description",
                                         text=tagC.taghelp+":",
                                         twsty_tags=[]),
                                 PC.Span(#"Notation",
                                         text=tagC.elabel,
                                         twsty_tags=[noop/fw.bold])]
                          )

    childs = [_ for _ in map(lambda kv: hc_twtag_info(kv[1]), styTagDict.items())]
    twtags_panel = PC.Subsubsection("Tailwind tags",
                                     PC.StackG(num_cols=5,  childs=childs)
                     )

    # ================ Panel with style tags and style values ===============
    # oj.Subsection_("Panel",
    #                        "Tailwind Style Directives",
    #                        oj.StackV_("content",
    #                                   cgens = [_ictx.styValuesPanel,
    #                                            oj.Divider_("sep", pcp=[mr/st/8, mr/sb/8]),
    #                                            _ictx.styTagsPanel
    #                                            ]
    #                                   )
    #                        )
            
    
    # childs = [_ for _ in map(lambda kv: hc_enum_selector(kv[1]), sv.styValueDict.items())]
    # PC.StackG(num_cols=3, childs=childs)
    
    return twtags_panel, twstyle_panel
