<div align="center">

# 🐍 Python Mastery

### A structured, hands-on Python learning journey from fundamentals to APIs and beginner projects.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Learning-orange?style=for-the-badge)](#-progress-tracker)

*An evolving learning portfolio containing dozens of executable examples, practical exercises, visual references, and beginner-friendly command-line projects.*

[Getting Started](#-getting-started) • [Learning Path](#-learning-path) • [Exercises](#-mini-exercises) • [Projects](#-beginner-projects)

</div>

---

## 📋 Overview

`python-mastery` documents a progressive Python learning journey. The repository begins with syntax and data types, then moves through control flow, collections, functions, loops, object-oriented programming, exception handling, modules, REST APIs, practical exercises, and beginner projects.

The examples are intentionally small and independent so that learners can open a file, read the comments, run it, modify it, and observe the result.

Some modules are complete, while file handling, learning notes, automated tests, and intermediate projects are still being expanded.

## 🎯 Topics Covered

- Python syntax, variables, data types, and type casting
- User input and formatted output
- Strings, indexing, slicing, and formatting
- Conditional statements and boolean logic
- Lists, sets, tuples, dictionaries, and 2D collections
- Functions, arguments, return values, docstrings, lambdas, and `map()`
- `for`, `while`, and nested loops
- Classes, objects, class variables, inheritance, abstraction, and polymorphism
- Exception handling with `try`, `except`, `finally`, and `raise`
- Modules, packages, and decorators
- HTTP requests, REST APIs, headers, status codes, and authentication concepts
- Interactive calculators, games, validators, and beginner projects

## 📁 Repository Structure

```text
python-mastery/
├── 01_basics/                  Python syntax, variables, strings, math, randomness
├── 02_control-flow/            Conditions and boolean logic
├── 03_data_structures/         Lists, sets, tuples, dictionaries, 2D collections
├── 04_functions/               Functions, arguments, docstrings, lambdas, map()
├── 05_oop/                     Classes, objects, inheritance, abstraction, polymorphism
├── 06_exception-handling/      try/except/finally and raise
├── 07_file-handling/           Planned file I/O lessons
├── 08_loops/                   while, for, and nested loops
├── 09_mini-exercises/          Calculators, games, validators, and utilities
├── 10_beyond-basics/           Modules, packages, decorators, APIs, authentication
├── 11_projects/                Beginner command-line projects
├── 12_notes/                   Planned learning notes
├── LICENSE                     MIT license
├── pyproject.toml              Project metadata and tool configuration
├── requirements.txt            Runtime dependencies
├── .gitignore                  Python and IDE ignore rules
└── README.md                   Project documentation
```

The repository currently includes **78 Python files** across the learning modules, exercises, API lessons, and beginner projects. This number may change as the learning journey grows.

## 🧭 Learning Path

The recommended order is:

1. `01_basics` — Build a foundation with syntax, variables, strings, and math.
2. `02_control-flow` — Practice decisions and boolean expressions.
3. `03_data_structures` — Learn Python's core collections.
4. `04_functions` — Write reusable and organized code.
5. `08_loops` — Practice repetition and iteration.
6. `09_mini-exercises` — Apply the concepts to small programs.
7. `05_oop` — Learn classes, objects, inheritance, and polymorphism.
8. `06_exception-handling` — Handle invalid input and runtime errors.
9. `10_beyond-basics` — Explore modules, decorators, APIs, and authentication.
10. `11_projects` — Combine your skills in complete beginner programs.

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or newer
- Git
- Basic command-line knowledge

### Clone the repository

```bash
git clone https://github.com/AbdulRehman393/python-mastery.git
cd python-mastery
```

### Create a virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

Most examples use Python's standard library. API examples use `requests`.

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Project metadata and optional development tools are defined in [`pyproject.toml`](pyproject.toml).

## ▶️ Running Examples

Run a basic program:

```bash
python 01_basics/01_display.py
```

Run an OOP example:

```bash
python 05_oop/01_classes_and_objects/main.py
```

Run a mini-exercise:

```bash
python 09_mini-exercises/17_countdown_timer.py
```

Run a beginner project:

```bash
python 11_projects/beginners/quiz_game.py
```

Run the PokeAPI example:

```bash
python 10_beyond-basics/api.py
```

The API example requires an internet connection and the `requests` package.

## 💪 Mini-Exercises

The `09_mini-exercises` directory contains small programs for practicing concepts such as:

- Mad Libs and interactive storytelling
- Area, circumference, hypotenuse, and compound-interest calculators
- Shopping carts
- Unit and temperature conversion
- Input validation
- Credit-card string slicing
- Countdown timers
- Number guessing
- Phone and email generation
- Password validation
- String concatenation and formatting

These programs are designed to be modified. Try adding validation, functions, tests, or a different user interface to each one.

## 🧩 Beginner Projects

The `11_projects/beginners` directory currently includes:

- `concession_stand.py` — A command-line concession stand program
- `number_guessing_game.py` — A number guessing game with input validation
- `quiz_game.py` — A multiple-choice Python quiz

## 🌐 API Learning

The `10_beyond-basics` directory introduces:

- Python modules and packages
- Decorators
- Basic HTTP requests with `requests`
- Query parameters
- HTTP verbs such as GET, POST, PUT, and DELETE
- Request headers
- HTTP status codes
- Basic authentication
- API-key and token authentication concepts
- JSON response handling

The API examples are educational demonstrations. Do not place real passwords, API keys, or tokens directly in source files.

## 🛠️ Technologies

- **Language:** Python 3.11+
- **Standard library examples:** `math`, `random`, `time`, `string`, `os`, and `urllib`
- **External dependency:** `requests`
- **Project configuration:** `pyproject.toml`
- **License:** MIT

## 🧪 Validation

The repository contains standalone learning scripts rather than a formal test suite. You can still verify that the Python files compile:

```bash
python -m compileall .
```

To compile an individual file:

```bash
python -m py_compile path/to/example.py
```

Many scripts are interactive and wait for user input, so they should be run manually rather than executed as a large automated batch.

## 📊 Progress Tracker

- ✅ Python basics
- ✅ Control flow
- ✅ Data structures
- ✅ Functions
- ✅ Loops
- ✅ Object-oriented programming
- ✅ Exception handling
- ✅ Modules and API fundamentals
- ✅ Beginner projects
- 🔄 File handling
- 🔄 Learning notes
- 🔄 Automated tests
- 🔄 Intermediate projects

## 🗺️ Roadmap

- [ ] Complete the file-handling module
- [ ] Add learning notes for each major topic
- [ ] Implement the `urllib` API example
- [ ] Add tests for reusable functions
- [ ] Add automated code-quality checks
- [ ] Add intermediate projects
- [ ] Add SQLite examples
- [ ] Explore Pandas and data analysis
- [ ] Explore Flask or FastAPI
- [ ] Add more API integrations

## 🤝 Contributing

This is primarily a personal learning repository, but suggestions, corrections, and educational improvements are welcome.

1. Fork the repository.
2. Create a branch for your change.
3. Add or improve an example.
4. Run `python -m compileall .`.
5. Commit your change with a clear message.
6. Open a pull request describing what you changed.

Please keep examples beginner-friendly, explain the learning objective, and avoid adding unnecessary dependencies.

## 📚 Resources

- [Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Real Python](https://realpython.com/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abdul Rehman**

- GitHub: [@AbdulRehman393](https://github.com/AbdulRehman393)
- Repository: [python-mastery](https://github.com/AbdulRehman393/python-mastery)

## ⭐ Support

If this repository helps you learn Python, consider starring it, sharing it with other learners, or opening an issue with suggestions.

<div align="center">

### 🚀 Keep Learning, Keep Building

**[Start with the Basics](./01_basics/)** • **[Try the Exercises](./09_mini-exercises/)** • **[Explore the Projects](./11_projects/)**

---

*Built with ❤️ and lots of ☕ by Abdul Rehman*

*Last updated: September 19, 2026*

</div>
