#1

data = "Python rules!"

# a. Obtain a list of words in the string.
words_list = data.split()
print("List of words:", words_list)

# b. Convert the string to upper case.
upper_case_data = data.upper()
print("Upper case string:", upper_case_data)

# c. Locate the position of the string "rules!".
position_rules = data.find("rules!")
print("Position of 'rules!':", position_rules)

# d. Replace the "!" with a "?".
replaced_data = data.replace("!", "?")
print("Replaced string:", replaced_data)

data = "Python rules!"

#1

# a. data.endswith(i)
end_with_i = data.endswith('i')
print("Does data end with 'i'?", end_with_i)

# b. "totally".join(data.split())
joined_data = "totally".join(data.split())
print("Joined data:", joined_data)
