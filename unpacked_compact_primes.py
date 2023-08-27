import time
# * print([2]+[number for number in range(3, int(input('amount:')), 2) if not any([(number % factor == 0) for factor in range(3,round(number**0.5), 2)])])

# writing the code out
prime_list = [2]
amount = int(input('amount:'))+1
start = time.perf_counter()
for number in range(3, amount, 2):
    for factor in range(3, round(number**0.5)+1, 2):
        if number % factor == 0:
            break
    else:
        prime_list.append(number)
    
end = time.perf_counter() - start

print(prime_list)
print(len(prime_list))
print(f'{end}seconds')
