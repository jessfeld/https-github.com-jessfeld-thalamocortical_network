: originally form knoxmodel inak2005.mod

NEURON { 
    SUFFIX ik2005
    USEION kf READ ekf WRITE ikf CHARGE 1
    RANGE gkf, gkfbar, nfinf, nftau
    GLOBAL q10
}

PARAMETER {
    celsius
    ekf  (mV)
    gkfbar (mho/cm2)
}

ASSIGNED {
    v (mV) 
    q10
    gkf (mho/cm2)
    ikf (mA/cm2)
    nfinf nftau
} 

STATE { nf }
 
BREAKPOINT {
    SOLVE states METHOD cnexp
    gkf = gkfbar*nf*nf*nf*nf
    ikf = gkf*(v-ekf)
}

INITIAL {
    rates(v)
    nf = nfinf
}

DERIVATIVE states {
    rates(v)           
    nf' = (nfinf - nf) / nftau
}
 
PROCEDURE rates(v (mV)) {   :Computes rate and other constants at current v. Call once from HOC to initialize inf at resting v.
    LOCAL  alpha, beta, sum
    : TABLE minf, hinf, sinf,  nfinf, mtau, htau, stau, nftau DEPEND celsius FROM -100 TO 100 WITH 200
    q10 = 3^((celsius - 6.3)/10)
    :"nf" fKDR activation system				
    alpha = -0.07*vtrap((v+65-47),-6)
    beta = 0.264/exp((v+65-22)/40)
    sum = alpha+beta        
    nftau = 1/sum/q10
    nfinf = alpha/sum
}
 
FUNCTION vtrap(x,y) {  :Traps for 0 in denominator of rate eqns.
    if (fabs(x/y) < 1e-6) {
        vtrap = y*(1 - x/y/2)
    } else {  
        vtrap = x/(exp(x/y) - 1)
    }
}
