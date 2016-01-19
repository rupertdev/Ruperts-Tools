import mobi2epub

import mock
import unittest

class ScriptTestCase(unittest.TestCase):
    @mock.patch('mobi2epub.ArgumentParser')
    def test_args_start(self, argparse_mock):

        mobi2epub()

        self.assertTrue(argparse_mock.called)

class BatchConvertTestCase(unittest.TestCase):
    def test_works(self):
        self.assertFalse(False)
