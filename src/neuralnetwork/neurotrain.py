import time
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("src\\neuralnetwork\\data.csv")

features = ["age", "weight", "height", "arm_span", "wins_count",
            "wins_knockouts_count", "wins_submissions_count", "wins_judges_decisions_count",
            "defeats_count",
            "defeats_knockouts_count", "defeats_submissions_count", "defeats_judges_decisions_count"]

columns_to_fill = ["age", "weight", "height", "arm_span"]
data[columns_to_fill] = data[columns_to_fill].fillna(data[columns_to_fill].mean())


X = data.drop(columns=["wins_count"])
y = data["wins_count"]

imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.31, random_state=60)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


selector = RFE(estimator=SVC(kernel='linear'), n_features_to_select=5)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)

svm_model = SVC(kernel='linear')
svm_model.fit(X_train_selected, y_train)

y_pred_svm = svm_model.predict(X_test_selected)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("Accuracy with SVM on Test Data:", accuracy_svm)


svm_weights = svm_model.coef_
print("Coefficients from SVM model:", svm_weights)


selector = RFE(estimator=SVC(kernel='linear'), n_features_to_select=5)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)


# Оценка того, какаие коэфиценты самые влиятельные. нашел в интернете
# rf_model = RandomForestClassifier()
# rf_model.fit(X_train_scaled, y_train)
# feature_importances = rf_model.feature_importances_
# print("Feature importances:", feature_importances)
