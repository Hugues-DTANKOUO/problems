# Problems

Welcome to the **Problems** repository! This is a learning project focused on algorithm implementation and problem-solving. The application provides a web interface for practicing coding problems with immediate feedback through automated tests.

---

## 📚 **Project Overview**

The **Problems** repository currently offers:
- **Two Core Problems:** Anagram checking and the Knapsack problem
- **Web Interface:** A simple, clean interface for viewing problems and their descriptions
- **Code Testing:** Basic test validation for submitted solutions
- **Problem Documentation:** Markdown-based problem descriptions with examples

---

## ⚙️ **Current Implementation**

1. **Problem Structure:**
   - Each problem is self-contained with its implementation and tests
   - Problems are categorized by difficulty (Easy/Medium)
   - Test cases validate core functionality

2. **Web Interface:**
   - FastAPI backend with Jinja2 templates
   - Problems are displayed with Markdown formatting
   - Basic routing between problems and documentation

---

## 🛠 **Technology Stack**

- **Backend:**
  - Python 3.10+
  - FastAPI for the web framework
  - Pytest for test cases

- **Frontend:**
  - HTML/CSS for layout and styling
  - Basic JavaScript for interactivity
  - Markdown rendering for problem descriptions

- **Development Tools:**
  - Poetry for dependency management
  - Ruff for linting
  - MyPy for type checking

---

## 🚀 **Getting Started**

### 1. Prerequisites
You need Python 3.10 or later and Poetry. Install Poetry using:
```bash
curl -sSL https://install.python-poetry.org | python3
```

### 2. Clone the Repository
```bash
git clone https://github.com/Hugues-DTANKOUO/problems.git
cd problems
```

### 3. Install Dependencies
```bash
poetry install
```

### 4. Development Server
Start the local development server:
```bash
poetry run server
```

### 5. Local Access
Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📂 **Available Problems**

Currently, four problems are implemented:

1. **Anagram Checker** (Easy)
   - String comparison problem
   - [View Implementation](/src/problems/anagram.py)

2. **Palindrome Checker** (Easy)
   - String pattern matching problem
   - [View Implementation](/src/problems/palindrome.py)

3. **Knapsack Problem** (Medium)
   - Classic optimization problem
   - [View Implementation](/src/problems/knapsack.py)

4. **N Queens Puzzle** (Hard)
   - Chess board placement problem
   - [View Implementation](/src/problems/nqueens.py)

---

## 🤝 **Contributing**

Contributions are welcome! See our [Contributing Guide](CONTRIBUTING.md) for details about:
- Project setup
- Development workflow
- Code style guidelines
- Testing requirements

Ways to contribute:
- Implementing new problems
- Improving existing problems
- Enhancing documentation
- Adding tests
- Fixing bugs

---

## 🧑‍💻 **About the Author**

Maintained by **Hugues Dtankouo**, a Senior Full Stack Developer with extensive Python experience.

📧 **Contact:** [huguesdtankouo@gmail.com](mailto:huguesdtankouo@gmail.com)  
🔗 **LinkedIn:** [Hugues Dtankouo](https://www.linkedin.com/in/dtankouo)  
🔗 **GitHub:** [Hugues-DTANKOUO](https://github.com/Hugues-DTANKOUO)  

---

## 📄 **License & Documentation**

- **License:** [MIT License](LICENSE)
- **Change Log:** [CHANGELOG.md](CHANGELOG.md)

---

## 🚧 **Project Status**

This is an early-stage project with basic functionality implemented. Future plans include:
- User authentication
- More problem categories
- Enhanced UI/UX
- Progress tracking
- Community features

Contributions and feedback are highly appreciated!

---

## 🎯 **Current Focus**

The project is currently focused on:
1. Stabilizing core functionality
2. Improving test coverage
3. Enhancing documentation
4. Adding new problems

---

![screenshot](/src/problems/static/images/problems-screenshot.png)