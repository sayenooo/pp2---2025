# main.py

from func import unique_elements, guess_the_number


print("Testing unique_elements function:")
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(my_list)
print("Unique elements:", unique_list)


print("\nStarting the 'Guess the Number' game:")
guess_the_number()
