# simple-ai

**simple-ai** is a small console-based Python experiment that simulates **evolutionary learning** without using matrices or external libraries.
It evolves small neural-like structures through mutation and selection, improving their performance generation by generation.

---

## 🌱 Overview

This project demonstrates how simple evolutionary principles can be applied to improve an algorithm over time.
Each generation:

1. Several candidates are mutated versions of the current best.
2. All candidates are tested against the given problem.
3. The best-performing one "survives" and reproduces for the next generation.

There are no fancy optimizations — everything is handled with pure Python lists and loops, so the process is intentionally slow but easy to understand.

---

## ⚙️ Usage

Run the program from the console:

```bash
python main.py
```

All key parameters (mutation rate, spread, number of hidden layers, etc.) can be found and modified directly inside `main.py`.

---

## 🧠 Concept

Instead of gradient descent or backpropagation, this program uses **evolution**:

* Random mutations explore the search space.
* A simple selection rule keeps only the best individual each generation.
* Over time, the population “learns” to perform better on the task.

This approach is inspired by **genetic algorithms** and **neuroevolution**, but implemented in a very minimal way.

---

## 🔍 Notes

* Written in **pure Python 3** (only import Math for rounding).
* Designed for experimentation and learning, not performance.
* Ideal for understanding how mutation and selection can replace traditional neural training methods.

---

## 🧩 Future Ideas

* Add matrix operations (NumPy) for speed.
* Introduce problems linke ping pong.
* Implement visualization of progress over generations.

---

disclaimer: README.md was written by AI
