# sorted() - Returns a new list with sorted elements from an iterable

lst = [43,557,2,-123,218,32]

print(list(sorted(lst)))
print(list(sorted(lst,reverse=True)))

string = "cbwuirdojwecb"
print(list(sorted(string)))

pairs = [[1,2],[3,3],[2,5],[4,1]]
print(list(sorted(pairs,key=sum)))