CREATE DEFINER=`myski`@`%` PROCEDURE `add_new_device`(
IN builName VARCHAR(255), 
IN zoneName VARCHAR(255),
IN devName VARCHAR(255), 
IN location VARCHAR(255)
)
thisprocedure:BEGIN
declare thisIDzone INT DEFAULT 0;
declare IDbuild INT DEFAULT 0;
declare existingDeviceID INT DEFAULT 0;

SELECT 
    idbuilding
INTO IDbuild FROM
    building
WHERE
    name = builName;

IF IDbuild = 0 THEN
	SELECT "Building does not exist";
    LEAVE thisprocedure;
END IF;

SELECT 
    idzone
INTO thisIDzone FROM
    zone
WHERE
    name = zoneName
AND
	idbuilding = IDbuild;

IF thisIDzone = 0 THEN
	SELECT "Zone does not exist";
    LEAVE thisprocedure;
END IF;


SELECT iddevices INTO existingDeviceID
FROM devices
WHERE
	idzone = thisIDzone
AND
	idbuilding = IDbuild
AND
	name = devName;

IF existingDeviceID != 0 THEN
	SELECT "Device already exists";
    LEAVE thisprocedure;
END IF;




#INSERT INTO devices(idbuilding, idzone, name, location) VALUES(IDbuild, thisIDzone, devName, location);
INSERT INTO devices VALUES(DEFAULT, IDbuild, thisIDzone, devName, location, JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT(), JSON_OBJECT());
SELECT LAST_INSERT_ID();
END