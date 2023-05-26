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
ON D.Ddeptno = Dept.DeptNo;

DROP VIEW if exists RegisterFormView;
CREATE VIEW RegisterFormView AS
SELECT RF.*, D.DeptName, Doc.Dname, P.Pname,P.uid
FROM `cs2305.Register_Form` AS RF
JOIN `cs2305.Dept` AS D ON RF.RFdept = D.DeptNo
JOIN `cs2305.Doctor` AS Doc ON RF.RFdoctor = Doc.Dno
JOIN `cs2305.Patient` AS P ON RF.RFpatient = P.Pno;
"""
ret=db.execute(sql)
print(ret)