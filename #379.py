#This is solution for Reddit daily programmer challenge #379
#https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/

import math

def TRate(Income_cap,Tax_rate,Income,Income_tax):
    if len(Income_cap) > 0:
        if Income > Income_cap[-1]:
            Income_tax += (Income - Income_cap[-1])*Tax_rate[-1]
            Income = Income_cap[-1]
            Income_cap.pop()
            Tax_rate.pop()
            return(TRate(Income_cap,Tax_rate,Income,math.floor(Income_tax)))
        else:
            Income_cap.pop()
            Tax_rate.pop()
            return(TRate(Income_cap,Tax_rate,Income,math.floor(Income_tax)))
    else:
        print(Income_tax)


if __name__ == "__main__":
  
    #TRate([10000,30000,100000],[0.10,0.25,0.4],0,0)
    #TRate([10000,30000,100000],[0.10,0.25,0.4],10000,0)
    #TRate([10000,30000,100000],[0.10,0.25,0.4],10009,0)
    #TRate([10000,30000,100000],[0.10,0.25,0.4],10010,0)
    #TRate([10000,30000,100000],[0.10,0.25,0.4],12000,0)
    #TRate([10000,30000,100000],[0.10,0.25,0.4],56789,0)
    TRate([10000,30000,100000],[0.10,0.25,0.4],1234567,0)
