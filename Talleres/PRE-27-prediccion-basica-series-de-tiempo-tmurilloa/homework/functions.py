import os

import numpy as np  #  type: ignore
import matplotlib.pyplot as plt  #  type: ignore
import pandas as pd  #  type: ignore

from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.stattools import acf, pacf  #  type: ignore
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf  #  type: ignore



def load_data():
    df = pd.read_csv("../files/input/sutter.csv")
    df = df.set_index("date")
    return df
    	
    
    
def plot_time_series(df, yt_col="yt_true"):
    """Time series plot."""

    plt.figure(figsize=(12, 4))

    # yt_real
    plt.plot(df[yt_col], ".-k", linewidth=0.5, label=yt_col)
    plt.grid(color="lightgray", linestyle="--", linewidth=0.5)

    cols = [col for col in df.columns if col.startswith("yt_pred")]
    colors = "rbgcmy"
    for i, col in enumerate(cols):
        plt.plot(df[col], ".-", color=colors[i], linewidth=0.7, label=col)

    # line division
    plt.plot(
        [len(df[yt_col]) - 24, len(df[yt_col]) - 24],
        [min(df[yt_col]), max(df[yt_col])],
        "--",
        linewidth=2,
    )

    # format
    plt.xticks(rotation=90)
    plt.xticks(range(0, len(df[yt_col]), 12), df[yt_col].index[::12])
    plt.yticks(fontsize=8)
    plt.xticks(fontsize=8)
    plt.legend()
    plt.show()
    
    
    


def acf_pacf_plots(z):
    """Correlation plot."""

    def format_plot():
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["bottom"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().collections[0].set_color("k")
        plt.gca().collections[1].set_color("gray")
        plt.grid(color="lightgray", linestyle="--", linewidth=0.5)
        plt.ylim(-1.03, 1.03)
        plt.yticks(fontsize=8)
        plt.xticks(fontsize=8)
        plt.title(plt.gca().get_title(), fontsize=8)

    plt.figure(figsize=(9, 3))

    plt.subplot(1, 2, 1)
    plot_acf(z, lags=24, ax=plt.gca(), color="k")
    format_plot()

    plt.subplot(1, 2, 2)
    plot_pacf(z, lags=24, ax=plt.gca(), color="k")
    format_plot()

    plt.show()
    
    
    
    
def add_linear_trend_component(df):
    """Add linear trend component to the dataframe."""
    df = df.assign(trend=list(range(len(df))))
    return df
    
    
    
def add_month_component(df):
    df = df.assign(month=df.index.str[5:7].astype(int))
    return df
    
    
    
    
def train_test_split(df, x_columns, y_column):
    """Train test split using last 24 observations as test set."""

    X_complete = df[x_columns]
    y_complete = df[y_column]

    X_train = df[x_columns].iloc[:-24]
    y_train = df[y_column].iloc[:-24]

    X_test = df[x_columns].iloc[-24:]
    y_test = df[y_column].iloc[-24:]

    return X_complete, y_complete, X_train, y_train, X_test, y_test
    
    
    
    
def compute_evaluation_metrics(df, y_true_column="yt_true"):
    """Compute metrics for train and test sets"""

    cols = [col for col in df.columns if "yt_pred" in col]

    y_train_true = df[y_true_column].iloc[:-24]
    y_test_true = df[y_true_column].iloc[-24:]

    results = {}
    results["Metrics"] = ["MSE Train", "MSE Test", "MAE Train", "MAE Test"]

    for col in cols:

        y_train_pred = df[col].iloc[:-24]
        y_test_pred = df[col].iloc[-24:]

        metrics = [
            mean_squared_error(y_train_true, y_train_pred),
            mean_squared_error(y_test_true, y_test_pred),
            mean_absolute_error(y_train_true, y_train_pred),
            mean_absolute_error(y_test_true, y_test_pred),
        ]

        results[col] = metrics

    results = pd.DataFrame(results)

    results = results.round(2)

    return results
    
    
    
    
def save_forecasts(df):
    """Save forecasts to a csv file."""

    if not os.path.exists("../files/output"):
        os.makedirs("../files/output")

    columns = [col for col in df.columns if col.startswith("yt_pred")]

    forecasts = df[columns].copy()

    if os.path.exists("../files/output/forecasts.csv"):
        saved_forecasts = pd.read_csv("../files/output/forecasts.csv", index_col=0)
        for col in forecasts.columns:
            saved_forecasts[col] = forecasts[col].values
        forecasts = saved_forecasts

    if "yt_true" not in forecasts.columns:
        forecasts["yt_true"] = df["yt_true"].values

    forecasts.to_csv("../files/output/forecasts.csv", index=True)
    
    
    
    
def save_metrics(metrics):
    """Save metrics to a csv file."""

    if not os.path.exists("../files/output"):
        os.makedirs("../files/output")

    if os.path.exists("../files/output/metrics.csv"):
        saved_metrics = pd.read_csv("../files/output/metrics.csv")
        for col in metrics.columns:
            saved_metrics[col] = metrics[col]
        metrics = saved_metrics

    metrics.to_csv("../files/output/metrics.csv", index=False)
    
    
    
    
def add_sin_cos_components(df):

    df = df.assign(sin_12m=np.sin(2 * np.pi * df.month / 12))
    df = df.assign(cos_12m=np.cos(2 * np.pi * df.month / 12))

    df = df.assign(sin_6m=np.sin(2 * np.pi * df.month / 6))
    df = df.assign(cos_6m=np.cos(2 * np.pi * df.month / 6))

    df = df.assign(sin_4m=np.sin(2 * np.pi * df.month / 4))
    df = df.assign(cos_4m=np.cos(2 * np.pi * df.month / 4))

    df = df.assign(sin_3m=np.sin(2 * np.pi * df.month / 3))
    df = df.assign(cos_3m=np.cos(2 * np.pi * df.month / 3))

    return df
    
    
    
def make_lagged_ts(df, p_max, y_column, fmt="lagged_{}m"):
    for i in range(1, p_max + 1):
        df[fmt.format(i)] = df[y_column].shift(i)
    return df
    
    
    
def make_yt_true_scaled(df, scaler):
    df["yt_true_scaled"] = scaler.fit_transform(df[["yt_true"]])
    return df
    
    
    
def remove_trend_and_cycle(df, yt_true_name="yt_true"):
    df[yt_true_name + "_d1d12"] = df[yt_true_name].diff(1).diff(12)
    return df