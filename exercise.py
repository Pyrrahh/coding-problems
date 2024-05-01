import time
import random
import numpy as np

def fill_list_with_random():
    return [random.uniform(10, 30) for _ in range(100000)]

def fill_list_with_random_comp():
    return [random.uniform(10, 30) for _ in range(100000)]

def fill_numpy_array_with_random():
    return np.random.uniform(10, 30, 100000)

def measure_time_and_compute_mean(func):
    start_time = time.time()
    result = func()
    elapsed_time = time.time() - start_time
    # Compute mean
    if isinstance(result, list):
        mean_value = sum(result) / len(result)
        print(f"Mean of the list: {mean_value:.4f}")
    elif isinstance(result, np.ndarray):
        mean_value = np.mean(result)
        print(f"Mean of the numpy array: {mean_value:.4f}")
    print(f"Time to execute {func.__name__}: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    measure_time_and_compute_mean(fill_list_with_random)
    measure_time_and_compute_mean(fill_list_with_random_comp)
    measure_time_and_compute_mean(fill_numpy_array_with_random)