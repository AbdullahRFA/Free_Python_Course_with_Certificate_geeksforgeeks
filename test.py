n = 25
if n <= 1:
  print("No")
else:
  x = 2
  while x * x <= n:
    if n % x == 0:
      print("No")
      break
    x = x + 1
  else:
    print("Yes")