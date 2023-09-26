#import psycopg2
#from config import (
#    DB_USER,
#    DB_NAME,
#    DB_PASSWORD,
#    DB_HOST,
#    DB_PORT
#)
#
#class DBConnection:
#    def __init__(self):
#        self.user = DB_USER
#        self.dbname = DB_NAME
#        self.password = DB_PASSWORD
#        self.host = DB_HOST
#        self.port = DB_PORT
#    def __enter__(self):
#        self.conn = psycopg2.connect(
#            "user={user} dbname={dbname} password={password}".format(user=self.user,dbname=self.dbname,password=self.password),
#            host=self.host,
#            port=self.port
#        )
#        return self.conn
#    
#    def __exit__(self, ext_type, exc_value, traceback):
#        self.conn.close()
#        
#class DBControl:
#    def __inig__(self):
#        self.connection = DBConnection()
#        
#    def select(self, table, targets=None, params=None):
#        with self.connection as conn:
#            cur = conn.cursor()
#            sql = "SELECT {target_str} FROM {table}".format(
#                target_str = ",".join(targets) if targets != None else "*",
#                table = table)
#            if params:
#                sql += "WHERE {params_str}".format(
#                    params_str=" ".join(["{} = %s".format(key) for key in params.keys()]))
#            cur.execute(sql,list(params.values()))
#            result = cur.fetchall()
#            cur.close()
#        return result
#
#    def update(self, table, column, new_value, params):
#        with self.connection as conn:
#            cur = conn.cursor()
#            sql = "UPDATE {table} set {column}={new_value}".format(
#                table=table,
#                column=column,
#                new_value=new_value
#            )
#            if len(params) > 0:
#                sql + " WHERE {params_str}".format(
#                    params_str=" ".join(["{} = %s".format(key) for key in params.keys()])
#                )
#                cur.execute(sql,list(params.values()))
#            else:
#                cur.execute(sql)
#            conn.commit()
#            cur.close()
#        return
#    
#    def insert(self, table, params):
#        with self.connection as conn:
#            cur = conn.cursor()
#            sql = "INSERT INTO {table} ({column_str}) VALUES ({value_str})".format(
#                table=table,
#                column_str=",".join(list(params.keys())),
#                value_str=",".join(["%s" for i in range(len(params))])
#            )
#            cur.execute(sql, list(params.values()))
#            conn.commit()
#            cur.close()
#        return
#        