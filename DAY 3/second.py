# #tuples
# from itertools import count

# tup=('1','2','3','4')
# t = len(tup)
# for i in range(t):
#            print(i,tup[i])
#            print(i,tup)
#            print(i,len(tup))

#converting list into tuples
l =[1,2,3,4,5,6]
tup = tuple(l)
print(tup)
print(type(tup))

#methods of tuples
print(f"{min(tup)}")
print(f"{max(tup)}")
print(f"{tup.count(3)}")
print(f"{tup.index(3)}")
print(f"{sum(tup)}")
