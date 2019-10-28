TITLE nafjr.mod   squid sodium channel with erev shifted to reflect passage of K as well as Na (Josh Rosenthal mRNA edited)
 
COMMENT

ENDCOMMENT
 
UNITS {
        (mA) = (milliamp)
        (mV) = (millivolt)
	(S) = (siemens)
}
 
NEURON {
        SUFFIX nafjr
        USEION na READ ena WRITE ina
        RANGE gnabar, gna, erev
        GLOBAL minf, hinf, mtau, htau
	THREADSAFE : assigned GLOBALs will be per thread
}
 
PARAMETER {
        gnabar = .12 (S/cm2)	<0,1e9>
        erev = -20.0 (mV)
}
 
STATE {
        m h
}
 
ASSIGNED {
        ena (mV)
        ina (mA/cm2)
	gna (S/cm2)
        minf hinf
	mtau (ms) htau (ms)
}
 
BREAKPOINT {
        SOLVE states METHOD cnexp
        gna = gnabar*m*m*m*h
	ina = gna*(v - erev)
}
 
 
INITIAL {
	rates(v)
	m = minf
	h = hinf
}

? states
DERIVATIVE states {  
        rates(v)
        m' =  (minf-m)/mtau
        h' = (hinf-h)/htau
}
 
:LOCAL q10

PROCEDURE rates(v(mV)) {  :Computes rate and other constants at current v.
                      :Call once from HOC to initialize inf at resting v.
        LOCAL  alpha, beta, sum, q10
        TABLE minf, mtau, hinf, htau DEPEND celsius FROM -100 TO 100 WITH 200

UNITSOFF
        q10 = 3^((celsius - 6.3)/10)
                :"m" sodium activation system
        alpha = .1 * vtrap(-(v+40),10)
        beta =  4 * exp(-(v+65)/18)
        sum = alpha + beta
	mtau = 1/(q10*sum)
        minf = alpha/sum
                :"h" sodium inactivation system
        alpha = .07 * exp(-(v+65)/20)
        beta = 1 / (exp(-(v+35)/10) + 1)
        sum = alpha + beta
	htau = 1/(q10*sum)
        hinf = alpha/sum
}
 
FUNCTION vtrap(x,y) {  :Traps for 0 in denominator of rate eqns.
        if (fabs(x/y) < 1e-6) {
                vtrap = y*(1 - x/y/2)
        }else{
                vtrap = x/(exp(x/y) - 1)
        }
}
 
UNITSON
