from flask import Flask, jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS
#_________________________________________________________________
app=Flask(__name__)
cors=CORS(app,resources={r'/*':{'origins':'*'}})
#_________________________________________________________________
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123456'
app.config['MYSQL_DB']='peluqueriadb'
mysql = MySQL(app)



@app.route('/general',methods=['POST'])
def report_general():
    try:
        fi=request.json['FechaInicial']
        ff=request.json['FechaFinal']

        cursor=mysql.connection.cursor()
        cursor.execute("""SELECT s.Id, s.NombreServicio , count(*) as cantidad from tiposervicio s , servicio ac where ac.ServicioId = s.Id  AND ac.CreationDate BETWEEN '{0}' AND '{1}' group by ac.ServicioId order by cantidad DESC""".format(fi,ff))
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Id':dato[0],'NombreServicio':dato[1],'cantidad':dato[2]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
         return('Error al observar los Usuarios')


@app.route('/persona',methods=['POST'])
def report_persona():
    try:
        fi=request.json['FechaInicial']
        ff=request.json['FechaFinal']

        cursor=mysql.connection.cursor()
        cursor.execute("""select p.Id , CONCAT(p.Nombre,' ', p.ApellidoPaterno,' ', p.ApellidoMaterno) AS 'Nombre completo' , SUM(s.Precio) as 'TotalGastado' from  servicio ac, usuario p , tiposervicio s where ac.ClienteId = p.Id and ac.ServicioId = s.Id AND ac.CreationDate BETWEEN '{0}' AND '{1}' group by ac.ClienteId order by TotalGastado desc""".format(fi,ff))
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Id':dato[0],'Nombre':dato[1],'TotalGastado':dato[2]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
         return('Error al observar los Usuarios')


@app.route('/genero',methods=['POST'])
def report_genero():
    try:
        fi=request.json['FechaInicial']
        ff=request.json['FechaFinal']

        cursor=mysql.connection.cursor()
        cursor.execute("""SELECT if(u.Genero > 0 , 'masculino', 'femenino') ,COUNT(*) AS 'Cantidad' FROM servicio s, usuario u WHERE s.ServicioId = u.Id AND s.CreationDate BETWEEN '{0}' AND '{1}' GROUP BY u.Genero ORDER BY Cantidad desc""".format(fi,ff))
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Genero':dato[0],'Cantidad':dato[1]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
         return('Error al observar los Usuarios')


@app.route('/vipSucursal',methods=['POST'])
def vip_sucursal():
    try:
        fi=request.json['FechaInicial']
        ff=request.json['FechaFinal']

        cursor=mysql.connection.cursor()
        cursor.execute("""select su.Direccion ,CONCAT(u.Nombre,' ', u.ApellidoPaterno,' ', u.ApellidoMaterno) AS 'Nombre completo' , count(*) as 'cantidad' from servicio s , sucursal su, usuario u where s.SucursalId = su.Id and s.ClienteId  =  u.Id AND s.CreationDate BETWEEN '{0}' AND '{1}' group by s.ClienteId , SucursalId order by s.SucursalId , cantidad desc """.format(fi,ff))
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Direccion':dato[0],'Nombre':dato[1],'cantidad':dato[2]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
         return('Error al observar los Usuarios')


@app.route('/servicioSucursal',methods=['POST'])
def servicio_sucursal():
    try:
        fi=request.json['FechaInicial']
        ff=request.json['FechaFinal']

        cursor=mysql.connection.cursor()
        cursor.execute("""select su.Direccion ,t.NombreServicio  , count(*) as 'cantidad' from servicio s , sucursal su, tiposervicio t  where s.SucursalId = su.Id and s.ServicioId  =  t.Id AND s.CreationDate BETWEEN '{0}' AND '{1}' group by s.ServicioId  , SucursalId order by s.SucursalId , cantidad DESC """.format(fi,ff))
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Direccion':dato[0],'NombreServicio':dato[1],'cantidad':dato[2]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
         return('Error al observar los Usuarios')


@app.route('/gastoSucursal',methods=['POST'])
def gasto_sucursal():
    try:
        fi=request.json['FechaInicial']
        ff=request.json['FechaFinal']

        cursor=mysql.connection.cursor()
        cursor.execute("""select su.Direccion ,CONCAT(u.Nombre,' ', u.ApellidoPaterno,' ', u.ApellidoMaterno) AS 'Nombre completo' , count(*) as 'cantidad', sum(t.Precio) as 'TotalGastado' from servicio s , sucursal su, usuario u, tiposervicio t  where s.SucursalId = su.Id and s.ClienteId  =  u.Id and s.ServicioId = t.Id AND s.CreationDate BETWEEN '{0}' AND '{1}' group by s.ClienteId , SucursalId order by s.SucursalId , TotalGastado desc """.format(fi,ff))
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Direccion':dato[0],'Nombre':dato[1],'cantidad':dato[2],'TotalGastado':dato[3]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
         return('Error al observar los Usuarios')


@app.route('/generoSucursal',methods=['POST'])
def genero_sucursal():
    try:
        fi=request.json['FechaInicial']
        ff=request.json['FechaFinal']

        cursor=mysql.connection.cursor()
        cursor.execute("""select su.Direccion , if(u.Genero > 0 , 'femenino', 'masculino') ,COUNT(*) AS 'Cantidad' FROM servicio s, usuario u, sucursal su WHERE s.ServicioId = u.Id and s.SucursalId = su.Id AND s.CreationDate BETWEEN '{0}' AND '{1}' GROUP BY u.Genero, s.SucursalId  ORDER BY su.Direccion """.format(fi,ff))
        datos=cursor.fetchall()
        contenedor=[]
        for dato in datos:
            reader={'Direccion':dato[0],'Genero':dato[1],'Cantidad':dato[2]}
            contenedor.append(reader)
        return contenedor        
    except Exception as ex:
         return('Error al observar los Usuarios')

if(__name__ == '__main__'):
    app.run( debug = True, port=3000)