import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.impute import SimpleImputer

data = pd.read_csv("data.csv")

features = ["age", "weight", "height", "arm_span", "wins_count",
            "wins_knockouts_count", "wins_submissions_count", "wins_judges_decisions_count",
            "defeats_count",
            "defeats_knockouts_count", "defeats_submissions_count", "defeats_judges_decisions_count",
            ]

X = data[features]
y = data["wins_count"]

# Обработка отсутствующих значений
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=17)

# Нормализация признаков
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Отбор наиболее информативных признаков
selector = SelectKBest(score_func=f_classif, k=len(features))  # Выберем 5 лучших признаков
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)

# Поиск оптимальных гиперпараметров
param_grid = {'C': [0.1, 1, 10, 100, 1000],
              'gamma': ['scale', 'auto', 0.1, 0.01, 0.001]}
svm_model = SVC(kernel='linear')
grid_search = GridSearchCV(svm_model, param_grid)
grid_search.fit(X_train_selected, y_train)

# Оптимальные гиперпараметры
# print("Best parameters:", grid_search.best_params_)

# Использование модели с лучшими параметрами
best_svm_model = grid_search.best_estimator_

# Предсказание результатов на тестовом наборе данных
y_pred = best_svm_model.predict(X_test_selected)

# Оценка производительности модели
accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy with SVM on Test Data:", accuracy)

svm_weights = (best_svm_model.coef_)
# print("Weights from SVM model:", svm_weights)

# Получение индексов отобранных признаков
selected_indices = selector.get_support(indices=True)
# Извлечение названий отобранных признаков
selected_features = [features[i] for i in selected_indices]

# Извлечение весов для отобранных признаков
selected_weights = svm_weights[0][selected_indices]

# Соединение названий признаков с их весами
feature_weights = list(zip(selected_features, selected_weights))

# print("Selected features by SVM model with corresponding weights:")
# for feature, weight in feature_weights:
#     print(f"Feature: {feature}, Weight: {weight}")
