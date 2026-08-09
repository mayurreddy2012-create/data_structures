box1 = ["Chips", "Chocolate", "Juice"]
box2 = ["Chocolate", "Cookies", "Juice"]
print("Box 1:", box1)
print("Box 2:", box2)
box1.append("Popcorn")
print("\nAfter adding Popcorn:")
print("Box 1:", box1)
used_snack = box1.pop()
print("\nSnack used:", used_snack)
print("Box 1:", box1)
shared_snacks = set(box1) & set(box2)
print("\nShared snacks:", shared_snacks)
snack_counts = [5, 8, 3, 6]
print("\nSnack counts:", snack_counts)
snack_counts.append(10)
print("After adding 10:", snack_counts)
snack_counts.reverse()
print("\nReversed snack counts:", snack_counts)