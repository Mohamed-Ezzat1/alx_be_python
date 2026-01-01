def outer_function():
    x = 10  # Variable in the enclosing function

    def inner_function():
        nonlocal x  # Using nonlocal to modify x from the enclosing function
        x += 5  # Modifying the value of x

    inner_function()  # Calling the nested function
    print("Modified value of x from inner function:", x)
outer_function()

dic_example = {1:100, 2:2, 5:3,"m":4}
print("Tuple example:", dic_example[1])
list_example = [1,2,3,4,5]
print("List example:", list_example[2])
del list_example[2]
print("List example:", list_example)
print(dic_example.items())
tuple_example = (1,2,3,4,5)
print("Tuple example:", tuple_example)
print(dic_example.get(4))