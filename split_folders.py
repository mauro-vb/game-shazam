import splitfolders
import os
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.

folder = 'Dirty_10k'
folder_path = os.path.join('data',folder)

splitfolders.ratio(folder_path, output=folder_path + '_split',
    seed=1500, ratio=(.8, .2), group_prefix=None, move=True) # default values
