class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n 
        digit_sum = 0
        digit_product = 1

        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_product *= digit
            n //= 10

        divisor = digit_sum + digit_product
        return original % divisor == 0