======
reclib
======

****************************
Sample usage (with caution):
****************************

>>> import reclib
>>> X = reclib.load_data.load_filmtrust()
>>> n_users, n_items = reclib.utils.get_num_users_items(X)
>>> rec = reclib.WSVD(n_users=n_users, n_items=n_items)  # use Weighted-SVD model
>>> rec.train(X)
>>> rec.predict_single_rating(1, 10)  # predict user 1's rating on item 10
>>> rec.predict([(1,10), (2,5)])  # predict user 1's rating on item 10 and user 2's rating on item 5
>>> 
>>> rec2 = reclib.SVD(n_users=n_users, n_items=n_items)  # use the SVD model
>>> rec2.train(X)

***************
How to install:
***************

``python setup.py install``

*******************
Command line tools:
*******************

To generate the WSVD model, run:
=================================

``wsvd-train.py [train-file]``

This will generate a model file of the name ``[train-file]-wsvd-model.pck``

To generate the SVD model, run:
================================

``svd-train.py [train-file]``

This will generate a model file of the name ``[train-file]-svd-model.pck``

Test the model by:
===================

``rec-predict.py [test-file] [model-file] [output-file]``

This will show the RMSE scores on the screen and also saved in the ``[output-file]``.
