# https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/infix_prefix_postfix.ipynb
# https://codingalzi.github.io/algopy/infix_prefix_postfix.html
# https://woochan-autobiography.tistory.com/786#4.%20%EC%9E%85%EB%A0%A5%20%EC%98%88%EC%A0%9C%201

import numpy as np
import matplotlib.pyplot as plts
from collections import deque
from util import utils

operator_priority = {
  "+": 0,
  "-": 0,
  "/": 1,
  "*": 1,
  "(": -1
}

def operate(v1, v2, op):
  if op == "+":
    return float(v1) + float(v2)
  elif op == "-":
    return float(v1) - float(v2)
  elif op == "*":
    return float(v1) * float(v2)
  elif op == "/":
    return float(v1) / float(v2)

def is_operator(s):
  if(s == "+") or \
    (s == "-") or \
    (s == "*") or \
    (s == "/"):
    return True
  return False

def is_high_prority_than_previous(p, c):
  if operator_priority[p] < operator_priority[c]:
    return True
  return False

def pop_operators_until_loop_close(
  ops_stack,
  final_queue
):
  while (len(ops_stack) > 0) and (ops_stack[-1] != "("):
    final_queue.append(ops_stack.pop())
    
def check_last_part_of_equation(
  final_queue,
  last_part
):
  if utils.isDigit(last_part):
    final_queue.append(float(last_part))

def equation_transformer(eq: str) -> deque:
  
  # 1. 방정식 체크하기
  if eq.count('(') != eq.count(')'): raise("부등호 개수가 유효하지 않습니다.")
  
  current_number = ""
  operator_stack = [] # 스택!
  queue = deque()
  
  for eq_char in equation:
    if eq_char == "(":
      operator_stack.append(eq_char)
      
    elif eq_char == ")":
      if not current_number == ")":
        queue.append(float(current_number))
      pop_operators_until_loop_close(operator_stack, queue)
      operator_stack.pop()  # '(' 제거
      current_number = ")"
      
    elif is_operator(eq_char):
      if not current_number == ")":
        queue.append(float(current_number))
        
      if len(operator_stack) > 0:
        if not is_high_prority_than_previous(operator_stack[-1], eq_char):
          # 1. 이전 연산자가 현재 연산자보다 우선순위가 높은
          # => 5 * 4 + 3
          # => * : 이전 연산자 / + : 현재 연산자
          # => 이전 연산자(*)를 pop하고 저장한다.
          queue.append(operator_stack.pop())  
        else:
          # 2. 이전 연산자의 우선순위가 더 낮은 경우.. 대기한다.
          # => 가장 마지막에 모두 pop한다.
          pass
          
      operator_stack.append(eq_char)
      current_number = ""
    else:
      current_number += eq_char
  
  # 마지막 숫자 입력하기
  check_last_part_of_equation(queue, current_number)
  pop_operators_until_loop_close(operator_stack, queue)
  return queue
  
def solver(queue: deque) -> float:
  value_stack = []
  while len(queue) > 0:
    v = queue.popleft()
    if is_operator(v):
      if len(value_stack) < 2: raise("연산을 수행할 값이 유효하지 않습니다.")
      v1 = value_stack.pop()
      v2 = value_stack.pop()
      value_stack.append(operate(v1, v2, v))
    else:
      value_stack.append(v)

  if len(value_stack) < 1: raise("연산 결과가 유효하지 않습니다.")
  final_value = value_stack.pop()
  return final_value

if __name__ == "__main__":
  equation = "(5*4+((2*6+7*2)*(2.45/2.45)))"
  trasformed_eq = equation_transformer(equation)
  final_value = solver(trasformed_eq)