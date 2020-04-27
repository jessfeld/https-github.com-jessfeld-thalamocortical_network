COMMENT
-----------------------------------------------------------------------------

Potassium passive leak current

-----------------------------------------------------------------------------
ENDCOMMENT

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	SUFFIX kleak
	USEION k READ ek WRITE ik
	RANGE gkbar, ik
}

UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)
	(umho) = (micromho)
}

PARAMETER {
	gkbar	= 0.004	(umho)		: maximum conductance (microSiemens)
}

ASSIGNED {
	v		(mV)		: postsynaptic voltage
	ik 		(nA)		: passive current
	ek      (mV)        : reversal voltage
}

BREAKPOINT {
	ik = gkbar * (v - ek)
}
