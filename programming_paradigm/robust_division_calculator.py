def safe_divide(numerator, denominator):
    try:
        result = float(numerator / denominator)
        return f"The result of the division is {result:.01f}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
