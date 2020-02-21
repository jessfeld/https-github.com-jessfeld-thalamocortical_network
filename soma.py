'''
Cells -- PY, TC, RE, IN  
'''

from neuron import h

class PYsoma():
    def __init__(self, x = 0, y = 0, z = 0, ID = 0):
        soma = h.Section()
        soma.L, soma.nseg, soma.diam, soma.Ra, soma.cm = 96, 1, 96, 100, 1
        
        soma.insert('im')
        soma.gkbar_im = 3e-5
        soma.taumax_im = 1000
        
        soma.insert('ina2005')
        soma.gnabar_ina2005 = 0.3
        
        soma.insert('ik2005')
        soma.gkbar_ik2005 = 0.03
        
        soma.insert('pas')
        soma.g_pas = 0.0001
        soma.e_pas = -77
        
        soma.ek = -100
        soma.ena = 50
        
        self.soma = soma

class TCsoma():
    def __init__(self, x = 0, y = 0, z = 0, ID = 0):
        soma = h.Section()
        soma.L, soma.nseg, soma.diam, soma.Ra, soma.cm = 96, 1, 96, 100, 1
        
        soma.insert('cad')
        soma.cainf_cad = 0.00024
        soma.depth_cad = 1.0
        soma.kt_cad = 0
        soma.taur_cad = 5

        soma.insert('iar')
        soma.Pc_iar = 0.01
        soma.cac_iar = 0.002
        soma.ghbar_iar = 2e-5
        soma.ginc_iar = 2
        soma.k2_iar = 0.0004
        soma.k4_iar = 0.001
        soma.nca_iar = 4
        soma.nexp_iar = 1

        soma.insert('ina2005')
        soma.gnabar_ina2005 = 0.15

        soma.insert('ik2005')
        soma.gkbar_ik2005 = 0.06

        soma.insert('it')
        soma.gcabar_it = 0.002
        soma.shift_it = 2

        soma.insert('pas')
        soma.g_pas = 1e-5
        soma.e_pas = -70

        soma.ek = -100
        soma.ena = 50
        
        kleak = h.kleak(soma(0.5))        
        kleak.gmax = 0.004
        
        self.soma = soma
        self.kleak = kleak

class REsoma():
    def __init__(self, x = 0, y = 0, z = 0, ID = 0):
        soma = h.Section()
        soma.L, soma.nseg, soma.diam, soma.Ra, soma.cm = 96, 1, 96, 100, 1
        
        soma.insert('cad')
        soma.cainf_cad = 0.00024
        soma.depth_cad = 1.0
        soma.kt_cad = 0
        soma.taur_cad = 5

        soma.insert('ina2005')
        soma.gnabar_ina2005 = 0.19

        soma.insert('ik2005')
        soma.gkbar_ik2005 = 0.06

        soma.insert('it2')
        soma.gcabar_it2 = 0.003
        soma.qh_it2  = 2.5
        soma.qm_it2 = 2.5
        soma.shift_it2  = 2.0
        soma.taubase_it2 = 85

        soma.insert('pas')
        soma.g_pas = 5e-5
        soma.e_pas = -90


        
        kleak.gmax = 0.004
        self.soma = soma
        self.kleak = kleak