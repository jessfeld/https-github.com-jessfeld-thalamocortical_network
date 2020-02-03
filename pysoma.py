'''
Cells -- PY, TC, RE, IN  
'''

from neuron import h

class PYsoma():
    def __init__(self, x = 0, y = 0, z = 0, ID = 0):
        soma = h.Section()
        soma.L, soma.nseg, soma.diam, soma.Ra, soma.cm = 96, 1, 96, 100, 1
        
        soma.insert('im')
        soma.insert('ina2005')
        soma.insert('ik2005')
        soma.insert('pas')
        
        soma.gkbar_im = 3e-5
        soma.taumax_im = 1000

        soma.gnabar_ina2005 = 0.3
        
        soma.gkbar_ik2005 = 0.03

        soma.g_pas = 0.0001
        soma.e_pas = -77

        self.soma = soma

class TCsoma():
    def __init__(self, x = 0, y = 0, z = 0, ID = 0):
        soma = h.Section()
        soma.L, soma.nseg, soma.diam, soma.Ra, soma.cm = 96, 1, 96, 100, 1
        
        soma.insert('cad')
        soma.insert('iar')
        soma.insert('ina2005')
        soma.insert('ik2005')
        soma.insert('it')
        soma.insert('pas')

        kleak = h.kleak(soma(0.5))
        soma(0.5).insert('kleak')
        
        soma.cainf_cad = 0.00024
        soma.depth_cad = 1.0
        soma.kt_cad = 0
        soma.taur_cad = 5

        soma.Pc_iar = 0.01
        soma.cac_iar = 0.002
        soma.ghbar_iar = 2e-5
        soma.ginc_iar = 2
        soma.k2_iar = 0.0004
        soma.k4_iar = 0.001
        soma.nca_iar = 4
        soma.nexp_iar = 1

        soma.gnabar_ina2005 = 0.15
        soma.gkbar_ik2005 = 0.06

        soma.gcabar_it = 0.002
        soma.shift_it = 2
        
        soma.g_pas = 1e-5
        soma.e_pas = -77
        
        soma(0.5).k
        self.soma = soma





gk = gkbar * (v - ek)

.03 * (v + 100)

.03*v + 3

.03*v + 2.31
class cfiber():
    secs = {'axnperi': {'nseg':100, 'L':5000, 'diam': .8  }, 
            'axncntr': {'nseg':100, 'L':5000, 'diam': .4  },
            'drgperi': {'nseg':100, 'L':100,  'diam': .8  },
            'drgcntr': {'nseg':100, 'L':100,  'diam': .4  },
            'drgstem': {'nseg':100, 'L':75,   'diam': 1.4 },
            'drgsoma': {'nseg':1,   'L':25,   'diam': 25  }}
        #if we treat the total expression of NaV channels as 1
        #we can distribute conductance as approximately
        #gnabar17 = 1/6, gnabar18 = 3/6, gnabar19 = 2/6
        #if using transcriptome profile

    def __init__(self,x=0,y=0,z=0,ID=0, navs = {'na17a': 0.04/6, 'na18a': 0.12/6, 'na19a': 0.08/6} ):
        self.regions = {'all': [], 'axn': [], 'drg': [], 'soma': []}
        
        self.navs = navs

        self.set_morphology()
        self.insert_conductances()
        
        self.connect_secs()
        self.initialize_values()

    def add_comp(self, sec, *regions):
        self.__dict__[sec] = h.Section(name=sec)
        for region in regions:
            self.regions[region].append(self.__dict__[sec])

    def set_morphology(self):

        for sec in ['axnperi', 'axncntr', 'drgperi', 'drgcntr', 'drgstem']:
            self.add_comp(sec, sec[0:3], 'all')
            self.set_geom(sec)

        for sec in ['drgsoma']:
            self.add_comp(sec, 'drg', 'soma', 'all')
            self.set_geom(sec)

    def set_geom(self, sec):
        self.__dict__[sec].nseg = cfiber.secs[sec]['nseg']
        self.__dict__[sec].L    = cfiber.secs[sec]['L']
        self.__dict__[sec].diam = cfiber.secs[sec]['diam']

    def insert_conductances (self):
        
        for sec in self.regions['axn'] + self.regions['drg']:
            sec.Ra    = 100
            
            for nav in self.navs:
                sec.insert(nav)
                exestr = "sec.gnabar_%s = self.navs[nav]" %(nav)
                exec(exestr)

            sec.insert('borgkdr')
            sec.gkdrbar_borgkdr = 0.04
            sec.ek = -90
            
            sec.insert('pas')
            sec.g_pas = 1/10000
            ##sec.e_pas = -60
            
        for sec in self.regions['drg']:
            
            ##sec.e_pas = -54
            
            sec.insert('iM')
            sec.gkbar_iM = 0.0004
            sec.vshift_iM = -5

        for sec in self.regions['soma']:

            for nav in self.navs:
                sec.insert(nav)
                exestr = "sec.gnabar_%s = self.navs[nav] / 2" %(nav)
                exec(exestr)

    def connect_secs(self):
        self.drgperi.connect(self.axnperi)
        self.drgstem.connect(self.drgperi)
        self.drgsoma.connect(self.drgstem)
        self.drgcntr.connect(self.drgperi)
        self.axncntr.connect(self.drgcntr)

    def initialize_values(self):
        #sets passive current to allow for steady state voltage.
        e_pas = [-65, -65, -62, -62, -62, -62]
        for i, sec in enumerate(self.regions['all']):
            h.finitialize(-65)
            h.fcurrent()
            sec.e_pas = sec.v + (sec.ina + sec.ik) / sec.g_pas
            print(sec.e_pas)
            sec.e_pas = e_pas[i]
            print(sec.e_pas)


