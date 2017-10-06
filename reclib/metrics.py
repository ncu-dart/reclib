# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 09-02-2017
# Last Modified: Fri Oct  6 18:39:12 2017

def rmse(X, X_hat):
    assert(len(X) == len(X_hat))
    sum_of_squares = 0.
    for i in range(len(X)):
        user, item, r = X[i]
        user_hat, item_hat, r_hat = X_hat[i]
        assert(user == user_hat)
        assert(item == item_hat)
        sum_of_squares += (r - r_hat) ** 2
    return (sum_of_squares / len(X)) ** .5


def r2_score(X, X_hat):
    assert(len(X) == len(X_hat))
    avg_score = _get_avg_score(X)
    sum_of_squares = 0.
    total_sum_of_squares = 0.
    for i in range(len(X)):
        user, item, r = X[i]
        user_hat, item_hat, r_hat = X_hat[i]
        assert(user == user_hat)
        assert(item == item_hat)
        sum_of_squares += (r - r_hat) ** 2
        total_sum_of_squares += (r - avg_score) ** 2
    return 1 - sum_of_squares / total_sum_of_squares


def  _get_avg_score(X):
    s = 0.
    for (user, item , r) in X:
        s += r
    return s / len(X)
