def check_email(email: str) -> bool:
  if "@" in email and "." in email:
    if " " not in email:
      return True
    else: return False
  else:
    return False

print(check_email('em@il.ru'))