def isPowerOfThree(n):
    if n == 1:
        return True
    if n<=2:
        return False  
    while n >1:
        if n % 3 != 0:
            return False
        n = n // 3
    return True
        
nums = [i for i in range(2, 82)]
for num in nums:
    print(num, isPowerOfThree(num))

