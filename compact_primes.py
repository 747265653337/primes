import time
# * slowest algorithm ever written
start = time.perf_counter()
[2]+[number for number in range(3, 1299710, 2) if not any([(number % factor == 0) for factor in range(3,round(number**0.5), 2)])]
print(f'{time.perf_counter() - start} seconds')
