# myKnoxRepo

Port of Dravet thalamocortical seizure model.
For proper results, run with the multiple synapse netpyne version at: 
https://github.com/jchen6727/netpyne.git 
(a pull request is pending on the official netpyne version)

run with
python init.py

or with openmpi

mpiexec -n <numcores> nrniv -python -mpi init.python

a raster plot of the network activity will be in the images directory

raster plot of our results is located in the images folder as RESULTS.png


