# vapor pressure $e$ Pa from mixing ratio, $r$ (Kg/Kg) and pressure, $P$ (Pa).
def e(r, p): return p*r/(epsilon + r)

#   Saturation vapor pressure over water (Pa) (Emanuel) from temperature T (K)
def e_star(T):
    return 100.*numpy.exp(53.67957 - 6743.769/T - 4.8451*numpy.log(T))

#   saturation mixing ratio rs (Kg/Kg) from temperature t (K) and pressure P (Pa)
def r_star(p, T):
    return epsilon*e_star(T)/(p - e_star(T))
