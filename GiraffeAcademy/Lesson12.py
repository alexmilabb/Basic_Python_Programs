is_male = True
is_tall = True

#  or --> only needs one of the conditions to be met

# and --> needs both conditions to be met

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male, but you are tall")
else:
    print("You are not a male and not tall")
