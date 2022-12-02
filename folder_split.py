import splitfolders
import os
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.

folder = 'initial_scrape'
folder_path = os.path.join('data',folder)

splitfolders.ratio(folder_path, output=folder_path + '_split',
    seed=1337, ratio=(.6, .2,.2), group_prefix=None, move=True) # default values
