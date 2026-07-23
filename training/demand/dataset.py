from preprocess import load_dataset, clean_dataset
from feature_engineering import create_features


def load_training_data():
    """
    Returns:
        X -> Features
        y -> Target labels
    """

    df = load_dataset()
    df = clean_dataset(df)
    df = create_features(df)

    X = df.drop(columns=["target"])
    y = df["target"]

    return X, y