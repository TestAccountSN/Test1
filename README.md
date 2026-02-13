# Test1 Repository

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A test repository demonstrating GitHub integration and basic Python functionality.

## 📋 Description

This repository serves as a testing ground for GitHub CLI integration and repository operations. It includes a simple calculator module showcasing basic arithmetic operations with proper documentation and error handling.

## 🚀 Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Error Handling**: Proper validation for edge cases (e.g., division by zero)
- **Well-Documented Code**: Comprehensive docstrings for all functions
- **Example Usage**: Demonstration of calculator functionality

## 📁 Repository Structure

```
Test1/
├── README.md          # This file
└── calculator.py      # Simple calculator module with basic arithmetic functions
```

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/TestAccountSN/Test1.git
cd Test1
```

## 💻 Usage

### Running the Calculator

```bash
python calculator.py
```

### Using as a Module

```python
from calculator import add, subtract, multiply, divide

# Perform calculations
result_add = add(10, 5)        # Returns: 15
result_sub = subtract(10, 5)   # Returns: 5
result_mul = multiply(10, 5)   # Returns: 50
result_div = divide(10, 5)     # Returns: 2.0
```

## 📚 API Reference

### Functions

#### `add(a, b)`
Adds two numbers together.
- **Parameters**: `a` (float), `b` (float)
- **Returns**: Sum of a and b

#### `subtract(a, b)`
Subtracts b from a.
- **Parameters**: `a` (float), `b` (float)
- **Returns**: Difference of a and b

#### `multiply(a, b)`
Multiplies two numbers.
- **Parameters**: `a` (float), `b` (float)
- **Returns**: Product of a and b

#### `divide(a, b)`
Divides a by b.
- **Parameters**: `a` (float), `b` (float)
- **Returns**: Quotient of a and b
- **Raises**: `ValueError` if b is zero

## 🧪 Testing

The calculator includes built-in example usage that runs when executed directly:

```bash
python calculator.py
```

Expected output:
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
```

## 📝 Repository Details

- **Owner**: TestAccountSN
- **Repository**: Test1
- **Default Branch**: master
- **Language**: Python
- **Created**: July 31, 2025
- **Last Updated**: December 6, 2025

## 🤝 Contributing

This is a test repository, but contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m "Add some AmazingFeature"`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**TestAccountSN**
- GitHub: [@TestAccountSN](https://github.com/TestAccountSN)

## 🔗 Links

- [Repository](https://github.com/TestAccountSN/Test1)
- [Issues](https://github.com/TestAccountSN/Test1/issues)
- [Pull Requests](https://github.com/TestAccountSN/Test1/pulls)

---

⭐ If you find this repository useful, please consider giving it a star!