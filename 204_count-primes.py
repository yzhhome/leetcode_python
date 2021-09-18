"""
    204. 计数质数（统计素数）
    素数是只能被1和自身整除的数
    https://leetcode-cn.com/problems/count-primes/
"""

def coutPrimes(n):
    isPrime = [1] * n
    for i in range(2, n):
        if isPrime[i] == 1:
            for j in range(i * i, n, i):
                isPrime[j] = 0
    
    # 减去record[0] + record[1]中的两个1
    return sum(isPrime) - 2 if n > 1 else 0

if __name__ == '__main__':
    print(coutPrimes(10))    