from datetime import datetime
import httpagentparser
import pandas as pd
import requests
import streamlit as st
from streamlit_js_eval import streamlit_js_eval

def obtener_informacion_ip(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json').json()
    return response

def main():
    st.title("Información de los encuestados")

    # Obtener información del navegador y sistema operativo del cliente
    navegador_y_sistema = streamlit_js_eval(js_expressions='window.navigator.userAgent', key="get_user_agent")
    cliente_ip = streamlit_js_eval(js_expressions='fetch("https://api64.ipify.org?format=json").then(response => response.json()).then(data => data.ip)', key="get_ip")
    
    if navegador_y_sistema is None or cliente_ip is None:
        st.error("No se pudo obtener la información del navegador, sistema operativo o IP del cliente.")
        return

    informacion_navegador_y_sistema = httpagentparser.detect(navegador_y_sistema)

    # Obtener información adicional sobre la IP del cliente
    informacion_ip = obtener_informacion_ip(cliente_ip)

    diccionario_info_navegador_y_sistema = {
        "Fecha y hora de la conexión": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Dirección IP": cliente_ip,
        "Ciudad": informacion_ip.get('city', 'N/A'),
        "Región": informacion_ip.get('region', 'N/A'),
        "País": informacion_ip.get('country', 'N/A'),
        "Ubicación geográfica (LAT/LON)": informacion_ip.get('loc', 'N/A'),
        "Proveedor de Servicios de Internet": informacion_ip.get('org', 'N/A'),
        "Navegador": informacion_navegador_y_sistema.get('browser', {}).get('name', 'N/A'),
        "Sistema operativo": informacion_navegador_y_sistema.get('os', {}).get('name', 'N/A')
    }

    df_ip_encuestado_actual = pd.DataFrame([diccionario_info_navegador_y_sistema])

    # Cargar el archivo CSV existente, si existe
    try:
        df_ips_encuestados = pd.read_csv("ips_encuestados.csv")
        df_ips_encuestados = pd.concat([df_ips_encuestados, df_ip_encuestado_actual], ignore_index=True)
    except FileNotFoundError:
        df_ips_encuestados = df_ip_encuestado_actual

    # Guardar el DataFrame actualizado en el archivo CSV
    df_ips_encuestados.to_csv("ips_encuestados.csv", index=False)

    # Mostrar el DataFrame en Streamlit
    st.write("## Datos de los encuestados")
    st.dataframe(df_ips_encuestados)

if __name__ == "__main__":
    main()
