# TODO APP REST API


## GET All Task List
### Method: GET
#### URL: /todo/list-task/


#### example response: 
[
    {
        "id": 2,
        "title": "Todo satu",
        "description": "Lorem Ipsum",
        "complete": false,
        "created_at": "2022-01-04T02:38:21.299385Z",
        "updated_at": "2022-01-04T02:38:21.299385Z"
    }
]


## Add Task
### Method: POST
#### URL: /todo/add-task/

#### example request:
{
    "title": "Todo baru",
    "description": "Dolor sit amet",
    "complete": false,
}

#### example response: 
{
    "id": 3,
    "title": "Todo baru",
    "description": "Dolor sit amet",
    "complete": false,
    "created_at": "2022-01-04T02:39:43.451145Z",
    "updated_at": "2022-01-04T02:39:43.451145Z"
}


## Update Task
### Method: PUT
#### URL: /todo/update-task/<int:id>/

#### example request:
/todo/update-task/3/

{
    "title": "Todo edit",
    "description": "Dolor sit amet",
    "complete": true,
}

#### example response: 
{
    "id": 3,
    "title": "Todo edit",
    "description": "Dolor sit amet",
    "complete": true,
    "created_at": "2022-01-04T02:39:43.451145Z",
    "updated_at": "2022-01-04T02:42:29.266742Z"
}


## Delete task
### Method: DELETE
#### URL: /todo/delete-task/<int:id>/
#### example request:
/todo/delete-task/3/

#### example response: 
"Todo berhasil dihapus"
