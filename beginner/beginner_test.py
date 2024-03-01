import unittest
from unittest.mock import patch

from io import StringIO
import csv
import itertools
import sys
import argparse
from heredity_beginner import *

class TestHeredity(unittest.TestCase):

    
    def test_parent_genotype(self):
        self.assertEqual(parent_genotype({2: 0, 1: 1, 0: 0}), 1)
        self.assertEqual(parent_genotype({2: 1, 1: 0, 0: 0}), 2)
        self.assertEqual(parent_genotype({2: 0, 1: 0, 0: 1}), 0)

    def test_trait_helper(self):
        self.assertEqual(trait_helper(2, 2)['gene'][2], 1)
        self.assertEqual(trait_helper(2, 1)['gene'][2], 0.5)
        self.assertEqual(trait_helper(2, 1)['gene'][1], 0.5)
        self.assertEqual(trait_helper(2, 0)['gene'][1], 1)
        self.assertEqual(trait_helper(1, 1)['gene'][2], 0.25)
        self.assertEqual(trait_helper(1, 1)['gene'][1], 0.5)
        self.assertEqual(trait_helper(1, 1)['gene'][0], 0.25)
        self.assertEqual(trait_helper(0, 0)['gene'][0], 1)

    @patch('sys.argv', ['heredity_beginner_pa.py', 'data/family0.csv'])
    def test_main(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main_output = main()

        print(mock_stdout.getvalue())
        '''
        The above print should match with this: \
        
        Harry:
            Gene:
                2: 0.0000
                1: 1.0000
                0: 0.0000
            Trait: 0
        James:
            Gene:
                2: 1.0000
                1: 0.0000
                0: 0.0000
            Trait: 1
        Lily:
            Gene:
                2: 0.0000
                1: 0.0000
                0: 1.0000
            Trait: 0
        '''

if __name__ == '__main__':
    unittest.main()
