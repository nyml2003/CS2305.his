from dataBase import DataBase

db=DataBase()
sql = """
CREATE VIEW PatientAllInformation_view AS
SELECT P.Pno, P.Pname, P.Pid, P.Pino, P.Pmno, P.Psex,
DATE_FORMAT(P.Pbd, '%Y-%m-%d') AS Pbd,
P.Padd,
MAX(CASE WHEN Pt.Pteltype = '手机' THEN Pt.Ptel END) AS 手机,
MAX(CASE WHEN Pt.Pteltype = '家庭电话' THEN Pt.Ptel END) AS 家庭电话,
MAX(CASE WHEN Pt.Pteltype = '单位电话' THEN Pt.Ptel END) AS 单位电话
FROM `cs2305.Patient` P
LEFT JOIN `cs2305.Patient_tel` Pt
ON P.Pno = Pt.Pno
GROUP BY P.Pno;



CREATE VIEW DeptView AS
SELECT D.DeptNo, D.DeptName, P.DeptName AS ParentDeptName, M.Dname AS ManagerName
FROM `cs2305.Dept` D
LEFT JOIN `cs2305.Dept` P
ON D.ParentDeptNo = P.DeptNo
LEFT JOIN `cs2305.Doctor` M
ON D.Manager = M.Dno;
"""
ret=db.execute(sql)
print(ret)