#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hung-Hsuan Chen <hhchen@g.ncu.edu.tw>
# Creation Date : 10-06-2017
# Last Modified: Sat Oct  7 07:56:44 2017

from unittest import TestCase

import numpy as np

import reclib

class TestMetrics(TestCase):
    def test_rmse(self):
        X = [(1,2,3), (2,3,4), (3,4,5), (1,3,5), (1,4,5), (1,11,3)]
        X_hat = [(1,2,3), (2,3,4), (3,4,5), (1,3,5), (1,4,5), (1,11,3)]
        self.assertTrue(reclib.metrics.rmse(X, X_hat) == 0)

        X_hat = [(1,2,4), (2,3,3), (3,4,4.5), (1,3,5), (1,4,5), (1,11,2.5)]
        self.assertTrue(reclib.metrics.rmse(X, X_hat) == (2.5/6) ** .5)

    def test_r2_score(self):
        X = [(1,2,2), (2,3,4), (3,4,5), (1,3,5), (1,4,5), (1,11,3)]
        X_hat = [(1,2,2), (2,3,4), (3,4,5), (1,3,5), (1,4,5), (1,11,3)]
        self.assertTrue(reclib.metrics.r2_score(X, X_hat) == 1)

        X_hat = [(1,2,4), (2,3,3), (3,4,4.5), (1,3,5), (1,4,5), (1,11,2.5)]
        r_bar = np.mean([x[2] for x in X])
        rmse = (1 - np.sum([(X[i][2]-X_hat[i][2]) ** 2 for i in range(len(X))]) / 
                np.sum([(X[i][2]-r_bar) ** 2 for i in range(len(X))]))
        self.assertTrue(reclib.metrics.r2_score(X, X_hat) == rmse)
