from functools import wraps

def log_type(func):
   @wraps(func)
   def arg_type(arg):
      return f'{calc_cube.__name__}({arg}: {type(func(arg))})'
   return arg_type


@log_type
def calc_cube(arg):
   return arg ** 3


print(calc_cube(1.5))
