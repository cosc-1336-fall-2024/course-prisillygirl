
#from tests.homework.b_in_proc_out import tests_in_proc_out

import unittest
from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets
#from tests.homework.c_decisions import tests_decisions #replace tests_in_proc_out with tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
from tests.homework.e_functions import tests_functions
suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)