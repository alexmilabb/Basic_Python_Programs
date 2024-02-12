lucky_numbers = [8, 4, 15, 42, 23, 16]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# friends.extend(lucky_numbers) # -->  literally extends and adds the second list to the first one

# friends.append("Creed") # -->  appends another item to the end of the list

# friends.insert(1, "Kelly") # -->  inserts another element in the list

# friends.remove("Jim") # -->  removes an element

# friends.clear() # -->  clears everything from the list and gives back an empy list

# friends.pop() # -->  removes the last element from the list

# friends.sort()  # -->  sorts the names in alphabetical order

# lucky_numbers.sort()  # --> sorts the numbers in ascending order

# lucky_numbers.reverse()  #  --> reverses the entire list and starts from the last element

# print(friends.index("Oscar"))  # --> gives out the index of the name from the list

# print(friends.count("Jim"))  # --> gives back the number of the times this string is counted in the list

friends2 = friends.copy()  # --> makes a copy of the entire list

print(friends2)

print(lucky_numbers)
