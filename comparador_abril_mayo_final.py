
import streamlit as st
import pandas as pd

# ---------- CONFIGURACIÓN ----------
VALOR_INDICE_MAYO = 87.608881
VALOR_INDICE_ABRIL = 85.056195

# Puntajes abril y mayo integrados
puntajes_abril = {}
puntajes_mayo = {}
cargos = []

GREMIOS = {
    "AMET": 0.015, "SUTEF": 0.02, "SUETRA": 0.02,
    "ATE": 0.022, "UDAF": 0.013, "UDA": 0.015, "UPCN": 0.022
}

def calcular_total(puntaje, vi, descuentos):
    basico = puntaje * vi
    antiguedad = basico * 0.2
    zona = basico * 0.3
    transformacion = basico * 0.08
    foid = 3000
    total_remun = basico + antiguedad + zona + transformacion
    total_bruto = total_remun + foid
    total_desc = sum(GREMIOS[g] * (total_remun + foid) for g in descuentos if g in GREMIOS)
    neto = total_bruto - total_desc
    return {
        "Básico": basico,
        "Antigüedad": antiguedad,
        "Zona": zona,
        "Transformación": transformacion,
        "FOID": foid,
        "Remunerativo": total_remun,
        "Descuento Gremial": total_desc,
        "Neto": neto
    }

# ---------- INTERFAZ ----------
st.title("📊 Comparador Salarial Abril vs Mayo 2025")

cargo = st.selectbox("Seleccionar cargo:", cargos)

gremio1 = st.selectbox("Gremio 1:", ["Ninguno"] + list(GREMIOS.keys()))
gremio2 = st.selectbox("Gremio 2:", ["Ninguno"] + list(GREMIOS.keys()))

descuentos = []
if gremio1 != "Ninguno": descuentos.append(gremio1)
if gremio2 != "Ninguno" and gremio2 != gremio1: descuentos.append(gremio2)

puntaje_abril = puntajes_abril.get(cargo, 0)
puntaje_mayo = puntajes_mayo.get(cargo, 0)

abril = calcular_total(puntaje_abril, VALOR_INDICE_ABRIL, descuentos)
mayo = calcular_total(puntaje_mayo, VALOR_INDICE_MAYO, descuentos)

resultado = pd.DataFrame({
    "Concepto": abril.keys(),
    "Abril ($)": abril.values(),
    "Mayo ($)": mayo.values(),
    "Diferencia ($)": [mayo[k] - abril[k] for k in abril],
    "Variación (%)": [((mayo[k] - abril[k]) / abril[k] * 100) if abril[k] != 0 else 0 for k in abril]
})

st.dataframe(
    resultado.style.format(subset=["Abril ($)", "Mayo ($)", "Diferencia ($)"], formatter="{:,.2f}")
    .format({"Variación (%)": "{:+.2f}%"})
)
