# -*- coding: utf-8 -*-
"""
Python Learning: For loops, While loops, If-else statements, and Strings

This module demonstrates fundamental Python concepts with practical examples.
Based on: 60H_Lab_2_01_06_26.ipynb
"""


def print_separator(title=""):
    """Print a formatted separator line."""
    if title:
        print(f"\n{'='*50}")
        print(f"  {title.upper()}")
        print(f"{'='*50}\n")
    else:
        print("-" * 50)


def demo_for_loops():
    """Demonstrate various for loop patterns."""
    print_separator("For Loops in Python")

    # For loop with range
    print("Example 1: range(5)")
    for i in range(5):
        print(i)

    print_separator()

    # For loop with list
    print("Example 2: Looping through a list")
    list_1 = ["apple", 10, "banana", 10.5]
    for item in list_1:
        print(item)

    print_separator()

    # For loop with range (start, stop, step)
    print("Example 3: range(5, 10, 2) - start, stop, step")
    for i in range(5, 10, 2):
        print(i)


def demo_while_loop():
    """Demonstrate while loop."""
    print_separator("While Loops in Python")

    print("Counting from 1 to 10:")
    cnt = 1
    while cnt <= 10:
        print(cnt, end=" ")
        cnt += 1
    print("\n")  # New line after loop


def demo_if_else():
    """Demonstrate if-else statements."""
    print_separator("If-Else Statements")

    # Basic if-elif-else
    print("Example 1: Basic if-elif-else")
    flag = 7
    if flag == 1:
        print("Apple")
    elif flag == 2:
        print("Mango")
    else:
        print("Banana")

    print_separator()

    # Age check
    print("Example 2: Age classification")
    age = 18
    if age < 18:
        print("Minor")
    elif age == 18:
        print("Just Adult")
    else:
        print("Adult")


def demo_nested_if_else():
    """Demonstrate nested if-else statements."""
    print_separator("Nested If-Else Statements")

    # Nested if example 1
    print("Example 1: Number range check")
    x = 2
    if x > 5:
        if x <= 10:
            print("The number is in a perfect range")
        else:
            print("The number is out of perfect range")
    else:
        print("The number is not applicable")

    print_separator()

    # Nested if example 2
    print("Example 2: Positive even/odd check")
    x = 16
    if x > 0:
        if x % 2 == 0:
            print("Positive even")
        else:
            print("Positive odd")


def demo_shorthand_if_else():
    """Demonstrate shorthand if-else (ternary operator)."""
    print_separator("Shorthand If-Else (Ternary Operator)")

    # Shorthand if
    print("Example 1: Single line if")
    x = 56
    if x > 0:
        print("The Number is Positive")

    print_separator()

    # Ternary operator
    print("Example 2: Ternary operator (condition ? true : false)")
    x = -47
    print("Number is Positive") if x > 0 else print("Number is Negative")


def demo_string_indexing():
    """Demonstrate string indexing."""
    print_separator("String Indexing")

    str_1 = "Hello_1"
    str_2 = "Hello_2"
    str_3 = "Hello_3"

    print(f"String: '{str_1}'")
    print(f"Index [0] (first): {str_1[0]}")
    print(f"Index [-7] (7th from end): {str_1[-7]}")
    print(f"Index [-1] (last): {str_1[-1]}")


def demo_string_slicing():
    """Demonstrate string slicing."""
    print_separator("String Slicing")

    str_2 = "Hello_2"
    str_3 = "Hello_3"

    # Positive indexing
    print("Positive Indexing:")
    print(f"str_2[0:4]: '{str_2[0:4]}'")
    print(f"str_2[2:6]: '{str_2[2:6]}'")
    print(f"str_3[:5]: '{str_3[:5]}'  (from start to index 5)")
    print(f"str_3[3:]: '{str_3[3:]}'  (from index 3 to end)")

    print_separator()

    # Negative indexing
    print("Negative Indexing:")
    print(f"str_2[-7:-3]: '{str_2[-7:-3]}'")
    print(f"str_2[-5:-1]: '{str_2[-5:-1]}'")
    print(f"str_3[:-2]: '{str_3[:-2]}'  (everything except last 2)")
    print(f"str_3[-4:]: '{str_3[-4:]}'  (last 4 characters)")


def demo_string_operations():
    """Demonstrate string operations."""
    print_separator("String Operations")

    a = "Hello"
    b = "World"

    print(f"Concatenation: '{a}' + ' ' + '{b}' = '{a + ' ' + b}'")
    print(f"Repetition: ('{a} ') * 3 = '{(a + ' ') * 3}'")
    print(f"Membership: 'L' in '{a}' = {'L' in a}")
    print(f"Membership: 'x' in '{a}' = {'x' in a}")


def demo_string_methods():
    """Demonstrate string methods."""
    print_separator("String Methods")

    s = "python programming"

    print(f"Original: '{s}'")
    print(f".upper(): '{s.upper()}'")
    print(f".lower(): '{s.lower()}'")

    s_stripped = " python programming "
    print(f"\nString with spaces: '{s_stripped}'")
    print(f".strip(): '{s_stripped.strip()}'")

    print(f"\n.replace('python', 'Java'): '{s.replace('python', 'Java')}'")
    print(f"Original string (unchanged): '{s}'")

    print(f"\n.split(): {s.split()}")
    print(f".find('gram'): {s.find('gram')} (index position)")
    print(f".find('gram') in ' python programming ': {s_stripped.find('gram')} (index position)")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 50)
    print("  PYTHON FUNDAMENTALS LEARNING GUIDE")
    print("=" * 50)

    demo_for_loops()
    demo_while_loop()
    demo_if_else()
    demo_nested_if_else()
    demo_shorthand_if_else()

    print_separator("Strings in Python")
    demo_string_indexing()
    demo_string_slicing()
    demo_string_operations()
    demo_string_methods()

    print("\n" + "=" * 50)
    print("  END OF DEMONSTRATIONS")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
