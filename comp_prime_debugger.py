
def compact_primes(amount):
    prime_list = ['2']+[str(number) for number in range(3, int(amount)+1, 2) if not any([(number % factor == 0) for factor in range(3,round(number**0.5+1), 2)])]
    return prime_list

for i in range(200000):
    prime_list = compact_primes(i)
    prime_string = str(prime_list)
    if prime_string[-1] != "]":
        print(f"Error for amount: {i}")
        count = 0
        for _ in prime_string:
            count += 1
        print(f"Stopping at {count} characters\n")