from unittest.mock import patch
import importlib
def gen_HC_type(*args, **kwargs):
    assert False
    
with patch('ofjustpy.HC_TF.gen_HC_type', new=gen_HC_type):
    import ofjustpy as oj
    wp_comp_mod = importlib.import_module("td_gen_HC_type")
