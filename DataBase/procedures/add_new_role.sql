CREATE DEFINER=`myski`@`%` PROCEDURE `add_new_role`(
IN rolename VARCHAR(255)
)
thisprocedure:BEGIN
	DECLARE existingID INT DEFAULT 0;

	SELECT idroles
	INTO existingID
	FROM roles
	WHERE name = rolename;

	IF existingID != 0 THEN
		SELECT "Role already exists";
		LEAVE thisprocedure;
	END IF;

	INSERT INTO roles(name) VALUES(rolename);
	SELECT LAST_INSERT_ID();
END