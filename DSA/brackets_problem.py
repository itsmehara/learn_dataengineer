stack = list()

def top():
  if stack:
    _top = stack[-1]
  else:
    _top = None
  return _top

def push(elem):
  stack.append(elem)
  print(f"element pushed : {elem}")
  print(f"after push: {stack}")

def pop():
  popped_elem = stack.pop()
  print(f"popping {popped_elem}")
  print(f"after popping: {stack}")

given_list = ['(', ')', '[', ']', '{', '}', '{', '}']
print(f"Top is {top()}")

open_pairs = {"(": ")",
              "[": "]",
              "{": "}"}

for each in given_list:
  current_top = top()
  if open_pairs.get(current_top, None) == each:
    pop()
  else:
    push(each)
