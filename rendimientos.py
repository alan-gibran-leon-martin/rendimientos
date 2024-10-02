#Rendimientos para fondo de inversiòn
import pandas as pd
import statistics as sts
rendimientos = pd.read_csv("./rendimientos.csv")
vacia= [0]
fecha= rendimientos.columns[0]
fecha = pd.to_datetime (rendimientos[fecha])
precio = rendimientos.columns [1]
precio= rendimientos[precio]
analisis_ren = [(precio[i+1]- precio[i])/ precio[i] for i in range (len(precio)-1)]
fecha2= [dia + pd.Timedelta(days=1) for dia in fecha]

media= sts.mean (analisis_ren)
moda = sts.mode(analisis_ren)
mediana = sts.median(analisis_ren)

vacia.extend(analisis_ren)

tabla_final = pd.DataFrame({
    "fecha": fecha,
    "precio": precio,
    "Analisis de rendimientos": vacia
    })
print(f"Los estadisticos del analisis de rendimiento es:\n Media: {media} \n Moda: {moda} \n Mediana {mediana}")
tabla_final.to_csv("./tabla_final.csv")

