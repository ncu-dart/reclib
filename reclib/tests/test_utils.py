#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hung-Hsuan Chen <hhchen@g.ncu.edu.tw>
# Creation Date : 10-06-2017
# Last Modified: Fri Oct  6 18:17:54 2017

from unittest import TestCase

import reclib

class TestUtils(TestCase):
    def test_get_num_users_items(self):
        X = [(1,2,3), (2,3,4), (3,4,5), (1,3,5), (1,4,5), (1,11,3)]
        n_users, n_items = reclib.utils.get_num_users_items(X)
        self.assertTrue(n_users == 3)
        self.assertTrue(n_items == 4)

        X = [('a','b',3), ('a','c',4), ('a','f',5), ('b','g',5), ('b','c',5), ('b','xyz',3)]
        n_users, n_items = reclib.utils.get_num_users_items(X)
        self.assertTrue(n_users == 2)
        self.assertTrue(n_items == 5)
