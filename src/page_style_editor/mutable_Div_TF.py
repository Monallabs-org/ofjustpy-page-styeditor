"""
A single API to generate various types of mutable Div: HCCMutable, HCCStatic, Mutable
"""
import json

from addict_tracking_changes import Dict
from addict_tracking_changes_fixed_attributes import EmptyDict, OneKeyDict

from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine.mutable_TF_impl import (CoreChildMixin,
                                             DivMutable_JsonMixin,
                                             HCCMixin_MutableChilds,
                                             RenderHTML_HCCMutableChildsMixin,
                                             RenderHTML_HCCStaticChildsMixin,
                                             Prepare_HtmlRenderMixin,
                                             HCCMixin_StaticChilds,
                                             HCCMutable_JsonMixin,
                                             HCCStatic_JsonMixin,
                                             StaticCore_JsonMixin,
                                             StaticCoreSharer_BaseMixin,
                                             StaticCoreSharer_ClassesMixin,
                                             StaticCoreSharer_EventMixin,
                                             StaticCoreSharer_HCCStaticMixin,
                                             StaticCoreSharer_IdMixin,
                                             )


def HCCMutableClassGen(
    hc_tag="Div",
    hctag_mixin=TR.DivMixin,
    static_core_mixins=[],
    mutable_shell_mixins=[],
        is_childs_mutable=True,
    is_self_mutable=False,
):
    """
    mutable_shell_json_mixin: this argument has been added
    to configure gen Div Types from page_style_editor
    """
    assert is_childs_mutable or is_self_mutable

    core_mixins = [
            TR.jpBaseComponentMixin,
        TR.EventMixin,
            TR.PassiveKeyMixin,
            StaticCore_JsonMixin,
            #CoreChildMixin,
            hctag_mixin,
            Prepare_HtmlRenderMixin,
        
    ]

    shell_mixins = [TR.TwStyMixin]
    static_core_sharer = (StaticCoreSharer_BaseMixin, StaticCoreSharer_EventMixin, StaticCoreSharer_IdMixin)

    core_mixins.append(CoreChildMixin)
    shell_mixins.append(HCCMixin_MutableChilds)
    shell_mixins.append(RenderHTML_HCCMutableChildsMixin)
    shell_mixins.append(DivMutable_JsonMixin)
    
    attr_tracked_keys = []
    domDict_tracked_keys = []

    for mixin in [*mutable_shell_mixins, *shell_mixins]:
        for _ in mixin.attr_tracked_keys:
            attr_tracked_keys.append(_)
        for _ in mixin.domDict_tracked_keys:
            domDict_tracked_keys.append(_)

    shell_mixins.append(TR.DOMEdgeMixin)

    class StaticCore(*core_mixins, *static_core_mixins):
        def __init__(self, *args, **kwargs):
            self.domDict = Dict()
            self.attrs = Dict()
            self.htmlRender_attr = []
            self.htmlRender_body = []
            for _ in core_mixins:
                _.__init__(self, *args, **kwargs)

            for _ in static_core_mixins:
                _.__init__(self, *args, **kwargs)

        def post_id_assign_callback(self):
            self.prepare_htmlRender()
            pass
        
        def prepare_htmlRender(self):
            self.htmlRender_chunk1 = f'''<{self.html_tag} {" ".join(self.htmlRender_attr)}'''
            self.htmlRender_chunk2 = f'''>{"".join(self.htmlRender_body)}'''
            self.htmlRender_chunk3 = f'''</{self.html_tag}>'''
            
            pass
        
    class MutableShell(
        *static_core_sharer,
        *shell_mixins,
        *mutable_shell_mixins,
    ):
        def __init__(self, *args, **kwargs):
            if len(domDict_tracked_keys) == 0:
                self.domDict = EmptyDict()
            elif len(domDict_tracked_keys) == 1:
                self.domDict = OneKeyDict(domDict_tracked_keys[0])
            else:
                self.domDict = Dict(track_changes=True)

            self.attrs = Dict(track_changes=True)
            self.htmlRender_attr = []
            self.htmlRender_body = []
            for _ in static_core_sharer:
                _.__init__(self, *args, **kwargs)

            for _ in shell_mixins:
                _.__init__(self, *args, **kwargs)

            for _ in mutable_shell_mixins:
                _.__init__(self, *args, **kwargs)

        def prepare_htmlRender(self):
            """
            mutable shells do not prepare render chunks
            
            """
            pass


    return StaticCore, MutableShell
