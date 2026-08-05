habits = ("Exercise", "Read Book", "Drink Water", "Meditation")
week_record = (True, True, False, True, False, True, True)
print("Habits:", habits)
print("Weekly Record:", week_record)
print("\nNumber of habits:", len(habits))
print("Number of days recorded:", len(week_record))
print("\nFirst habit:", habits[0])
print("Second habit:", habits[1])
print("Last day status:", week_record[-1])
print("\nFirst two habits:", habits[:2])
print("Last two habits:", habits[-2:])
print("First three day records:", week_record[:3])
print("\nTrying to modify a tuple...")
try:
    habits[0] = "Yoga"
except TypeError as e:
    print("Error:", e)

print("\nTuples are immutable, so their values cannot be changed after creation.")