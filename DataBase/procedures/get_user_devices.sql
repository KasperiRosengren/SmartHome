CREATE DEFINER=`myski`@`%` PROCEDURE `get_user_devices`(
IN userID VARCHAR(255)
)
thisprocedure:BEGIN
	SELECT
		d.iddevices AS devID,
        b.name AS Building,
        z.name AS Zone,
        d.name AS devName,
        dt.types AS dataTypes
	FROM users u
	JOIN users_roles ur ON u.idusers=ur.idusers
    JOIN roles r ON ur.idroles=r.idroles
    JOIN zone_roles zr ON r.idroles=zr.idroles
    JOIN zone z ON zr.idzone=z.idzone
    JOIN building b ON z.idbuilding=b.idbuilding
    JOIN devices d ON z.idzone=d.idzone
    JOIN data_types dt ON d.iddevices=dt.iddevices
    WHERE
		u.idusers = userID;

END