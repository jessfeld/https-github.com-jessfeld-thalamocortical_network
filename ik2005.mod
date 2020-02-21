: originally form knoxmodel inak2005.mod

NEURON { 
    SUFFIX ik2005
    USEION k READ ek WRITE ik CHARGE 1
    RANGE gk, gkbar, ninf, ntau
    GLOBAL q10
}

PARAMETER {
    celsius
    ek  (mV)
    gkbar (mho/cm2)
}

ASSIGNED {
    v (mV) 
    q10
    gk (mho/cm2)
    ik (mA/cm2)
    ninf ntau
} 

STATE { n }
 
BREAKPOINT {
    SOLVE states METHOD cnexp
    gk = gkbar*n*n*n*n
    ik = gk*(v-ek)
}

INITIAL {
    rates(v)
    n = ninf
}

DERIVATIVE states {
    rates(v)           
    n' = (ninf - n) / ntau
}
 
PROCEDURE rates(v (mV)) {   :Computes rate and other constants at current v. Call once from HOC to initialize inf at resting v.
    LOCAL  alpha, beta, sum
    : TABLE min, hin, sin,  ninf, mtau, htau, stau, ntau DEPEND celsius FROM -100 TO 100 WITH 200
    q10 = 3^((celsius - 6.3)/10)
    :"n" KDR activation system				
    alpha = -0.07*vtrap((v+65-47),-6)
    beta = 0.264/exp((v+65-22)/40)
    sum = alpha+beta        
    ntau = 1/sum/q10
    ninf = alpha/sum
}
 
FUNCTION vtrap(x,y) {  :Traps for 0 in denominator of rate eqns.
    if (fabs(x/y) < 1e-6) {
        vtrap = y*(1 - x/y/2)
    } else {  
        vtrap = x/(exp(x/y) - 1)
    }
}
