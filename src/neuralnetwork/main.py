import asyncio
import sys
import json
from src.factories import get_repository
from src.services.database import DBFighter, Repository
from neurotrain import svm_weights

async def calculate_probability(fighter1: DBFighter, fighter2: DBFighter, svm_weights):
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

    #Альтернативный вид с прямым испрользованием весов
    # age_weight = 1.1988397511564817
    # weight_weight = -0.20566306520909716
    # height_weight = -0.10988991979202933
    # span_weight = 0.07760138349250933
    # wins_weight = -0.2601286961343403
    # wkc_weight = -0.33153297315333896
    # wsc_weight = 0.5236474289291326
    # wjdc_weight = 0.2744404237376621
    # defeats_weight = 0.01640528134506658
    # dkc_weight = -1.3177968538027653
    # dsc_weight = -2.220446049250313e-16
    # djdc_weight = 1.0849840035592986

    total_score1 = (
            age1 * age_weight +
            height1 * height_weight +
            weight1 * weight_weight +
            span1 * span_weight +
            wins_count1 * wins_weight +
            wkc1 * wkc_weight +
            wsc1 * wsc_weight +
            wjdc1 * wjdc_weight -
            defeats_count1 * defeats_weight -
             dkc1 * dkc_weight -
             dsc1 * dsc_weight -
             djdc1 * djdc_weight
    )

    total_score2 = (
            age2 * age_weight +
            height2 * height_weight +
            weight2 * weight_weight +
            span2 * span_weight +
            wins_count2 * wins_weight +
            wkc2 * wkc_weight +
            wsc2 * wsc_weight +
            wjdc2 * wjdc_weight -
            defeats_count2 * defeats_weight -
             dkc2 * dkc_weight -
             dsc2 * dsc_weight -
             djdc2 * djdc_weight
    )

    total_score = total_score1 + total_score2
    probability_fighter1 = total_score1 / total_score *100
    probability_fighter2 = total_score2 / total_score *100

    return probability_fighter1, probability_fighter2

# ЭТО ТОЛЬКО ДЛЯ ТЕСТИРОВАНИЯ!!
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
#             probability_fighter1, probability_fighter2 = await calculate_probability(fighter1, fighter2, svm_weights)
#
#             callback_function(first_fighter_name, second_fighter_name, winner, probability_fighter1,
#                               probability_fighter2)
#
#             predicted_winner = first_fighter_name if sum((probability_fighter1)) > sum((probability_fighter2)) else second_fighter_name
#
#             if (predicted_winner == first_fighter_name and winner == 1) or (predicted_winner == second_fighter_name and winner == 2):
#                 correct_predictions += 1

#     print("\nУгадано: {} из {}".format(correct_predictions, total_fights))
#     print("Не угадано: {} из {}".format(total_fights - correct_predictions, total_fights))
#
#
# async def main():
#     def my_callback_function(first_fighter_name, second_fighter_name, winner, probability_fighter1,
#                              probability_fighter2):
#         print(f"\nБойцы: {first_fighter_name} vs {second_fighter_name}")
#         print("\nВероятность победы для {}: {:.2f}%".format(first_fighter_name, probability_fighter1[0]))
#         print("Вероятность победы для {}: {:.2f}%".format(second_fighter_name, probability_fighter2[0]))
#         print("Победитель: {}".format(first_fighter_name if winner == 1 else second_fighter_name))
#     json_file_path = "winners.json"
#     await process_fights(json_file_path, my_callback_function)

async def main():
    repo: Repository = get_repository()
    fighter1: DBFighter = await repo.fighter.get_by_name("Келвин Гастелум")  #сюда первого бойца
    fighter2: DBFighter = await repo.fighter.get_by_name("Шон Брэди")  #сюда второго бойца

    probability_fighter1, probability_fighter2 = await calculate_probability(fighter1, fighter2, svm_weights)

    print("\nВероятность победы для {}: {:.2f}%".format(fighter1.name, probability_fighter1[0]))
    print("Вероятность победы для {}: {:.2f}%".format(fighter2.name, probability_fighter2[0]))


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

