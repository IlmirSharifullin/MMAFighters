from src.services.database import DBFighter


def get_fighter_card(fighter: DBFighter):
    text = (f'{fighter.name}\n')
    text+=(f'Возраст - {fighter.age}\n' if fighter.age else '')
    text+=(f'Страна - {fighter.country}\n' if fighter.country else '')
    text+=(f'Базовый стиль - {fighter.base_style}\n' if fighter.base_style else '')
    text+=(f'Город - {fighter.city}\n' if fighter.city else '')
    text+=(f'Рост - {fighter.height} см\n' if fighter.height else '')
    text+=(f'Вес - {fighter.weight} кг\n' if fighter.weight else '')
    text+=(f'Весовая категория - {fighter.weight_category}\n' if fighter.weight_category else '')
    text+=(f'Промоушен - {fighter.promotion}\n' if fighter.promotion else '')
    text+=(f'Размах рук - {fighter.arm_span} см\n' if fighter.arm_span else '')
    text+=(f'----------\nКоличество побед - {fighter.wins_count}\nПобед нокаутом - {fighter.wins_knockouts_count}\n'
           f'Побед судейским решением - {fighter.wins_judges_decisions_count}'
           f'\nСабмишн побед - {fighter.wins_submissions_count}\n----------\nКоличество поражений - {fighter.defeats_count}'
           f'\nПоражений нокаутом - {fighter.defeats_knockouts_count}\nПоражений судейским решением - {fighter.defeats_judges_decisions_count}'
           f'\nСабмишн поражений - {fighter.defeats_submissions_count}')

    return text