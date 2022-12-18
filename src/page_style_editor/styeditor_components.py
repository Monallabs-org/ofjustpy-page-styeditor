from py_tailwind_utils import *
from py_tailwind_utils import style_values_noop as sv

def handle_twSty_select(dbref, msg, to_target):
    print ("stySelector: ",  dbref.name)
    print ("msg.value = ", msg.value)
    
def build_tw_styValues_panel(oj):
    def enum_selector(attrClass):
        """Build selector htmlcomponent for enum class
        attrClass: enum type that describes a tailwind utility -- e.g. fw, fsz, etc.
        """
        twsty_tags = [noop/shadow.md, bg/gray/1]
        enum_class = attrClass._sv_class
        name = enum_class.__name__

        return oj.HC_wrappers.WithBanner(name,
                          oj.AC.Select(key=name,
                                    childs = [oj.PC.Option(
                                                     text = _.value ,
                                                     value=_.name
                                                     )
                                              for _ in enum_class],
                                       on_change= handle_twSty_select
                                       ),
                          content_type="passive"
                          
                          )
    
    childs = [_ for _ in map(lambda kv: enum_selector(kv[1]), sv.styValueDict.items())]
    twstyle_panel = oj.PC.Subsubsection("Style Values",
                                        oj.PC.StackG(num_cols=3,  childs=childs)
                           )
    return twstyle_panel

def build_tw_styTags_panel(oj):

    def infobox(tagC):
        """
        given a tag (e.g. bg, mr, pd) -- create a info box with description and label
        """
        # todo: finally use oj.AC. to
        return oj.PC.StackH(key = tagC.__class__.__name__[1:],
                            childs=[oj.PC.Span(#"description",
                                text=tagC.taghelp+":",
                                twsty_tags=[]),
                                    oj.PC.Span(#"Notation",
                                        text=tagC.elabel,
                                        twsty_tags=[noop/fw.bold])]
                            )
    

    childs = [_ for _ in map(lambda kv: infobox(kv[1]), styTagDict.items())]
    # TODO: change num cols based on screen size
    twtags_panel = oj.PC.Subsubsection("Tailwind tags",
                                    oj.PC.StackG(num_cols=5,  childs=childs)
                                    )
    return twtags_panel
