CREATE DEFINER=`myski`@`%` PROCEDURE `add_new_device_outlet`(
IN builName VARCHAR(255),
IN zoneName VARCHAR(255),
IN devName VARCHAR(255),
IN outletBoxOriginalName VARCHAR(255),
IN outletOriginalName VARCHAR(255),
IN outletName VARCHAR(255),
IN outletPosition VARCHAR(255)
)
thisprocedure:BEGIN
DECLARE buildingID INT DEFAULT 0;
DECLARE zoneID INT DEFAULT 0;
DECLARE deviceID INT DEFAULT 0;
DECLARE boxID INT DEFAULT 0;
DECLARE outletID INT DEFAULT 0;

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

SELECT idoutletbox INTO boxID
FROM outletbox
WHERE iddevices = deviceID
AND originalname = outletBoxOriginalName;

IF boxID = 0 THEN
	SELECT 'Outletbox does not exist in this device';
    LEAVE thisprocedure;
end if;

SELECT idoutlets INTO outletID
FROM outlets
WHERE idoutletbox = boxID
AND originalname = outletOriginalName;

IF outletID != 0 THEN
	SELECT 'Outlet already exists in this Box';
    LEAVE thisprocedure;
end if;


set @creation:=CONCAT('UPDATE devices SET outlets = '
					"JSON_SET(outlets, '$.",outletBoxOriginalName,".outlets.",outletOriginalname,"', JSON_OBJECT(
                                'name','",outletName,"', 'position', '",outletPosition,"', 'status', 'off'))"
					'WHERE iddevices = ',deviceID,';');
PREPARE stmt from @creation;
EXECUTE stmt;

#Also add the data to the temperature data table
INSERT INTO outlets(idoutletbox, originalname, name, position, status, time) VALUES(boxID, outletOriginalName, outletName, outletPosition, 'off', CURRENT_TIMESTAMP());
END