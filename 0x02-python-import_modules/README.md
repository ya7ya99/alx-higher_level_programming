# Python Import Modules Exercises

This repository contains solutions to the Python import modules exercises.

## Table of Contents

1. [Task 0: Import a simple function from a simple file](#task-0-import-a-simple-function-from-a-simple-file)
2. [Task 1: My first toolbox!](#task-1-my-first-toolbox)
3. [Task 2: How to make a script dynamic!](#task-2-how-to-make-a-script-dynamic)
4. [Task 3: Infinite addition](#task-3-infinite-addition)
5. [Task 4: Who are you?](#task-4-who-are-you)
6. [Task 5: Everything can be imported](#task-5-everything-can-be-imported)
7. [Task 6: Build my own calculator!](#task-6-build-my-own-calculator)
8. [Task 7: Easy print](#task-7-easy-print)
9. [Task 8: ByteCode -> Python #3](#task-8-bytecode--python-3)
10. [Task 9: Fast alphabet](#task-9-fast-alphabet)

## Task 0: Import a simple function from a simple file

**Description:**
Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

**Solution:**
```python
a = 1
b = 2
from add_0 import add
result = add(a, b)
print(f"{a} + {b} = {result}")

