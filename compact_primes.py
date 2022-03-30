
#! not yet working
prime_list = [number for number in range(2, int(input('amount:'))) if not any([(number % factor == 0)for factor in (prime_list if 'prime_list' in locals() else [2])])]
print(prime_list)
