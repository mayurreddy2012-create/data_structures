basket1 = {"apple", "banana", "mango", "apple", "grape"}
basket2 = {"mango", "banana", "kiwi", "kiwi"}
print("basket1", basket1)
print("baske2", basket2)

basket1.add("orange")
print("basket 1 after adding orange: ", basket1)

common_fruits = basket1.intersection(basket2)
print("Fruits in both baskets: ", common_fruits)

import array as arr
fruit_count = arr.array('i', [3,5,2,4])
print("Fruit counts array: ", fruit_count)

fruit_count.insert(0,1)
fruit_count.append(6)
print("Fruit counts after adding items: ", fruit_count)

count_of_4 = fruit_count.count(4)
print("Nuumber of times 4 appears: ", count_of_4)

fruit_count.reverse()
print("Reversed fruit counts array: ", fruit_count)

print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("basket 1", basket1)
print("basket 2", basket2)
print("Shared fruits", common_fruits)
print("Fruit counts", fruit_count)
print("=========================================")
