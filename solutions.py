# Exercise 1: F-Strings with User Input
def exercise1():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    word3 = input("Enter third word: ")
    print(f"{word1}, {word2}, and {word3} are three words you entered.")

# Exercise 2: List Operations
def exercise2():
    my_list = ["apple", "banana"]
    print(my_list[1].upper())
    print(my_list[0][::-1])

# Exercise 3: Printing Every Other Name
def exercise3():
    names = ["Alice", "Bob", "Carol", "Dave"]
    print(names[::2])

# Exercise 4: Inserting Number in List
def exercise4():
    numbers = [1, 2, 3, 4]
    new_number = int(input("Enter a number: "))
    numbers.insert(-1, new_number)
    print(numbers)

# Exercise 5: Dictionary Creation
def exercise5():
    personal_info = {
        "name": "John",
        "age": 30,
        "gender": "Male",
        "favorite_food": "Pizza"
    }
    print(personal_info)

# Exercise 6: Blood Alcohol Level Check
def exercise6():
    level = float(input("Enter your blood alcohol level: "))
    if level >= 0.5:
        print("You're not sober. Take a cab.")
    else:
        print("You can drive home.")

# Exercise 7: Retirement Check
def exercise7():
    gender = input("Enter your gender (male/female): ").lower()
    age = int(input("Enter your age: "))
    if (gender == "male" and age > 65) or (gender == "female" and age > 60):
        print("You may retire.")
    else:
        print("It's not time to retire yet.")

# Exercise 8: Loop from 10 to 20
def exercise8():
    for i in range(10, 21):
        print(i)

# Exercise 9: Print Odd Numbers
def exercise9():
    for i in range(1, 21, 2):
        print(i)

# Exercise 10: Print Names Using Loop
def exercise10():
    names = ["Emily", "John", "Anna", "Mike", "Sarah"]
    for name in names:
        print(name)

# Exercise 11: Sum of Numbers Until 0
def exercise11():
    sum = 0
    while True:
        number = int(input("Enter a number (0 to stop): "))
        if number == 0:
            break
        sum += number
    print("Sum:", sum)

# Exercise 12: Find Longest Word
def exercise12():
    longest_word = ""
    while True:
        word = input("Enter a word ('done' to stop): ")
        if word == 'done':
            break
        if len(word) > len(longest_word):
            longest_word = word
    print("Longest word:", longest_word)

# Exercise 13: Function to Print String Length
def string_length(s):
    print("Length:", len(s))

# Exercise 14: Average of Three Numbers
def average_of_three(a, b, c):
    print("Average:", (a + b + c) / 3)

# Exercise 15: String Length Comparison
def is_string_longer(s, n):
    return len(s) > n

# Exercise 16: Copy String
def copy_string(s, times=1):
    return s * times

# Main function to run the exercises
def main():
    exercise1()
    exercise2()
    # ... You can call other exercises here as needed

if __name__ == "__main__":
    main()
