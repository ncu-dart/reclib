# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 09-02-2017
# Last Modified: Thu 08 Feb 2018 03:26:16 PM CST

import collections


import numpy as np

from .rec_base import RecBase


class RVSVD(RecBase):
    """
    Regularization-Variant SVD
    """
    def __init__(
            self, n_users, n_items, n_factors=15, n_epochs=50,
            lr=.005, lr_bias=None, lr_latent=None,
            lmbda=1., lmbda_p=None, lmbda_q=None, lmbda_u=None, lmbda_i=None,
            lr_shrink_rate=.9, method="log", alpha=np.exp(1)):
        self.n_users = n_users
        self.n_items = n_items
        self.n_epochs = n_epochs
        self.n_factors = n_factors
        self.lr = lr
        self.lr_bias = lr if lr_bias is None else lr_bias
        self.lr_latent = lr if lr_latent is None else lr_latent
        self.lmbda = lmbda
        self.lmbda_p = lmbda if lmbda_p is None else lmbda_p
        self.lmbda_q = lmbda if lmbda_q is None else lmbda_q
        self.lmbda_u = lmbda if lmbda_u is None else lmbda_u
        self.lmbda_i = lmbda if lmbda_i is None else lmbda_i
        self.lr_shrink_rate = lr_shrink_rate
        self.eu2iu = {}  # external-user to internal-user id
        self.iu2eu = {}  # internal-user to external-user id
        self.ei2ii = {}  # external-item to internal-item id
        self.ii2ei = {}  # internal-item to external-item id
        self.P = np.random.randn(self.n_users, self.n_factors)
        self.Q = np.random.randn(self.n_items, self.n_factors)
        self.bu = np.zeros(self.n_users)
        self.bi = np.zeros(self.n_items)
        self.method = method
        self.alpha = alpha
        self.n_user_rating = None
        self.n_item_rating = None

    def train(self, ratings, validate_ratings=None, show_process_rmse=True):
        self._external_internal_id_mapping(ratings)
        self.global_mean = self._compute_global_mean(ratings)
        self._compute_n_user_item_rating(ratings)


        for epoch in range(self.n_epochs):
            epoch_shrink = self.lr_shrink_rate ** epoch
            for (ext_user_id, ext_item_id, r) in ratings:
                err = r - self.predict_single_rating(ext_user_id, ext_item_id)
                u = self.eu2iu[ext_user_id]
                i = self.ei2ii[ext_item_id]
                r = float(r)
                bu = self.bu[u]
                bi = self.bi[i]
                pu = self.P[u, :]
                qi = self.Q[i, :]

                reg_bu = (
                    self.lmbda_u / np.log(self.n_user_rating[u] + self.alpha)
                    ) if self.method == "log" else (
                    self.lmbda_u / (self.n_user_rating[u] + self.alpha))
                reg_bi = (
                    self.lmbda_i / np.log(self.n_item_rating[i] + self.alpha)
                    ) if self.method == "log" else (
                    self.lmbda_i / (self.n_item_rating[i] + self.alpha))
                reg_pu = (
                    self.lmbda_p / np.log(self.n_user_rating[u] + self.alpha)
                    ) if self.method == "log" else (
                    self.lmbda_p / (self.n_user_rating[u] + self.alpha))
                reg_qi = (
                    self.lmbda_q / np.log(self.n_item_rating[i] + self.alpha)
                    ) if self.method == "log" else (
                    self.lmbda_q / (self.n_item_rating[i] + self.alpha))

                self.bu[u] -= (self.lr_bias * epoch_shrink) * (
                    -err + reg_bu * bu)
                self.bi[i] -= (self.lr_bias * epoch_shrink) * (
                    -err + reg_bi * bi)
                self.P[u, :] -= (self.lr_latent * epoch_shrink) * (
                    -err * qi + reg_pu * pu)
                self.Q[i, :] -= (self.lr_latent * epoch_shrink) * (
                    -err * pu + reg_qi * qi)
            if show_process_rmse:
                if validate_ratings is None:
                    loss, rmse = self._compute_err(ratings)
                    print("After %i epochs, loss=%.6f, training rmse=%.6f" % (
                        epoch+1, loss, rmse))
                else:
                    loss, rmse = self._compute_err(validate_ratings)
                    print(
                        "After %i epochs, loss=%.6f, validating rmse=%.6f" % (
                            epoch+1, loss, rmse))
            else:
                print("After %i epoch" % (epoch+1))

    def predict_single_rating(self, ext_user_id, ext_item_id):
        u = self.eu2iu[ext_user_id] if ext_user_id in self.eu2iu else -1
        i = self.ei2ii[ext_item_id] if ext_item_id in self.ei2ii else -1
        bu = self.bu[u] if u >= 0 else 0
        bi = self.bi[i] if i >= 0 else 0
        pu = self.P[u, :] if u >= 0 else np.zeros(self.n_factors)
        qi = self.Q[i, :] if i >= 0 else np.zeros(self.n_factors)
        return self.global_mean + bu + bi + np.dot(pu, qi)

    def predict(self, user_item_pairs):
        return super().predict(user_item_pairs)

    def _external_internal_id_mapping(self, ratings):
        return super()._external_internal_id_mapping(ratings)

    def _compute_global_mean(self, ratings):
        return super()._compute_global_mean(ratings)

    def _compute_n_user_item_rating(self, ratings):
        n_user_rating = collections.defaultdict(int)
        n_item_rating = collections.defaultdict(int)
        for (ext_user_id, ext_item_id, r) in ratings:
            u = self.eu2iu[ext_user_id]
            i = self.ei2ii[ext_item_id]
            n_user_rating[u] += 1
            n_item_rating[i] += 1
        self.n_user_rating = dict(n_user_rating)
        self.n_item_rating = dict(n_item_rating)

    def _compute_err(self, ratings):
        loss = 0.
        sse = 0.

        for (ext_user_id, ext_item_id, r) in ratings:
            num_user_rating = self.n_user_rating[ext_user_id] if ext_user_id in self.n_user_rating else 0
            num_item_rating = self.n_item_rating[ext_item_id] if ext_item_id in self.n_item_rating else 0
            r = float(r)
            err_square = (
                r - self.predict_single_rating(ext_user_id, ext_item_id)) ** 2
            sse += err_square
            loss += err_square
        loss += self.lmbda_p / np.log(num_user_rating + self.alpha) * np.linalg.norm(self.P) + \
            self.lmbda_q / np.log(num_item_rating + self.alpha) * np.linalg.norm(self.Q) + \
            self.lmbda_u / np.log(num_user_rating + self.alpha) * np.linalg.norm(self.bu) + \
            self.lmbda_i / np.log(num_item_rating + self.alpha) * np.linalg.norm(self.bi)
        return loss, (sse / len(ratings)) ** .5
