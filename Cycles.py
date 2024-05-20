def solve(receipts: list):
  result = [i for i in receipts[2::3]]
  return result, len(result)

print(solve([123, 145, 346, 246, 235, 166, 112, 351, 342]))