# 4. Lists

:::{admonition} Overview
:class: ore-overview

**Teaching:** 15 min · **Exercises:** 10 min

**Questions**
- How do I store many values together?

**Objectives**
- Create lists and pick out items by position.
- Add items to a list and find its length.
:::

## Creating a list

A **list** holds several values in order, inside square brackets.

```python
depths_m = [10.5, 22.0, 35.2, 48.9, 60.1]   # core sample depths
minerals = ["quartz", "feldspar", "biotite"]
```

## Indexing: getting one item

Positions start at **0**, not 1.

```python
print(depths_m[0])    # first item
print(depths_m[-1])   # last item
```

```output
10.5
60.1
```

## Slicing: getting several items

`list[start:stop]` returns items from `start` up to, but not including, `stop`.

```python
depths_m[1:3]
```

```output
[22.0, 35.2]
```

## Changing a list

```python
minerals.append("muscovite")   # add to the end
print(minerals)
print(len(minerals))           # number of items
```

```output
['quartz', 'feldspar', 'biotite', 'muscovite']
4
```

Useful functions for lists of numbers: `min()`, `max()`, `sum()`.

```python
print(max(depths_m), sum(depths_m) / len(depths_m))
```

```output
60.1 35.339999999999996
```

Computers store decimal numbers approximately, so long tails like this are
normal. Use `round(value, 2)` to tidy them.

::::{admonition} Exercise: Core samples
:class: ore-challenge

Using `depths_m` above:
1. Print the second and third depths.
2. Add a new sample at 72.3 m.
3. Print the deepest sample and the total number of samples.

:::{dropdown} Solution
```python
print(depths_m[1:3])
depths_m.append(72.3)
print(max(depths_m), len(depths_m))
```

```output
[22.0, 35.2]
72.3 6
```
:::
::::

:::{admonition} Key points
:class: ore-keypoints
- Lists store ordered values: `[a, b, c]`.
- Indexing starts at 0; `-1` is the last item.
- `append()` adds an item and `len()` counts them.
:::
