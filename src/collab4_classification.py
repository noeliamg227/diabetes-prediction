import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


def run_knn_classification(
    df: pd.DataFrame,
    target_col: str,
    k: int = 5
):
    """
    Train and evaluate a KNN classifier.

    Parameters
    ----------
    df : pd.DataFrame
        Aggregated dataframe with features and target
    target_col : str
        Name of the target variable column
    k : int
        Number of neighbors for KNN

    Returns
    -------
    model : KNeighborsClassifier
        Trained model
    metrics : dict
        Accuracy and classification report
    """

    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "report": classification_report(y_test, y_pred)
    }

    return model, metrics
