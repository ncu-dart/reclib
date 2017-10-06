#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hung-Hsuan Chen <hhchen@g.ncu.edu.tw>
# Creation Date : 10-06-2017
# Last Modified: Fri Oct  6 17:55:08 2017

import os
import sys
import pickle

import reclib

def usage(cmd):
    print('Usage: %s [test-file] [model-file] [output-file]' % (cmd))
    return


def check_args(argv):
    if len(argv) != 4:
        usage(argv[0])
        sys.exit(-1)

    if not os.path.isfile(argv[1]):
        print("[%s] is not a valid file" % (argv[1]))
        usage(argv[0])
        sys.exit(-1)

    if not os.path.isfile(argv[2]):
        print("[%s] is not a valid file" % (argv[2]))
        usage(argv[0])
        sys.exit(-1)


def output(f, s):
    print(s)
    f.write(s + '\n')


def main(argv):
    check_args(argv)

    with open(argv[2], 'rb') as f_in:
        wsvd = pickle.load(f_in)

    X_test = reclib.load_data.load_data(argv[1])
    loss, rmse = wsvd.compute_err(X_test)
    # TODO: compute other regression performance measures

    with open(argv[3], 'w') as f_out:
        output(f_out, "RMSE: %f" % (rmse))


if __name__ == "__main__":
    main(sys.argv)
