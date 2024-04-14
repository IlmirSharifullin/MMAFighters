# import pandas as pd
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler
# from sklearn.feature_selection import SelectKBest, f_classif
#
# # Загрузка данных из файла
# data = pd.read_csv("data.csv")
#
# # Создание нового признака - отношение побед к поражениям
# data["win_loss_ratio"] = data["wins_count"] / (data["defeats_count"] + 1)  # Добавляем 1, чтобы избежать деления на ноль
#
# # Разделение данных на признаки (X) и целевую переменную (y)
# features = ["age", "weight", "height", "arm_span",
#             "wins_knockouts_count", "wins_submissions_count", "wins_judges_decisions_count",
#             "defeats_knockouts_count", "defeats_submissions_count", "defeats_judges_decisions_count",
#             "win_loss_ratio"]
# X = data[features]
# y = data["wins_count"]
#
# # Разделение данных на обучающий и тестовый наборы
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Нормализация признаков
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)
#
# # Отбор наиболее информативных признаков
# selector = SelectKBest(score_func=f_classif, k=5)  # Выберем 5 лучших признаков
# X_train_selected = selector.fit_transform(X_train_scaled, y_train)
# X_test_selected = selector.transform(X_test_scaled)
#
# # Создание и обучение модели градиентного бустинга
# model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
# model.fit(X_train_selected, y_train)
#
# # Предсказание результатов на тестовом наборе данных
# y_pred = model.predict(X_test_selected)
#
# # Оценка производительности модели с помощью кросс-валидации
# cv_results = cross_val_score(model, X_train_selected, y_train, cv=5)
# print("Cross-validated Accuracy:", cv_results.mean())
#
# # Оценка производительности модели
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy with feature selection and cross-validation:", accuracy)
# #
#
#
#
# from sklearn.model_selection import GridSearchCV
# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
# #
# # # # Создание пустой модели градиентного бустинга
# # # model = GradientBoostingClassifier()
# # #
# # # # Определение сетки гиперпараметров для перебора
# # # param_grid = {
# # #     'n_estimators': [50, 100, 150],
# # #     'learning_rate': [0.05, 0.1, 0.2],
# # #     'max_depth': [3, 5, 7]
# # # }
# # #
# # # # Поиск оптимальных гиперпараметров с помощью GridSearchCV
# # # grid_search = GridSearchCV(model, param_grid, cv=5)
# # # grid_search.fit(X_train_selected, y_train)
# # #
# # # # Получение лучших параметров и оценка производительности
# # # best_params = grid_search.best_params_
# # # best_model = grid_search.best_estimator_
# # # cv_accuracy = grid_search.best_score_
# # #
# # # # Обучение лучшей модели и оценка производительности на тестовом наборе данных
# # # best_model.fit(X_train_selected, y_train)
# # # test_accuracy = best_model.score(X_test_selected, y_test)
# # #
# # # print("Best Parameters:", best_params)
# # # print("Cross-validated Accuracy with Gradient Boosting:", cv_accuracy)
# # # print("Accuracy with Gradient Boosting on Test Data:", test_accuracy)
# # #
# # # # Теперь попробуем другую модель, например, метод опорных векторов (SVM)
# # #
# # Создание пустой модели SVM
# svm_model = SVC()
#
# # Определение сетки гиперпараметров для перебора
# svm_param_grid = {
#     'C': [0.1, 1, 10],
#     'gamma': ['scale', 'auto'],
#     'kernel': ['linear', 'rbf']
# }
#
# # Поиск оптимальных гиперпараметров для SVM
# svm_grid_search = GridSearchCV(svm_model, svm_param_grid, cv=5)
# svm_grid_search.fit(X_train_selected, y_train)
#
# # Получение лучших параметров и оценка производительности
# best_svm_params = svm_grid_search.best_params_
# best_svm_model = svm_grid_search.best_estimator_
# svm_cv_accuracy = svm_grid_search.best_score_
#
# # Обучение лучшей модели SVM и оценка производительности на тестовом наборе данных
# best_svm_model.fit(X_train_selected, y_train)
# svm_test_accuracy = best_svm_model.score(X_test_selected, y_test)
#
# print("Best Parameters for SVM:", best_svm_params)
# print("Cross-validated Accuracy with SVM:", svm_cv_accuracy)
# print("Accuracy with SVM on Test Data:", svm_test_accuracy)
# # #
# # # # Теперь попробуем еще одну модель, например, k-ближайших соседей (KNN)
# # #
# # # # Создание пустой модели KNN
# # # knn_model = KNeighborsClassifier()
# # #
# # # # Определение сетки гиперпараметров для перебора
# # # knn_param_grid = {
# # #     'n_neighbors': [3, 5, 7, 9],
# # #     'weights': ['uniform', 'distance'],
# # #     'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
# # # }
# # #
# # # # Поиск оптимальных гиперпараметров для KNN
# # # knn_grid_search = GridSearchCV(knn_model, knn_param_grid, cv=5)
# # # knn_grid_search.fit(X_train_selected, y_train)
# # #
# # # # Получение лучших параметров и оценка производительности
# # # best_knn_params = knn_grid_search.best_params_
# # # best_knn_model = knn_grid_search.best_estimator_
# # # knn_cv_accuracy = knn_grid_search.best_score_
# # #
# # # # Обучение лучшей модели KNN и оценка производительности на тестовом наборе данных
# # # best_knn_model.fit(X_train_selected, y_train)
# # # knn_test_accuracy = best_knn_model.score(X_test_selected, y_test)
# # #
# # # print("Best Parameters for KNN:", best_knn_params)
# # # print("Cross-validated Accuracy with KNN:", knn_cv_accuracy)
# # # print("Accuracy with KNN on Test Data:", knn_test_accuracy)
# # #

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.model_selection import train_test_split
from src.factories import get_repository
from src.services.database import DBFighter, Repository
import asyncio
import sys


# Определение архитектуры нейронной сети
class FighterClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(FighterClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.softmax(out)
        return out


# Подготовка данных
async def prepare_data():
    repo: Repository = get_repository()
    fighters = await repo.fighter.get_all()  # Получаем всех бойцов из базы данных
    X = []  # Характеристики бойцов
    y = []  # Результаты боев

    for fighter1 in fighters:
        for fighter2 in fighters:
            if fighter1 != fighter2:
                # Создаем вектор характеристик бойцов
                features = [
                    fighter1.age, fighter1.weight, fighter1.height, fighter1.arm_span,
                    fighter1.weight_category, fighter1.base_style,
                    fighter2.age, fighter2.weight, fighter2.height, fighter2.arm_span,
                    fighter2.weight_category, fighter2.base_style
                ]
                X.append(features)

                # Определяем результат боя (1 - победа первого бойца, 0 - победа второго бойца)
                result = 1 if fighter1.wins_count > fighter2.wins_count else 0
                y.append(result)

    X = np.array(X)
    y = np.array(y)
    return X, y


# Разделение данных на обучающий и тестовый наборы
async def split_data():
    X, y = await prepare_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


# Обучение нейронной сети
async def train_neural_network():
    X_train, X_test, y_train, y_test = await split_data()

    input_size = X_train.shape[1]
    hidden_size = 64
    output_size = 2  # Два класса: победа первого бойца или второго

    model = FighterClassifier(input_size, hidden_size, output_size)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Преобразование данных в тензоры PyTorch
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.long)

    # Обучение модели
    for epoch in range(100):
        optimizer.zero_grad()
        outputs = model(X_train_tensor)
        loss = criterion(outputs, y_train_tensor)
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/100], Loss: {loss.item():.4f}')

    # Оценка модели
    with torch.no_grad():
        X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
        outputs = model(X_test_tensor)
        _, predicted = torch.max(outputs.data, 1)
        total = y_test.size
        correct = (predicted == y_test).sum().item()
        accuracy = correct / total
        print(f'Accuracy: {accuracy:.2f}')


# Запуск асинхронной функции
async def main():
    await train_neural_network()


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
