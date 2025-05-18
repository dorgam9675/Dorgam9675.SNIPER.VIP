import streamlit as st

st.set_page_config(page_title="Dorgam9675.SNIPER.VIP", layout="centered")
st.title("🔍 نظام Dorgam9675.SNIPER.VIP")
st.markdown("مرحبًا بك في النسخة التجريبية من النظام")

symbol = st.selectbox("اختر زوج العملات أو الذهب", ["XAUUSD", "EURUSD", "GBPUSD"])
timeframe = st.selectbox("الإطار الزمني", ["1h", "4h", "1d"])
history = st.selectbox("البيانات التاريخية", ["1mo", "3mo", "6mo"])

if st.button("ابدأ التحليل"):
    st.success(f"✅ جاهز لتحليل {symbol} على الإطار {timeframe} باستخدام بيانات {history}")
