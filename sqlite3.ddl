CREATE TABLE "main"."privileges" (	"priv_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	"priv_name"	TEXT NOT NULL,	"role_id"	INTEGER NOT NULL);


CREATE TABLE "main"."roles" (	"role_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	"role_name"	TEXT NOT NULL);

INSERT INTO "main"."privileges" ("priv_id", "priv_name", "role_id") VALUES ('1', 'enter spaceship via trap door', '1');
INSERT INTO "main"."privileges" ("priv_id", "priv_name", "role_id") VALUES ('2', 'start spaceship', '1');
INSERT INTO "main"."privileges" ("priv_id", "priv_name", "role_id") VALUES ('3', 'increase speed to warp 10', '1');
INSERT INTO "main"."privileges" ("priv_id", "priv_name", "role_id") VALUES ('4', 'connect spaceship to charge', '3');
INSERT INTO "main"."privileges" ("priv_id", "priv_name", "role_id") VALUES ('5', 'check battery level', '3');
INSERT INTO "main"."privileges" ("priv_id", "priv_name", "role_id") VALUES ('6', 'get water from tap near green door', '4');
INSERT INTO "main"."privileges" ("priv_id", "priv_name", "role_id") VALUES ('7', 'entry through all doors', '4');



INSERT INTO "main"."roles" ("role_id", "role_name") VALUES ('1', 'user');
INSERT INTO "main"."roles" ("role_id", "role_name") VALUES ('2', 'admin');
INSERT INTO "main"."roles" ("role_id", "role_name") VALUES ('3', 'space-pilot');
INSERT INTO "main"."roles" ("role_id", "role_name") VALUES ('4', 'guy with mop');