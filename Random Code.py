# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

def Main() -> None:
    code = []
    numbers = list(set(range(0,10,1)))
    while len(code) < 4:
        code.append(numbers.pop(random.randint(0,len(numbers)-1)))
    print(code)
    

if __name__ == "__main__":
    Main()