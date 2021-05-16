CREATE PROCEDURE `new_device` (
IN devName VARCHAR(255), 
IN devDesc TEXT, 
IN builName VARCHAR(255), 
IN zoneName VARCHAR(255),
OUT createdDevice INT
)
thisprocedure:BEGIN
declare IDzone INT DEFAULT 0;
declare IDbuild INT DEFAULT 0;

SELECT idbuilding
INTO IDbuild
FROM building
WHERE name = builName;

IF IDbuild = 0 THEN
	SELECT 'Building does not exist';
    LEAVE thisprocedure;
END IF;

SELECT idzone
INTO IDzone
FROM zone
WHERE name = zoneName;

IF IDzone = 0 THEN
	SELECT 'Zone does not exist';
    LEAVE thisprocedure;
END IF;

INSERT INTO devices(idbuilding, idzone, name, description) VALUES(IDbuild, IDzone, devName, devDesc);
SELECT last_insert_id() INTO createdDevice;
END