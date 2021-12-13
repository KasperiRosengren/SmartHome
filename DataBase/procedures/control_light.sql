CREATE DEFINER=`myski`@`%` PROCEDURE `control_light`(
IN builName VARCHAR(255),
IN zoneName VARCHAR(255),
IN devName VARCHAR(255),
IN lightName VARCHAR(255),
IN newstatus VARCHAR(255),
IN newColor VARCHAR(255),
IN newPattern VARCHAR(255)
)
thisprocedure:BEGIN
DECLARE buildingID INT DEFAULT 0;
DECLARE zoneID INT DEFAULT 0;
DECLARE deviceID INT DEFAULT 0;

#First we need to check if the building with the given
#name exists. If not, leave function.
SELECT idbuilding INTO buildingID
FROM building
WHERE name = builName;

IF buildingID = 0 THEN
	SELECT "Building does not exist";
    LEAVE thisprocedure;
END IF;


#Then we need to check if the zone exists inside the given building
#Again if it does not, leave function
SELECT idzone INTO zoneID
FROM zone
WHERE name = zoneName
AND idbuilding = buildingID;

IF zoneID = 0 THEN
	SELECT "Zone does not exist in this building";
    LEAVE thisprocedure;
END IF;

#Then we need to see if the device exists
#in the given zone. Leave function if it does not
SELECT iddevice INTO deviceID
FROM devices
WHERE name = devName
AND idbuilding = buildingID
AND idzone = zoneID;

IF deviceID = 0 THEN
	SELECT "device does not exist int his zone";
    LEAVE thisprocedure;
END IF;


#Now that we have the deviceID we can add the new data to the lights JSON variable
#in the devices table
set @creation:=CONCAT('UPDATE devices '
					"JSON_SET(lights, '$.",lightName.status,"', ",newStatus,", '$.",lightName.color,"', ",newColor,", '$.",lightName.pattern,"', ",newPattern,")"
					'WHERE iddevices = ',deviceID);
PREPARE stmt from @creation;
EXECUTE stmt;

#Also add the data to the lights data table
INSERT INTO lights(iddevices, name, status, color, pattern, time)
	VALUES(deviceID, lightName, newStatus, newColor, newPattern, CURRENT_TIMESTAMP());

END