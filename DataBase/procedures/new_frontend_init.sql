CREATE DEFINER=`myski`@`%` PROCEDURE `new_frontend_init`(
IN userName VARCHAR(255)
)
thisprocedure:BEGIN
#Saves the access code to the temporary table created in
#The get_user_device_data1
	DECLARE userID INT DEFAULT 0;
    DROP TEMPORARY TABLE IF EXISTS useraccess;
	SELECT 
			idusers
		INTO userID FROM
			users
		WHERE
			username = userName
		LIMIT 1;
		
		IF userID = 0 THEN
			SELECT "User does not exist";
			LEAVE thisprocedure;
		END IF;



	CREATE TEMPORARY TABLE useraccess(
    Building VARCHAR(255),
	Zone varchar(255),
    ZoneID INT,
    outlets JSON,
    lights JSON,
    temperature JSON,
    humidity JSON,
    airpressure JSON,
    brightness JSON,
    motion JSON,
    leakage JSON,
    smokedetector JSON,
    doorlock JSON,
    noicedetector JSON,
    UNIQUE (Building, Zone)
    );
	
    INSERT INTO useraccess(Building, Zone, ZoneID, outlets, lights, temperature, humidity, airpressure, brightness, motion, leakage, smokedetector, doorlock, noicedetector)
	SELECT b.name, z.name, z.idzone,
		JSON_ARRAYAGG(JSON_OBJECT('outlets',d.outlets, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('lights',d.lights, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('temperature',d.temperature, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('humidity',d.humidity, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('airpressure',d.airpressure, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('brightness',d.brightness, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('motion',d.motion, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('leakage',d.leakage, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('smokedetector',d.smokedetector, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('doorlock',d.doorlock, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('noicedetector',d.noicedetector))
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
		br.endtime > CURRENT_TIME()
	GROUP BY b.name, z.name, z.idzone;
	
    
    
    
    REPLACE INTO useraccess(Building, Zone, ZoneID, outlets, lights, temperature, humidity, airpressure, brightness, motion, leakage, smokedetector, doorlock, noicedetector)
	SELECT b.name, z.name, z.idzone,
		JSON_ARRAYAGG(JSON_OBJECT('outlets',d.outlets, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('lights',d.lights, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('temperature',d.temperature, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('humidity',d.humidity, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('airpressure',d.airpressure, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('brightness',d.brightness, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('motion',d.motion, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('leakage',d.leakage, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('smokedetector',d.smokedetector, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('doorlock',d.doorlock, 'location', d.location)),
        JSON_ARRAYAGG(JSON_OBJECT('noicedetector',d.noicedetector))
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
		zr.endtime > CURRENT_TIME()
	GROUP BY b.name, z.name, z.idzone;
    
    
    
	SELECT * FROM useraccess;
	DROP TEMPORARY TABLE useraccess;

END