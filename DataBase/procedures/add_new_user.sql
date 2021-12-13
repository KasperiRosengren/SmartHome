CREATE DEFINER=`myski`@`%` PROCEDURE `add_new_user`(
IN newusername VARCHAR(255),
IN pswd VARCHAR(255)
)
thisprocedure:BEGIN
DECLARE existingID INT DEFAULT 0;

SELECT idusers
INTO existingID
FROM users
WHERE username = newusername;

IF existingID != 0 THEN
	SELECT "User already exists";
    LEAVE thisprocedure;
END IF;

INSERT INTO users(username, password) VALUES(newusername, pswd);
SELECT LAST_INSERT_ID();
END