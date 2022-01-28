hatvany = 0
a = 0 
c = 0
while a <= 64:
  eredmeny = 2 ** hatvany
  hatvany = hatvany + 1
  a = a + 1
  print(f"a {c} számnak a hatványa: {eredmeny}")
  c = c + 1