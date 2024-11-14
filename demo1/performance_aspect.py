import aspectlib
import time

@aspectlib.Aspect
def measure_time(*args, **kwargs):
    start_time = time.time()
    result = yield  # Tiếp tục thực thi hàm gốc
    end_time = time.time()
    print(f"Function executed in {end_time - start_time:.4f} seconds")
    return result
