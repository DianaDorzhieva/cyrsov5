import requests  # Для запросов по API
import psycopg2
from confing import config

id_companies = [1740,  # яндекс
                3529,  # сбер
                78638,  # тинькоф
                3388,  # газпромбанк
                4181,  # ВТБ
                907345,  # лукойл
                6596,  # роснефть
                39305,  # газпромнефть
                80,  # альфабанк
                3294092]  # халва


def get_info(id_companies):
    company_vacanci = []
    try:
        for id_company in id_companies:
            url_hh = f'https://api.hh.ru/employers/{id_company}'
            info = requests.get(url_hh).json()
            company_vacanci.append({'company': info['name'], 'url': info['vacancies_url']})
    except KeyError:
        print("По данным кретериям не нашлось вакансий")
    return company_vacanci


def get_vacanci(url):
    info_vacanci = []
    info = requests.get(url).json()['items']
    for i in range(len(info)):
        info_vacanci.append({'id_vacanci': info[i]['id'],
                             'id_company': info[i]['department']['id'],
                             'name': info[i]['name'],
                             'url': info[i]['area']['url'],
                             'salary': info[i]['salary']
                             })
    return info_vacanci


# hh = get_info(id_companies)
# dd = get_vacanci(hh[1]['url'])
# for i in dd:
#     print(i)


class DBManager:
    def __init__(self):
        pass

    def create_db(self):
        db_param = config()
        return db_param

    def connect_db(self, db_name, params):
        connection = psycopg2.connect(dbname='postgres', **params)
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            # cursor.execute(f"DROP DATABASE {db_name}")
            cursor.execute(f"CREATE DATABASE {db_name}")
        except psycopg2.ProgrammingError:
            pass
        cursor.close()
        connection.close()

    def create_table(self, db_name, params):
        connection = psycopg2.connect(dbname=db_name, **params)
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute("""
                           CREATE TABLE vacanci (
                           id_vacanci int PRIMARY KEY,
                           company_id varchar(100) REFERENCES companies(company_id) NOT NULL,
                           vacanci_name varchar(100) NOT NULL,
                           url varchar(100) NOT NULL,
                           salary varchar(100)
                           )
                           """)

            cursor.execute("""
                           CREATE TABLE companies (
                           company_id varchar(100) PRIMARY KEY,
                           company_name varchar(50) NOT NULL,
                           description text
                           )
                           """)


        except psycopg2.ProgrammingError:
            pass
        connection.commit()
        cursor.close()
        connection.close()

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass


params = config()
diana = DBManager()
diana.create_db()
diana.connect_db('salary', params)
diana.create_table('salary', params)
