def factorizing_number(n):
  res = [1, n]
  for i in range(2, int(n ** .5)):
    if not n % i:
      res.append(i)
      if n // i != i:
        res.append(n//i)
  return sorted(res)

print(factorizing_number(int(input("Enter number: "))))
