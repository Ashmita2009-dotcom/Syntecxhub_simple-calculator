""A simple command-line calculator with basic arithmetic operations."""

from __future__ import annotations

import os
from typing import Optional


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """Return the quotient of two numbers, or None if dividing by zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def parse_number(raw_value: str) -> float:
    """Convert a string input to a float and reject invalid values."""
    value = raw_value.strip()
    if not value:
        raise ValueError("Input cannot be empty.")

    try:
        return float(value)
    except ValueError as exc:
        raise ValueError("Invalid number.") from exc


def normalize_choice(raw_choice: str) -> str:
    """Convert a menu number or direct operator to a normalized operator value."""
    choice = raw_choice.strip()
    if choice in {"1", "+"}:
        return "+"
    if choice in {"2", "-"}:
        return "-"
    if choice in {"3", "*", "x"}:
        return "*"
    if choice in {"4", "/", "÷"}:
        return "/"
    if choice in {"5"}:
        return "5"
    if choice in {"6"}:
        return "6"
    raise ValueError("Invalid choice.")


def get_menu_choice() -> str:
    """Prompt the user for a calculator menu choice or direct operator."""
    while True:
        choice = input("Enter your choice (1-6 or +, -, *, x, /, ÷): ").strip()
        try:
            return normalize_choice(choice)
        except ValueError:
            print("Invalid choice. Please enter a number from 1 to 6 or a valid operator.")


def prompt_for_numbers() -> tuple[float, float]:
    """Prompt the user for two valid numbers."""
    while True:
        try:
            first_number = parse_number(input("Enter first number: "))
            second_number = parse_number(input("Enter second number: "))
            return first_number, second_number
        except ValueError as exc:
            print(f"Error: {exc}")


def perform_calculation(operator: str, first_number: float, second_number: float) -> Optional[float]:
    """Perform a selected arithmetic operation."""
    if operator in {"+"}:
        return add(first_number, second_number)
    if operator in {"-"}:
        return subtract(first_number, second_number)
    if operator in {"*", "x"}:
        return multiply(first_number, second_number)
    if operator in {"/", "÷"}:
        return divide(first_number, second_number)
    raise ValueError("Unsupported operator")


def display_result(operator: str, first_number: float, second_number: float, result: Optional[float]) -> None:
    """Display the calculation result in a readable format."""
    if result is None:
        print("Error: Cannot divide by zero.")
        return

    display_operator = {
        "+": "+",
        "-": "-",
        "*": "*",
        "/": "/",
    }[operator]
    print(f"{first_number} {display_operator} {second_number} = {result}")


def prompt_for_repeat() -> bool:
    """Ask whether the user wants to perform another calculation."""
    while True:
        answer = input("\nDo you want to perform another calculation? (Y/N): ").strip().upper()
        if answer == "Y":
            return True
        if answer == "N":
            return False
        print("Please enter Y or N.")


def main() -> None:
    """Run the calculator application."""
    print("Welcome to the Python Calculator!")

    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Clear Screen")
        print("6. Exit")

        choice = get_menu_choice()

        if choice == "5":
            clear_screen()
            continue

        if choice == "6":
            print("Thank you for using the calculator!")
            break

        operator = {
            "+": "+",
            "-": "-",
            "*": "*",
            "/": "/",
        }[choice]

        first_number, second_number = prompt_for_numbers()
        result = perform_calculation(operator, first_number, second_number)
        display_result(operator, first_number, second_number, result)

        if not prompt_for_repeat():
            print("Thank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
