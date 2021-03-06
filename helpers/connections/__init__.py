import arctic
import pymysql
import rethinkdb as r
import redis

def get_arctic_store(config):
	''' get arctic connection '''

	return arctic.Arctic(config.get('MONGODB', 'MONGO_SERVER'))

def get_mysql_connection(config):
    ''' get mysql connection '''

    return pymysql.connect(host=config.get('MYSQL', 'MYSQL_HOST'),
                            user=config.get('MYSQL', 'MYSQL_USER'),
                            passwd=config.get('MYSQL', 'MYSQL_PASSWD'),
                            db=config.get('MYSQL', 'MYSQL_DATABASE'))

def get_rethink_connection(config):
	''' get rethink db connection  '''

	rethink_conn = r.connect(host=config.get('RETHINKDB', 'RETHINK_HOST'),\
								port=config.get('RETHINKDB', 'RETHINK_PORT'),\
								db=config.get('RETHINKDB', 'RETHINK_DB'),\
								user=config.get('RETHINKDB', 'RETHINK_USER'),\
								password=config.get('RETHINKDB', 'RETHINK_PASSWORD'),\
								timeout=int(config.get('RETHINKDB', 'RETHINK_TIMEOUT')))
	return rethink_conn

def get_redis_connection(config):

	return redis.Redis(
		host=config.get('REDIS', 'REDIS_HOST'),\
		port=config.get('REDIS', 'REDIS_PORT'),\
		db=config.get('REDIS', 'REDIS_DB'),\
	)
