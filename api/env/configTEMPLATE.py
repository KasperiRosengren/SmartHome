class TestConfig(object):
    DEBUG = True
    TESTING = True

    #Database config
    MYSQL_HOST = 'HOST URL'
    MYSQL_USER = 'HOST USERNAME'
    MYSQL_PASSWORD = 'HOST PASSWORD'
    MYSQL_DB = 'HOST DB NAME'

    #MQTT config
    MQTT_BROKER_URL = 'HOST URL'
    MQTT_BROKER_PORT = HOSTPORT
    MQTT_REFRESH_TIME = 1.0
