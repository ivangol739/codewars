def my_range(first=0, last=10, step=1):
  number = first
  while number < last:
    yield number
    number += step

ranger = my_range(1, 5)

for i in ranger:
  print(i)
  
  
def fibonachi(n):
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a + b
    
for num in fibonachi(10):
  print(num, end=" ")
    
  