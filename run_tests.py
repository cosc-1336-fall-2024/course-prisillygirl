import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.b_in_proc_out import tests_in_proc_out
from examples.a_example input_process_output import input_process_output

suite = unittest.TestLoader().loadTestsFromModule(input_process_output)
unittest.TextTestRunner(verbosity=2).run(suite)
