## Install and running app
```
$ git clone https://github.com/vubom01/pes_rescue
$ cd pes_rescue
$ virtualenv -p python3 .venv
$ source .venv/bin/activate (Ubuntu)
  .venv\Scripts\activate (Windows)
$ pip install -r requirements.txt
$ cd app
$ python main.py
```

## Cấu trúc project
```
├── app  
│   ├── api         // các file api được đặt trong này  
│   ├── models      // Database model, tích hợp với alembic để auto generate migration  
│   ├── schemas     // Pydantic Schema  
│   ├── services    // Chứa logic CRUD giao tiếp với DB  
│   └── main.py     // cấu hình chính của toàn bộ project  
├── .env-example  
├── .gitignore  
├── docker-compose.yaml  
├── pes_rescue.sql  // database
├── README.md  
└── requirements.txt