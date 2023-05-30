# ## How to install:

1. Install python requirements:

```
pip install -r requirements.txt
```

2. Install **MySQL** (working on **v8.0.31**)
3. Add in the root **config.json** file of format:

```json
{
    "url": 		"link you want to scan (yandex maps)",
    "page_path": 	"Dump path",
    "db_host": 		"Database host ip",
    "db_user": 		"Database login",
    "db_password": 	"Database password",
    "db_database": 	"Database name"
}
```

4. Download dump file

```
mysql> use db_name;
mysql> source backup-file.sql;
```
