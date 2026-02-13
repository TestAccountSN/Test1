# Test1 🧮

A comprehensive test repository showcasing GitHub integration with SuperNinja AI and featuring a Python calculator module.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 About

This repository demonstrates basic Python functionality with a calculator module that performs arithmetic operations. It serves as a test project for GitHub integration with SuperNinja AI and showcases best practices in Python development.

## ✨ Features

- ✅ **Basic Arithmetic Operations**: Add, subtract, multiply, and divide
- ✅ **Error Handling**: Robust error handling for edge cases (division by zero, invalid inputs)
- ✅ **Well-Documented Code**: Clear documentation and inline comments
- ✅ **Easy to Use**: Simple API for quick integration
- ✅ **Type Hints**: Modern Python type annotations
- ✅ **Unit Tests**: Comprehensive test coverage (coming soon)

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/TestAccountSN/Test1.git
cd Test1
```

### Requirements

- Python 3.6 or higher
- No external dependencies required!

## 💻 Usage

### Command Line

Run the calculator directly:

```bash
python calculator.py
```

### As a Module

Import and use in your Python projects:

```python
from calculator import add, subtract, multiply, divide

# Perform calculations
result = add(10, 5)        # Returns: 15
result = subtract(10, 5)   # Returns: 5
result = multiply(10, 5)   # Returns: 50
result = divide(10, 5)     # Returns: 2.0
```

## 📚 API Reference

### `add(a, b)`
Adds two numbers together.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Sum of a and b

### `subtract(a, b)`
Subtracts the second number from the first.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Difference of a and b

### `multiply(a, b)`
Multiplies two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Product of a and b

### `divide(a, b)`
Divides the first number by the second.

**Parameters:**
- `a` (int/float): Numerator
- `b` (int/float): Denominator

**Returns:** Quotient of a and b

**Raises:** `ZeroDivisionError` if b is zero

## 🔍 Examples

### Basic Operations

```python
from calculator import add, subtract, multiply, divide

# Addition
print(add(15, 25))        # Output: 40

# Subtraction
print(subtract(100, 42))  # Output: 58

# Multiplication
print(multiply(7, 8))     # Output: 56

# Division
print(divide(100, 4))     # Output: 25.0
```

### Error Handling

```python
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Project Link:** [https://github.com/TestAccountSN/Test1](https://github.com/TestAccountSN/Test1)

---

<div align="center">
  <sub>Built with ❤️ using SuperNinja AI</sub>
</div>