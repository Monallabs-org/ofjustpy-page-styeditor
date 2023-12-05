
Code layouts
^^^^^^^^^^^^
styeditor_components.py
.......................

- build_tw_styTags_panel(oj)
- build_tw_styValues_panel
  
mutable_wrapper
...............

provides new implementation for static/passive components
so that they can be modified via styeditor

- HCCPassiveJsonMixin

styjson_utils
..............
- build_component_hierarchy
- to_sty_json  

The super basics
++++++++++++++++
1. pse.create_endpoint to use pse services
2. pse.create_endpoint requires that the component be in separate
   file "wp_components'
3. `oj.load_app` should be called in the components file
4. for patch to work do reload from lowest component to top-most component.
5. we have created a mess with dpath and changes over dict and list item; stubstore
   cannot be int. 

   
Bits and Pieces
---------------

to_sty_json
^^^^^^^^^^^
The data model:

.. code-block:: json
		
   "parent_comp_key" :{
    "_cref": {
       "_sty": {
	  "passthrough": []
	  "spath" : ??
	  }
     } //end _cref
     "child_comp_key" {
     _cref : {
      _sty : {
	"
      "}

     }
     }

   }

The example:


.. code-block:: json

   {
       "test_page": {
	   "_cref": {
	       "_sty": {
		   "passthrough": [],
		   "spath": "/test_page"
	       }
	   },
	   "ati": {
	       "_cref": {
		   "_sty": {
		       "passthrough": [],
		       "bg": [{
			   "_val": "pink-100",
			   "_modifier_chain": []
		       }],
		       "opacity": [{
			   "_val": 80,
			   "_modifier_chain": []
		       }],
		       "spath": "/ActiveComps/ati"
		   }
	       }
	   },
	   "abtn": {
	       "_cref": {
		   "_sty": {
		       "passthrough": [],
		       "bg": [{
			   "_val": "green-300",
			   "_modifier_chain": []
		       }, {
			   "_val": "gray-200",
			   "_modifier_chain": ["hover"]
		       }],
		       "fc": [{
			   "_val": "gray-600",
			   "_modifier_chain": []
		       }],
		       "mr": [{
			   "sr": {
			       "_val": "1"
			   },
			   "_modifier_chain": []
		       }, {
			   "sb": {
			       "_val": "1"
			   },
			   "_modifier_chain": []
		       }],
		       "pd": [{
			   "x": {
			       "_val": "4"
			   },
			   "_modifier_chain": []
		       }, {
			   "y": {
			       "_val": "2"
			   },
			   "_modifier_chain": []
		       }],
		       "FontWeight": [{
			   "_val": "bold",
			   "_modifier_chain": []
		       }],
		       "Outline": [{
			   "_val": "_",
			   "_modifier_chain": []
		       }],
		       "BoxShadow": [{
			   "_val": "md",
			   "_modifier_chain": ["hover"]
		       }],
		       "TextTransform": [{
			   "_val": "u",
			   "_modifier_chain": []
		       }],
		       "outline": [{
			   "_val": 4,
			   "_modifier_chain": ["hover"]
		       }],
		       "BorderRadius": [{
			   "_val": "md",
			   "_modifier_chain": ["hover"]
		       }],
		       "spath": "/MutableComps/abtn"
		   }
	       }
	   }
       }
   }

   
The panels
+++++++++++

styTables
..........

For the selected component: show its twsty tags: why select to delete it.



devel
+++++

td_sbs_styedit_take1:
.....................
create endpoint via pse

td_sbs_mutable_wrapper
.........................
  
build_json and get_json_diff for passive components

./devel/td_build_and_view_component_hierarchy.py
.................................................

the test code to create  styeditor for a target webpage. Its already incorporated and
no longer needed.

devel/td_sbs_modify_via_navigator.py
.....................................

use wp_components to describe a page and load it.


Latest so far
+++++++++++++

- Added routines to build edit pipeline
  with ojr.ReactDomino.

- Next add mouseover (in edit-mode) to select components
  instead of hinav
  
  
  
