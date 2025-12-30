import streamlit as st
import pandas as pd

st.title("🚀 AI-Based Satellite Health Monitoring System")

df = pd.read_csv("output_with_anomalies.csv")

st.subheader("📊 Satellite Sensor Data")
st.dataframe(df.head(20))

st.subheader("📈 Satellite Health Parameters")
st.line_chart(df[['battery', 'temperature', 'signal']])

st.subheader("⚠️ Detected Anomalies")
anomalies = df[df['anomaly'] == 'Anomaly']

if len(anomalies) == 0:
    st.success("No anomalies detected 🚀")
else:
    st.error(f"{len(anomalies)} anomalies detected!")
    st.dataframe(anomalies)
