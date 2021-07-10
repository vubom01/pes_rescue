## Install 
```
$ git clone https://github.com/vubom01/pet_rescue
$ cd pet_rescue
$ virtualenv -p python3 .venv
$ source .venv/bin/activate (Ubuntu)
  .venv\Scripts\activate (Windows)
$ pip install -r requirements.txt
```

## Connect database 
```
$ docker build -t {name_image} .
$ docker run --name {name} --restart unless-stopped -p 3306:3306 -d {name_image}
```

## Cấu trúc project
```
├── app  
│   ├── api         // các file api được đặt trong này  
│   ├── schemas     // Pydantic Schema  
│   ├── services    // Chứa logic CRUD giao tiếp với DB  
│   └── main.py     // cấu hình chính của toàn bộ project  
├── .gitignore  
├── Dockerfile
├── pet_rescue.sql  // database
├── README.md  
└── requirements.txt
  