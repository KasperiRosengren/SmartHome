CREATE DEFINER=`myski`@`%` PROCEDURE `get_zone_temperature_daily`(
IN buildingName VARCHAR(255),
IN zoneName VARCHAR(255)
)
thisprocedure:BEGIN
	DECLARE buildingID INT DEFAULT 0;
    DECLARE zoneID INT DEFAULT 0;
    
    SELECT idbuilding INTO buildingID
    from building WHERE name = buildingName;
    
    IF buildingID = 0 THEN
		SELECT 'Building does not exist';
        LEAVE thisprocedure;
    END IF;
    
    SELECT idzone INTO zoneID
    from zone WHERE name=zoneName AND idbuilding=buildingID;
    
    if zoneID = 0 THEN
		SELECT 'Zone does not exist in this building';
		LEAVE thisprocedure;
	END IF;
    
    
    SELECT
		d.name,
		JSON_OBJECT(
			'temperature', JSON_ARRAYAGG(t.temperature),
			'time', JSON_ARRAYAGG(DATE_FORMAT(t.time, '%H:%i'))) AS lastday
	FROM
		devices d JOIN temperature t ON d.iddevices=t.iddevices
	WHERE
		d.idbuilding = buildingID
	AND
		d.idzone = zoneID
	AND
		time > now() - INTERVAL 24 hour
	GROUP BY d.name;

END