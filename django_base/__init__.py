#解决pymysql导致的数据库连接报错问题↓
import pymysql
pymysql.install_as_MySQLdb()