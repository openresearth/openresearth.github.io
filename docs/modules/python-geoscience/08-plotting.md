# 8. Plotting

:::{admonition} Overview
:class: ore-overview

**Teaching:** 20 min · **Exercises:** 15 min

**Questions**
- How do I make a figure from my data?

**Objectives**
- Make line and scatter plots with matplotlib.
- Label axes and save a figure to a file.
:::

## Importing matplotlib

[matplotlib](https://matplotlib.org/) is the most widely used plotting library
in Python.

```python
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("rock-samples.csv")
```

## A line plot

```python
depth_m = [0, 10, 20, 30, 40]
temperature_c = [25, 26.1, 27.3, 28.2, 29.4]

plt.plot(temperature_c, depth_m, marker="o")
plt.gca().invert_yaxis()          # depth increases downwards
plt.xlabel("Temperature (°C)")
plt.ylabel("Depth (m)")
plt.show()
```

## A scatter plot of geochemical data

A total alkali–silica (TAS) style plot compares SiO₂ with Na₂O + K₂O:

```python
data["total_alkali"] = data["Na2O"] + data["K2O"]

plt.scatter(data["SiO2"], data["total_alkali"])
plt.xlabel("SiO$_2$ (wt%)")
plt.ylabel("Na$_2$O + K$_2$O (wt%)")
plt.title("Total alkalis vs silica")
plt.show()
```

## Colouring by group

Loop over each rock type and plot it separately so it gets its own colour and
legend entry:

```python
for rock in data["rock_type"].unique():
    subset = data[data["rock_type"] == rock]
    plt.scatter(subset["SiO2"], subset["total_alkali"], label=rock)

plt.xlabel("SiO$_2$ (wt%)")
plt.ylabel("Na$_2$O + K$_2$O (wt%)")
plt.legend()
plt.savefig("tas-plot.png", dpi=300)
```

`savefig()` writes the figure to a file you can use in reports and papers.

::::{admonition} Exercise: Harker diagram
:class: ore-challenge

Make a scatter plot of MgO (y-axis) against SiO₂ (x-axis), with labelled
axes, and save it as `harker-mgo.png`. How does MgO change as SiO₂ increases?

:::{dropdown} Solution
```python
plt.scatter(data["SiO2"], data["MgO"])
plt.xlabel("SiO$_2$ (wt%)")
plt.ylabel("MgO (wt%)")
plt.savefig("harker-mgo.png", dpi=300)
```

MgO decreases as SiO₂ increases, the typical trend in a magmatic
differentiation series.
:::
::::

:::{admonition} Key points
:class: ore-keypoints
- `import matplotlib.pyplot as plt` loads matplotlib.
- `plt.plot()` draws lines; `plt.scatter()` draws points.
- Always label axes with units.
- `plt.savefig()` saves the figure to a file.
:::

## What next?

You have finished the module. To go further:

- [Software Carpentry: Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder/)
- [Earth and Environmental Data Science (Columbia University)](https://earth-env-data-science.github.io/)
- [PyGMT tutorials](https://www.pygmt.org/latest/tutorials/index.html) for maps
