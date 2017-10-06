# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 09-02-2017
# Last Modified: Fri Oct  6 16:14:03 2017

import pkg_resources

resource_package = __name__
rel_data_folder = '../data'


def load_data(filename):
    X = []
    with open(filename) as f:
        for line in f:
            user, item, rating = line.strip().split()
            X.append((int(user), int(item), float(rating)))
    return X


def load_movielens_100k():
    filename = pkg_resources.resource_filename(resource_package, '/'.join((rel_data_folder, 'ml-100k.dat')))
    return load_data(filename)


def load_filmtrust():
    filename = pkg_resources.resource_filename(resource_package, '/'.join((rel_data_folder, 'filmtrust.dat')))
    return load_data(filename)
