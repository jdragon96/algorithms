def isDigit(num):
  if num is None: return False
  try:
    new_num = float(num)
    return True
  except:
    return False