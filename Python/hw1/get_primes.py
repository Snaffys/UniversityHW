def get_primes(n):
    try:
        number_check = int(n)
        if(number_check < 2):
            print("There are no primes")
            return []
        elif(number_check == 2):
            return [2]
    except(ValueError, TypeError):
        print("There are no primes")
        return []
    
    odd_size = (n - 1) // 2
    sieve = bytearray([1]) * odd_size
    primes = [2]
    
    for i in range(odd_size):
        if sieve[i]:
            current_num = 2 * i + 3
            primes.append(current_num)

            start_index = (current_num * current_num - 3) // 2
            step = current_num

            for j in range(start_index, odd_size, step):
                sieve[j] = 0    

    return primes