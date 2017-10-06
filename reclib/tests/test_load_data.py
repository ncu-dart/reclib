#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hung-Hsuan Chen <hhchen@g.ncu.edu.tw>
# Creation Date : 10-06-2017
# Last Modified: Fri Oct  6 16:35:28 2017

from unittest import TestCase

import reclib

class TestLoadData(TestCase):
    def test_load_filmtrust(self):
        X = reclib.load_data.load_filmtrust()
        self.assertTrue(isinstance(X, list))
        self.assertTrue(isinstance(X[0], tuple))
        self.assertTrue(len(X[0]), 3)
        self.assertTrue(len(X) == 35497)

    # TODO: test other functions and modules
