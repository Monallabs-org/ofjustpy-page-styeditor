""" manipulation of webpage style represented as json
"""
from py_tailwind_utils import tstr

import json
import logging
import os
import sys
import jsbeautifier
from dpath.util import get as dget, set as dset,  new as dnew
from addict_tracking_changes import Dict
#from jsonpath_ng import parse
from jsonpath_ng.ext import parse
from  py_tailwind_utils import styClause

opts = jsbeautifier.default_options()
logger = logging.getLogger(__name__)

import re

def convert_jsonpath_to_dpath(jsonpath):
    # Parse the JSONPath expression
    
    logger.debug(f"input = {jsonpath}")
    # Convert the expression to a string and replace index-based syntax with key-based syntax
    output = "/" + re.sub(r'\.\[(\d+)\]', r'/\1', str(jsonpath)).replace('.', '/')  
    logger.debug(f"{jsonpath} converted-to  {output}" )
    return output



def matched_kpaths(jsonPathExpr: str, jsonDict: Dict):
    """find paths in jsonDict that match jsonPathExpr. 
    jsonDict:json expressed as nested dictionary
    jsonPathExpr: json path query
    Returns kpath of type /a/b/c.
    """
    try:
        
        jsonpath_expr = parse(jsonPathExpr)
    except:
        logger.debug(f"unable to parse {jsonPathExpr}")
        return
    
    num_matches = 0
    for _ in jsonpath_expr.find(jsonDict):
        #logger.debug(f"mpath: {_.full_path}")
        num_matches += 1
    if num_matches == 0:
        print(f"json path expression {jsonPathExpr} has no matches")
        logger.info(
            f"json path expression {jsonPathExpr} has no matches")
        # logger.debug(session_dict['styj'])
    for jpath_matched in jsonpath_expr.find(jsonDict):
        yield convert_jsonpath_to_dpath(jpath_matched.full_path)
        



# def save_sty():
#     logger.debug("saving sty in styreport.json")
#     with open("styreport.json", "w") as fh:
#         res = jsbeautifier.beautify(json.dumps(session_dict['styj']), opts)
#         fh.write(res)

def update_sty(abs_sty_xpath, sty_attr_xpath, sty_value, styj, stubStore):
    """
    update 
    """
    # path from root to sty
    # TODO: this needs to be more generic
    #logger.debug(f"update a match {kpath}")
    dset(styj, abs_sty_xpath +
         "/_val", sty_value)

    # from kpath remove the tail
    # assuming tail doesnot have .. expression
    component_path = abs_sty_xpath.replace("/" + sty_attr_xpath.replace(".", "/"), "")
    component_spath = dget(styj,   component_path + "/spath")
    sref = dget(stubStore, component_spath)
    dbref = sref.target
    styUpdated = tstr(*styClause.to_clause(styj))
    #logger.debug(f"styUp {styUpdated}")
    # print(spath, " ", dbref.key, " ", dbref.classes)
    if 'webpage' in kpath:
        logger.debug(
            f"SKIPPING : {kpath} for now : FIX ME {styUpdated}")
    else:
        logging.debug(
            f"updatding {spath}-/-{kpath}/{dbref.key} from {dbref.classes} to {styUpdated}")
        
    # not so fast. update the twsty_tags and then update classes
    #dbref.classes = styUpdated

    # ====================== end =====================
                    

# def set_sty(stypath: str, styreport: Dict):
#     """
#     update the sty/classes of hc defined
#     styreport/stypath.
#     """
#     spath = dget(
#         styreport,   stypath + "/spath")
#     styj = dget(styreport,   stypath)
#     #logger.debug(f"spath {spath}")
#     sref = dget(stubStore, spath)
#     dbref = sref.target

#     styUpdated = tstr(*styClause.to_clause(styj))
#     #logger.debug(f"styUp {styUpdated}")

#     if 'wp_index._sty' in stypath:  # TODO: this isn't correct predicate to locate webapge
#         logger.debug(
#             f"SKIPPING : {stypath} for now : FIX ME {styUpdated}")
#     else:
#         logger.debug(
#             f"updatding {spath}-/-{dbref.key} from {dbref.classes} to {styUpdated}")
#         dbref.classes = styUpdated


# def set_sty_styreport(styreport: Dict):
#     """
#     apply sty to every HC of the main wp
#     """
#     for k, v in dict_walker(styreport, guards=["_sty"]):
#         set_sty(k, styreport)
#         pass
#     pass


# def apply_sty_from_file():
#     with open("styreport.json", "r") as fh:
#         styreport = Dict(json.load(fh.read()))
#         set_sty_styreport(styreport)
#     pass


# def build_json_from_kpaths(kpaths):
#     resJson = Dict()

#     def process_kpath(kpath):
#         print(f"now processing {kpath}")
#         try:
#             dnew(resJson, kpath, True)
#         except Exception as e:
#             print("got exception is build_json", e)
#             pass
#     res = [_ for _ in map(process_kpath, kpaths)]
#     print(resJson)
#     return resJson



def walker(de, kpath="/"):
    if getattr(de, 'components', None):
        if de.components:
            for ce in de.components:
                yield from walker(ce, f"{kpath}{de.key}/")
            yield f"{kpath}{de.key}/_cref", de
        elif getattr(de, "key", None):
            yield f"{kpath}{de.key}", de
    elif getattr(de, "key", None):
        yield f"{kpath}{de.key}/_cref", de

    


# def walker(de, kpath="/"):
#     if de.components:
#         for ce in de.components:
#             yield from walker(ce, f"{kpath}{de.stub.key}/")
#     else:
#         yield f"{kpath}{de.stub.key}", de


def build_component_hierarchy(root_component):
    component_hierarchy = Dict()
    for cpath, ce in walker(root_component):
        #print ("walker ", cpath, " ", ce.stub.spath)
        dnew(component_hierarchy, cpath, ce)
    return component_hierarchy


def annotate_styreport(de):
    rr = styClause.to_json(*de.twsty_tags)
    #rr.hctype = de.stub.hcgen.__name__
    rr.spath = de.id
    x = Dict()
    x._sty = rr
    return x


def to_sty_json(rootdspe):
    """
    rootdspe: basically root dbref

    """
    styreport = Dict(track_changes=True)
    for kpath, de in walker(rootdspe):
        rr = annotate_styreport(de)
        dnew(styreport, kpath, rr)

    return styreport
