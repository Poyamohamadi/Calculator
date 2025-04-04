
# Calculator: A Simple Kivy-Based Calculator

This project is a simple calculator application built using the **Kivy** framework in Python. The calculator provides basic arithmetic operations and some additional features such as clearing input, handling errors, and toggling positive/negative values.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Structure](#structure)
5. [Contributing](#contributing)
6. [License](#license)

---

## Program Demo

![Calculator](https://github.com/Poyamohamadi/Calculator/blob/main/demo.gif)

---

## Features

- **Basic Arithmetic Operations**: Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Error Handling**: Displays "Erorr" if an invalid operation is performed (e.g., division by zero).
- **Input Management**:
  - `CE`: Clears the last entered number or operator.
  - `C`: Resets the entire input to `0`.
  - `<<`: Removes the last character from the input.
- **Positive/Negative Toggle**: The `+/-` button toggles the sign of the current number or the last entered number in the sequence.
- **Responsive UI**: Designed with a vertical layout for ease of use on small screens.
- **Dynamic Display**: The input and results are displayed in a large, easy-to-read text box.

---

## Installation

### Prerequisites

1. **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Kivy**: Install the Kivy library using pip:

   ```bash
   pip install kivy
   ```

3. **Clone the Repository**:

   ```bash
   git clone https://github.com/Poyamohamadi/Calculator.git
   cd Calculator
   ```

---

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Use the buttons to perform calculations:
   - Enter numbers using the numeric buttons (`0-9`).
   - Use the operators (`+`, `-`, `*`, `/`) to perform arithmetic operations.
   - Press `=` to calculate the result.
   - Use `C` or `CE` to clear the input.
   - Use `<<` to delete the last character.
   - Use `+/-` to toggle the sign of the current number.

---

## Structure

The application is structured as follows:

1. **Main Application Class (`Poya_CalculatorApp`)**:
   - Inherits from `App` and initializes the main layout.

2. **Layout Class (`MyLayout`)**:
   - Extends `BoxLayout` and defines the structure of the calculator.
   - Contains:
     - A `TextInput` widget for displaying input and results.
     - A `GridLayout` containing buttons for numbers and operations.

3. **Button Handling**:
   - Buttons are dynamically created and bound to the `enter_value` method.
   - The `enter_value` method handles all button actions, including:
     - Input validation.
     - Arithmetic operations.
     - Error handling.

4. **Utility Functions**:
   - Regular expressions (`re`) are used for parsing and manipulating input strings.
   - The `eval` function is used to compute the result of arithmetic expressions.

---

## Dependencies

This project relies on the following Python library:

- **Python**: Version 3.6 or higher.
- **Kivy**: A modern, cross-platform GUI framework for building interactive applications. Install it using:

  ```bash
  pip install kivy
  ```

---

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request detailing your changes.

Please ensure your code adheres to the existing style and includes appropriate documentation.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Kivy Framework**: Thanks to the Kivy team for providing an excellent framework for building cross-platform applications.
- **Python Community**: Special thanks to the Python community for their support and resources.

---

For questions or feedback, feel free to reach out:

- **GitHub**: [Poyamohamadi](https://github.com/Poyamohamadi)

---

Thank you for using **Calculator**! 😊
