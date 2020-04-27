from genrn import genrn

class PY(genrn):
    def __init__(self):
        self.cellRule = {
            'secs' : {'soma': {'L': 96.0, 'nseg': 1, 'diam': 96.0, 'Ra': 100.0, 'cm': 1.0}},
            'ions' : {'k': -77.0, 'kf': -100.0, 'nat': 50.0},
            'mechs': {'im': {'gkbar': 3e-05, 'taumax': 1000.0},
                      'inak2005': {'gkfbar': 0.03, 'gnatbar': 0.3},
                      'pas': {'g': 0.0001, 'e': -70.0}},
            }
        super(PY, self).__init__(**self.cellRule)

class TC(genrn):
    def __init__(self):
        self.cellRule = {
            'secs' : {'soma': {'L': 96.0, 'nseg': 1, 'diam': 96.0, 'Ra': 100.0, 'cm': 1.0}},
            'ions' : {'ca': 120.0, 'h': -40.0, 'k': -100.0, 'kf': -100.0, 'nat': 50.0},
            'mechs': {'cad': {'cainf': 0.00024, 'depth': 1.0, 'kt': 0.0, 'taur': 5.0},
                      'iar': {'Pc'  : 0.01, 'cac' : 0.002 , 'ghbar': 2e-05,
                              'ginc': 2.0 , 'k2'  : 0.0004, 'k4': 0.001,
                              'nca' : 4.0 , 'nexp': 1.0},
                      'inak2005': {'gkfbar': 0.06, 'gnatbar': 0.15},
                      'it': {'gcabar': 0.002, 'shift': 2.0},
                      'pas': {'g': 1e-05, 'e': -70.0},
                      'kleak': {'gkbar': 0.004}},
            }
        super(TC, self).__init__(**self.cellRule)

class RE(genrn):
    def __init__(self):
        self.cellRule = {
            'secs' : {'soma': {'L': 64.86, 'nseg': 1, 'diam': 70.0, 'Ra': 100.0, 'cm': 1.0}},
            'ions' : {'ca': 120.0, 'kf': -100.0, 'nat': 50.0},
            'mechs': {'cad': {'cainf': 0.00024, 'depth': 1.0, 'kt': 0.0, 'taur': 5.0},
                      'inak2005': {'gkfbar': 0.06, 'gnatbar': 0.19},
                      'it2': {'gcabar': 0.003, 'qh': 2.5, 'qm': 2.5, 'shift': 2.0, 'taubase': 85.0},
                      # 'itrecustom': {'gcabar': 0.0, 'qh': 2.5, 'qm': 2.5, 'shift': 2.0, 'taubase': 85.0},
                      'pas': {'g': 5e-05, 'e': -90.0}},
            }
        super(RE, self).__init__(**self.cellRule)

class IN(genrn):
    def __init__(self):
        self.cellRule = {
            'secs' : {'soma': {'L': 67.0, 'nseg': 1, 'diam': 67.0, 'Ra': 100.0, 'cm': 1.0}},
            'ions' : {'kf': -100.0, 'nat': 50.0},
            'mechs': {'inak2005': {'gkfbar': 0.03, 'gnatbar': 0.152},
                      'inak2005mut': {'gkfbar': 0.03, 'gnatbar': 0.152},
                      'pas': {'g': 0.00015, 'e': -70.0}},
            }
        super(IN, self).__init__(**self.cellRule)
