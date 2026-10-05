# 2. Variables

:::{admonition} Overview
:class: ore-overview

**Teaching:** 10 min · **Exercises:** 10 min

**Questions**
- How do I store a value so I can use it later?

**Objectives**
- Create variables and use them in calculations.
- Choose clear variable names.
:::

## Assigning values

A **variable** is a name that refers to a value. Use `=` to assign it.

```python
sample_id = "KA-01"
sio2 = 72.4        # SiO2 in wt%
depth_m = 125
```

Use the name anywhere you would use the value:

```python
print(sample_id, "has", sio2, "wt% SiO2")
```

```output
KA-01 has 72.4 wt% SiO2
```

## Updating variables

A variable keeps its value until you change it.

```python
depth_m = 125
depth_m = depth_m + 10   # drilled 10 m further
print(depth_m)
```

```output
135
```

## Naming rules

- Names can contain letters, digits and `_`, but **cannot start with a digit**.
- Names are case-sensitive: `MgO` and `mgo` are different variables.
- Prefer clear names with units: `depth_m` is better than `d`.

:::{note}
Notebook cells can be run in any order. If a result looks wrong, use
**Kernel → Restart & Run All** to run everything from the top.
:::

::::{admonition} Exercise: Sum of alkalis
:class: ore-challenge

A basalt has 2.9 wt% Na₂O and 0.8 wt% K₂O. Store each in a variable, then
calculate and print the total alkalis (Na₂O + K₂O).

:::{dropdown} Solution
```python
na2o = 2.9
k2o = 0.8
total_alkali = na2o + k2o
print(total_alkali)
```

```output
3.7
```
:::
::::

:::{admonition} Key points
:class: ore-keypoints
- `name = value` creates a variable.
- Variables can be reused and updated.
- Use clear, descriptive names, ideally including units.
:::
