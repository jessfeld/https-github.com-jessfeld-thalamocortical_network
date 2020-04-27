# myKnoxRepo

test branch has 3 versions of inak2005
inak2005 is the orig
inak2005a is the one switched to NEURON inegration with cnexp
inak2005b is similar to orig but was editing to see if any minor changes made any difference

cd mods
`nrnivmodl` # to compile
cd ..
mv -rf mods/x86_64 x86_64
nrniv -python test.py

Port of Dravet thalamocortical seizure model.
For proper results, run with the multiple synapse netpyne version at: 
https://github.com/jchen6727/netpyne.git 
(a pull request is pending on the official netpyne development version)

cells are handled with genrn generic neuron cell template.

run with
python init.py

or with openmpi

mpiexec -n <numcores> nrniv -python -mpi init.py

a raster plot of the network activity will be in the images directory

raster plot of our results when running on 4 cores:

mpiexec -n 4 nrniv -python -mpi init.py

is located in the images folder as RESULTS.png:

images/RESULTS.png

NOTE IF YOU ARE USING OFFICIAL NETPYNE VERSION:

working with the current dev branch of netpyne will yield different results,
as GABA b receptors will be implemented as a single point process instead of
multiple point processes.

A raster plot resulting from running with the official netpyne development 
version (as opposed to the multiple synapse netpyne version) is located in the
images folder as RESULTS_DEV.png

images/RESULTS_DEV.png
