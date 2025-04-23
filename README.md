# LOVEStackInterpreter

<!-- # Short Description -->

LOVE Stack Interpreter is an interpreter for the unique stack-based programming language "LOVE". This project includes a core interpreter implemented in Python and an HTML/JavaScript-based frontend that allows you to interactively execute and visualize LOVE programs in your browser.

<!-- # Badges -->

[![Github issues](https://img.shields.io/github/issues/Accord33/LOVEStackInterpreter)](https://github.com/Accord33/LOVEStackInterpreter/issues)
[![Github forks](https://img.shields.io/github/forks/Accord33/LOVEStackInterpreter)](https://github.com/Accord33/LOVEStackInterpreter/network/members)
[![Github stars](https://img.shields.io/github/stars/Accord33/LOVEStackInterpreter)](https://github.com/Accord33/LOVEStackInterpreter/stargazers)
[![Github top language](https://img.shields.io/github/languages/top/Accord33/LOVEStackInterpreter)](https://github.com/Accord33/LOVEStackInterpreter/)
[![Github license](https://img.shields.io/github/license/Accord33/LOVEStackInterpreter)](https://github.com/Accord33/LOVEStackInterpreter/)

[Japanese Version](./README.ja.md)

# Demo

![Demo](img/screenshot.png)

# Advantages

*   **Unique Programming Language "LOVE":** A unique stack-based language consisting of 8 simple instructions (`L`, `O`, `V`, `E`, `C`, `R`, `-`, `[`, `]`).
*   **Interactive Web Execution Environment:** The frontend, built with HTML/JavaScript, allows you to write LOVE programs in your browser and visually check the execution steps.
    *   Real-time display of the stack state
    *   Adjustable execution speed (delay setting)
    *   Step-by-step execution control (Run/Stop)
*   **Python Interpreter:** The core interpreter logic is implemented in Python and can also be run from the command line.
*   **Learning and Educational Purposes:** Suitable as a teaching material for learning the operating principles of stack-based languages and the mechanisms of interpreters.

# Installation

### 1. Web Page (Recommended)
The easiest and most interactive way.
1. Access [lovestackinterpreter.accord33.org](https://lovestackinterpreter.accord33.org).
2. Enter the LOVE program in the left text area.
3. Optionally, set the delay time (in milliseconds) between execution steps using "Delay (ms)".
4. Click the "Run" button to start execution.
5. Check the changes in the stack state in the "Stack" area on the right and the output results from the `V` instruction in the "Output" area.
6. You can interrupt the execution with the "Stop" button.

**Sample Program:**

```
LLOO[ROOOOR-]E[ROOOOOOOOR-]EV
```

This outputs the ASCII codes 72 ('H') and 105 ('i').

### 2. Python Interpreter

You can also run the interpreter directly from the command line.

1.  Open a terminal and navigate to the `python` directory.
2.  Run `main.py`.
    ```bash
    python main.py
    ```
3.  The LOVE program written in the `prg` variable within `main.py` will be executed, and the output from the `V` instruction will be displayed in the terminal. In debug mode (`DEBUG = True`), the stack state at each step will also be displayed.

# Grammar

The LOVE language operates as a stack machine. There are 8 instructions to manipulate data on the stack.

| Instruction | Description                                                               |
| :---------- | :------------------------------------------------------------------------ |
| `L`         | Push `0` onto the stack.                                                  |
| `O`         | Increment (+1) the top element of the stack.                              |
| `V`         | Pop the top element of the stack and output the character corresponding to its ASCII code. |
| `E`         | Pop and discard the top element of the stack.                             |
| `C`         | Duplicate the top element of the stack and push it.                       |
| `R`         | Swap the positions of the top two elements of the stack.                  |
| `-`         | Decrement (-1) the top element of the stack.                              |
| `[`         | If the top element of the stack is `0`, jump to the corresponding `]`.      |
| `]`         | If the top element of the stack is not `0`, jump back to the corresponding `[`. |

*(Spaces, tabs, and newlines are ignored)*

# Contributors

- [Accord33](https://github.com/Accord33)

<!-- CREATED_BY_LEADYOU_README_GENERATOR -->