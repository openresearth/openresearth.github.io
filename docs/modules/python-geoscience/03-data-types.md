# 3. Data types

:::{admonition} Overview
:class: ore-overview

**Teaching:** 15 min · **Exercises:** 10 min

**Questions**
- What kinds of data can Python store?
- How do I convert between them?

**Objectives**
- Recognise integers, floats, strings and booleans.
- Check a value's type with `type()`.
- Convert between types.
:::

## The four basic types

| Type | Name | Geoscience example |
|---|---|---|
| `int` | whole number | `number_of_samples = 24` |
| `float` | decimal number | `mgo = 8.25` |
| `str` | text (string) | `rock_type = "basalt"` |
| `bool` | True or False | `is_volcanic = True` |

Use `type()` to check:

```python
type(8.25)
```

```output
float
```

## Types matter

Numbers and text behave differently:

```python
print(2 + 3)
print("2" + "3")
```

```output
5
23
```

Adding a string to a number gives an error:

```python
"Depth: " + 120
```

```output
TypeError: can only concatenate str (not "int") to str
```

## Converting types

```python
depth_text = "120"          # e.g. read from a file
depth = float(depth_text)   # convert to a number
print(depth + 5)
print("Depth: " + str(depth) + " m")
```

```output
125.0
Depth: 120.0 m
```

An **f-string** is an easier way to put values in text:

```python
rock_type = "andesite"
sio2 = 58.6
print(f"The {rock_type} has {sio2} wt% SiO2")
```

```output
The andesite has 58.6 wt% SiO2
```

::::{admonition} Exercise: What type is it?
:class: ore-challenge

Predict the type of each value, then check with `type()`:

```python
"8.25"
8.25
8
8 > 5
```

:::{dropdown} Solution
`str` (it is in quotes), `float`, `int`, and `bool` (a comparison gives `True` or `False`).
:::
::::

:::{admonition} Key points
:class: ore-keypoints
- Every value has a type: `int`, `float`, `str` or `bool`.
- `int()`, `float()` and `str()` convert between types.
- f-strings (`f"...{value}..."`) put values into text.
:::
