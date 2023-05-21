from dataBase import DataBase

db=DataBase()
sql = """
DROP VIEW if exists patient_info;
CREATE VIEW patient_info AS
SELECT * 
FROM `cs2305.Patient`;

DROP VIEW if exists doctor_info;
CREATE VIEW doctor_info AS
SELECT D.Dno, D.Dname, D.Dsex, D.Dage, D.Ddeptno, T.Tno, Dept.DeptName,T.Ttype, T.Ttrade, S.Slevel, S.Snumber
FROM `cs2305.Doctor` D
JOIN `cs2305.Title` T
ON D.Tno = T.Tno
JOIN `cs2305.Salary` S
ON T.Sno = S.Sno
JOIN `cs2305.Dept` Dept
ON D.Ddeptno = Dept.DeptNo
"""
ret=db.execute(sql)
print(ret)