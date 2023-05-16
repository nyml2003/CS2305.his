from dataBase import DataBase

db=DataBase()
sql = """
create table `cs2305.Patient`(
 Pno int primary key COMMENT '患者编号',
 Pname varchar(20) not null COMMENT '患者姓名',
 Pid varchar(20) not null COMMENT '身份证号',
 Pino varchar(20) not null COMMENT '社会保险号',
 Pmno varchar(20) not null COMMENT '医疗卡识别号',
 Psex varchar(20) not null COMMENT '性别',
 Pbd date not null COMMENT '出生日期',
 Padd varchar(100) not null COMMENT '地址'
) COMMENT '患者';
INSERT INTO `cs2305.Patient` VALUES(161,'刘景','142201198702130061','1201676','6781121941','男','1987-2-13','新华路光源街');
INSERT INTO `cs2305.Patient` VALUES(181,'陈禄','142201196608190213','1204001','5461021938','男','1966-8-19','城建路茂源路');
INSERT INTO `cs2305.Patient` VALUES(201,'曾华','142201197803110234','0800920','1231111932','男','1978-3-11','新建路柳巷');
INSERT INTO `cs2305.Patient` VALUES(421,'傅伟相','142202199109230221','0700235','4901021947','男','1991-9-23','高新区西源大道');
INSERT INTO `cs2305.Patient` VALUES(481,'张珍','142201199206200321','1200432','3451121953','女','1992-6-20','西湖区南街');
INSERT INTO `cs2305.Patient` VALUES(501,'李秀','142203198803300432','0692015','3341111936','女','1988-3-30','泰山大道北路');
create table `cs2305.Patient_tel`(
 Ptno int primary key AUTO_INCREMENT COMMENT '患者联系电话编号',
 Pno int not null COMMENT '患者编号',
 Pteltype varchar(20) not null COMMENT '联系方式类型',
 Ptel varchar(20) not null COMMENT '联系号码'
) COMMENT '患者联系电话';
INSERT INTO `cs2305.Patient_tel`(Pno, Pteltype, Ptel) VALUES(161,'手机','12988011007');
INSERT INTO `cs2305.Patient_tel`(Pno, Pteltype, Ptel) VALUES(161,'家庭电话','01166699988');
INSERT INTO `cs2305.Patient_tel`(Pno, Pteltype, Ptel) VALUES(161,'单位电话','01244552277');
CREATE TABLE `cs2305.Dept` (
    DeptNo INT PRIMARY KEY NOT NULL,
    DeptName VARCHAR(20) NOT NULL,
    ParentDeptNo INT,
    Manager INT
) COMMENT '组织机构';
INSERT INTO `cs2305.Dept` VALUES (00, 'XX医院', NULL, NULL);
INSERT INTO `cs2305.Dept` VALUES (10, '门诊部', 00, NULL);
INSERT INTO `cs2305.Dept` VALUES (101, '消化内科', 10, 82);
INSERT INTO `cs2305.Dept` VALUES (102, '急诊内科', 10, 368);
INSERT INTO `cs2305.Dept` VALUES (103, '门内三诊室', 10, 21);
INSERT INTO `cs2305.Dept` VALUES (20, '社区医疗部', 00, NULL);
INSERT INTO `cs2305.Dept` VALUES (201, '家庭病床病区', 20, 73);
CREATE TABLE `cs2305.Doctor` (
    Dno INT PRIMARY KEY,
    Dname VARCHAR(20) NOT NULL,
    Dsex VARCHAR(20) NOT NULL,
    Dage INT NOT NULL,
    Ddeptno INT NOT NULL,
    Tno INT NOT NULL
);
INSERT INTO `cs2305.Doctor` VALUES (140, '郝亦柯', '男', 28, 101, 01);
INSERT INTO `cs2305.Doctor` VALUES (21, '刘伟', '男', 43, 104, 01);
INSERT INTO `cs2305.Doctor` VALUES (368, '罗晓', '女', 27, 103, 04);
INSERT INTO `cs2305.Doctor` VALUES (73, '邓英超', '女', 43, 105, 33);
INSERT INTO `cs2305.Doctor` VALUES (82, '杨勋', '男', 104, 104, 35);
create table `cs2305.Title`(
 Tno int primary key not null,
 Sno int not null,
 Ttype varchar(20) not null,
 Ttrade varchar(20) not null
);
INSERT INTO `cs2305.Title` VALUES(102,05,'医师','医疗');
INSERT INTO `cs2305.Title` VALUES(104,03,'副主任医师','医疗');
INSERT INTO `cs2305.Title` VALUES(103,04,'主治医师','医疗');
INSERT INTO `cs2305.Title` VALUES(105,01,'主任医师','医疗');
INSERT INTO `cs2305.Title` VALUES(233,06,'初级护师','护理');
INSERT INTO `cs2305.Title` VALUES(235,03,'主任护师','护理');
create table `cs2305.Salary`(
 Sno int not null primary key,
 Slevel varchar(20) not null,
 Snumber DECIMAL(12,4) not null
);
INSERT INTO `cs2305.Salary` VALUES(03,'高级',4000);
INSERT INTO `cs2305.Salary` VALUES(05,'中级',3000);
INSERT INTO `cs2305.Salary` VALUES(01,'高级',5000);
INSERT INTO `cs2305.Salary` VALUES(06,'初级',2500);
INSERT INTO `cs2305.Salary` VALUES(04,'高级',4500);
create table `cs2305.Godown_Entry`(
 GMno int not null primary key,
 GMdate DATETIME not null,
 GMname varchar(20) not null
);
INSERT INTO `cs2305.Godown_Entry` VALUES(1,'2016-1-2 13:00:12','抗生素类药品');
INSERT INTO `cs2305.Godown_Entry` VALUES(12,'2016-11-24 18:00:00','心脑血管用药');
INSERT INTO `cs2305.Godown_Entry` VALUES(31,'2017-1-14 9:02:01','消化系统用药');
INSERT INTO `cs2305.Godown_Entry` VALUES(34,'2017-3-20 12:19:10','呼吸系统用药');
INSERT INTO `cs2305.Godown_Entry` VALUES(2,'2016-1-3 14:00:00','泌尿系统用药');
INSERT INTO `cs2305.Godown_Entry` VALUES(11,'2016-11-20 18:00:00','血液系统用药');
INSERT INTO `cs2305.Godown_Entry` VALUES(3,'2016-1-10 09:10:22','抗风湿类药品');
INSERT INTO `cs2305.Godown_Entry` VALUES(9,'2016-4-27 13:20:00','注射剂类药品');
INSERT INTO `cs2305.Godown_Entry` VALUES(14,'2016-12-20 17:00:31 ','激素类药品');
INSERT INTO `cs2305.Godown_Entry` VALUES(4,'2016-1-12 20:10:02','皮肤科用药');
INSERT INTO `cs2305.Godown_Entry` VALUES(6,'2016-4-27 13:20:00','妇科用药');
INSERT INTO `cs2305.Godown_Entry` VALUES(7,'2016-5-10 18:30:05','抗肿瘤用药');
INSERT INTO `cs2305.Godown_Entry` VALUES(13,'2016-12-01 12:15:00','抗精神病药品');
INSERT INTO `cs2305.Godown_Entry` VALUES(8,'2016-6-06 15:50:20','清热解毒药品');
INSERT INTO `cs2305.Godown_Entry` VALUES(33,'2017-2-24 8:02:52','维生素、矿物质药品');
INSERT INTO `cs2305.Godown_Entry` VALUES(32,'2017-1-19 7:22:00','糖尿病药品');
INSERT INTO `cs2305.Godown_Entry` VALUES(17,'2019-12-30 0:0:0','肾石通');
INSERT INTO `cs2305.Godown_Entry` VALUES(25,'2022-6-30 0:0:0','阿奇霉素');
create table `cs2305.Godown_Slave`(
 GSno int not null primary key,
 GMno int not null,
 Mno int not null,
 GSnumber DECIMAL(12,4) not null,
 GSunit varchar(20) not null,
 GSbatch varchar(20) not null,
 GSprice DECIMAL(12,4) not null,
 GSexpdate date not null
);
INSERT INTO `cs2305.Godown_Slave` VALUES(02,17,314941,23,'箱',232342345,3000,'2019-12-30');
INSERT INTO `cs2305.Godown_Slave` VALUES(12,1,315189,50,'箱',345465675,2560,'2020-12-30');
INSERT INTO `cs2305.Godown_Slave` VALUES(34,12,314172,100,'盒',678786994,50300,'2022-3-10');
INSERT INTO `cs2305.Godown_Slave` VALUES(55,25,315501,85,'盒',534525342,1450,'2022-6-20');
INSERT INTO `cs2305.Godown_Slave` VALUES(114,31,315977,120,'盒',114514191,9810,'2023-1-1');
INSERT INTO `cs2305.Godown_Slave` VALUES(514,2,316910,77,'盒',191981011,4514,'2022-1-1');
create table `cs2305.Medicine`(
 Mno int not null primary key,
 GSno int not null,
 Mname varchar(20) not null,
 Mprice DECIMAL(12,4) not null,
 Munit varchar(20) not null,
 Mtype varchar(20) not null
);
INSERT INTO `cs2305.Medicine` VALUES(314172,34,'卡托普利片',0.037,'片','西药');
INSERT INTO `cs2305.Medicine` VALUES(314941,02,'肾石通颗粒',27.1,'盒','西药');
INSERT INTO `cs2305.Medicine` VALUES(315189,12,'心胃止痛胶囊',26.9,'盒','西药');
INSERT INTO `cs2305.Medicine` VALUES(315501,55,'阿奇霉素胶囊',21,'盒','西药');
INSERT INTO `cs2305.Medicine` VALUES(315977,114,'胃立康片',26.5,'盒','西药');
INSERT INTO `cs2305.Medicine` VALUES(316910,514,'依诺沙星注射液',46,'支','西药');
create table `cs2305.Cashier`(
 Cno int not null primary key
);
INSERT INTO `cs2305.Cashier` VALUES(09);
INSERT INTO `cs2305.Cashier` VALUES(01);
INSERT INTO `cs2305.Cashier` VALUES(02);
INSERT INTO `cs2305.Cashier` VALUES(05);
INSERT INTO `cs2305.Cashier` VALUES(08);
create table `cs2305.Diagnosis`(
 DGno varchar(20) primary key not null,
 Pno int not null,
 Dno varchar(20) not null,
 Symptom varchar(20) not null,
 Diagnosis varchar(20) not null,
 DGtime DATETIME not null,
 Rfee DECIMAL(12,4) not null
);
INSERT INTO `cs2305.Diagnosis` VALUES(1645,481,140,'呼吸道感染','伤风感冒','2016-7-21 01:12:01',3);
INSERT INTO `cs2305.Diagnosis` VALUES(2170,201,21,'皮肤和软组织干扰','细菌感染','2016-7-22 10:10:03',5);
INSERT INTO `cs2305.Diagnosis` VALUES(3265,161,82,'胃溃疡','螺杆菌感染','2016-7-23 10:59:42',5);
INSERT INTO `cs2305.Diagnosis` VALUES(3308,181,82,'消化不良','胃病','2016-7-23 11:11:34',5);
INSERT INTO `cs2305.Diagnosis` VALUES(3523,501,73,'心力衰竭','高血压','2017-7-23 02:01:05',7);
INSERT INTO `cs2305.Diagnosis` VALUES(7816,421,368,'肾盂结石','肾结石','2017-1-8 05:17:03',3);
create table `cs2305.Recipe_Master`(
  RMno int not null primary key,
  DeptNo int not null,
  Dno int not null,
  Pno int not null,
  RMage int not null,
  RMtime DATETIME not null
);
INSERT INTO `cs2305.Recipe_Master` VALUES(1282317,103,140,181,12,'2016-7-21 01:12:01');
INSERT INTO `cs2305.Recipe_Master` VALUES(1282872,201,368,161,50,'2016-7-22 10:10:03');
INSERT INTO `cs2305.Recipe_Master` VALUES(1283398,20,73,481,23,'2016-7-23 10:59:42');
INSERT INTO `cs2305.Recipe_Master` VALUES(1284041,101,368,501,48,'2017-7-23 11:11:34');
INSERT INTO `cs2305.Recipe_Master` VALUES(1284256,103,21,201,36,'2017-7-23 02:01:05');
INSERT INTO `cs2305.Recipe_Master` VALUES(1458878,102,82,421,30,'2017-1-8 05:17:03');
create table `cs2305.Recipe_Detail`(
 RDno int not null primary key,
 RMno int not null,
 Mno int not null,
 RDprice DECIMAL(12,4) not null,
 RDnumber int not null,
 RDunit varchar(20) not null
);
INSERT INTO `cs2305.Recipe_Detail` VALUES(16,1282872,314941,200,3,'盒');
INSERT INTO `cs2305.Recipe_Detail` VALUES(32,1458878,315189,360,4,'盒');
INSERT INTO `cs2305.Recipe_Detail` VALUES(47,1284041,315977,14,1,'片');
INSERT INTO `cs2305.Recipe_Detail` VALUES(89,1282317,316910,2.5,10,'粒');
create table `cs2305.Register_Form`(
 RFno int not null primary key,
 RFdept int not null,
 RFdoctor int not null,
 RFpatient int not null,
 RFcashier int not null,
 RFtime DATETIME not null,
 RFvisittime DATETIME not null,
 RFfee DECIMAL(12,4) not null,
 RFnotes varchar(20)
);
INSERT INTO `cs2305.Register_Form` VALUES(13,20,73,481,01,'2016-7-11 06:12:09','2016-7-11 08:00:00',5,NULL);
INSERT INTO `cs2305.Register_Form` VALUES(56,201,368,161,08,'2016-7-28 09:20:19','2016-7-28 09:30:00',7,NULL);
INSERT INTO `cs2305.Register_Form` VALUES(71,103,140,181,09,'2017-1-10 16:09:02','2017-1-10 17:30:00',7,NULL);
INSERT INTO `cs2305.Register_Form` VALUES(89,102,82,421,02,'2017-3-16 19:18:10','2017-3-16 19:20:00',5,NULL);
create table `cs2305.Fee`(
 Fno int not null primary key,
 Fnumber varchar(20) not null,
 Fdate DATETIME not null,
 DGno int not null,
 RMno int not null,
 Cno int not null,
 Pno int not null,
 FRecipefee DECIMAL(12,4) not null,
 Fdiscount DECIMAL(12,4) not null,
 Fsum DECIMAL(12,4) not null
);
INSERT INTO `cs2305.Fee` VALUES(1281645,'02995606','2016-7-21 01:12:01',1645,1282317,09,181,200,0,200);
INSERT INTO `cs2305.Fee` VALUES(1282170,'02994356','2016-7-22 10:10:03',7816,1282872,01,481,189,37.8,151.2);
INSERT INTO `cs2305.Fee` VALUES(1283265,'02996768','2016-7-23 10:59:42',2170,1283998,02,501,560,112,448);
INSERT INTO `cs2305.Fee` VALUES(1283308,'02995687','2016-7-23 11:11:34',3308,1284041,05,201,17,3.4,13.6);
INSERT INTO `cs2305.Fee` VALUES(1283523,'02997432','2016-7-23 02:01:05',3523,1284256,08,481,13,0,13);
INSERT INTO `cs2305.Fee` VALUES(1457816,'02990101','2017-1-8 05:17:03',3265,1458878,09,21,111,0,111); 
ALTER TABLE `cs2305.Patient`_tel ADD FOREIGN KEY(Pno) REFERENCES `cs2305.Patient`(Pno);   
ALTER TABLE `cs2305.Dept` ADD FOREIGN KEY (ParentDeptNo) REFERENCES `cs2305.Dept` (DeptNo);
ALTER TABLE `cs2305.Dept` ADD FOREIGN KEY (Manager) REFERENCES `cs2305.Doctor` (Dno);
ALTER TABLE `cs2305.Doctor` ADD FOREIGN KEY (Ddeptno) REFERENCES `cs2305.Dept` (DeptNo);
ALTER TABLE `cs2305.Doctor` ADD FOREIGN KEY (Tno) REFERENCES `cs2305.Title` (Tno);
ALTER TABLE `cs2305.Title` ADD FOREIGN KEY(Sno) REFERENCES `cs2305.Salary`(Sno);
ALTER TABLE `cs2305.Godown_Slave` ADD FOREIGN KEY(GMno) REFERENCES `cs2305.Godown_Entry`(GMno);
ALTER TABLE `cs2305.Godown_Slave` ADD FOREIGN KEY(Mno) REFERENCES `cs2305.Medicine`(Mno);
ALTER TABLE `cs2305.Medicine` ADD FOREIGN KEY(GSno) REFERENCES `cs2305.Godown_Slave`(GSno);
ALTER TABLE `cs2305.Diagnosis` ADD FOREIGN KEY(Pno) REFERENCES `cs2305.Patient`(Pno);
ALTER TABLE `cs2305.Diagnosis` ADD FOREIGN KEY(Dno) REFERENCES `cs2305.Doctor`(Dno);
ALTER TABLE `cs2305.Recipe_Master` ADD FOREIGN KEY(DeptNo) REFERENCES `cs2305.Dept`(DeptNo);
ALTER TABLE `cs2305.Recipe_Master` ADD FOREIGN KEY(Dno) REFERENCES `cs2305.Doctor`(Dno);
ALTER TABLE `cs2305.Recipe_Master` ADD FOREIGN KEY(Pno) REFERENCES `cs2305.Patient`(Pno);
ALTER TABLE `cs2305.Recipe_Detail` ADD FOREIGN KEY(RMno) REFERENCES `cs2305.Recipe_Master`(RMno);
ALTER TABLE `cs2305.Recipe_Detail` ADD FOREIGN KEY(Mno) REFERENCES `cs2305.Medicine`(Mno);
ALTER TABLE `cs2305.Register_Form` ADD FOREIGN KEY(RFdept) REFERENCES `cs2305.Dept`(DeptNo);
ALTER TABLE `cs2305.Register_Form` ADD FOREIGN KEY(RFdoctor) REFERENCES `cs2305.Doctor`(Dno);
ALTER TABLE `cs2305.Register_Form` ADD FOREIGN KEY(RFpatient) REFERENCES `cs2305.Patient`(Pno);
ALTER TABLE `cs2305.Register_Form` ADD FOREIGN KEY(RFcashier) REFERENCES `cs2305.Cashier`(Cno);
ALTER TABLE `cs2305.Fee` ADD FOREIGN KEY(DGno) REFERENCES `cs2305.Diagnosis`(DGno);
ALTER TABLE `cs2305.Fee` ADD FOREIGN KEY(RMno) REFERENCES `cs2305.Recipe_Master`(RMno);
ALTER TABLE `cs2305.Fee` ADD FOREIGN KEY(Cno) REFERENCES `cs2305.Cashier`(Cno);
ALTER TABLE `cs2305.Fee` ADD FOREIGN KEY(Pno) REFERENCES `cs2305.Patient`(Pno);
"""
ret=db.execute(sql)
print(ret)