# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 09-02-2017
# Last Modified: Wed Oct 18 22:24:30 2017

import pkg_resources

resource_package = __name__
data_folder = 'data'


def load_data(filename):
    X = []
    with open(filename) as f:
        for line in f:
            # TODO: what if the separator is not space-like symbols?
            # fix the issue
            user, item, rating = line.strip().split()
            X.append((user, item, float(rating)))
    return X


def load_movielens_100k():
    filename = pkg_resources.resource_filename(resource_package, '/'.join((data_folder, 'ml-100k.dat')))
    return load_data(filename)


def load_filmtrust():
    filename = pkg_resources.resource_filename(resource_package, '/'.join((data_folder, 'filmtrust.dat')))
    return load_data(filename)
