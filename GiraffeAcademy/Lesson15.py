month_Conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# print(month_Conversions["Nov"]) # --> one way to get the entire value from the Dictionary

print(month_Conversions.get("What", "Not a valid Key"))  # --> will print out the second statement if there is no key
# for a value

