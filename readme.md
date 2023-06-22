## Description
Many restaurants want to improve their rating on various platforms, and for this 
they write custom reviews. **We are an open source project to identify custom reviews
for restaurants, bars and cafés on Yandex maps.** Our solution is designed for regular
users who want to make the right restaurant choice, and for site moderators to make
their job easier.  Our browser extension will show the likelihood that the review is 
a commissioned one. 

**It is important** to say that we do not undertake to consider the review exactly ordered
or not, we only ask to pay attention to such a review.

## How to install:

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
5. Download Google extension called **Reviews Project**