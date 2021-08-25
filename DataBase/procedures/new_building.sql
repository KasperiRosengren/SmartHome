CREATE PROCEDURE `new_building` (
IN builName VARCHAR(255),
IN builAdd VARCHAR(255),
OUT IDbuilding INT
)
thisprocedure:BEGIN
DECLARE existingID INT DEFAULT 0;

SELECT idbuilding
INTO existingID
FROM building
WHERE name = builName;

IF existingID != 0 THEN
	SELECT `Building already exists`;
    LEAVE thisprocedure;
END IF;

INSERT INTO building(name, address) VALUES(builName, builAdd);
SELECT LAST_INSERT_ID() INTO IDbuilding;
END