import sys

def main():
  text = sys.stdin.read()
  words = text.split()
  a = set(words)
  print(len(a))

if __name__ == '__main__':
  main()