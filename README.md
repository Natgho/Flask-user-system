# Flask-user-system
Flask user register and login system

# How to Build?
1. Create Mysql docker container;
```bash
docker run --name flask-mysql-service -e MYSQL_ROOT_PASSWORD=test_password -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```
2. Create virtualenv and install requirements;
```bash
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Change env.example name to .env and fill in the content appropriately.
4. The code that will create the database;
```bash
python db.conf.py
```