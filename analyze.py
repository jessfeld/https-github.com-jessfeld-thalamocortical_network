# Analyze spike rasters

import pickle as pkl

pops = ['PY'       ,'IN'       ,'IN'       ,'TC'       ,'RE'   ]
#       0->99       100->199    200->299    300-399     400-499
spkdata = {}

# spike times, spike IDs, population, time granularity
def analyze( spkts, spkids, pops, mapfunc, dt ):
    spkts   = [ int( spkt/dt ) for spkt in spkts ]
    spktmax = spkts[-1]
    spkdata['PY'] = [ 0 for x in range(spktmax) ]
    spkdata['IN'] = [ 0 for x in range(spktmax) ]
    spkdata['TC'] = [ 0 for x in range(spktmax) ]
    spkdata['RE'] = [ 0 for x in range(spktmax) ]
    spkpops = [ pops[ int( spkid/100) ] for spkid in spkids]
    for i , spkpop in enumerate(spkpops):
        spk
    spkdata[spkpops][spkts]

    
    


if __name__ == "__main__":
    import re
    import os
    from batch import b, params

    directory = b.saveFolder

    rgx_str = b.batchLabel + "_([0-9]+)" * len(params) + "\.pkl"
    for src in [file for file in os.listdir(directory) if file[-3:] == 'pkl']:

        rgx = re.match(rgx_str, src)
        src = directory + '/' + src
        data = pkl.load( open( src, "rb") )

        spkt, spkid = data[[]]
        dst = directory + '/raster'

        for i, j in enumerate(rgx.groups()[1:-1]):
            dst = dst + '_' + batchParams[i][int(j)]
        dst = dst + '.png'

        print("renaming: " + src + "->" + dst)
        os.rename(src, dst)



    