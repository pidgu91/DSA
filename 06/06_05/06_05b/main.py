from collections import deque

def check_matching_parentheses(s):
  stack = deque()
  for char in s:
    if char == "(":
      stack.append(char)
    elif char == ")":
      if not stack:
        return False
      stack.pop()
  return len(stack) == 0

print(check_matching_parentheses("()"))    
print(check_matching_parentheses("())"))
print(check_matching_parentheses("(ok)"))
print(check_matching_parentheses(")linkedin()"))

# stacks are great if you need to keep track of state
# if you need to index, don't use stacks
# searching is bad too
