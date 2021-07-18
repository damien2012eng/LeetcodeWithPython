def countPrime(num):
        if num < 2:
            return 0
        orig_list = [True] * (num+1)
        
        for i in range(num):
            if i < 2:
                orig_list[i] = False
            if i > 1 and orig_list[i]:
                j = 2
                while i * j <= num:
                    orig_list[i*j] = False
                    j += 1
    
        if orig_list[num]:
            return sum(orig_list)-1
        else:
            return sum(orig_list)
    
    

print(countPrime(0))