def sternBrocot(num, den):
    lnum, lden = 0, 1
    rnum, rden = 1, 0
    cnum, cden = lnum + rnum, lden + rden
    while cnum != num and cden != den:
        if cnum/cden > num/den:
            print('L', end ='')
            rnum, rden = cnum, cden
            cnum, cden = lnum + rnum, lden + rden
        else:
            print('R', end ='')
            lnum, lden = cnum, cden
            cnum, cden = lnum + rnum, lden + rden
sternBrocot(5, 7)
