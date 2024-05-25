def factorial(nums):
    result = []
    for n in nums:
        value = 1
        if n == 0:
            result.append(value)
        if (n>0 and n<16):
            for i in range (1,n+1):
                value *= i
            result.append(value)
        if (n<0 or n>15):
            result.append('ERROR')
    return result

print(factorial([]))