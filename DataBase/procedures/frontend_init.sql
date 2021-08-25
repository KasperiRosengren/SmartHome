CREATE DEFINER=`myski`@`%` PROCEDURE `frontend_init`(
IN userID INT
)
thisprocedure:BEGIN
#Saves the access code to the temporary table created in
#The get_user_device_data1
CREATE TEMPORARY TABLE useraccess AS
SELECT 
    b.name AS BuildingName,
    z.name AS ZoneName,
    d.name AS DeviceName,
    r.name AS RoleName,
	r.idroles AS RoleID,
    br.device AS DevAcc,
    br.status AS StaAcc,
    br.doorlock AS LocAcc,
	br.building AS BuiAcc,
	d.*
FROM users u
JOIN users_roles ur ON 
	u.idusers = ur.idusers
JOIN roles r ON
	ur.idroles = r.idroles
JOIN building_roles br ON
	r.idroles = br.idroles
JOIN building b ON 
	br.idbuilding = b.idbuilding
JOIN zone z ON
	b.idbuilding = z.idbuilding
JOIN devices d ON
	z.idzone = d.idzone
WHERE
	u.idusers = userID
AND
	br.weekday = WEEKDAY(CURDATE())
AND
	br.starttime <= CURRENT_TIME()
AND
	br.endtime > CURRENT_TIME();


INSERT INTO useraccess
SELECT 
    b.name AS BuildingName,
    z.name AS ZoneName,
    d.name AS DeviceName,
    r.name AS RoleName,
	r.idroles AS RoleID,
    zr.device AS DevAcc,
    zr.status AS StaAcc,
    zr.doorlock AS LocAcc,
    NULL,
	d.*
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
JOIN devices d ON
	z.idzone = d.idzone
WHERE
	u.idusers = userID
AND
	zr.weekday = WEEKDAY(CURDATE())
AND
	zr.starttime <= CURRENT_TIME()
AND
	zr.endtime > CURRENT_TIME();
    
    
SELECT * FROM useraccess;
DROP TEMPORARY TABLE useraccess;

END