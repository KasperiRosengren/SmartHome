CREATE DEFINER=`myski`@`%` PROCEDURE `user_add_role`(
IN userName VARCHAR(255),
IN rolename VARCHAR(255)
)
thisprocedure:BEGIN
	DECLARE roleID INT DEFAULT 0;
	DECLARE userID INT DEFAULT 0;

	SELECT 
		idusers
	INTO userID FROM
		users
	WHERE
		username = userName
	LIMIT 1;
    
	IF userID = 0 THEN
		SELECT "User does not exist";
		LEAVE thisprocedure;
	END IF;

	
	SELECT 
		idroles
	INTO roleID FROM
		roles
	WHERE
		name = rolename;

	IF roleID = 0 THEN
		SELECT "Role does not exist";
		LEAVE thisprocedure;
	END IF;
    
    
	INSERT INTO users_roles(idusers, idroles) VALUES(userID, roleID);
	SELECT 'Success!';
END