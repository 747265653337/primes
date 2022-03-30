# fastest algorithm i made so far

from math import sqrt
import time

maxNum = 1299709
prime_list = [2,3]
number = 3
start_time = time.perf_counter()
for number in range(3, maxNum+1, 2):
    lim = sqrt(number)
    for check in prime_list:
        if number % check == 0:
            break
        elif check > lim:
            prime_list.append(number)
            break
end_time = time.perf_counter() - start_time
print(prime_list[-3:])
print(f'{end_time} seconds')
# fastest 5.394183999999996 seconds