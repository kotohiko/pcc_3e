# -*- coding: utf-8 -*-
"""
Python String Quotes Demo
This script demonstrates how to include quotes inside Python strings.
"""

print("=== 1. Alternating Quotes ===")
s1 = 'He said, "Hello!"'  # Single quotes outside, double quotes inside
s2 = "It's a book."       # Double quotes outside, single quotes inside
print("s1:", s1)
print("s2:", s2)
print()

print("=== 2. Escape Characters ===")
s3 = "He said, \"Hello!\""  # Escaping double quotes
s4 = 'It\'s a book.'        # Escaping single quotes
print("s3:", s3)
print("s4:", s4)
print()

print("=== 3. Triple Quotes ===")
s5 = """He said, "It's mine." """  # Contains both single and double quotes
print("s5:", s5)
print()
