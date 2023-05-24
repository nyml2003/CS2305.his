from sqlalchemy import create_engine,text,MetaData
from dataBase import DataBase
sql='''
ALTER TABLE `cs2305.Dept` DROP FOREIGN KEY `cs2305.dept_ibfk_1`;
ALTER TABLE `cs2305.Dept` DROP FOREIGN KEY `cs2305.dept_ibfk_2`;
ALTER TABLE `cs2305.Doctor` DROP FOREIGN KEY `cs2305.doctor_ibfk_1`;
ALTER TABLE `cs2305.Doctor` DROP FOREIGN KEY `cs2305.doctor_ibfk_2`;
ALTER TABLE `cs2305.Title` DROP FOREIGN KEY `cs2305.title_ibfk_1`;
ALTER TABLE `cs2305.Godown_Slave` DROP FOREIGN KEY `cs2305.godown_slave_ibfk_1`;
ALTER TABLE `cs2305.Godown_Slave` DROP FOREIGN KEY `cs2305.godown_slave_ibfk_2`;
ALTER TABLE `cs2305.Medicine` DROP FOREIGN KEY `cs2305.medicine_ibfk_1`;
ALTER TABLE `cs2305.Diagnosis` DROP FOREIGN KEY `cs2305.diagnosis_ibfk_1`;
ALTER TABLE `cs2305.Diagnosis` DROP FOREIGN KEY `cs2305.diagnosis_ibfk_2`;
ALTER TABLE `cs2305.Recipe_Master` DROP FOREIGN KEY `cs2305.recipe_master_ibfk_1`;
ALTER TABLE `cs2305.Recipe_Master` DROP FOREIGN KEY `cs2305.recipe_master_ibfk_2`;
ALTER TABLE `cs2305.Recipe_Master` DROP FOREIGN KEY `cs2305.recipe_master_ibfk_3`;
ALTER TABLE `cs2305.Recipe_Detail` DROP FOREIGN KEY `cs2305.recipe_detail_ibfk_1`;
ALTER TABLE `cs2305.Recipe_Detail` DROP FOREIGN KEY `cs2305.recipe_detail_ibfk_2`;
ALTER TABLE `cs2305.Register_Form` DROP FOREIGN KEY `cs2305.register_form_ibfk_1`;
ALTER TABLE `cs2305.Register_Form` DROP FOREIGN KEY `cs2305.register_form_ibfk_2`;
ALTER TABLE `cs2305.Register_Form` DROP FOREIGN KEY `cs2305.register_form_ibfk_3`;
ALTER TABLE `cs2305.Register_Form` DROP FOREIGN KEY `cs2305.register_form_ibfk_4`;
ALTER TABLE `cs2305.Fee` DROP FOREIGN KEY `cs2305.fee_ibfk_1`;
ALTER TABLE `cs2305.Fee` DROP FOREIGN KEY `cs2305.fee_ibfk_2`;
ALTER TABLE `cs2305.Fee` DROP FOREIGN KEY `cs2305.fee_ibfk_3`;
ALTER TABLE `cs2305.Fee` DROP FOREIGN KEY `cs2305.fee_ibfk_4`;
'''
print(DataBase().execute(sql))

engine = create_engine("mysql+pymysql://root:uestc2022!@124.71.219.185:3306/CS2305.his")
metadata = MetaData()
metadata.reflect(bind=engine)
tables = metadata.sorted_tables

with engine.connect() as connection:
    for table in reversed(tables):
        connection.execute(table.delete())
    metadata.drop_all(bind=engine)
exit()