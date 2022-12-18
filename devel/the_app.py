import ofjustpy as oj
import ofjustpy_engine
from unittest.mock import patch

import uvicorn, logging, sys, os, traceback

# with patch.object(ofjustpy_engine.SHC_types_mixin.PassiveJsonMixin,
#                                                                                                                                                                     'get_changed_diff_patch',
#                                                                                                                                                                     return_value = wrapper_get_changed_diff_patch(ofjustpy_engine.SHC_types_mixin.PassiveJsonMixin.get_changed_diff_patch)
#                                                                                                                                                                     ):

app  = oj.build_app()





