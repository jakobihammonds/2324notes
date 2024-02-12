for i in range(10):
  row = ' '.join(f"{i*10 +11 * j:02}" for j in range(10-i))
  print(row)