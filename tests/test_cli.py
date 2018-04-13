"""Tests for our main placeholder_name CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from placeholder_name import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['placeholder_name', '-h'], stdout=PIPE, universal_newlines=True).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['placeholder_name', '--help'], stdout=PIPE, universal_newlines=True).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['placeholder_name', '--version'], stdout=PIPE, universal_newlines=True).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
