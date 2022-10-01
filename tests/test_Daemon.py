from .context import Daemon
import unittest

class TestDaemon(unittest.TestCase):

    def test_okay_to_run(self):
        args = []
        d = Daemon(args=args)
        self.assertTrue(d.okay_to_run())

    def test_args(self):
        args = ['-i', '10']
        d = Daemon(args=args)
        self.assertEqual(10, d.args.interval)

    def test_args_default(self):
        args = []
        d = Daemon(args=args)
        self.assertEqual(5, d.args.interval)

    def test_runner(self):
        args = []
        d = Daemon(args=args)
        d.run_daemon()
        self.assertTrue(True)