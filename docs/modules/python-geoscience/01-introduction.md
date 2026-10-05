# 1. Introduction

:::{admonition} Overview
:class: ore-overview

**Teaching:** 10 min · **Exercises:** 10 min

**Questions**
- What is Python and why do geoscientists use it?
- How do I run Python code?

**Objectives**
- Run code in a Jupyter notebook cell.
- Use Python as a calculator and print results.
- Write comments in code.
:::

## Why Python?

Python is a free programming language that is easy to read and widely used in
the earth sciences. With it you can process thousands of samples in seconds,
repeat an analysis exactly, and make publication-quality figures. Many
geoscience tools are written in Python, such as
[PyGMT](https://www.pygmt.org/), [GemPy](https://www.gempy.org/) and
[ObsPy](https://www.obspy.org/).

## Running code in a notebook

A Jupyter notebook is made of **cells**. Type code into a cell and press
**Shift + Enter** to run it. The result appears below the cell.

```python
2 + 3
```

```output
5
```

## Python as a calculator

```python
# Density of granite in g/cm³ converted to kg/m³
2.65 * 1000
```

```output
2650.0
```

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` `-` | add, subtract | `10 - 4` | `6` |
| `*` `/` | multiply, divide | `7 / 2` | `3.5` |
| `**` | power | `10 ** 3` | `1000` |
| `//` | whole-number division | `7 // 2` | `3` |
| `%` | remainder | `7 % 2` | `1` |

## Printing and comments

`print()` shows a value. Everything after `#` is a **comment**: Python ignores
it, but it explains your code to other people (and to you, later).

```python
# Average crustal thickness in km
print("Continental crust is about", 35, "km thick")
```

```output
Continental crust is about 35 km thick
```

::::{admonition} Exercise: Unit conversion
:class: ore-challenge

A borehole is 1250 feet deep. One foot is 0.3048 m. Use Python to find the
depth in metres.

:::{dropdown} Solution
```python
1250 * 0.3048
```

```output
381.0
```
:::
::::

:::{admonition} Key points
:class: ore-keypoints
- Run a notebook cell with **Shift + Enter**.
- Python follows normal maths rules; `**` means "to the power of".
- Use `print()` to show values and `#` to write comments.
:::
