Known bugs


#. Passive/active components are not getting selected
   

Test-drive/Devel files
~~~~~~~~~~~~~~~~~~~~~~

#. td_sbs_item1_test_passive_event_handling.py : runs but selection via hinav not working


#. td_styedit_advanced_demos.py
   Turning out to be too broad; needs something simpler.
   HC_TF:gen_HC_type:mutable case is getting a bit too broad based. 

#. td_sbs_styedit_take1.py
   This one is outdated now; doesn't use wp_components

#. td_sbs_mutable_wrapper.py   
   This is up and running; not all features are active

#. td_sbs_item9_exec_attr_update_pipeline.py
   non-gui test script:

   • render the webpage
   • render the styeditor_endpoint
   • grab hold of stubStore, hinav of styeditor
   • grab the first child of the hierarchy
   • invoke the click on the button (selects the page)
   • again grab the first child
   • invoke the click on first child (button gets selected)
   • grab the input -- the utility class, fire change with mr as input
   • grab the input -- the attr , fire change with x as input
   • grab the input -- attr_value, fire change with 5 as input
   • click on the apply button 
     
#. td_sbs_item4_hinav_selection.py
   • test get_changed_diff_patch on active component
   • test get_changed_diff_patch on passive component
     

Patching logic
~~~~~~~~~~~~~~
- We are certainly replacing gen_HC_TF with our own gen_HC_TF.
  We also have hooks to swap out `ofjustpy_engine.SHC_types_mixin.StaticCore` with
  our own StaticCore. Not sure which one is being used.


- The patch/hook is working: pathced HC_TF.gen_HC_type is being used.
  Our gen_HC_type calls the oj.SHC_types_mixins.staticClassTypeGen.
  
- We have patched ofjustpy_engine.SHC_types_mixin.StaticCore which is working.
  So now the Dict is tracking Dict.

- What about JsonMixin
  
Stub and Mixins
~~~~~~~~~~~~~~~

For Passive Component
"""""""""""""""""""""
#. The stub: class 'page_style_editor.TF_impl.Stub_HCPassive
#. The WithStub class: declared in type-generator function page_style_editor.HC_TF   
#. The tracker gen_Stub_HCPassive(target, **kwargs):

For Passive Divs
""""""""""""""""
#. 
#.
#. 
Code Files
~~~~~~~~~~~~

#. mutable_wrapper

#. HC_TF
   HC_TF imports TR.EventMixin  

#. Div_TF
   

#. TF_impl:
   provides stubs for passives so that they can be registered.
   Also mixins common to both Div_TF and HC_TF

#. styeditor_sbs
   provides build_styeditor_endpoint



Component Architecture : which software component holds what
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Styeditor Page
   
   + hinav (depth_selector, childpanel)
   + selection panel
   + twstyle_panel
   + twtags_panel
     



The React Framework
~~~~~~~~~~~~~~~~~~~

/selected_hcobj 
