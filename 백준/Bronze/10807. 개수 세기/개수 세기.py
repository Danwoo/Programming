while True:
  count = int(input())
  input_array = list(input().split())
  number = input()
  if count == len(input_array):
    print(input_array.count(number))
    break