# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:01:11 2017

@author: rt
"""

from neuron import h

class sTC(object):
    def __init__(self):
        self.v_potassium = -100		# potassium reversal potential 
        self.v_sodium = 50			# sodium reversal potential 
        self.vtraub = -25	# High threshold to simulated IA
        self.proportion_custom = 0
          
        self.create_sections()
        self.define_geometry()
        self.define_biophysics()
    #
    def create_sections(self):
        """Create the sections of the cell."""
        # NOTE: cell=self is required to tell NEURON of this object.
        self.soma = h.Section(name='soma', cell=self)
    #
    def define_geometry(self):
        """Set the 3D geometry of the cell."""
        self.soma.L = self.soma.diam = 96 # microns
    #
    def define_biophysics(self):
        """Assign the membrane properties across the cell."""
        self.soma.Ra = 100    # Axial resistance in Ohm * cm
        self.soma.cm = 1      # Membrane capacitance in micro Farads / cm^2
        # Insert active Hodgkin-Huxley current in the soma
        self.soma.insert('hh2')
        self.soma.gnabar_hh2 = 0.09  # Sodium conductance in S/cm2
        self.soma.gkbar_hh2 = 0.01  # Potassium conductance in S/cm2
        self.soma.ek = self.v_potassium
        self.soma.ena = self.v_sodium
        self.soma.vtraub_hh2 = self.vtraub
        
        self.soma.insert('pas')
        self.soma.g_pas = 1e-5    # Leak conductance in S/cm2
        self.soma.e_pas = -70     # Reversal potential in mV
        
        self.soma.insert('it')		# T-current 
        self.soma.cai = 2.4e-4 
        self.soma.cao = 2 
        self.soma.eca = 120 
        self.soma.gcabar_it = 0.002 * (1-self.proportion_custom)
        self.soma.shift_it = 2
        
        self.soma.insert('ittccustom')
        self.soma.gcabar_ittccustom = 0.002 * self.proportion_custom
        self.soma.shift_ittccustom = 2
        self.soma.taubase_ittccustom = 30.8
        
        self.soma.insert('iar')		# h-current
        self.soma.eh = -40
        self.soma.nca_iar = 4		# nb of binding sites for Ca++ on protein
        self.soma.k2_iar = 0.0004		# decay of Ca++ binding on protein
        self.soma.cac_iar = 0.002		# half-activation of Ca++ binding
        self.soma.nexp_iar = 1		# nb of binding sites on Ih channel
        self.soma.k4_iar = 0.001		# decay of protein binding on Ih channel
        self.soma.Pc_iar = 0.01		# half-activation of binding on Ih channel
        self.soma.ginc_iar = 2		# augm of conductance of bound Ih
        self.soma.ghbar_iar = 1.7e-5 # 2e-5	# low Ih for slow oscillations
        
        self.soma.insert('cad')		# calcium decay
        self.soma.depth_cad = 1
        self.soma.taur_cad = 5
        self.soma.cainf_cad = 2.4e-4
        self.soma.kt_cad = 0		# no pump
    #
