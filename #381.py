#Solution for Dail Programmer challenge #381
#https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

import re
import time
import requests

def yahtzee(dice):
    val = {}
    max_val = 0

    for i in dice:
        if i not in val:
            val.update({i:i})
            if i > max_val:
                max_val = i
        else:
            New_val = val[i] + i
            val.update({i:New_val})
            if val[i] > max_val:
                max_val = val[i]
    return(max_val)    

if __name__ == "__main__":
  
    #Fetch large input
    url = 'https://gist.githubusercontent.com/cosmologicon/beadf49c9fe50a5c2a07ab8d68093bd0/raw/fb5af1a744faf79d64e2a3bb10973e642dc6f7b0/yahtzee-upper-1.txt'
    Input_get  = requests.get(url)
    Input_list = re.findall(r'[\d]+',Input_get.text)
    Input_list = list(map(int,Input_list))
    
    print('Test inputs: ')
    print('[2, 3, 5, 5, 6]: ',yahtzee([2, 3, 5, 5, 6]))
    print('[2, 3, 5, 5, 6]: ',yahtzee([1, 1, 1, 1, 3]))
    print('[1, 1, 1, 3, 3]: ',yahtzee([1, 1, 1, 3, 3]))
    print('[1, 2, 3, 4, 5]: ',yahtzee([1, 2, 3, 4, 5]))
    print('[6, 6, 6, 6, 6]: ',yahtzee([6, 6, 6, 6, 6]))
    print('Score for bigger input: ',yahtzee([1654, 1654, 50995, 30864, 1654, 50995, 22747, 1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654, 30864, 4868, 30864]))
    T0 = time.time() 
    print('Score for 100k val input: ',yahtzee(Input_list))
    print('Exec time: ',time.time() - T0)
