# 🐍 Python Mastery

> A structured, hands-on Python learning journey from fundamentals to advanced concepts with 80+ practical examples, 20+ mini-exercises, OOP, APIs, and beginner projects.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-blue?style=for-the-badge)](https://pep8.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Learning-orange?style=for-the-badge)](#)

---

## 📋 Overview

**python-mastery** is a comprehensive, self-paced Python learning repository designed for:

- **Absolute beginners** starting their Python journey
- **Students building a learning portfolio** to showcase on GitHub
- **Self-learners** who prefer hands-on examples over theory alone
- **Developers** transitioning from other languages to Python

The repository contains **79 Python files** organized into **12 progressive modules**, from basic syntax to object-oriented programming, exception handling, modules, and REST API integration.

Every file includes:
- ✅ Detailed inline comments explaining concepts
- ✅ Real, executable code examples
- ✅ Best practices and PEP 8 compliance
- ✅ Type hints and docstrings where applicable

---

## 🎯 What You Will Master

### Core Python Skills
- **Syntax & Data Types** → Variables, strings, numbers, type casting
- **Control Flow** → if/elif/else, boolean logic, ternary operators
- **Data Structures** → Lists, sets, tuples, dictionaries, 2D collections
- **Functions** → Parameters, return values, default arguments, arbitrary arguments, lambdas
- **Object-Oriented Programming** → Classes, objects, inheritance, polymorphism, abstraction
- **Exception Handling** → try/except/finally, custom exceptions, input validation
- **Iteration** → for loops, while loops, nested loops, break/continue

### Advanced Concepts
- **Modules & Packages** → Creating and importing reusable code
- **Decorators** → Function and class decorators
- **REST APIs** → HTTP requests, headers, status codes, authentication
- **Command-Line Programs** → Interactive games, calculators, validators

---

## 📁 Repository Structure

```
python-mastery/
│
├── 01_basics/                           [11 files] Foundation concepts
│   ├── 01_display.py                    # Print functions and output
│   ├── 02_variables.py                  # Variables, data types, f-strings
│   ├── 03_type_casting.py               # Type conversion and validation
│   ├── 04_user_input.py                 # Interactive input from users
│   ├── 05_arithmetic_operators.py       # Math operations and operators
│   ├── 06_builtinmath_functions.py      # round(), abs(), pow(), min(), max()
│   ├── 07_math_module_function.py       # math module functions
│   ├── 08_string_methods.py             # String manipulation methods
│   ├── 09_string_indexing.py            # Slicing, indexing, reversal
│   ├── 10_format_specifiers.py          # F-string formatting
│   └── 11_random_numbers.py             # random module for randomness
│
├── 02_control-flow/                     [4 files] Decision making
│   ├── 01_if_elif_else.py               # Conditional statements
│   ├── 02_boolean_in_conditional.py     # Boolean values in conditions
│   ├── 03_conditional_expressions.py    # Ternary operator (one-line if-else)
│   └── 04_conditional_expressions.py    # More conditional examples
│
├── 03_data_structures/                  [5 files] Collections mastery
│   ├── 01_list.py                       # Lists (ordered, mutable)
│   ├── 02_set.py                        # Sets (unordered, unique)
│   ├── 03_tuple.py                      # Tuples (immutable sequences)
│   ├── 04_2d_collections.py             # 2D lists and nested loops
│   └── 05_dictionary.py                 # Dictionaries (key-value pairs)
│
├── 04_functions/                        [8 files] Reusable code
│   ├── 01_functions.py                  # Function basics and parameters
│   ├── 02_default_arguments.py          # Functions with default values
│   ├── 03_keyword_arguments.py          # Named arguments
│   ├── 04_docstrings.py                 # Function documentation
│   ├── 05_arbitrary_arguments.py        # *args and **kwargs
│   ├── 06_lambda_functions.py           # Anonymous functions
│   ├── 07_map_function.py               # map() with functions
│   └── 01_Functions versus methods.png  # Visual reference guide
│
├── 05_oop/                              [8 files] Object-oriented programming
│   ├── 01_classes_and_objects/          # Subdirectory with OOP examples
│   │   ├── car.py                       # Car class definition
│   │   └── main.py                      # Using the Car class
│   ├── 02_class_variables.py            # Class vs instance variables
│   ├── 03_inheritance.py                # Single inheritance
│   ├── 04_multiple_inheritance.py       # Multiple inheritance
│   ├── 05_abstract_class.py             # Abstract base classes
│   ├── 06_super_function.py             # Using super() function
│   ├── 07_polymorphism_inheritance.py   # Polymorphism concepts
│   └── pillars-of-oop.jpg               # Visual reference: OOP pillars
│
├── 06_exception-handling/               [1 file] Error management
│   ├── exception_handling.py            # try/except/finally, custom exceptions
│   └── 01_try-except vs. raise.png      # Visual reference guide
│
├── 07_file-handling/                    [Planned] File I/O operations
│   └── README.md                        # Placeholder for future content
│
├── 08_loops/                            [3 files] Iteration techniques
│   ├── 01_while_loops.py                # While loops and input validation
│   ├── 02_for_loops.py                  # For loops, range(), break, continue
│   └── 03_nested_loops.py               # Nested loops and patterns
│
├── 09_mini-exercises/                   [25+ files] Practice problems
│   ├── 01_mad_libs_game.py              # Interactive story game
│   ├── 02_area_calc.py                  # Rectangle area and volume
│   ├── 03_shopping_cart.py              # Shopping cart calculator
│   ├── 04_circle_circumference.py       # Circle calculations
│   ├── 05_circle_area.py                # Using math.pi
│   ├── 06_hypotenuse_calculator.py      # Pythagorean theorem
│   ├── 07_food_check.py                 # Y/N input validation
│   ├── 08_name_checker.py               # Empty string validation
│   ├── 09_arithmetic_calculator.py      # Basic calculator
│   ├── 10_weight_convertor.py           # Unit conversion
│   ├── 11_temperature_convertor.py      # Celsius to Fahrenheit
│   ├── 12_user_input_validation.py      # Input validation patterns
│   ├── 13_creditcard_last4.py           # String slicing
│   ├── 15_compound_interest_calculator.py# Financial calculations
│   ├── 16_rectangle_printer.py          # Pattern printing
│   ├── 17_countdown_timer.py            # Formatted timer with time.sleep()
│   ├─�� 18_shopping_cart.py              # Advanced cart with lists
│   ├── 19_keypad_2d.py                  # 2D tuple iteration (phone keypad)
│   ├── 20_number_guessing_game.py       # Number guessing game
│   ├── 22_phone_number_generator.py     # Random phone number
│   ├── 23_email_generator.py            # Email generation
│   ├── 24_password_validator.py         # Password strength checking
│   ├── 25_string_concat_args.py         # String concatenation
│   └── README.md                        # Placeholder
│
├── 10_beyond-basics/                    [12 files] Advanced topics
│   ├── 01_modules-and-packages/         # Module organization
│   │   ├── 01_modules.py                # Python modules overview
│   │   └── 02_packages.py               # Package structure
│   ├── 02_api/                          # REST API integration
│   │   ├── 01_requests.py               # HTTP requests basics
│   │   ├── 02_urillib.py                # urllib alternative
│   │   ├── 03_query_params_with_requests.py  # URL query parameters
│   │   ├── 04_http_verbs.py             # GET, POST, PUT, DELETE
│   │   ├── 05_headers_with_requests.py  # HTTP headers
│   │   ├── 06_status_code_with_requests.py   # Status code handling
│   │   ├── 07_headers_and_status_codes_exercises.py # Practice
│   │   ├── 08_Basic_authentication.py   # Basic auth
│   │   ├── 09_API_key_or_token_authentication.py    # Token auth
│   │   └── images/                      # API reference diagrams
│   ├── api.py                           # Complete PokeAPI example
│   ├── decorator.py                     # Decorators tutorial
│   └── README.md                        # Placeholder
│
├── 11_projects/                         [3 files] Beginner projects
│   └── beginners/
│       ├── concession_stand.py          # Movie concession stand program
│       ├── number_guessing_game.py      # Guessing game with validation
│       └── quiz_game.py                 # Multi-question quiz
│
├── 12_notes/                            [Planned] Learning notes
│   └── README.md                        # Placeholder
│
├── .gitignore                           # Python-specific ignore patterns
└── README.md                            # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** ([Download](https://www.python.org/))
- **Git** (for cloning the repository)
- Basic command-line knowledge

### 1. Clone the Repository

```bash
git clone https://github.com/AbdulRehman393/python-mastery.git
cd python-mastery
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Most examples use only Python's standard library. The API examples require `requests`:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests
```

### 4. Run Your First Program

```bash
python 01_basics/01_display.py
```

---

## 📖 Learning Path

### ⭐ Recommended Study Order (25-35 hours)

1. **01_basics** (2-3 hours) - Fundamentals and syntax
2. **02_control-flow** (1 hour) - Decision making
3. **03_data_structures** (2-3 hours) - Collections
4. **04_functions** (2-3 hours) - Reusable code
5. **08_loops** (1-2 hours) - Iteration
6. **09_mini-exercises** (5-8 hours) - Practice problems
7. **05_oop** (3-4 hours) - Object-oriented programming
8. **06_exception-handling** (1 hour) - Error handling
9. **10_beyond-basics** (4-5 hours) - Advanced topics
10. **11_projects** (2-3 hours) - Complete applications

---

## 🎮 Quick Examples

### Run a Basic Program
```bash
python 01_basics/01_display.py
```

### Run an Interactive Game
```bash
python 11_projects/beginners/quiz_game.py
```

### Run an API Example
```bash
python 10_beyond-basics/api.py
```

### Run a Countdown Timer
```bash
python 09_mini-exercises/17_countdown_timer.py
```

---

## 💡 Key Features

### ✅ Best Practices
- Detailed comments and docstrings
- PEP 8 style compliance
- Type hints where applicable
- Input validation and error handling
- F-string formatting
- DRY principle implementation
- Modular code structure

### 📊 Progress Tracker
```
✅ Basics (11 files)              100% Complete
✅ Control Flow (4 files)         100% Complete
✅ Data Structures (5 files)      100% Complete
✅ Functions (8 files)            100% Complete
✅ OOP (8 files)                  100% Complete
✅ Exception Handling (1 file)    100% Complete
✅ Loops (3 files)                100% Complete
✅ Mini-Exercises (25+ files)     100% Complete
✅ Advanced Topics (12 files)     100% Complete
✅ Projects (3 files)             100% Complete
🔄 File Handling                  0% (Planned)
🔄 Notes                          0% (Planned)
```

---

## 🛠️ Technologies Used

- **Python 3.11+**
- Standard libraries: `math`, `random`, `time`, `string`, `os`
- External: `requests` (for API examples)
- PEP 8 style guide
- Git & GitHub

---

## 📋 Validation

Verify all Python files compile:

```bash
python -m compileall .
```

---

## 🗺️ Future Improvements

- [ ] Complete file handling module
- [ ] Advanced OOP patterns
- [ ] SQLite database examples
- [ ] Pandas data analysis
- [ ] Web scraping with BeautifulSoup
- [ ] Flask/FastAPI web applications
- [ ] Unit testing with pytest
- [ ] GitHub Actions CI/CD pipeline

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/improve-example`
3. Commit changes: `git commit -m "Add improved example"`
4. Push and open a Pull Request

---

## ❓ FAQ

**Q: What if I get an error?**
A: Ensure Python 3.11+, virtual environment activated, and `pip install -r requirements.txt` run.

**Q: Do I need to follow the order?**
A: The path is recommended but flexible. Skip ahead if you already know basics.

**Q: Can I modify the examples?**
A: Absolutely! Experiment and break things—that's how you learn.

**Q: Can I use this commercially?**
A: Yes, under the MIT License.

---

## 📚 Additional Resources

- [Python Official Docs](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [PEP 8 Style Guide](https://pep8.org/)
- [LeetCode](https://leetcode.com/) - Coding challenges

---

## 🏆 What You'll Learn

✅ Write Python programs from scratch  
✅ Use variables, loops, and conditional logic  
✅ Work with data structures  
✅ Create reusable functions and modules  
✅ Build object-oriented programs  
✅ Handle errors gracefully  
✅ Make HTTP requests and work with APIs  
✅ Write interactive command-line programs  
✅ Follow Python best practices  
✅ Debug code independently  

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Abdul Rehman**
- GitHub: [@AbdulRehman393](https://github.com/AbdulRehman393)
- Repository: [python-mastery](https://github.com/AbdulRehman393/python-mastery)

---

## ⭐ Show Your Support

- ⭐ Star this repository
- 🍴 Fork for your learning journey
- 📢 Share with other learners
- 💬 Discuss by opening issues
- 🤝 Contribute improvements

---

<div align="center">

### 🚀 Ready to Master Python?

**[Start Learning](./01_basics/)** • **[View Projects](./11_projects/)** • **[Try Exercises](./09_mini-exercises/)**

---

*Built with ❤️ and lots of ☕ by Abdul Rehman*

*Last Updated: January 2026 | Actively Maintained*

</div>
