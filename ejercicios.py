import pandas as pd
import matplotlib.pyplot as plt






# ANTES DE CORRER EL CODIGO DESCARGAR DEPENDENCIAS, LUEGO DE DESCARGARLAS, INGRESAR EL SIGUIENTE COMANDO EN LA TERMINAL: python ejercicios.py








archivo_excel = 'ejercicio.xlsx' 
info1 = pd.read_excel(archivo_excel, sheet_name='INFO1')
info2 = pd.read_excel(archivo_excel, sheet_name='INFO2', header=0, index_col=0)





#SECTOR ECONOMICO
sector_economico = info1.groupby('SECTOR')['CARTERA'].sum()  
pais_desglose = info1.groupby('PAIS')['CARTERA'].sum()
tipo_persona_desglose = info1.groupby('TIPO PERSONA')['CARTERA'].sum()


plt.figure(figsize=(12, 6))
sector_economico.plot(kind='bar', color='green', alpha=0.7)
plt.title('Desglose de la Cartera de Créditos por Sector Económico')
plt.xlabel('Sector Económico')
plt.ylabel('Montos')
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig('sector_economico.png')
plt.close()

print("El gráfico de desglose por sector económico ha sido generado exitosamente.")





#PAIS
plt.figure(figsize=(12, 6))
pais_desglose.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Desglose de la Cartera de Créditos por País')
plt.xlabel('País')
plt.ylabel('Montos')
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig('desglose_por_pais.png')
plt.close()

print("El gráfico de desglose por país ha sido generado exitosamente.")




#PERSONA JURIDICA CON NATURAL
plt.figure(figsize=(8, 5))
tipo_persona_desglose.plot(kind='bar', color='green', alpha=0.7)
plt.title('Desglose de la Cartera de Créditos por Tipo de Persona')
plt.xlabel('Tipo de Persona')
plt.ylabel('Montos')
plt.xticks(rotation=0)  
plt.tight_layout()


plt.savefig('desglose_por_tipo_persona.png')
plt.close()

print("El gráfico de desglose por tipo de persona ha sido generado exitosamente.")


#PRESTAMOS REESTRUCTURADOS
restructuraciones = info2.loc['Reestructuraciones']  


plt.figure(figsize=(10, 6))
restructuraciones.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Desglose de la Cartera de Créditos por Préstamos Reestructurados')
plt.xlabel('Meses')
plt.ylabel('Montos')
plt.xticks(rotation=45) 
plt.tight_layout()


plt.savefig('desglose_por_prestamos_reestructurados.png')
plt.close()

print("El gráfico de desglose por préstamos reestructurados ha sido generado exitosamente.")





#CASTIGADOS
castigos = info2.loc['Castigos']  


plt.figure(figsize=(10, 6))
castigos.plot(kind='bar', color='red', alpha=0.7)
plt.title('Desglose de la Cartera de Créditos por Préstamos Castigados')
plt.xlabel('Meses')
plt.ylabel('Montos')
plt.xticks(rotation=45)  
plt.tight_layout()


plt.savefig('desglose_por_prestamos_castigados.png')
plt.close()

print("El gráfico de desglose por préstamos castigados ha sido generado exitosamente.")















#MONTO DE PRESTAMOS PROMEDIO
monto_promedio = info1['CARTERA'].mean()


plt.figure(figsize=(6, 6))
plt.bar(['Monto Promedio de Préstamos'], [monto_promedio], color='skyblue', alpha=0.7)


plt.title('Monto Promedio de Préstamos')
plt.ylabel('Monto en pesos')

plt.text(0, monto_promedio, f'{monto_promedio:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')


plt.tight_layout()
plt.savefig('monto_promedio_prestamos.png')
plt.close()

print("El gráfico del monto promedio de préstamos ha sido generado exitosamente.")






#PLAZO PROMEDIO DE LA CARTERA
info1['FECHA_DESEMBOLSO'] = pd.to_datetime(info1['FECHA_DESEMBOLSO'])
info1['FECHA_VENCIMIENTO'] = pd.to_datetime(info1['FECHA_VENCIMIENTO'])


info1['PLAZO_DIAS'] = (info1['FECHA_VENCIMIENTO'] - info1['FECHA_DESEMBOLSO']).dt.days


plazo_promedio = info1['PLAZO_DIAS'].mean()


plt.figure(figsize=(6, 6))
plt.bar(['Plazo Promedio de la Cartera'], [plazo_promedio], color='lightgreen', alpha=0.7)


plt.title('Plazo Promedio de la Cartera')
plt.ylabel('Plazo en Días')


plt.text(0, plazo_promedio, f'{plazo_promedio:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')


plt.tight_layout()
plt.savefig('plazo_promedio_cartera.png')
plt.close()

print("El gráfico del plazo promedio de la cartera ha sido generado exitosamente.")




#c) Saldo de la cartera por días de atraso: 1 día a 30 días, 31 días a 60 días, 61 días a 90 días, 91 días a 180 días, 181 días a 1 año y superior a 1 año.
info1['ATRASO_CATEGORIA'] = pd.cut(
    info1['DIAS_MORA'], 
    bins=[0, 30, 60, 90, 180, 365, float('inf')], 
    labels=['1-30 días', '31-60 días', '61-90 días', 
        '91-180 días', '181 días - 1 año', 'Más de 1 año'],
    right=True
)



saldo_por_atraso = info1.groupby('ATRASO_CATEGORIA', observed=False)['CARTERA'].sum()


plt.figure(figsize=(10, 6))
saldo_por_atraso.plot(kind='bar', color='purple', alpha=0.7)



plt.title('Saldo de la Cartera por Intervalo de Días de Atraso')
plt.xlabel('Intervalo de Días de Atraso')
plt.ylabel('Saldo de la Cartera')
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig('saldo_cartera_por_dias_de_atraso.png')
plt.close()

print("El gráfico de saldo de la cartera por días de atraso ha sido generado exitosamente.")



