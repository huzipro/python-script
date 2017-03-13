def largestPrime(n):
  i = 2
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
  print(n)

largestPrime(13195)
largestPrime(600851475143)