#Solution for /r Programmer Challenge #378
#https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

def HaHa_algorithm(Ans):
    if 0 in Ans:
        Ans = [x for x in Ans if x!=0]
    if len(Ans) > 0:
        Ans.sort(reverse=True)
        N=Ans[0]
        Ans.pop(0)
        if (N > 0) and (len(Ans) >= N):
            for i in range(0,N):
                Ans[i]=Ans[i]-1
            HaHa_algorithm(Ans)
        else:
            print(False)
    else:
        print(True)
  
if __name__ == '__main__':
   
    HaHa_algorithm([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])
    HaHa_algorithm([4, 2, 0, 1, 5, 0])
    HaHa_algorithm([3, 1, 2, 3, 1, 0])
    HaHa_algorithm([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16])
    HaHa_algorithm([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12])
    HaHa_algorithm([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3])
    HaHa_algorithm([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1])
    HaHa_algorithm([2, 2, 0])
    HaHa_algorithm([3, 2, 1])
    HaHa_algorithm([1,1])
    HaHa_algorithm([1])
    HaHa_algorithm([])
