from netpyne import specs
from netpyne.batch import Batch

params = specs.ODict()

params['nav_type'] = ['WT', 'T875M', 'W1204R', 'R1648H', 'R859C', 'knock out'] 
params['drug']     = ['no drug', 'carbamazepine', 'oxcarbazepine', 'lamictal', 'eslicarb', 'VPA', 'diazepam']

b = Batch(params = params, cfgFile = 'cfg.py', netParamsFile = 'netParams.py')

b.batchLabel = 'mut_drug'
b.saveFolder = 'batch_data'
b.method = 'grid'
b.runCfg = {'type': 'mpi_bulletin', 'script': 'init.py', 'skip': True}

b.run()