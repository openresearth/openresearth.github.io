# 5. For loops

:::{admonition} Overview
:class: ore-overview

**Teaching:** 15 min · **Exercises:** 15 min

**Questions**
- How can I repeat the same task for every value?

**Objectives**
- Write a `for` loop over a list.
- Build up a result inside a loop.
- Use `range()` to loop a set number of times.
:::

## Repeating a task

Without a loop you would repeat yourself:

```python
print(10.5 * 3.281)
print(22.0 * 3.281)
print(35.2 * 3.281)
```

A **for loop** does the same work for every item in a list:

```python
depths_m = [10.5, 22.0, 35.2]

for depth in depths_m:
    depth_ft = depth * 3.281
    print(depth, "m =", round(depth_ft, 1), "ft")
```

```output
10.5 m = 34.5 ft
22.0 m = 72.2 ft
35.2 m = 115.5 ft
```

- The line ends with a colon `:`.
- The lines that repeat (the **body**) are **indented** by 4 spaces.
- `depth` takes each value of the list in turn.

## Building up a result

Start with an empty value before the loop and add to it each time:

```python
thicknesses_m = [2.5, 4.0, 1.2, 6.3]   # layer thicknesses
total = 0

for t in thicknesses_m:
    total = total + t

print("Total thickness:", total, "m")
```

```output
Total thickness: 14.0 m
```

## Looping with `range()`

`range(n)` gives the numbers 0 to n − 1.

```python
for year in range(2020, 2025):
    print("Field season", year)
```

```output
Field season 2020
Field season 2021
Field season 2022
Field season 2023
Field season 2024
```

::::{admonition} Exercise: Convert a list of oxides
:class: ore-challenge

These are FeO values in wt%. Make a new list with each value converted to
Fe₂O₃ by multiplying by 1.1113.

```python
feo = [8.1, 10.4, 6.7, 12.0]
```

:::{dropdown} Solution
```python
fe2o3 = []
for value in feo:
    fe2o3.append(round(value * 1.1113, 2))
print(fe2o3)
```

```output
[9.0, 11.56, 7.45, 13.34]
```
:::
::::

:::{admonition} Key points
:class: ore-keypoints
- `for item in collection:` repeats the indented body for every item.
- Indentation defines which lines are inside the loop.
- Start a total or an empty list before the loop, then update it inside.
:::
