my_numbers = [1, 2, 3, 5]
my_numbers[3] = 4
print(my_numbers)

#লিস্টের মধ্যের এলিমেন্ট চেক

print("starts elements checking with in operator")

fruits = ["apple", "orange", "pineappe", "grape"]

print("orange" in fruits)
print("rice" in fruits)
print("apple" in fruits)

#একই ভাবে এর সাথে not অপারেটর ব্যবহার করে কোন এলিমেন্টের অনুপস্থিতিও চেক করা যাতে পারে।

print("starts checking not present with not operator")

fruits = ["apple", "orange", "pineappe", "grape"]

print("orange" not in fruits)
print("rice" not  in fruits)
print("apple" in fruits)
