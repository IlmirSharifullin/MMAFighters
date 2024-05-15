import asyncio
import sys
import json
from src.factories import get_repository
from src.services.database import DBFighter, Repository
from .neurotrain import svm_weights

async def calculate_probability(fighter1: DBFighter, fighter2: DBFighter):
    age1 = fighter1.age
    weight1 = fighter1.weight
    height1 = fighter1.height
    span1 = fighter1.arm_span
    wins_count1 = fighter1.wins_count
    wkc1 = fighter1.wins_knockouts_count
    wsc1 = fighter1.wins_submissions_count
    wjdc1 = fighter1.wins_judges_decisions_count
    defeats_count1 = fighter1.defeats_count
    dkc1 = fighter1.defeats_knockouts_count
    dsc1 = fighter1.defeats_submissions_count
    djdc1 = fighter1.defeats_judges_decisions_count

    age2 = fighter2.age
    weight2 = fighter2.weight
    height2 = fighter2.height
    span2 = fighter2.arm_span
    wins_count2 = fighter2.wins_count
    wkc2 = fighter2.wins_knockouts_count
    wsc2 = fighter2.wins_submissions_count
    wjdc2 = fighter2.wins_judges_decisions_count
    defeats_count2 = fighter2.defeats_count
    dkc2 = fighter2.defeats_knockouts_count
    dsc2 = fighter2.defeats_submissions_count
    djdc2 = fighter2.defeats_judges_decisions_count

    age_weight = svm_weights[0]
    weight_weight = svm_weights[1]
    height_weight = svm_weights[2]
    span_weight = svm_weights[3]
    wins_weight = svm_weights[4]
    wkc_weight = svm_weights[5]
    wsc_weight = svm_weights[6]
    wjdc_weight = svm_weights[7]
    defeats_weight = svm_weights[8]
    dkc_weight = svm_weights[9]
    dsc_weight = svm_weights[10]
    djdc_weight = svm_weights[11]
    # age_weight = 1.1986478377823848
    # weight_weight = -0.23364424902161374
    # height_weight = -0.1136839384776156
    # span_weight = 0.06893293397933253
    # wins_weight = -0.26352747361195306
    # wkc_weight = -0.3315750105958557
    # wsc_weight = 0.508491070682267
    # wjdc_weight = 0.266124682937833
    # defeats_weight = 0.023686426096847235
    # dkc_weight = -1.280754818381829
    # dsc_weight = 4.440892098500626e-16
    # djdc_weight = 1.07195549714112

    total_score1 = ((
            sum(age1 * age_weight )+
            sum(height1 * height_weight) +
            sum(weight1 * weight_weight) +
            sum(span1 * span_weight) +
            sum(wins_count1 * wins_weight) +
            sum(wkc1 * wkc_weight) +
            sum(wsc1 * wsc_weight) +
            sum(wjdc1 * wjdc_weight) -
            sum(defeats_count1 * defeats_weight) -
             sum(dkc1 * dkc_weight) -
             sum(dsc1 * dsc_weight) -
             sum(djdc1 * djdc_weight)
    ))

    total_score2 = ((
            sum(age2 * age_weight) +
            sum(height2 * height_weight) +
            sum(weight2 * weight_weight) +
            sum(span2 * span_weight) +
            sum(wins_count2 * wins_weight) +
            sum(wkc2 * wkc_weight) +
            sum(wsc2 * wsc_weight) +
            sum(wjdc2 * wjdc_weight) -
            sum(defeats_count2 * defeats_weight) -
             sum(dkc2 * dkc_weight) -
             sum(dsc2 * dsc_weight) -
             sum(djdc2 * djdc_weight)
    ))

    total_score = total_score1 + total_score2
    probability_fighter1 = total_score1 / total_score * 100
    probability_fighter2 = total_score2 / total_score * 100
    print('total1', total_score1)
    print('total2', total_score2)
    print('total', total_score)
    print('pr1', probability_fighter1)
    print('pr2', probability_fighter2)

    return probability_fighter1, probability_fighter2

#ДЛЯ ПРОВЕРКИ
# async def process_fights(json_file_path, callback_function):
#     repo: Repository = get_repository()
#     total_fights = 0
#     correct_predictions = 0
#     with open(json_file_path, 'r', encoding='utf-8') as file:
#         fights_data = json.load(file)
#         for fight in fights_data:
#             total_fights += 1
#             first_fighter_name = fight["first"]
#             second_fighter_name = fight["second"]
#             winner = fight["winner"]
#
#             fighter1 = await repo.fighter.get_by_name(first_fighter_name)
#             fighter2 = await repo.fighter.get_by_name(second_fighter_name)
#
#             # Ожидание выполнения корутины calculate_probability
#             probability_fighter1, probability_fighter2 = await calculate_probability(fighter1, fighter2)
#
#
#             callback_function(first_fighter_name, second_fighter_name, winner, probability_fighter1,
#                               probability_fighter2)
#
#             # Выбор предсказанного победителя
#             predicted_winner = first_fighter_name if ((probability_fighter1)) > ((probability_fighter2)) else second_fighter_name
#             # Проверка, соответствует ли предсказанный победитель действительному
#             if (predicted_winner == first_fighter_name and winner == 1) or (predicted_winner == second_fighter_name and winner == 2):
#                 correct_predictions += 1
#
#     # Вывод информации о количестве угаданных и неугаданных результатов
#     print("\nУгадано: {} из {}".format(correct_predictions, total_fights))
#     print("Не угадано: {} из {}".format(total_fights - correct_predictions, total_fights))
#
#
# async def main():
#     def my_callback_function(first_fighter_name, second_fighter_name, winner, probability_fighter1,
#                              probability_fighter2):
#         print(f"\nБойцы: {first_fighter_name} vs {second_fighter_name}")
#         print("\nВероятность победы для {}: {:.2f}%".format(first_fighter_name, probability_fighter1))
#         print("Вероятность победы для {}: {:.2f}%".format(second_fighter_name, probability_fighter2))
#         print("Победитель: {}".format(first_fighter_name if winner == 1 else second_fighter_name))
#     json_file_path = "winners.json"
#     await process_fights(json_file_path, my_callback_function)


async def main():
    repo: Repository = get_repository()
    fighter1: DBFighter = await repo.fighter.get_by_name("Келвин Гастелум")  #сюда первого бойца
    fighter2: DBFighter = await repo.fighter.get_by_name("Шон Брэди")  #сюда второго бойца

    probability_fighter1, probability_fighter2 = await calculate_probability(fighter1, fighter2)

    print("\nВероятность победы для {}: {:.2f}%".format(fighter1.name, probability_fighter1))
    print("Вероятность победы для {}: {:.2f}%".format(fighter2.name, probability_fighter2))


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

