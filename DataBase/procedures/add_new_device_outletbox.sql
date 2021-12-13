CREATE DEFINER=`myski`@`%` PROCEDURE `add_new_device_outletbox`(
IN builName VARCHAR(255),
IN zoneName VARCHAR(255),
IN devName VARCHAR(255),
IN outletBoxOriginalName VARCHAR(255),
IN outletBoxName VARCHAR(255),
IN outletBoxPosition VARCHAR(255)
)
thisprocedure:BEGIN
DECLARE buildingID INT DEFAULT 0;
DECLARE zoneID INT DEFAULT 0;
DECLARE deviceID INT DEFAULT 0;
DECLARE boxID INT DEFAULT 0;

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

IF boxID != 0 THEN
	SELECT 'This box already exists';
    LEAVE thisprocedure;
end if;



#Now that we have the deviceID we can add the new data to the outletbox JSON variable
set @creation:=CONCAT('UPDATE devices SET outlets = '
					"JSON_SET(outlets, '$.",outletBoxOriginalName,"', JSON_OBJECT('position', '",outletBoxPosition,"',
								'name', '",outletBoxName,"',
                                'outlets', JSON_OBJECT('outlet_0', JSON_OBJECT('name','default', 'position', 'default', 'status', 'default'))))"
					'WHERE iddevices = ',deviceID,';');
PREPARE stmt from @creation;
EXECUTE stmt;

#Also add the data to the temperature data table
INSERT INTO outletbox(iddevices, originalname, name, position) VALUES(deviceID, outletBoxOriginalName, outletBoxName, outletBoxPosition);

END