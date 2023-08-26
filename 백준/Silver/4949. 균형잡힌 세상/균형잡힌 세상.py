while True:
  sentence = input()
  if sentence == '.':
    break  
  
  stack = []
  is_balanced = True

  # 입력받은 문장에서 여는 소괄호, 여는 대괄호만 추출해 stack에 담는다.
  # 이 때 서로의 짝이 있기 때문에 짝을 고려하여 stack 리스트과 비교한다.
  for s in sentence:
    if s in '([':
      stack.append(s)
    elif s in ')]':
      if len(stack)==0:
        is_balanced = False
        break
      if s == ')' and stack[-1] == '(':
        stack.pop()
      elif s == ']' and stack[-1] == '[':
        stack.pop()
      else:
        is_balanced = False
        break

  if len(stack)==0 and is_balanced:
    print("yes")
  else:
    print("no")