reclib
--------
Sample usage (with caution)::

>>> import reclib
>>> X = reclib.load_data.load_filmtrust()
>>> n_users, n_items = reclib.utils.get_num_users_items(X)
>>> rec = reclib.WSVD(n_users=n_users, n_items=n_items)
>>> rec.train(X)
>>> rec.predict_single_rating(1, 10)  # predict user 1's rating on item 10
>>> rec.predict([(1,10), (2,5)])  # predict user 1's rating on item 10 and user 2's rating on item 5
