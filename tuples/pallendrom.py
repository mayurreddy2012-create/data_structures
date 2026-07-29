def is_palindrome(tup):
    start = 0
    end = len(tup) - 1
    while start<end:
        if tup[start]!= tup[end]:
            return False
        start+=1
        end-=1
    return True
my_tuple = (1,2,3,3,2,1)
if is_palindrome(my_tuple):
    print("the tuple is a palindrome")
else:
    print("the tuple is not a palindrome")        