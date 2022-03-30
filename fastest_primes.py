# fastest algorithm i made so far

from math import sqrt
import time

amount = 100000
prime_list = [2,3]
number = 3
start_time = time.perf_counter()
for primenumber in range(2, amount):
    prime_found = False
    while not prime_found:
        number += 2
        lim = sqrt(number)
        for check in prime_list:
            prime_found = not (number % check == 0)
            if check > lim or not prime_found: break
    prime_list.append(number)
end_time = time.perf_counter() - start_time
print(f'{end_time} seconds')