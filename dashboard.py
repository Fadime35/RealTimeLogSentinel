import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Real-Time SIEM Dashboard", layout="wide")
st.title("Real-Time SIEM Dashboard")

log_file = "logs/sample_logs.csv"

# Log dosyasını oku
try:
    df = pd.read_csv(log_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
except:
    st.warning("Log dosyası bulunamadı!")
    st.stop()

# -------- Son Loglar --------
st.subheader("Son Loglar")
st.dataframe(df.tail(10))

# -------- Action Distribution --------
st.subheader("Action Distribution")
st.bar_chart(df["action"].value_counts())

# -------- Failed Login Alerts --------
st.subheader("Failed Login Alerts")
failed_counts = df[df['action']=='FAILED_LOGIN']['ip'].value_counts()
for ip, count in failed_counts.items():
    if count > 5:
        st.error(f"ALERT: {ip} has {count} failed login attempts!")

# -------- Suspicious IPs --------
st.subheader("Suspicious IPs")
for ip in df["ip"].unique():
    if not ip.startswith("192.168"):
        st.warning(f"Suspicious IP detected: {ip}")

# -------- Heatmap: IP vs Action --------
st.subheader("IP vs Action Heatmap")
pivot_df = df.pivot_table(index='ip', columns='action', aggfunc='size', fill_value=0)
fig_heatmap = px.imshow(pivot_df, text_auto=True, color_continuous_scale='RdYlGn')
st.plotly_chart(fig_heatmap, use_container_width=True, key="heatmap_chart")

# -------- Time Series: Log Count Over Time --------
st.subheader(" Log Count Over Time")
time_series = df.groupby(pd.Grouper(key='timestamp', freq='10S')).size()
st.line_chart(time_series)