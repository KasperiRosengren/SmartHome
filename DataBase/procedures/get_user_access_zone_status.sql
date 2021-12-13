CREATE DEFINER=`myski`@`%` PROCEDURE `get_user_access_zone_status`(
IN userID INT,
IN buildingName VARCHAR(255),
IN zoneName VARCHAR(255)
)
thisprocedure:BEGIN
DECLARE buildingID INT DEFAULT 0;
DECLARE zoneID INT DEFAULT 0;

SELECT idbuilding INTO buildingID
FROM building
WHERE name = buildingName;

if buildingID = 0 THEN
	SELECT 'Building does not exist';
    LEAVE thisprocedure;
end if;

SELECT idzone INTO zoneID
FROM zone z JOIN
	building b ON
    z.idbuilding = b.idbuilding
WHERE
	z.name = zoneName AND
    b.name = buildingName;

if zoneID = 0 THEN
	SELECT 'This zone does not exist in this building';
    LEAVE thisprocedure;
end if;



#Saves the access code to the temporary table created 
CREATE TEMPORARY TABLE useraccess AS
SELECT 
    br.status AS StatusAccess
FROM users u
JOIN users_roles ur ON 
	u.idusers = ur.idusers
JOIN roles r ON
	ur.idroles = r.idroles
JOIN building_roles br ON
	r.idroles = br.idroles
JOIN building b ON 
	br.idbuilding = b.idbuilding
WHERE
	u.idusers = userID
AND
	b.idbuilding = buildingID
AND
	br.weekday = WEEKDAY(CURDATE())
AND
	br.starttime <= CURRENT_TIME()
AND
	br.endtime > CURRENT_TIME();


INSERT INTO useraccess
SELECT 
    zr.status AS StatusAccess
FROM users u
JOIN users_roles ur ON 
	u.idusers = ur.idusers
JOIN roles r ON
	ur.idroles = r.idroles
JOIN zone_roles zr ON
	r.idroles = zr.idroles
JOIN zone z ON
	zr.idzone = z.idzone
JOIN building b ON
	z.idbuilding = b.idbuilding
WHERE
	u.idusers = userID
AND
	z.idzone = zoneID
AND
	zr.weekday = WEEKDAY(CURDATE())
AND
	zr.starttime <= CURRENT_TIME()
AND
	zr.endtime > CURRENT_TIME();
    
    
SELECT * FROM useraccess;
DROP TEMPORARY TABLE useraccess;

END