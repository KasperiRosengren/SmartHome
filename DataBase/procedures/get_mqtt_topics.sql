CREATE PROCEDURE `get_mqtt_topics` ()
thisprocedure:BEGIN
#Example topic 'Building/Zone/Device/Data'
#One real topic 'home/livingroom/ceiling/temp
#This doesn't actually build the topic, but the backend can combine every
#row as individual topic
#columns are:
# Building name, Zone name, Device name, Data types
# The backend will pick apart the json formated datatypes
	SELECT
		b.name AS building,
        z.name AS zone,
        d.name AS device,
        d.datatypes AS datatypes
	FROM building b
    JOIN zone z ON b.idbuilding = z.idbuilding
    JOIN devices d ON z.idzone = d.idzone;
END