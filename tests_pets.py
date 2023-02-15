from API import PetFriends
from Settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()


# Test №1
def test_get_api_key_with_valid_mail_and_invalid_password(email=valid_email, password=invalid_password):
    """Проверяем запрос с верным email и неверным паролем."""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
    print(f'Статус {status} для теста с неправильным паролем')

# Test №2
def test_get_api_key_with_invalid_email_and_valid_password(email=invalid_email, password=valid_password):
    """Проверяем запрос с неверным email и верным паролем."""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
    print(f'Статус {status} для теста с неправильным email')

# Test №3
def test_get_api_key_with_wrong_email_and_wrong_password(email=invalid_email, password=invalid_password):
    """Проверяем запрос с неверным email и паролем."""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
    print(f'Статус {status} для теста с неправильным email и паролем')


# Test №4
def test_add_pet_with_valid_data_without_photo(name='Безликий кот', animal_type='кот', age='1'):
    """Проверяем возможность добавления нового питомца без фото"""
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

# Test №5
def test_add_pet_with_only_numbers(name='1467458', animal_type='567976', age='1'):
    """Проверяем возможность ввода чисел в name и animal_type"""
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    print('Пользователь может вводит числа в текстовые строки')

# Test №6
def test_add_pet_with_only_letters(name='Вася', animal_type='кот', age='укрпвп'):
    """Проверяем возможность ввода букв в age"""
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['age'] == age
    print('Пользователь может вводит буквы в числовые строки')

# Test №7
def test_add_pet_with_another_language(name='Basil', animal_type='kitty', age='5'):
    """Проверяем возможность ввода букв в age"""
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    print('Пользователь может вводит данные на другом языке')

# Test №8
def test_add_pet_with_incorrect_symbols(name='💎♕  𝐰𝐄𝓘Řｄ Ｔ𝑒Ж𝕥  💎✋', animal_type='kitty', age='5'):
    """Проверяем возможность ввода букв в age"""
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    print('Пользователь может вводит данные с некорректными символами ')

# Test №9
def test_add_photo_at_pet(pet_photo='photos/minipig.jpg'):
    """Проверяем возможность добавления фотографии питомца отдельно"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, api_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(api_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(api_key, my_pets['pets'][0]['id'], pet_photo)
        _, my_pets = pf.get_list_of_pets(api_key, 'my_pets')

        assert status == 200
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
        print(f'\n фото добавлено {result}')
    else:
        raise Exception('Питомцы отсутствуют')

# Test №10
def test_add_pet_with_negative_num(name='Вася', animal_type='кот', age='-150'):
    """Проверяем возможность ввода отрицательных значений в age"""
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['age'] == age
    print('Пользователь может вводит отрицательные значения в числовые строки')



