from confing import config
from DBManager import DBManager

params = config()
db_manager = DBManager('name_bd', params)
db_manager.connect_db()
db_manager.create_table()
db_manager.write_info_in_table()
