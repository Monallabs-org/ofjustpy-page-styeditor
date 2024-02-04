import ofjustpy as oj
from ofjustpy_engine import HC_Div_type_mixins as TR

oj.HC_TF.gen_HC_type(oj.HC_TF.HCType.passive,
                     "Label",
                     TR.LabelMixin,
                     )

