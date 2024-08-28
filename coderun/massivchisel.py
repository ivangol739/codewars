import sys

def main():
  n = int(input())
  arr = list(map(int, input().split()))
  x = int(input())

  number = arr[0]
  mind = abs(arr[0] - x)
  for i in arr[1:]:
    diff = abs(i - x)
    if diff < mind:
      mind = diff
      number = i
  print(number)
    

if __name__ == "__main__":
  main()