sum = 0
dict = {"mary":80, "jack":90,"peter":91,"bryan":79,"chris":98}
students=dict.keys()
for i in students:
    print(i)
for i in dict.values():
  
    sum+=i
    
avg = sum/5
print("The class's average is",avg)
minimum = dict.values()
print("minimum value",min(minimum))
maximum= dict.values()
print("maximum value",max(maximum))

user = input("whose score do you want?")
print(dict.get(user))