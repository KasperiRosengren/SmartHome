CREATE DEFINER=`myski`@`%` PROCEDURE `alter_role_building_rules`(
IN rolename VARCHAR(255),
IN buildingname VARCHAR(255),
IN oldweekday TINYINT,
IN oldstarttime TIME,
IN oldendtime TIME,
IN newweekday TINYINT,
IN newstarttime TIME,
IN newendtime TIME,
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
    UPDATE building_roles SET
		weekday = newweekday,
        starttime = newstarttime,
        endtime = newendtime,
        device = accDev,
        status = accSta,
        doorlock = accLoc,
        building = accBui
	WHERE
		idroles = roleID
	AND
		idbuilding = buildingID
	AND
		weekday = oldweekday
	AND
		starttime = oldstarttime
	AND
		endtime = oldendtime;

END