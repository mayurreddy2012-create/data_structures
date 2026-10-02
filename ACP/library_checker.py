books = ["harry potter","secret seven","wings of fire"]
genres = ["fantasy","children's mystery","fantasy"]
rel = {book:genre for book,genre in zip(books,genres)}
print("Fantasy",rel)
final = list(map(lambda book: book="Fantasy",books))
print(final)
