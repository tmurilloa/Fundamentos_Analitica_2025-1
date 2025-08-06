#  example.py

"""Use example"""

# pylint: disable=import-error

import linear_regression  # type: ignore
import pandas as pd  # type: ignore


def main():
    """Main function."""

    # Load the data
    data = pd.read_csv("files/input/data.csv")
    X = data[["x1", "x2"]].values
    y = data["y"].values

    # Fit the model
    model = linear_regression.LinearRegression()
    model.fit(X, y)

    # Make predictions
    predictions = model.predict(X)

    for y_true, y_pred in zip(y, predictions):
        print(f"{y_true:8.4f}, {y_pred:8.4f}")


if __name__ == "__main__":
    main()
