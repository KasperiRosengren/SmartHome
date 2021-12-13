CREATE DEFINER=`myski`@`%` PROCEDURE `add_new_zone`(
IN zoneName VARCHAR(255),
IN buildName VARCHAR(255)
)
thisprocedure:BEGIN
DECLARE buildID INT DEFAULT 0;
DECLARE existingID INT DEFAULT 0;

SELECT idbuilding
INTO buildID
FROM building
WHERE name = buildName;

IF buildID = 0 THEN
	SELECT "Building does not exist";
    LEAVE thisprocedure;
END IF;

SELECT idzone
INTO existingID
FROM zone
WHERE name = zoneName;

IF existingID != 0 THEN
	SELECT "Zone already exists";
    LEAVE thisprocedure;
END IF;

INSERT INTO zone(idbuilding, name) VALUES(buildID, zoneName);
SELECT LAST_INSERT_ID();
END