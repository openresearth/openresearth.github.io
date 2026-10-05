# 0. Setup

:::{admonition} Overview
:class: ore-overview

**Time:** 15 min

**Questions**
- How do I get Python and Jupyter running on my computer?

**Objectives**
- Install Python with the packages used in this module, or open Google Colab.
- Download the example dataset.
:::

## Option A: Google Colab (no installation)

[Google Colab](https://colab.research.google.com/) runs Python notebooks in your
browser with a Google account. Everything in this module works there.

1. Open <https://colab.research.google.com/> and click **New notebook**.
2. Upload the dataset using the folder icon on the left.

## Option B: Install on your computer (recommended for regular use)

1. Install **[Miniforge](https://github.com/conda-forge/miniforge#install)**, a free Python distribution.
2. Open **Miniforge Prompt** (Windows) or a terminal (macOS/Linux) and run:

   ```bash
   conda create -n geopy python=3.12 jupyterlab pandas matplotlib
   conda activate geopy
   jupyter lab
   ```

3. JupyterLab opens in your browser. Click **Python 3** under *Notebook* to start.

The next time, you only need:

```bash
conda activate geopy
jupyter lab
```

## Download the data

Download {download}`rock-samples.csv <data/rock-samples.csv>` and save it in the
same folder as your notebook. It is a small, **synthetic** dataset made for
teaching: ten rock samples with major-element oxides in weight percent (wt%).

:::{admonition} Key points
:class: ore-keypoints
- Colab needs no installation; Miniforge gives you Python on your own computer.
- Keep your notebook and data file in the same folder.
:::
