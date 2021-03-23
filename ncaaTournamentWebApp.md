# NCAA Tournament Web App

## Notes
* Need to identify what databases work the best with flask, for medium usage
* Test using SQAlchemy to interact with the db
* Continue interpreting what tables will be needed and what should be captured per table

## Structure
Currently built based on the flask tutorial. Will update based on the apps need.
```
|-- ncaa/
|   |-- __init__.py
|   |-- db.py
|   |-- schema.sql
|   |-- auth.py
|   |-- blog.py
|   |-- templates/
|   |   |-- base.html
|   |   |-- auth/
|   |   |   |-- login.html
|   |   |   |-- register.html
|   |   |--blog/
|   |       |-- create.html
|   |       |-- index.html
|   |       |-- update.html
|   |-- static/|
|       |-- style.css
|-- tests/
|   |-- conftest.py
|   |-- data.sql
|   |-- testFactory.py
|   |-- testDb.py
|   |-- testAuth.py
|   |-- testBlog.py
|-- venv/
|-- setup.py
|-- MANIFEST.in
```

## Tables
A map of the tables needed to store and provide bets to users.
* Teams
    * Record ID#
    * Date Created
    * Record Owner
    * Date Modified
    * Last Modified By
    * Name
    * Seed
    * Region
    * Picked By (list of Participants who picked the team)
* Participants
    * Record ID#
    * Date Created
    * Record Owner
    * Date Modified
    * Last Modified By
    * Name
    * Email
    * Entry Fee (BOOL)
    * Entry Fee2 (BOOL)
    * Entry Fee3 (BOOL)
    * Image
* Games/Schedule
    * Record ID#
    * Date Created
    * Record Owner
    * Date Modified
    * Last Modified By
    * Date/Time
    * Home
    * Away
* Bets
    * Record ID#
    * Date Created
    * Record Owner
    * Date Modified
    * Last Modified By
    * Participant
    * Team
    * Team2
    * Team3
    * Team4
