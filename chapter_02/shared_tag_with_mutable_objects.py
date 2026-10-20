list_a = [1, 2, 3]
list_b = list_a  # You copied the label list_a to list_b. Both point to the SAME list!

list_b.append(4)  # You modify list_b

print("list_b:", list_b)
print("list_a:", list_a)  # Output is! list_a was changed too!
