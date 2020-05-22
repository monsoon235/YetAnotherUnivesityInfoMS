## 基于vue.js + django + mysql的数据库系统

##环境搭建

pip install -r requirements.txt

## 1. 后端django初始化

```bash
cd backend

pip intall django

pip install django-cors-headers

pip install mysqlclient   #直接安装无效，需要进入https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient下载python对应的mysqlclient

pip install web.py

```

#### 配置mysql(修改./backend/settings.py)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'api', #本地创建的数据库名
        'USER': 'root', #用户名，默认是root
        'PASSWORD': 'root',  #密码
        'HOST': '127.0.0.1',
    }
}
```

#### 数据库迁移

```bash

python manage.py makemigrations api

python manage.py migrate

python manage.py runserver
```

## 2. 前段vue.js初始化

```bash
cd appfront

npm install

npm install vue-resource

npm install element-ui

npm run dev
```
