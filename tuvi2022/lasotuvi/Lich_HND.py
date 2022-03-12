import math
from re import A
def jdFromDate(dd,mm,yy):
    a = int((14-mm)/12)
    y = yy +4800 -a
    m = mm +12*a -3
    jd = dd + int((153*m +2)/5) + 365 * y + int(y/4) - int(y/100) + int(y/400) - 32045
    if(jd<2299161):
        jd = dd + int((153*m +2)/5) + 365*y+int(y/4)-32083
    return jd