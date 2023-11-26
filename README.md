Проект для получения информации из hh и внесение данных в таблицы pgAdmin.
Функция get_info получает данные о компаниях, используя id ( в данной реализации id прописаны в списке, при необходимости можно список дополнять ).
Данные формируются в словарик, из которого потом записываются в таблицу - companies.
Функция get_vacanci, используя url от get_info подключается к hh и вытягивает данные о вакансиях интересующих компаний. 
Данные формируются в словарик, из которого потом записываются в таблицу - vacanci.
Класс DBManager инциилизируется используя файл database.ini через функцию config и названия базы данных ( название можно использовать любое, пользователь сам придумывает). 
DBManager подключается к БЗ, формирует/или удаляет ранее созданную БД, заполняет таблицы.
DBManager имеет ряд функций для фильтрации информации.
