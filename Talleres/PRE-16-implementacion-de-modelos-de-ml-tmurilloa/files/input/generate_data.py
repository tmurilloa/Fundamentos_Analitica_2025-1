"""Generate artificial data for testing."""

# generate a file called "data.csv". The file has two independent variaibles,
# and a dependent variable. The relationship between the independent and
# dependent is lineal. The file has 20 rows. The independent variables
# follows a uniform distribution between 0 and 1.
# The dependent variable is the sum of the independent variables.
# The independent variable has normal noise with mean 0 and standard
# deviation 0.1.


import numpy as np  # type: ignore
import pandas as pd  # type: ignore

np.random.seed(0)

n = 20
x1 = np.random.uniform(0, 1, n)
x2 = np.random.uniform(0, 1, n)
y = x1 + x2 + np.random.normal(0, 0.1, n)

df = pd.DataFrame({"x1": x1, "x2": x2, "y": y})
df.to_csv("files/input/data.csv", index=False)
