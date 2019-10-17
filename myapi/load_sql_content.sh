#! /bin/sh

FILE_NAME="Chinook_Sqlite.sql"

if test [ ! -f '$FILE_NAME']; then
    echo "Chinook sample db query file doesnt exist, downloading..."
    wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql 
    echo "done"
fi

sqlite3 db.sqlite3 < ./Chinook_Sqlite.sql
