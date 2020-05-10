COMMENT
-----------------------------------------------------------------------------

GABAA tonic receptor

-----------------------------------------------------------------------------
ENDCOMMENT

NEURON {
<<<<<<< HEAD
    SUFFIX gabaatp
=======
    SUFFIX gabaat
>>>>>>> 6f98693... cl- tonic synapse implemented as a mechanism
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