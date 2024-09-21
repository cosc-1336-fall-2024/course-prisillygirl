
#from tests.homework.b_in_proc_out import tests_in_proc_out

import unittest
from tests.homework.c_decisions import tests_decisions #replace tests_in_proc_out with tests_decisions
#from tests.homework.c_decisions import tests_decisions #replace tests_in_proc_out with tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
from tests.homework.d_repetition import tests_repetition
suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)