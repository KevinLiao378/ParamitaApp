# Paramita Api
### 获取所有用户

**请求**

`GET /v1/users`

**参数**

无

**返回**

```json
{
    "code": 1,
    "message": "success",
    "data": [
        {
            "createdAt": "2019-01-15 08:36:14",
            "id": 1,
            "username": "Bill"
        },
        {
            "createdAt": "2019-01-15 08:36:22",
            "id": 2,
            "username": "王老五"
        },
        {
            "createdAt": "2019-01-15 08:36:35",
            "id": 3,
            "username": "周星星"
        }
    ]
}
```
### 根据id获取单个用户

**请求**

`GET /v1/users/{id}`

**参数**

无

**返回**

```json
// 成功
{
    "code": 1,
    "message": "success",
    "data": {
        "createdAt": "2019-01-15 08:36:14",
        "id": 1,
        "username": "Bill"
    }
}
// 失败
{
    "code": 0,
    "message": "用户不存在"
}
```
### 创建一个用户

**请求**

`POST /v1/users`

**参数**

```json
// Content-Type: application/json
{
	"username": "username",
	"password": "password"
}
```

 **返回**

```json
// 成功
{
    "code": 1,
    "message": "success"
}
// 失败
{
    "code": 0,
    "message": "用户已存在"
}
```
### 根据id删除单个用户

**请求**

`DELETE /v1/users/{id}`

**参数**

无

**返回**

```json
// 成功
{
    "code": 1,
    "message": "success"
}
// 失败
{
    "code": 0,
    "message": "用户不存在"
}
```