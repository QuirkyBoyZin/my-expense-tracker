import time


def measure_perf(base_fn):
    """A decorator for measuring code execution time of a function"""
    def wrapper(*args):
        
        start_time   = time.perf_counter()
        result = base_fn(*args)
        end_time     = time.perf_counter()
        elasped_time = end_time - start_time
        
        print(f"Execution time for {base_fn.__name__}: {elasped_time:.3f} Seconds")
        return result
       
    return wrapper

