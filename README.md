## Install and run project
```
$ git clone https://github.com/vubom01/pet-rescue
$ cd pet-rescue
$ virtualenv -p python3 .venv
$ source .venv/bin/activate (Ubuntu)
  .venv\Scripts\activate (Windows)
$ pip install -r requirements.txt
$ uvicorn app.main:app --host 127.0.0.1 --port 8000
$ gunicorn -k uvicorn.workers.UvicornWorker --bind "0.0.0.0:8080"  app.main:app
```

## Cấu trúc project
```
├── app  
│   ├── api         // các file api được đặt trong này
│   ├── core        // config and sercurity
│   ├── db          // cấu hình database
│   ├── helpers     // các function hỗ trợ
│   ├── schemas     // Pydantic Schema 
│   ├── services    // Chứa logic CRUD giao tiếp với DB  
│   └── main.py     // cấu hình chính của toàn bộ project  
├── .gitignore  
├── Procfile
├── README.md  
├── requirements.txt
└── runtime.txt
  
