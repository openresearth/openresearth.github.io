# 6. Conditionals

:::{admonition} Overview
:class: ore-overview

**Teaching:** 15 min · **Exercises:** 15 min

**Questions**
- How can my program make decisions?

**Objectives**
- Write `if`, `elif` and `else` statements.
- Combine conditions with `and` and `or`.
- Use conditionals inside a loop.
:::

## `if` statements

An `if` statement runs its body only when a condition is `True`.

```python
sio2 = 72.4

if sio2 > 63:
    print("felsic")
```

```output
felsic
```

## Comparisons

| Operator | Meaning |
|---|---|
| `>` `<` | greater than, less than |
| `>=` `<=` | greater or equal, less or equal |
| `==` | equal to (two `=` signs) |
| `!=` | not equal to |

## `elif` and `else`

Python checks each condition in order and runs the **first** one that is true.
Igneous rocks are often grouped by their silica content:

```python
sio2 = 49.8

if sio2 < 45:
    group = "ultramafic"
elif sio2 < 52:
    group = "mafic"
elif sio2 < 63:
    group = "intermediate"
else:
    group = "felsic"

print(group)
```

```output
mafic
```

## Combining conditions

```python
sio2 = 74.0
k2o = 4.6

if sio2 > 70 and k2o > 4:
    print("high-silica, potassic: possibly a granite or rhyolite")
```

## Conditionals inside loops

```python
samples = [43.2, 48.5, 57.9, 71.3]

for sio2 in samples:
    if sio2 < 52:
        print(sio2, "mafic or ultramafic")
    else:
        print(sio2, "intermediate or felsic")
```

```output
43.2 mafic or ultramafic
48.5 mafic or ultramafic
57.9 intermediate or felsic
71.3 intermediate or felsic
```

::::{admonition} Exercise: Count the felsic samples
:class: ore-challenge

Using the `samples` list above, count how many samples have SiO₂ greater
than 63 wt%.

:::{dropdown} Solution
```python
count = 0
for sio2 in samples:
    if sio2 > 63:
        count = count + 1
print(count)
```

```output
1
```
:::
::::

:::{admonition} Key points
:class: ore-keypoints
- `if`, `elif` and `else` choose which code runs.
- Only the first true branch runs.
- Use `==` to compare and `=` to assign.
- Conditionals inside loops let you sort or count data.
:::
