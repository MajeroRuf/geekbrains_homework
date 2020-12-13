def user_info(**kwargs):
    return kwargs


user = {'name': 'Konstantin',
        'surname': 'Overin',
        'sity_r': 'Kaluga',
        'year_b': 1981,
        'phone': '89051234567',
        'email': 'rufko@yandex.ru'}

user_data = user_info(**user)
print(f'Данные пользователя: Ф.И.О: {user_data.get("surname")} {user_data.get("name")} '
      f'Год рождения: {user_data.get("year_b")} Город рождения: {user_data.get("sity_r")} '
      f'Email: {user_data.get("email")} Телефон: {user_data.get("phone")}')

def user_info(name, surname, year_b, sity_r, email, phone):
    a = dict()
    a.update(user)
    return a


user = {'name': 'Konstantin',
        'surname': 'Overin',
        'sity_r': 'Kaluga',
        'year_b': 1981,
        'phone': '89051234567',
        'email': 'rufko@yandex.ru'}

user_data = user_info(**user)

print(f'Данные пользователя: Ф.И.О: {user_data.get("surname")} {user_data.get("name")} '
      f'Год рождения: {user_data.get("year_b")} Город рождения: {user_data.get("sity_r")} '
      f'Email: {user_data.get("email")} Телефон: {user_data.get("phone")}')