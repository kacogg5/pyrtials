# Pyrtials

To use:
In a terminal, navigate to the location of pyrtials.py

Run the command `py3 pyrtials.py -p <path_to_python_file>`, replacing `<path_to_python_file>` with the path to your python file containing partials.

<hr/>

Pyrtials is a compiler written in Python 3 to support custom partial syntax

For any function, parameters can be substituted with $ and the function becomes a partial. For instance, the following demonstrates using the built-in `print()` function for to produce a lambda only requiring a single parameter which is stored in `my_print`. This is then called 3 separate times with differing inputs.

```
my_print = print("Hello", $, end="!\n")

my_print("Harry Potter") # prints "Hello Harry Potter!"
my_print("Hermoine Granger") # prints "Hello Hermoine Granger!"
my_print("Ron Weasley") # prints "Hello Ron Weasley!"
```