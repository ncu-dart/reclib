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

Command line tools

1. Generating the training model:

    wsvd-train.py [train-file]

This will generate a model file of the name `[train-file]-wsvd-model.pck`

2. Test the model by:

    predict.py [test-file] [model-file] [output-file]

This will show the RMSE scores on the screen and also saved in the `[output-file]`.
