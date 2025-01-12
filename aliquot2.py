import decimal
import sys
import math
import time

def aliquot(number: int) -> None:
    aliquot_sequence = []
    upper_bound = decimal.Decimal(10 ** 18)

    while True:
        if number == 0:
            print(number)
            break
        else:
            print(number, end=", ", flush=True)
        
        aliquot_sequence.append(number)
        factor_sum = 1
        n = number + 0
        
        if aliquot_sequence.count(number) > 1 or number > upper_bound:
            print("...")
            break

        
        prime_factorization = {}
        limit = math.sqrt(n)
        x = 2

        while n > 1:
            if x > limit:
                if n not in prime_factorization.keys():
                    prime_factorization[n] = 1
                
                break

            else:
                while n % x == 0:
                    n = decimal.Decimal(n / x)
                    limit = math.sqrt(n)
                    
                    if x in prime_factorization.keys():
                        prime_factorization[x] += 1
                    else:
                        prime_factorization[x] = 1
            
                x += 1
        
        for prime in prime_factorization.keys():
            sigma = 0

            for i in range(prime_factorization[prime] + 1):
                sigma += prime ** i
            
            factor_sum *= sigma
        
        factor_sum -= number
        number = factor_sum


def main():
    try:
        n = decimal.Decimal(sys.argv[1])
        aliquot(n)
        print(f"Time: " + str(time.process_time()) + " seconds")
    
    except ValueError:
        print("Invalid argument.")
    except IndexError:
        n = 1

        while True:
            aliquot(n)
            print()
            n += 1


main()