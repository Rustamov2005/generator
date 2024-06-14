#generator 1
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
for value in gen:
    print(value)

#dekaratotr 2
def my_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        result = func()
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

# Dekoratsiyalangan funktsiyani chaqirish
say_hello()


#generator 2
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Fibonachchi generatorni chaqirib, birinchi 10 ta qiymatni chiqarish
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

#
