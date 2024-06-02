# 1

def my_decorator(func):
  def wrapper():
    print("Что-то делается перед вызовом функции")
    func()
    print("Что-то делается после вызова функции")
  return wrapper
  
@my_decorator
def say_hello():
  print('Hi')
  
say_hello()

#Использование для логирования

def log_func_call(func):
  def wrapper(*args, **kwargs):
    print(f"Вызова функции {func.__name__} с аргументами {args} и {kwargs}")
    result = func(*args, **kwargs)
    print(f"Фнкция {func.__name__} вернула {result}")
    return result
  return wrapper

@log_func_call
def add(a, b):
  return a + b

add(5, 3)

#Декоратор для проверки прав доступа

def require_admin(func):
  def wrapper(user, *args, **kwargs):
    if user.is_admin:
      return func(user, *args, **kwargs)
    else:
      print("Доступ запрещен")
  return wrapper

class User:
  def __init__(self, is_admin):
    self.is_admin = is_admin

@require_admin
def access_admin_panel(user):
  print("Добро пожаловать в админ-панель!")
  
admin = User(is_admin=True)
guest = User(is_admin=False)

access_admin_panel(admin)
access_admin_panel(guest)