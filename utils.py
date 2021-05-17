from requests import get, utils
from decimal import Decimal
import datetime


def url_inquiry():
    '''

    Принимает запрос с сервера и делит на строки.

    :return: Список со строками.
    '''
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    content = content.split('<Valute ')
    return content


def parce_list_url_to_dict():
    '''

    Преобразовывает строки в словарь сответствующей валюты.

    '''
    for list_valute in content_valute:
        code_valyt = parse_info_in_list_url(list_valute, '<CharCode>', '</CharCode>')
        id_valyt_list = parse_info_in_list_url(list_valute, 'ID="', '">')
        num_code_valyt_list = parse_info_in_list_url(list_valute, '<NumCode>', '</NumCode>')
        code_valyt_list = parse_info_in_list_url(list_valute, '<CharCode>', '</CharCode>')
        name_valute_list = parse_info_in_list_url(list_valute, '<Name>', '</Name>')
        nominal_valute_list = parse_info_in_list_url(list_valute, '<Nominal>', '</Nominal>')
        difference_valute_list_parse = parse_info_in_list_url(list_valute, '<Value>', '</Value>')
        difference_valute_list = difference_valute_list_parse.split(',')
        difference_valute_list = (Decimal('.'.join(difference_valute_list))).quantize(Decimal('1.00'))
        valute[code_valyt] = [id_valyt_list,
                              num_code_valyt_list,
                              code_valyt_list,
                              name_valute_list,
                              nominal_valute_list,
                              difference_valute_list]


def parse_info_in_list_url(valute_list_url_11, from_url, before_url):
    '''

    Выделяет из строки нужный элемент

    :param valute_list_url_11: Из какой строки выделяется эдемент
    :param from_url: От куда нужно выделить
    :param before_url: До куда нужно выделить
    :return: Выделенный элемент
    '''
    valute_id = valute_list_url_11
    valute_id = valute_id.split(from_url)
    valute_id = valute_id[1].split(before_url)
    valute_id = valute_id[0]
    return valute_id


def date_in_url(url_date):
    '''

    Выводит дату, полученную с сервера

    :param url_date: Строка с датой сервера
    :return: Дата сервера
    '''
    url_date = parse_info_in_list_url(url_date, 'Date="', '" name')
    url_date = url_date.split('.')
    url_date = datetime.date(int(url_date[2]), int(url_date[1]), int(url_date[0]))
    return url_date


def currency_output(valute_code, valute_rub):
    '''

    Преобразовывает строки полученные из url в словарь валют и выводит запрошенную по коду валюты.

    :param valute_code: Запрашиваемый код валюты.
    :param valute_rub: Запрашивает количество валюты.
    '''
    for valute_info in content_list:
        content_valute.append(valute_info)
    content_date = content_valute[0]
    content_valute.pop(0)
    date = date_in_url(content_date)
    parce_list_url_to_dict()

    if valute_code not in valute:
        print("Такого кода валют не существует!\n")
    else:
        valute_rub = Decimal(Decimal(valute_rub) * (valute[valute_code][5] / int(valute[valute_code][4])))
        print(f'ID:                {(valute[valute_code])[0]}\n'
              f'Номерной код:      {(valute[valute_code])[1]}\n'
              f'Код:               {(valute[valute_code])[2]}\n'
              f'Название:          {(valute[valute_code])[3]}\n'
              f'Номинал:           {(valute[valute_code])[4]}\n'
              f'Отношение к рублю: {(valute[valute_code])[5]}\n'
              f'Итог:              {valute_rub.quantize(Decimal("1.00"))} RUB\n'
              f'Дата:              {date}\n'
              f'Тип даты:          {type(date)}\n')


def input_outpat(valute_inquiry, valute_inquiry_rub):
    '''

    Получает запрос в ваде кода валют и выводит информацию по нему.

    :param valute_inquiry Запрашиваемый код валюты.
    :param valute_inquiry_rub Запрашивает количество валюты.

    '''
    valute_inquiry = valute_inquiry.upper()
    currency_output(valute_inquiry, valute_inquiry_rub)


def currency_rates(input_valute_code, input_rub):
    '''

    Создает глобальные переменные для работы функции и отчищает их для повторного использования.

    :param input_valute_code Запрашиваемый код валюты.
    :param input_rub Запрашивает количество валюты.

    '''
    global content_valute
    global valute
    global content_list
    content_valute = []
    valute = {}
    content_list = url_inquiry()
    input_outpat(input_valute_code, input_rub)
    content_valute = []
    valute = {}


if __name__ == '__main__':
    print('Этого не должно быть видно')
    check = input("код\n")
    check_rub = input("рубли?:\n")
    currency_rates(check, check_rub)
