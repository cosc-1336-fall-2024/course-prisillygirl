
#from tests.homework.b_in_proc_out import tests_in_proc_out

import unittest
from tests.homework.e_functions import tests_functions 
#from tests.homework.c_decisions import tests_decisions #replace tests_in_proc_out with tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
from tests.homework.e_functions import tests_functions
suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner(verbosity=2).run(suite)