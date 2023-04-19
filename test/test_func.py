import pytest

from main import find_max, filter_, find_unique, lst_to_dict


@pytest.mark.parametrize("list_,expected", [
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
    ({'facebook': 10, 'yandex': 12, 'vk': 118, 'google': 9, 'email': 14, 'ok': 23}, 'vk'),
    ({'facebook': 75, 'yandex': 53, 'vk': 12, 'google': 0, 'email': 95, 'ok': 70}, 'email'),
    ({'facebook': 12, 'yandex': 45, 'vk': 500, 'google': 109, 'email': 14, 'ok': 56}, 'vk'),
    ({'facebook': 235, 'yandex': 7, 'vk': 111, 'google': 46, 'email': 22, 'ok': 34}, 'facebook')
])
def test_find_max(list_, expected):
    res = find_max(list_)
    assert res == expected


@pytest.mark.parametrize('list_,expected', [
    (['2018-01-01', 'yandex', 'cpc', 100], {'2018-01-01': {'yandex': {'cpc': 100}}}),
    (['smthing', 10, 'text', 15.2], {'smthing': {10: {'text': 15.2}}}),
    (['key', ('ty', 'ple'), 'word', 100500], {'key': {('ty', 'ple'): {'word': 100500}}})
])
def test_list_to_dict(list_, expected):
    result = lst_to_dict(list_)
    assert result == expected


def test_find_unique():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    expected = [213, 15, 54, 119, 98, 35]
    res = find_unique(ids)
    assert res == expected


def test_filter():
    geo_logs = geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    expected = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']},
                {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]

    result = filter_(geo_logs)
    assert result == expected