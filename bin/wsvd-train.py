#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hung-Hsuan Chen <hhchen@g.ncu.edu.tw>
# Creation Date : 10-06-2017
# Last Modified: Wed Oct 11 14:30:45 2017

import os
import sys
import pickle

import reclib

def usage(cmd):
    print('Usage: %s [train-file]' % (cmd))
    return


def check_args(argv):
    if len(argv) != 2:
        usage(argv[0])
        sys.exit(-1)

    if not os.path.isfile(argv[1]):
        print("[%s] is not a valid file" % (argv[1]))
        usage(argv[0])
        sys.exit(-1)


def main(argv):
    check_args(argv)

    X = reclib.load_data.load_data(argv[1])
    n_users, n_items = reclib.utils.get_num_users_items(X)
    rec = reclib.WSVD(n_users=n_users, n_items=n_items)
    rec.train(X)

    dump_filename = os.path.splitext(os.path.basename(argv[1]))[0] + '-wsvd-model.pck'
    with open(dump_filename, 'wb') as f_out:
        pickle.dump(rec, f_out, pickle.HIGHEST_PROTOCOL)
    print("Model is saved at '%s'" % (dump_filename))


if __name__ == "__main__":
    main(sys.argv)
