: originally form knoxmodel inak2005.mod -- ina2005 split from ik2005
:   Alan Goldin Lab, University of California, Irvine; Jay Lickfett - Last Modified: 6 July 2005
:  This file is the Nav1.1 wild-type channel model described in:
:		Barela et al. An Epilepsy Mutation in the Sodium Channel SCN1A That Decreases Channel Excitability.  J. Neurosci. 26(10): p. 2714-2723 
: Spampanato et al. 2004 Increased Neuronal Firing in Computer Simulations of Sodium Channel Mutations that Cause Generalized Epilepsy with Febrile Seizures Plus. J Neurophys 91:2040-2050
: Spampanato et al. 2004 A Novel Epilepsy Mutation in the Sodium Channel SCN1A Identifies a Cytoplasmic Domain for Beta Subunit Interaction. J. Neurosci. 24:10022-10034

NEURON { 
    SUFFIX ina2005
    USEION na READ ena WRITE ina CHARGE 1
    RANGE gna
    RANGE gnabar, gnablock
    RANGE minf, mtau, hshift, sshift, mvhalf, mk, hvhalf, hk, svhalf, sk, mtaubase, htauk, htauvhalf, htauk, stauvhalf, stauk, hinf, htau, sinf, stau, inat
    RANGE m, h, s, htaubase, staubase
    GLOBAL q10, perc, emut
}

PARAMETER {
    celsius
    gnabar (mho/cm2)   
    ena
    gnablock = 1.0
    mvhalf = 27.4 (mV)
    mk = 5.4043
    hvhalf = 41.9 (mV)
    hk = 6.7
    svhalf = 46.0 (mV)
    sk = 6.6
    hshift = 0 (mV)
    sshift = 0 (mV)
    mtaubase = 0.15
    htaubase = 23.12
    htauvhalf = 77.58 (mV)
    htauk = 43.92
    staubase = 140400
    stauvhalf = 71.3 (mV)
    stauk = 30.9
    perc = 0
    emut = -40
}

ASSIGNED {
    v (mV) 
    q10
    gna (mho/cm2) 
    ina (mA/cm2)
    minf hinf sinf
    mtau htau stau
} 

STATE { m h s }
 
BREAKPOINT {
    SOLVE states METHOD cnexp
    gna = gnabar*gnablock*m*m*m*h*s  
    ina = gna*( ( 1 - perc) * (v - ena) + (perc) * (v - emut) )
}

INITIAL {
    rates(v)
    m = minf
    h = hinf
    s = sinf
}

DERIVATIVE states {
    rates(v)           
    m' = (minf - m) / mtau
    h' = (hinf - h) / htau
    s' = (sinf - s) / stau
}
 
PROCEDURE rates(v (mV)) {   :Computes rate and other constants at current v. Call once from HOC to initialize inf at resting v.
    LOCAL  alpha, beta, sum, vhs, vss
    : TABLE minf, hinf, sinf,  nfinf, mtau, htau, stau, nftau DEPEND celsius FROM -100 TO 100 WITH 200
    q10 = 3^((celsius - 6.3)/10)
    vhs = v - hshift
    vss = v - sshift
    :"m" sodium activation system
    minf = 1/(1+exp(-(v+mvhalf)/mk))		
    mtau = mtaubase/q10

    :"h" sodium fast inactivation system
    hinf = 1/(1+exp((vhs+hvhalf)/hk))				
    htau = htaubase*exp(-0.5*((v+htauvhalf)/htauk)^2)/q10
       
    :"s" sodium slow inactivation system
    sinf = 1/(1+exp((vss+svhalf)/sk))						
    stau = staubase*exp(-0.5*((v+stauvhalf)/stauk)^2)/q10
}
 
FUNCTION vtrap(x,y) {  :Traps for 0 in denominator of rate eqns.
    if (fabs(x/y) < 1e-6) {
        vtrap = y*(1 - x/y/2)
    }else{  
        vtrap = x/(exp(x/y) - 1)
    }
}
