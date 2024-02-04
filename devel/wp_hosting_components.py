import ofjustpy as oj
from py_tailwind_utils import *

app = oj.load_app()
oj.set_style("transparent")
oj.ui_styles.sty.li = [li.none]


with oj.uictx("topmatter"):
    title = oj.PC.StackV(childs = [oj.PC.Title("Python-Powered Web Services and Solutions", twsty_tags=[fc/yellow/9]),
                                   oj.PC.SubTitle("Your Gateway from Development to Hosting with Python Technologies",
                                                  twsty_tags=[fc/yellow/7]
                                                  )
                                   ]
                         )

    overview = oj.PC.Subsection("",
                                oj.PC.StackV(childs = [oj.PC.Halign(oj.PC.Prose(text="Create, manage, and maintain web applications with remarkable ease and runtime efficiency.",
                                                                                twsty_tags=[max/W/"prose", fz.xl3, ff.sans, fw.medium]
                                                                                )
                                                                    ),
                                                       
                                                       ],
                                             
                                             ), twsty_tags=[mr/st/8]
                                )
    divider = oj.PC.Hr(twsty_tags=[mr/sb/4])

    top_panel = oj.PC.StackV(childs=[title,  overview])


def on_mouseover_action(dbref, msg, target_of):
    print("in mouseover action")
    ms = target_of(dbref)
    ms.add_twsty_tags(fc/green/8, )
    pass


def on_mouseout_action(dbref, msg, target_of):
    # a button has been clicked
    # get the spath/id and the value of the button
    # print("in mouseover action")
    # ms = target_of(dbref)
    # ms.conc_twsty_tags(fc/green/1)
    #dbref.add_twsty_tags(fc/green/1)
    print ("mouseout event called")
    
    pass

# bg-blue-500 text-white p-4 rounded-md shadow-md transition-transform transform hover:scale-105 hover:bg-blue-300 hover:shadow-lg

def build_card(id, card_title, sharing_type, storage_quantity, bandwidth_quantity, price_monthly):
    
    return oj.AC.Div(
        key=f"{id}_card",
        twsty_tags=[
            #bg/green/2,
                        ta.center,
                        bdr.md,
                        # bd / yellow / 3,
                        # bt.bd,
                        fw.medium,
                        outline/yellow/2,
                        *hover(outline/yellow/6, shadow.lg, shadow / yellow / 5),
            *gradient(yellow / 2, yellow / 2, yellow/"200/50"),
                        shadow / yellow / 3,
                        shadow.md,
                        H/"full",
                        #W/"1/3",
                    ],
        childs = [oj.PC.TitledPara(card_title,
                                   content=oj.PC.Ul(childs = [oj.PC.Li(text=f"{sharing_type} VPS"),
                                                              oj.PC.Li(text=f"{storage_quantity}MB SSD Storage"),
                                                              oj.PC.Li(text=f"{bandwidth_quantity}GB Bandwidth"),
                                                              oj.PC.Li(text=f"Priced at Rs{price_monthly}/month*")], twsty_tags = [pd/st/8, db.g, G/cols /1, G / rows /4, gf.col, H/full, space/y/4]

                                                    ),
                                   twsty_tags=[mr/st/4, H/full]
                                   ),
                  
                  ],
        
    )

price_panel = oj.PC.Halign(oj.PC.StackG(num_rows=1, num_cols = 3, childs = [build_card("card1",  "Get Online", "Shared", 300, 50, 80),
                                                  build_card("card2", "Get Trending", "Shared",  1000, 100, 160),
                                                  build_card("card3",  "Be Exclusive", "Exclusive", 1000, 500, 900),
                                                  
                                                  ],
                                        twsty_tags=[H/full, W/full, gap/x/4]

                                        ), 
                           twsty_tags=[H/"1/2", W/full, mr/st/8] # 1/5th of the entire page height. 
                           )

launch_info_panel = oj.Halign(oj.PC.Prose(text="Service launching March 1st, 2024. Interested in using our service -- leave a contact below.  We will notify you when the service goes live"),
                              twsty_tags=[mr/st/4, fz.xl2, mr/st/8]
                              )

email_fieldbox = oj.PC.StackH(childs = [oj.PC.Label(text = "Enter Email"),
                                        oj.AC.TextInput(key="email_input",
                                                        placeholder = "me@mine.mydomain",
                                                        data_validators = [oj.validator.InputRequired(),
                                                                           oj.validator.Email(), 
                                                                           ]

                                                        )

                                        ],
                              twsty_tags=[space/x/2]
                              )

notification_bar = oj.Mutable.Span(key="notification_bar",
                                   text = "",
                                   twsty_tags = [bg/yellow/"100/30"]
                                   )

contact_us_panel = oj.HCCMutable.Subsection("Contact Us",
                                    oj.Mutable.Form(key="intouch_form",
                                               childs = [email_fieldbox,
                                                         oj.AC.Button(key="form_button", text="Submit Form", twsty_tags=[bg/yellow/2, outline/yellow/4, mr/sl/4]
                                                                      )


                                                         ],
                                                    twsty_tags = [mr/x/8]
                                                    ), 
                                            twsty_tags = [mr/st/4]
                                    )
                              


tlc = oj.HCCMutable.Container(childs = [top_panel,
                                        oj.PC.Valign(price_panel, height_tag=H/"3/4",
                                                     ),
                                        launch_info_panel,
                                        contact_us_panel

                                        
                                        ],
                              twsty_tags=[]
                        )

wp_childs = [tlc]


