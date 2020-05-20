# 后端 API 文档

使用方式

```
GET  api/<function>/<action>?<param1>=xxx&<param2>=xxx

POST  api/<function>/<action>     body 中携带数据
```

get, del 操作使用 GET

add, mod 操作使用 POST, body 内容如下

- add

```json
{
  "id":"xxx",
  "name":"xxx",
  // ...
}
```

- mod

```json
{
  "where":{
    "id":"xxx",
    "name":"xxx",
    // ...
  },
  "update":{
    "name":"yyy",
    // ...
  }
}
```

返回结果：

- 成功

```json
{
  "code": 1,
  "list": [
    // 返回的数据
  ]
}
```

- 失败

```json
{
  "code": 0,
  "msg": "错误信息"
}
```

## campus

校区信息管理

筛选参数：`id`,`name`,`address`

### get

查询校区信息，三个参数可以任选 0~3 个进行条件筛选。

返回示例：

```
GET  api/campus/get?address=cn
```

```json
{
  "code":1,
  "list":[
    {
      "id":"PB01",
      "name":"Alice",
      "address":"cn"
    },
    {
      "id":"PB02",
      "name":"Bob",
      "address":"cn"
    },
    // ......
  ]
}
```

### del

删除条目，任选 0~3 个参数进行筛选。

返回示例：

```
GET  api/campus/del?id=PB01
```

```json
{
  "code":1
  // 此时 id=PB01 的条目已被删除
}
```

### add

增加条目，没指定的参数为 `null`.

主键已存在时会返回错误，`not null` 字段没指定时也会返回错误。

```
POST  api/campus/add

{
  "id":"PB03",
  "name":"Cindy",
  "address":"us"
}
```

```json
{
  "code":1
  // 此时 id=PB03 的条目已被添加
}
```

### mod

修改条目，筛选参数取 0~3 个任意组合。

另外增加 `name_mod` 和 `address_mod` 作为修改后的值。

示例：

```
POST   api/campus/mod

{
  "where": {
    "id":"PB01"
  },
  "update":{
    "name":"Andy"
  }
}
```

```json
{
  "code":0
  // 此时 id=PB01 的条目 name 被改为 Andy
}
```

## major

大致和 campus 一样

筛选字段有 `id`, `name`, `address`, `campus_id`, `charge_person_id`.

返回字段中再加上 `campus_name`, `charge_person_name`.

## class

筛选字段有 `id`, `name`, `found_date`, `grade`, `major_id`, `charge_teacher_id`.

返回字段中加上 `major_name`, `charge_teacher_name`.

## student

筛选字段有 `id`, `enroll_date`, `email`, `class_id`, `class_name`, `major_id`, `major_name`, `person_id`, `person_name`, `person_id_type`, `gender`, `birth`, `country`, `family_address`, `family_zipcode`, `family_tel`.

返回字段同上。

<!-- todo 是否需要返回更多的信息？ -->

## teacher

筛选字段有 `id`, `enroll_date`, `email`, `title`, `major_id`, `major_name`, `person_id`, `person_name`, `person_id_type`, `gender`, `birth`, `country`, `family_address`, `family_zipcode`, `family_tel`.

返回的字段同上。

## course

筛选字段有 `id`, `name`, `assessment`, `major_id`.

返回的字段除了以上，还有 `major_name`.

## lecture

筛选字段有 `id`, `course_id`, `teacher_id`, `year`, `term`, `time`.

返回的字段除了以上，还有 `course_name`, `teacher_name`.

## selection

筛选字段有 `id`, `lecture_id`, `student_id`, `score`.

返回的字段除了以上，还有 `course_name`, `teacher_name`, `student_name`.

## adjustment

<!-- todo  待定 -->
