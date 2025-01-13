# Problems

Welcome to the **Problems** repository! This project is a collection of programming challenges designed to help developers improve their coding skills through hands-on exercises. With an integrated code editor, detailed problem descriptions, and automated test cases, this platform is ideal for learning and practicing algorithms and problem-solving.

---

## 📚 **Project Overview**

The **Problems** repository allows users to solve various coding challenges with the following features:
- **Detailed Problem Descriptions:** Each challenge includes a clear problem statement with examples.
- **Integrated Code Editor:** A browser-based code editor (powered by **CodeMirror**) to write and test your solutions.
- **Automated Test Cases:** Each challenge runs predefined tests to verify the correctness of your code.
- **Instant Feedback:** Get real-time results in the interactive console.

---

## ⚙️ **How It Works**

1. **Choose a Problem:**
   Browse the available challenges and select one based on its difficulty (Easy, Medium, Hard).

2. **Write Your Code:**
   Use the built-in editor

3. **Test Your Solution:**
   - Click the "Test" button to evaluate your solution.
   - The results of the tests (pass/fail) are displayed in the console output.

4. **Iterate and Improve:**
   Debug and improve your solution until it passes all test cases.

---

## 🛠 **Technology Stack**

- **Backend:**
  - Python (FastAPI/Jinja-based for handling API requests and running Python code).
  - Pytest for managing test cases and validating user solutions.

- **Frontend:**
  - HTML, CSS, JavaScript
  - **CodeMirror**: A rich text editor for code with Python syntax support.
  - Markdown rendering for problem descriptions.

- **Dependency Management:**
  - **Poetry**: For managing Python dependencies and virtual environments.

---

## 🚀 **Getting Started**

### 1. Prerequisites
Ensure that you have **Poetry** installed. If not, install it using:
```bash
curl -sSL https://install.python-poetry.org | python3
```
or refer to the official Poetry [installation guide](https://python-poetry.org/docs/#installation).

### 2. Clone the Repository
Clone the project from GitHub:
```bash
git clone https://github.com/Hugues-DTANKOUO/problems.git
cd problems
```

### 3. Install Dependencies
Use Poetry to install all dependencies:
```bash
poetry install
```

### 4. Start the Server
Run the development server:
```bash
poetry run server
```

### 5. Access the Platform
Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Available Problems

Here are the problems currently available in this repository:

1. **Anagram**
   - [View Problem](/src/problems/anagram.py)

2. **Knapsack**
   - [View Problem](/src/problems/knapsack.py)

---

## 🧑‍💻 **About the Author**

This repository is maintained by **Hugues Dtankouo**, a highly skilled **Senior Full Stack Developer** with over 7 years of professional experience in Python, web development, and software engineering.

### **Professional Highlights:**
- Proficient in Python frameworks like FastAPI, Django, and Flask.
- Experienced in frontend technologies such as Angular and React.
- Holder of multiple certifications, including **PCPP1 (Python Certified Professional Programmer)** and cloud-related certifications.
- Adept in Agile methodologies, including SAFe and Scrum frameworks.
- A Python trainer for companies, Hugues has successfully trained over 50 people across multiple countries through his social media outreach and professional programs.

Hugues is a dedicated professional who emphasizes high-quality standards, operational efficiency, and a strong focus on problem-solving.

📧 **Contact:** [huguesdtankouo@gmail.com](mailto:huguesdtankouo@gmail.com)  
🔗 **LinkedIn:** [Hugues Dtankouo](https://www.linkedin.com/in/dtankouo)  
🔗 **GitHub:** [Hugues-DTANKOUO](https://github.com/Hugues-DTANKOUO)  
🔗 **Facebook:** [Hugues Dtankouo](https://www.facebook.com/ing.hugues.dtankouo) (Over 20,000 followers)

---

## 🌟 **Contributing**

We welcome contributions from the community! Here's how you can contribute:

1. Fork the repository:
   ```bash
   git fork https://github.com/Hugues-DTANKOUO/problems.git
   ```

2. Create a feature branch:
    ```bash
    git checkout -b feature/new-feature
    ```

3. Commit your changes:
    ```bash
    git commit -m "Add a new feature"
    ```

4. Push to the branch
    ```bash
    git push origin feature/new-feature
    ```

5. Open a pull request on the GitHub repository

---

## 📄 **License**

This project is licensed under the **MIT License**. For more details, see the [LICENSE](LICENSE) file included in the repository.

---

## 🎉 **Enjoy Solving Problems**

Thank you for exploring this repository. We hope it helps you sharpen your programming skills and provides a fun, engaging way to tackle coding challenges.

Happy coding! 🚀

![screenshot](/src/problems/static/images/problems-screenshot.png)