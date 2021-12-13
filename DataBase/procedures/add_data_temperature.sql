CREATE DEFINER=`myski`@`%` PROCEDURE `add_data_temperature`(
IN builName VARCHAR(255),
IN zoneName VARCHAR(255),
IN devName VARCHAR(255),
IN newData VARCHAR(255)
)
thisprocedure:BEGIN
DECLARE buildingID INT DEFAULT 0;
DECLARE zoneID INT DEFAULT 0;
DECLARE deviceID INT DEFAULT 0;
DECLARE timeS timestamp DEFAULT CURRENT_TIMESTAMP();

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
SELECT iddevices INTO deviceID
FROM devices
WHERE name = devName
AND idbuilding = buildingID
AND idzone = zoneID;

IF deviceID = 0 THEN
	SELECT "device does not exist in this zone";
    LEAVE thisprocedure;
END IF;

#Now that we have the deviceID we can add the new data to the temperature JSON variable
set @creation:=CONCAT('UPDATE devices SET temperature = '
					"JSON_SET(temperature, '$.value', ",newData,", '$.time', '",timeS,"') "
					'WHERE iddevices = ',deviceID,';');
PREPARE stmt from @creation;
EXECUTE stmt;

#Also add the data to the temperature data table
INSERT INTO temperature(iddevices, temperature, time) VALUES(deviceID, newData, timeS);
SELECT LAST_INSERT_ID();
END