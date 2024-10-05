# made by appleflyer
# simple script to implement colors in your python script.

# how to use

# use by putting this python file where your main script is, and then `from color_lib import cprint`
# and then, in your main script, example:
# print(cprint['red'] + "hello " + cprint['yellow'] + "world")

# an incredibly inefficient script, brought to you by, appleflyer.

cprint = {'red': '\033[38;5;160m', 
          'green': '\033[38;5;49m',
          'green2': '\033[38;5;71m',
          'yellow': '\033[38;5;228m', 
          'lpurple': '\033[38;5;141m',
          'purple': '\033[38;5;140m',
          'cyan': '\033[38;5;87m',
          'lblue': '\033[38;5;153m',
          'black': '\033[38;5;232m',
          'white': '\033[38;5;255m',
          'italic': '\x1B[3m'
          }