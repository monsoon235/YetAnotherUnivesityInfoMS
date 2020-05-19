# 后端 API 文档

使用方式

```
GET  api/<function>/<action>?<param1>=xxx&<param2>=xxx
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

筛选参数：

1. id
2. name
3. address

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
GET  api/campus/add&id=PB03&name=Cindy&address=us
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
GET   api/campus/mod?id=PB01&name_mod=Andy
```

```json
{
  "code":0
  // 此时 id=PB01 的条目 name 被改为 Andy
}
```

(专业) api/major

(班级) api/class

(学生) api/student

(教师) api/teacher

(学籍异动) api/adjustment

(课程)  api/course

(开课)  api/lecture

(选课)  api/selection
