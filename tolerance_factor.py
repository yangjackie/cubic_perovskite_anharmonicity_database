import math
from element import *
from chemical_space import *

def tolerance_factor(a, b, c):
    if c in halide_C:
        a_charge = '1'
        b_charge = '2'
        c_charge = '-1'
    elif c in chalco_C:
        a_charge = '2'
        b_charge = '4'
        c_charge = '-2'
    coord = 'VI'  # all ions are six fold coordinated

    try:
        ra = shannon_radii[a][a_charge][coord]['r_ionic']
    except KeyError as e:
        print(a, e)
    try:
        rb = shannon_radii[b][b_charge][coord]['r_ionic']
    except KeyError as e:
        print(b, e)
    try:
        rc = shannon_radii[c][c_charge][coord]['r_ionic']
    except KeyError as e:
        print(c, e)

    tolerance_f = ra + rc
    tolerance_f /= rb + rc
    tolerance_f /= math.sqrt(2)

    return tolerance_f

