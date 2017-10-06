# Hung-Hsuan Chen <hhchen@g.ncu.edu.tw>
# Creation Date : 10-06-2017
# Last Modified: Fri Oct  6 16:20:28 2017

class RecBase:
    def __init__(self):
        pass

    def predict(self, user_item_pairs):
        all_predicts = []
        for (ext_user_id, ext_item_id) in user_item_pairs:
            u = self.eu2iu[ext_user_id] if ext_user_id in self.eu2iu else -1
            i = self.ei2ii[ext_item_id] if ext_item_id in self.ei2ii else -1
            all_predicts.append((ext_user_id, ext_item_id, self.predict_single_rating(u, i)))
        return all_predicts

    def _external_internal_id_mapping(self, ratings):
        for (eu, ei, r) in ratings:
            if eu not in self.eu2iu:
                iu = len(self.eu2iu)
                self.eu2iu[eu] = iu
                self.iu2eu[iu] = eu
            if ei not in self.ei2ii:
                ii = len(self.ei2ii)
                self.ei2ii[ei] = ii
                self.ii2ei[ii] = ei

    def _compute_global_mean(self, ratings):
        rating_sum = 0.
        for ext_user_id, ext_item_id, r in ratings:
            rating_sum += float(r)
        return rating_sum / len(ratings)
