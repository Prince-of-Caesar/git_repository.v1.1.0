def score_mean(lst):
    lst.sort()
    lst2=lst[1:(len(lst)-1)]
    return round((sum(lst2)/len(lst2)),1)

lst=[9.1,9.0,8.1,9.7,19,8.2,8.6,9.8]
print(score_mean(lst))