import math

def wittekind_model(f, V, Vc, Cb, Dt, m, n, E):
    Dt_ref = 10000
    Coeff = [125,0.35,-8*(10**-3),6*(10**-5),-2*(10**-7),2.2*(10**-10)]
    
    A = 80 * (math.log10(4*Cb*V/Vc))
    B = (20/3) * (math.log10(Dt/Dt_ref))
    C = 60 * (math.log10(1000*Cb*V/Vc))
    D = 15 * (math.log10(m)) + 10 * (math.log10(n))

    # SL1 represents the Low-Frequency Cavitation Noise
    SL1 = A + B
    for i in range(6):
        SL1 += Coeff[i] * (f**i)
    # SL2 represents the High-Frequency Cavitation Noise
    SL2 = -(5 * math.log2(f)) - (1000/f) + 10 + B + C
    # SL3 represents the Diesel Engine Noise
    SL3 = (10**-7) * (f**2) - 0.01*f + 140 + D + E

    if f >= 400:
        SL = 10* math.log10( 10**(SL2/10) + 10**(SL3/10))
    elif f<400 and SL1<=3082:
        SL = 10 * math.log10(10**(SL1/10) + 10**(SL2/10) + 10**(SL3/10))
    else:
        SL1 = 3082 
        SL = 10 * math.log10(10**(SL1/10) + 10**(SL2/10) + 10**(SL3/10))


    return SL

print(wittekind_model(600, 6.2, 9, 0.847956, 85898.06339, 800, 1, 0))
