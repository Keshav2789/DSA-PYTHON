class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# Create object and call function
obj = Solution()
print(obj.fib(5))
