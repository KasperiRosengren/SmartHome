CREATE DEFINER=`myski`@`%` PROCEDURE `role_access_zone`(
IN rolename VARCHAR(255),
IN buildingname VARCHAR(255),
IN zonename VARCHAR(255),
IN weekday TINYINT,
IN startime TIME,
IN endtime TIME,
IN accDev VARCHAR(1),
IN accSta VARCHAR(1),
IN accLoc VARCHAR(1)
)
thisprocedure:BEGIN
	DECLARE roleID INT DEFAULT 0;
	DECLARE buildingID INT DEFAULT 0;
    DECLARE zoneID INT DEFAULT 0;
	
    #Find the ID of the given rolename
	SELECT
		idroles INTO roleID
	FROM
		roles
	WHERE
		name = rolename;
	
    #If rolename doesn't exist. Leave
	IF roleID = 0 THEN
		SELECT "Role does not exist";
        LEAVE thisprocedure;
	END IF;
    
    #Find the ID of given building name
	SELECT
		idbuilding INTO buildingID
	FROM
		building
	WHERE
		name = buildingname;
	
    #If building doesn't exist. Leave
	IF buildingID = 0 THEN
		SELECT "building does not exist";
        LEAVE thisprocedure;
	END IF;
    
    
    #Find the ID of given zone,
    #in the given building
	SELECT
		idzone INTO zoneID
	FROM
		zone z
	JOIN
		building b ON
        z.idbuilding = b.idbuilding
	WHERE
		b.name = buildingname
	AND
		z.name = zonename;
	
    #If zone doesn't exist in the building. Leave
	IF zoneID = 0 THEN
		SELECT "Zone does not exist in the building";
        LEAVE thisprocedure;
	END IF;
    
    #When zone exist in the building and the role exists,
    #Insert the given variables into the
    #building_roles table
    INSERT INTO zone_roles(idroles, idzone, weekday, starttime, endtime, device, status, doorlock) VALUES(roleID, zoneID, weekday, starttime, endtime, accDev, accSta, accLoc);
    
END