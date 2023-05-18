#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

assert run("2 * 6").output == "12"
assert run("10 / 5").output == "2"
assert run("12 + 7").output == "19"
assert run("21 - 5").output == "16"

###

print("All tests passed!")
