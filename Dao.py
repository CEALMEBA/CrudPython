from Conexion import Conecttion
from persona import Person


class Dao(object):

   # Conec = Conexion.Conecttion()
    Conec = Conecttion()

    def insert(self, persona):
        sql = """INSERT INTO per (clave,nombre,direccion,telefono) VALUES(%s,%s,%s,%s) """
        toInsert = (persona.get_id(), persona.get_name(), persona.get_address(), persona.get_phone())
        self.Conec.execute(sql,toInsert)

    def update(self, persona):
        sql = """UPDATE per SET  nombre = %s ,direccion=%s,telefono = %s where clave = %s"""
        toUpdate_ = (persona.get_name(), persona.get_address(), persona.get_phone(), persona.get_id())
        self.Conec.execute(sql,toUpdate_)


    def delete(self, persona):
        sql = """DELETE FROM per WHERE clave =%s"""
        toDelete = (persona.get_id(),)
        self.Conec.execute(sql, toDelete)


    def find(self, persona):
        sql = """select * from  per where clave =%s"""
        toFind = (persona.get_id())
        self.Conec.executeQuery(sql,toFind)

    def findAll(self):
        sql = """select * from per"""
        toRead = ('per')
        self.Conec.executeQuery(sql)

if __name__ == '__main__':
    da = Dao()
    pr = Person()
    #pr.set_name('beto')
    pr.set_id('10')
    #pr.set_address('casa')
   # pr.set_phone('2222')

    #da.insert(pr)

    #da.update(pr)
    #da.delete(pr)
    #da.find(pr)

