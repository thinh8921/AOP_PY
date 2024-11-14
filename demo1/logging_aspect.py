import aspectlib

@aspectlib.Aspect
def log_call(*args, **kwargs):
    print(f"Calling function with arguments: {args}, {kwargs}")
    result = yield  # Tiếp tục thực thi hàm gốc
    print(f"Function returned: {result}")
    return result
