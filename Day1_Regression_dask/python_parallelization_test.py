import numpy as np
import time
import math
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor

# Verify how many CPU cores we have available
cores = cpu_count()
print(f"Your machine has {cores} CPU cores available for parallelization.")

# Generate a dataset of 5,000,000 numbers split into 50 large chunks
# Processing chunks allows us to distribute chunks to different cores
num_chunks = 50
chunk_size = 100_000
data_chunks = [np.random.uniform(1, 100, chunk_size) for _ in range(num_chunks)]


def heavy_array_operation(array):
    """
    Simulates a heavy, CPU-bound operation on an array of data.
    """
    output = []
    for x in array:
        # A series of math operations to force the CPU to work hard
        val = np.sin(x) * np.cos(x)
        val = np.exp(np.log(np.abs(val) + 1))
        output.append(val)
    return np.array(output)


print(
    f"Generated {num_chunks} chunks. Total elements to process: {num_chunks * chunk_size:,}"
)

print("Starting sequential processing...")
start_time = time.time()

sequential_results = []
for chunk in data_chunks:
    result = heavy_array_operation(chunk)
    sequential_results.append(result)

sequential_time = time.time() - start_time
print(f"Sequential processing finished in: {sequential_time:.2f} seconds")


print(f"Starting parallel processing using {cores} cores...")
start_time = time.time()

# ProcessPoolExecutor handles the creation and management of child processes
with ProcessPoolExecutor(max_workers=cores) as executor:
    # executor.map automatically applies the function to each chunk in parallel
    parallel_results = list(executor.map(heavy_array_operation, data_chunks))

parallel_time = time.time() - start_time
print(f"Parallel processing finished in: {parallel_time:.2f} seconds")
