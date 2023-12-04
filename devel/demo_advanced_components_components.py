import ofjustpy as oj
from py_tailwind_utils import *
import ofjustpy_components as ojx
from addict_tracking_changes import Dict
import json
from ofjustpy_components.htmlcomponents import  BiSplitView, Paginate, Dockbar
from ofjustpy_components.hierarchy_naviator import HierarchyNavigator

#@oj.webpage_cache
app = oj.load_app()

title = oj.PC.Title("Demo: Advanced capabilities")
# ==================== slider example ====================
def slider_select(dbref, msg, target_of):
    print("Slider selected")
    pass
theslider = oj.Mutable.Slider(key="theslider",
                               num_iter=range(8),
                              twsty_tags=[bg/green/1],
                              on_click = slider_select
                              )
slider_container = oj.Mutable.Container(key="slider_container",
                                           childs = [theslider]
                                           )

# ========================== end =========================


# ================ color selector example ================
def on_color_select(dbref, msg, target_of):
    pass

thecolorselector = oj.Mutable.ColorSelector(key = "colorselector",
                                            twsty_tags=[bg/rose/"200/20"],
                                            on_click = on_color_select
                                            )
colorselector_container = oj.Mutable.Container(key="colorselector_container",
                                               childs = [thecolorselector]
                                               )
# ================================ end ===============================

# ===================== deck example =====================

with oj.uictx("deckdemo") as  deckdemo:
    btn1 = oj.Mutable.Button(key="mybtn1",
                              value="/mybtn2",
                              text="Click me1 ",
                              twsty_tags=[bg/blue/"100/50"],
                              #on_click = on_btn_click
                              )

    btn2 = oj.Mutable.Button(key="mybtn2",
                              value="/mybtn1",
                              text="Click me2 ",
                              twsty_tags=[bg/blue/"100/50"],
                              #on_click = on_btn_click
                              )
            
    thedeck = oj.Mutable.StackD(key = "thedeck",
                                childs = [ btn1, btn2
                                          ],
                                height_anchor_key = btn1.key
                      )
    def on_btn_click(dbref, msg, target_of):
        target = dget(deckdemo, msg.value)
        ms_thedeck = target_of(thedeck)
        ms_thedeck.bring_to_front(target_of(target).id)
        pass


    btn1.on("click", on_btn_click)
    btn2.on("click", on_btn_click)

deck_container = oj.Mutable.Container(key="deck_container",
                                      childs = [thedeck]
                                      )

# ================================ end ===============================

# ====================== two column example======================
def on_btn_click(dbref, msg, target_of):
    print("Color selector called ")
    
    pass
view_directive= Dict()
view_directive.part_viewer = lambda **kwargs: oj.HCCMutable.StackV(**kwargs)
view_directive.full_viewer = lambda **kwargs: oj.HCCMutable.Div(**kwargs)
    
def gen_cs():
    for idx in range(0, 20):
        yield oj.Mutable.ColorSelector(key = f"tc_colorselector_{idx}",
                                       on_click = on_btn_click
                                       )
                             
                
twocolumn_view = BiSplitView([_ for _ in gen_cs()],
                             view_directive,
                             twsty_tags=[W/full])

twocolumn_container = oj.Mutable.Container(key="twocolumn_container",
                                           childs = [twocolumn_view]
                                           )
# ========================== end =========================


# ============================= paginate =============================

items = [oj.PC.Span(text=f"item {i}") for i in range(40 * 20)]
def page_container_gen(cid, childs, **pkwargs):
    hc_types = Dict()
    hc_types.part_viewer = lambda **kwargs: oj.PC.StackV(**kwargs)
    hc_types.full_viewer = lambda **kwargs: oj.HCCStatic.Div(key=f"{cid}_page_view", **kwargs)
    return BiSplitView(childs, hc_types, **pkwargs)

    
paginate = Paginate("mypaginate", items, page_container_gen,  num_pages=20, chunk_size=40)

paginate_container = oj.Mutable.Container(key = "paginate_container",
                                          childs = [paginate],
                                          twsty_tags=[H/64]
                                          )

# ================================ end ===============================


# ============================ dock/undock ===========================
def on_btn_click(dbref,msg):
    pass


span1  = oj.AC.Textarea(key="targetSpan1",
                        text="a text area with lots of lots of text",
                        pcp=[bg/green/1, pd/2]
                     )
span2  = oj.AC.Textarea(key="targetSpan2",
                       text="another text area with lots of lots of text",
                       pcp=[bg/blue/1, pd/2]
                       )

            
dockbar  = Dockbar([span1, span2],
                   ["Item1", "Item2" ],
                   )

undock_btn_panel = oj.Halign(oj.HCCMutable.Div(key = "undock_btn_panel",
                                     childs = dockbar.undock_btns.values(),
                                     twsty_tags=[space/x/4]
                                               ),
                             content_type="mutable"
                             )


wrapped_item_panel = oj.Halign(oj.HCCMutable.Div(
                                       childs = dockbar.wrapped_components.values(),
                                       twsty_tags=[space/y/4]
                                       ),
                               content_type="mutable"
                               )


dock_undock_tlc = oj.Mutable.Div(key="dock_undock",
                                       childs = [undock_btn_panel,
                                                 wrapped_item_panel
                                                 ],
                                       twsty_tags=[space/y/4]
                                       )

dock_undock_container = oj.Mutable.Container(key="dock_undock_container",
                                             childs = [dock_undock_tlc]
                                             )

# ================================ end ===============================

# ======================== hierarchy_naviator ========================
italian_cuisine_hierarchy = json.loads("""
{
    "Cuisine: Italian": {
        "Regions": {
            "Northern Italian cuisine": {
                "Dishes": {
                    "Risotto alla Milanese": {
                        "Ingredients": {
                            "Arborio rice": 1,
                            "Saffron": 1,
                            "Parmesan cheese": 1,
                            "Chicken stock": 1
                        },
                        "Techniques": {
                            "Toasting rice": 1,
                            "Adding saffron": 1,
                            "Gradually adding stock": 1,
                            "Finishing with Parmesan cheese": 1
                        },
                        "Utensils": {
                            "Risotto pan": 1,
                            "Wooden spoon": 1
                        }
                    },
                    "Osso Buco": 1,
                    "Polenta": 1,
                    "Tiramisu": 1
                }
            },
            "Central Italian cuisine": {
                "Dishes": {
                    "Spaghetti alla Carbonara": {
                        "Ingredients": {
                            "Spaghetti pasta": 1,
                            "Pancetta": 1,
                            "Eggs": 1,
                            "Pecorino Romano cheese": 1
                        },
                        "Techniques": {
                            "Cooking pasta al dente": 1,
                            "Making the sauce with eggs and cheese": 1,
                            "Crisping pancetta": 1
                        },
                        "Utensils": {
                            "Large pot for boiling pasta": 1,
                            "Skillet for cooking pancetta and making sauce": 1
                        }
                    },
                    "Fettuccine Alfredo": 1,
                    "Bistecca alla Fiorentina": 1,
                    "Panzanella": 1
                }
            },
            "Southern Italian cuisine": {
                "Dishes": {
                    "Pizza Margherita": {
                        "Ingredients": {
                            "Pizza dough": 1,
                            "Tomatoes": 1,
                            "Mozzarella cheese": 1,
                            "Basil": 1
                        },
                        "Techniques": {
                            "Stretching and shaping the dough": 1,
                            "Making tomato sauce": 1,
                            "Topping with cheese and basil": 1
                        },
                        "Utensils": {
                            "Pizza stone or baking sheet": 1,
                            "Pizza peel": 1
                        }
                    },
                    "Pasta alla Puttanesca": {
                        "Ingredients": {
                            "Spaghetti pasta": 1,
                            "Tomatoes": 1,
                            "Olives": 1,
                            "Capers": 1
                        },
                        "Techniques": {
                            "Making tomato sauce with olives and capers": 1,
                            "Cooking pasta al dente": 1
                        },
                        "Utensils": {
                            "Large pot for boiling pasta": 1,
                            "Skillet for making tomato sauce": 1
                        }
                    },
                    "Caponata": 1,
                    "Arancini": 1
                }
            },
            "Sicilian cuisine": {
                "Dishes": {
                    "Pasta alla Norma": 1,
                    "Arancini": 1,
                    "Cannoli": 1,
                    "Cassata": 1
                }
            }
        }
    }
}
"""
)

def terminal_node_callback(spath):
    print ('terminal node selected', spath)
    pass

hn = HierarchyNavigator(italian_cuisine_hierarchy, terminal_node_callback, key="myhinav")

hn_depth_selector = oj.HCCMutable.StackH(childs = hn.steps, twsty_tags=[space/x/4])

hinav_container = oj.Mutable.Container(key="hinav_container",
                                             childs = [hn_depth_selector,
                                                       oj.Halign(hn.childpanel, content_type="mutable"),
                                   
                                                       hn
                                                       ]
                                             )

# ================================ end ===============================

# ==================== putting everything together ===================
viewdeck = oj.Mutable.StackD(key = "viewdeck",
                             childs = [slider_container,
                                       colorselector_container,
                                       deck_container,
                                       twocolumn_container,
                                       paginate_container,
                                       dock_undock_container,
                                       hinav_container
                                       ],
                             twsty_tags=[W/full, H/"5/6", space/y/6, db.f, jc.center],
                             height_anchor_key = paginate_container.key
                             )



                                             
def on_btn_click(dbref, msg, target_of):
    print("deck button clicked for", msg.value)
    viewdeck_ms = target_of(viewdeck)
    viewdeck_ms.bring_to_front(msg.value)
    #viewdeck_.target.bring_to_front(msg.value)
    pass

button_bar = oj.HCCMutable.StackW(childs = [oj.AC.Button(key="slider_btn",
                                                          text="Slider selector",
                                                          value=slider_container.id,
                                                          on_click = on_btn_click
                                                          ),
                                             
                                             oj.AC.Button(key = "colorselector_btn",
                                                          text="Color selector",
                                                          value=colorselector_container.id,
                                                          on_click = on_btn_click
                                                          ),
                                             
                                             oj.AC.Button(key="thedeck_btn",
                                                          text="Deck Container",
                                                          value=deck_container.id,
                                                          on_click = on_btn_click
                                                          ),
                                             oj.AC.Button(key="twocolumn_btn",
                                                          text="Two column container",
                                                          value=twocolumn_container.id,
                                                          on_click = on_btn_click
                                                          ),
                                             oj.AC.Button(key = "paginate_btn",
                                                           text="Paginate a html component collection",
                                                           value=paginate_container.id,
                                                           on_click= on_btn_click),
                                             oj.AC.Button(key="dockundock_btn",
                                                          text="Dock/Undock components",
                                                          value=dock_undock_container.id,
                                                          on_click = on_btn_click
                                                          ),
                                            oj.AC.Button(key="hinav_btn",
                                                          text="Hierarchical Navigation",
                                                          value=hinav_container.id,
                                                          on_click = on_btn_click
                                                          )
                                            
                                            ],
                                  twsty_tags=[W/full, mr/st/4, space/x/4]
                                  )
            
tlc = oj.HCCMutable.Container(childs= [title, button_bar, viewdeck],
                              twsty_tags=[H/screen, W/screen, space/y/4]
                          )
wp_childs = [tlc]
