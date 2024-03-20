# add your code here

# Creating a FIZZBUZZ in a list

lst = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0
       else str(i) for i in range(1, 101)]

# Join together the strings and get rid of quotes

result = "\n".join(lst)
print(result)