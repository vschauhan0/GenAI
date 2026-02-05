# Import math_utils (full module)
import math_utils

# Import specific function
from math_utils import square

# Import string module
import string_utils

# Import package
import shop_package.discount as disc
from shop_package.billing import calculate_total


# ---- Testing math_utils ----
print("Add:", math_utils.add(10, 5))
print("Subtract:", math_utils.subtract(10, 5))
print("Square:", square(4))


# ---- Testing string_utils ----
text = "python programming is fun"

print("Capitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))


# ---- Testing shop_package ----
print("Discounted Price:", disc.apply_discount(1000, 10))
print("Flat Discount:", disc.flat_discount(1000))

print("Total Bill:", calculate_total([100, 200, 300]))
