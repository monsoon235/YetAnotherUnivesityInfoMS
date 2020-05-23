import requests

s = requests.Session()
url = "http://localhost:8000"
passwd = "123"
#管理员登录
print(s.post(url+"/api/login",json={"id":"admin","password":passwd}).content)
#加校区
s.post(url+"/api/campus/add",json={"id":"0","name":"东区","address":"东"})
s.post(url+"/api/campus/add",json={"id":"1","name":"西区","address":"西"})
s.post(url+"/api/campus/add",json={"id":"2","name":"南区","address":"南"})
s.post(url+"/api/campus/add",json={"id":"3","name":"北区","address":"北"})
#加专业
s.post(url+"/api/major/add",json={"id":"0","name":"生物","address":"东","campus_id":"0"})
s.post(url+"/api/major/add",json={"id":"1","name":"物理","address":"西","campus_id":"1"})
s.post(url+"/api/major/add",json={"id":"2","name":"化学","address":"南","campus_id":"2"})
s.post(url+"/api/major/add",json={"id":"3","name":"计算机","address":"北","campus_id":"3"})
#加老师
s.post(url+"/api/teacher/add",json={"id": "T1",
        "person_name": "老师一",
        "password": passwd,
        "gender": 0,
        "title": 0,
        "person_id_type": 0,
        "person_id": "T0",
        "country": "C",
        "birth": "1000-02-02",
        "major_id": "0",
        "family_address": "安徽",
        "family_zipcode": "404",
        "family_tel": "100",
        "enroll_date": "1020-02-02",
        "email": "1@ustc.edu.cn"})
s.post(url+"/api/teacher/add",json={"id": "T2",
        "person_name": "老师二",
        "password": passwd,
        "gender": 0,
        "title": 0,
        "person_id_type": 0,
        "person_id": "T1",
        "country": "C",
        "birth": "1000-02-02",
        "major_id": "1",
        "family_address": "安徽",
        "family_zipcode": "404",
        "family_tel": "200",
        "enroll_date": "1020-02-02",
        "email": "2@ustc.edu.cn"})
s.post(url+"/api/teacher/add",json={"id": "T3",
        "person_name": "老师三",
        "password": passwd,
        "gender": 0,
        "title": 0,
        "person_id_type": 0,
        "person_id": "T2",
        "country": "C",
        "birth": "1000-02-02",
        "major_id": "2",
        "family_address": "安徽",
        "family_zipcode": "404",
        "family_tel": "300",
        "enroll_date": "1020-02-02",
        "email": "3@ustc.edu.cn"})
s.post(url+"/api/teacher/add",json={"id": "T4",
        "person_name": "老师四",
        "password": passwd,
        "gender": 0,
        "title": 0,
        "person_id_type": 0,
        "person_id": "T3",
        "country": "C",
        "birth": "1000-02-02",
        "major_id": "4",
        "family_address": "安徽",
        "family_zipcode": "404",
        "family_tel": "400",
        "enroll_date": "1020-02-02",
        "email": "4@ustc.edu.cn"})

#加班级
s.post(url+"/api/class/add",json={"id":"0","name":"一班","found_date":"1020-02-02","grade":0,"major_id":"0","charge_teacher_id":"T0"})
s.post(url+"/api/class/add",json={"id":"1","name":"二班","found_date":"1020-02-02","grade":0,"major_id":"1","charge_teacher_id":"T1"})
s.post(url+"/api/class/add",json={"id":"2","name":"三班","found_date":"1020-02-02","grade":0,"major_id":"2","charge_teacher_id":"T2"})
s.post(url+"/api/class/add",json={"id":"3","name":"四班","found_date":"1020-02-02","grade":0,"major_id":"3","charge_teacher_id":"T3"})
#加学生
s.post(url+"/api/student/add",json={"id": "S1",
        "person_name": "学生一",
        "password": passwd,
        "gender": 0,
        "person_id_type": 0,
        "person_id": "S0",
        "country": "C",
        "birth": "1020-01-01",
        "class_id": "0",
        "family_address": "安徽",
        "family_zipcode": "404",
        "family_tel": "101",
        "enroll_date": "1020-02-02",
        "email": "1@mail.ustc.edu.cn"})
s.post(url+"/api/student/add",json={"id": "S2",
        "person_name": "学生二",
        "password": passwd,
        "gender": 0,
        "person_id_type": 0,
        "person_id": "S1",
        "country": "C",
        "birth": "1020-01-01",
        "class_id": "1",
        "family_address": "安徽",
        "family_zipcode": "404",
        "family_tel": "201",
        "enroll_date": "1020-02-02",
        "email": "2@mail.ustc.edu.cn"})
s.post(url+"/api/student/add",json={"id": "S3",
        "person_name": "学生一",
        "password": passwd,
        "gender": 0,
        "person_id_type": 0,
        "person_id": "S2",
        "country": "C",
        "birth": "1020-01-01",
        "class_id": "2",
        "family_address": "安徽",
        "family_zipcode": "404",
        "family_tel": "301",
        "enroll_date": "1020-02-02",
        "email": "3@mail.ustc.edu.cn"})
s.post(url+"/api/student/add",json={"id": "S4",
        "person_name": "学生一",
        "password": passwd,
        "gender": 0,
        "person_id_type": 0,
        "person_id": "S3",
        "country": "C",
        "birth": "1020-01-01",
        "class_id": "3",
        "family_address": "安徽",
        "family_zipcode": "404",
        "family_tel": "401",
        "enroll_date": "1020-02-02",
        "email": "4@mail.ustc.edu.cn"})

#加课程
s.post(url+"/api/course/add",json={"id":"0","name":"大物一","major_id":"0","assessment":0})
s.post(url+"/api/course/add",json={"id":"1","name":"大物二","major_id":"1","assessment":1})
s.post(url+"/api/course/add",json={"id":"2","name":"大物三","major_id":"2","assessment":0})
s.post(url+"/api/course/add",json={"id":"3","name":"大物四","major_id":"3","assessment":1})
