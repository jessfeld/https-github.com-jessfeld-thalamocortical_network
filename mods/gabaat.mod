COMMENT
-----------------------------------------------------------------------------

GABAA tonic receptor

-----------------------------------------------------------------------------
ENDCOMMENT

NEURON {
    SUFFIX gabaat
    USEION cl READ ecl WRITE icl VALENCE -1
    RANGE gclbar, icl
}

UNITS {
    (nA) = (nanoamp)
    (mV) = (millivolt)
    (umho) = (micromho)
}

PARAMETER {
    gclbar = 0.004 (umho)
}

ASSIGNED { 
    v (mV)
    icl (mA/cm2)
    ecl (mV)
}

BREAKPOINT {
    icl = gclbar * (v - ecl)
}