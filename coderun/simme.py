import sys


def main():
  n = int(input())
  arr = list(map(int, input().split()))
  for i in range(len(arr)):
    if arr[i:] == arr[i:][::-1]:
      if i == 0:
        print(0)
        break
      else: 
        print(i)
        print(*arr[:i][::-1]) 
        break



if __name__ == '__main__':
  main()