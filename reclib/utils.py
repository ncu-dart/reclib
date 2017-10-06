# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 09-02-2017
# Last Modified: Fri Oct  6 16:15:23 2017

def get_num_users_items(X):
    users = set()
    items = set()
    for (user, item, r) in X:
        users.add(user)
        items.add(item)
    return len(users), len(items)
