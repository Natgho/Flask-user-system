# Flask-user-system
Flask user register and login system

# How to Build?
> You have two option, short way, use docker. Long way;

1. Create Mysql docker container (If you have MySQL service, skip this step);
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
python dummy_processes.py
python setup.py
```
----
Test usernames and passwords:
* Sezer test123
* Barış 123test!.
* BengiSu 123test123
* Ayça 123test123

## Docker way
```bash
docker-compose up
# If you want to install dummy data
docker exec -d flask-core-system python3 dummy_processes.py
```
Thats all :)