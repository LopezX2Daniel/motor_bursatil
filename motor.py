import mysql.connector as server
from datetime import datetime
import time

db = server.connect(host="localhost", user="root", passwd="", db="emparejamiento")
db.autocommit = True
query = db.cursor(dictionary=True)

while True:
    
    time.sleep(0.1)
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"))
    
    query.execute("SELECT precio from p_compra order by precio DESC LIMIT 1")
    compra_check = query.fetchall()
    print(compra_check)
    
    query.execute("SELECT precio from p_venta order by precio ASC LIMIT 1")
    venta_check = query.fetchall()
    print(venta_check)
    
    try:
        if compra_check[0]["precio"] == venta_check[0]["precio"]:
            print("Existe match")
            precio_muestra = float(compra_check[0]["precio"])
            
            query.execute(f"SELECT * from p_compra WHERE precio = '{precio_muestra}' order by precio DESC, fecha_hora ASC")
            p_compra = query.fetchall()
            query.execute(f"SELECT * from p_venta WHERE precio = '{precio_muestra}' order by precio DESC, fecha_hora ASC")
            p_venta = query.fetchall()

            posicion_compra = 0

            for posicion_venta in range(len(p_venta)):
                titulos_disponibles_venta = p_venta[posicion_venta]["titulos"]
                while titulos_disponibles_venta > 0:
                    try:
                        if p_compra[posicion_compra]["titulos"] <= p_venta[posicion_venta]["titulos"]:
                            titulos_disponibles_venta = p_venta[posicion_venta]["titulos"]-p_compra[posicion_compra]["titulos"]
            
                            query.execute(f"DELETE FROM p_compra WHERE folio = {p_compra[posicion_compra]['folio']}")
                            ahora = datetime.today().strftime("%Y/%m/%d %H:%M:%S.%f")
                            query.execute(f"INSERT into hechos (emisora, precio, titulos, comprador, folio_comprador, vendedor, folio_vendedor, fecha_hora) VALUES ('{p_compra[posicion_compra]['emisora']}', '{p_compra[posicion_compra]['precio']}', '{p_compra[posicion_compra]['titulos']}', '{p_compra[posicion_compra]['casa']}', '{p_compra[posicion_compra]['folio']}', '{p_venta[posicion_venta]['casa']}', '{p_venta[posicion_venta]['folio']}', '{ahora}')")
                            p_compra[posicion_compra] = {'folio':p_compra[posicion_compra]['folio'], 'emisora':'', 'precio':'', 'titulos':0, 'casa':''}
                            posicion_compra=posicion_compra+1
                            if titulos_disponibles_venta > 0:
                                query.execute(f"UPDATE p_venta SET titulos = {titulos_disponibles_venta} WHERE folio = {p_venta[posicion_venta]['folio']}")
                                p_venta[posicion_venta] = {'folio':p_venta[posicion_venta]['folio'], 'emisora':p_venta[posicion_venta]['emisora'], 'precio':p_venta[posicion_venta]['precio'], 'titulos':titulos_disponibles_venta, 'casa':p_venta[posicion_venta]['casa']}
                            elif titulos_disponibles_venta == 0:
                                query.execute(f"DELETE FROM p_venta WHERE folio = {p_venta[posicion_venta]['folio']}")
                                p_venta[posicion_venta] = {'folio':p_venta[posicion_venta]['folio'], 'emisora':'', 'precio':'', 'titulos':0, 'casa':''}
                            continue
                        else:
                            titulos_disponibles_venta = 0
                            titulos_remanentes_compra = p_compra[posicion_compra]["titulos"]-p_venta[posicion_venta]["titulos"]
                            
                            query.execute(f"DELETE FROM p_venta WHERE folio = {p_venta[posicion_venta]['folio']}")
                            ahora = datetime.today().strftime("%Y/%m/%d %H:%M:%S.%f")
                            query.execute(f"INSERT into hechos (emisora, precio, titulos, comprador, folio_comprador, vendedor, folio_vendedor, fecha_hora) VALUES ('{p_venta[posicion_venta]['emisora']}', '{p_venta[posicion_venta]['precio']}', '{p_venta[posicion_venta]['titulos']}', '{p_compra[posicion_compra]['casa']}', '{p_compra[posicion_compra]['folio']}', '{p_venta[posicion_venta]['casa']}', '{p_venta[posicion_venta]['folio']}', '{ahora}')")
                            p_venta[posicion_venta] = {'folio':p_venta[posicion_venta]['folio'], 'emisora':'', 'precio':'', 'titulos':0, 'casa':''}
                            if titulos_remanentes_compra > 0:
                                query.execute(f"UPDATE p_compra SET titulos = {titulos_remanentes_compra} WHERE folio = {p_compra[posicion_compra]['folio']}")
                                p_compra[posicion_compra] = {'folio':p_compra[posicion_compra]['folio'], 'emisora':p_compra[posicion_compra]['emisora'], 'precio':p_compra[posicion_compra]['precio'], 'titulos':titulos_remanentes_compra, 'casa':p_compra[posicion_compra]['casa']}
                            elif titulos_remanentes_compra == 0:
                                query.execute(f"DELETE FROM p_compra WHERE folio = {p_compra[posicion_compra]['folio']}")
                                p_compra[posicion_compra] = {'folio':p_compra[posicion_compra]['folio'], 'emisora':'', 'precio':'', 'titulos':0, 'casa':''}
                                posicion_compra=posicion_compra+1
                            continue
                    except IndexError:
                        break
    except IndexError:
        continue
