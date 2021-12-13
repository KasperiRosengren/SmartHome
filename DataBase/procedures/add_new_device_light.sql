CREATE DEFINER=`myski`@`%` PROCEDURE `add_new_device_light`(
IN builName VARCHAR(255),
IN zoneName VARCHAR(255),
IN devName VARCHAR(255),
IN lightOriginalName VARCHAR(255),
IN lightName VARCHAR(255)
)
thisprocedure:BEGIN
DECLARE buildingID INT DEFAULT 0;
DECLARE zoneID INT DEFAULT 0;
DECLARE deviceID INT DEFAULT 0;
DECLARE lightID INT DEFAULT 0;

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

#Check if light already exists
SELECT idlights INTO lightID
FROM lights
WHERE originalname = lightOriginalName
AND
	iddevices = deviceID;

IF lightID != 0 THEN
	SELECT 'Light already exists';
    LEAVE thisprocedure;
end if;

set @creation:=CONCAT('UPDATE devices SET lights = '
					"JSON_SET(lights, '$.",lightOriginalname,"', JSON_OBJECT(
                                'name','",lightName,"',
                                'status', 'off',
                                'color_0', 'red',
                                'color_1', 'blue',
                                'color_2', 'green'))"
					'WHERE iddevices = ',deviceID,';');
PREPARE stmt from @creation;
EXECUTE stmt;

#Also add the data to the light data table
INSERT INTO lights(iddevices, originalname, name, status, color_0, color_1, color_2, time) VALUES(deviceID, lightOriginalName, lightName, "off", 'red', 'blue', 'green', CURRENT_TIMESTAMP());
END