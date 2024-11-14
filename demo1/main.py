from logging_aspect import log_call 
from performance_aspect import measure_time

# Áp dụng cả hai aspect: log_call và measure_time
@log_call
@measure_time
def say_hello(name):
    print(f"Hello, {name}!")

@log_call
@measure_time
def add(a, b):
    return a + b

# Test
say_hello("Alice")
result = add(5, 10)
print(f"Result of add: {result}")
