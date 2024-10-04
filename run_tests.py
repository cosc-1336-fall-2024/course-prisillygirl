
#from tests.homework.b_in_proc_out import tests_in_proc_out

import unittest
from tests.homework.h_strings import tests_strings
#from tests.homework.c_decisions import tests_decisions #replace tests_in_proc_out with tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
from tests.homework.e_functions import tests_functions
suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)