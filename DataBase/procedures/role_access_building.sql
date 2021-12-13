CREATE DEFINER=`myski`@`%` PROCEDURE `role_access_building`(
IN rolename VARCHAR(255),
IN buildingname VARCHAR(255),
IN weekday TINYINT,
IN startime TIME,
IN endtime TIME,
IN accDev VARCHAR(1),
IN accSta VARCHAR(1),
IN accLoc VARCHAR(1),
IN accBui VARCHAR(1)
)
thisprocedure:BEGIN
	DECLARE roleID INT DEFAULT 0;
	DECLARE buildingID INT DEFAULT 0;
	
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
    
    #When building and role exists,
    #Insert the given variables into the
    #building_roles table
    INSERT INTO building_roles(idroles, idbuilding, weekday, starttime, endtime, device, status, doorlock, building) VALUES(roleID, buildingID, weekday, starttime, endtime, accDev, accSta, accLoc, accBui);
    
END