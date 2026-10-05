# 7. Reading tabular data

:::{admonition} Overview
:class: ore-overview

**Teaching:** 20 min · **Exercises:** 15 min

**Questions**
- How do I load a table of measurements into Python?
- How do I select and filter data?

**Objectives**
- Read a CSV file with the pandas library.
- Inspect, select and filter columns.
- Calculate summary statistics.
:::

## Importing a library

A **library** adds extra tools to Python. [pandas](https://pandas.pydata.org/)
works with tables. By convention it is imported as `pd`:

```python
import pandas as pd
```

## Reading a CSV file

Make sure {download}`rock-samples.csv <data/rock-samples.csv>` is in the same
folder as your notebook.

```python
data = pd.read_csv("rock-samples.csv")
data.head()
```

```output
  sample_id rock_type  latitude  longitude  SiO2  MgO  Na2O  K2O
0     RS-01    basalt     21.15      79.09  49.2  7.8   2.8  0.6
1     RS-02    basalt     21.18      79.12  50.1  7.1   3.0  0.7
2     RS-03  andesite     21.21      79.05  58.6  3.4   3.6  1.5
3     RS-04  andesite     21.24      79.01  60.2  2.9   3.8  1.8
4     RS-05    dacite     21.26      79.15  66.3  1.6   4.1  2.4
```

The table is called a **DataFrame**. `head()` shows the first five rows.

## Looking at the data

```python
data.shape        # (rows, columns)
data.columns      # column names
data.describe()   # summary statistics of numeric columns
```

## Selecting columns

```python
data["SiO2"]             # one column
data[["SiO2", "MgO"]]    # several columns
data["SiO2"].mean()      # average SiO2
```

## Filtering rows

```python
felsic = data[data["SiO2"] > 63]
print(felsic[["sample_id", "rock_type", "SiO2"]])
```

## Adding a new column

Calculations work on whole columns at once, with no loop needed:

```python
data["total_alkali"] = data["Na2O"] + data["K2O"]
```

::::{admonition} Exercise: Explore the dataset
:class: ore-challenge

1. How many samples are in the dataset?
2. What is the average MgO of the basalts?
3. Which sample has the highest total alkalis?

:::{dropdown} Solution
```python
print(len(data))

basalts = data[data["rock_type"] == "basalt"]
print(basalts["MgO"].mean())

data["total_alkali"] = data["Na2O"] + data["K2O"]
print(data.loc[data["total_alkali"].idxmax(), "sample_id"])
```

```output
10
7.833333333333333
RS-08
```
:::
::::

:::{admonition} Key points
:class: ore-keypoints
- `import pandas as pd` loads the pandas library.
- `pd.read_csv()` reads a CSV file into a DataFrame.
- `data["column"]` selects a column; `data[condition]` filters rows.
- Calculations on columns apply to every row at once.
:::
