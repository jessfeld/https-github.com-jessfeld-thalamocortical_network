# Rename image files created by batch output for greater clarity

import re
import os

directory = "rasters_0.05"

nav_type = ['WT', 'T875M', 'W1204R', 'R1648H', 'R859C', 'knock_out'] 
drug     = ['no_drug', 'carbamazepine', 'oxcarbazepine', 'lamictal', 'eslicarb', 'VPA', 'diazepam']

batchParams = [nav_type, drug]

rgx_str = "(.*)" + "_([0-9]+)" * len(batchParams) + "(.*)"

for src in os.listdir(directory):

    rgx = re.match(rgx_str, src)

    src  = directory + '/' + src
    dst = directory + '/raster'
    
    for i, j in enumerate(rgx.groups()[1:-1]):
        dst = dst + '_' + batchParams[i][int(j)]
    dst = dst + '.png'

    print("renaming: " + src + "->" + dst)
    os.rename(src, dst)