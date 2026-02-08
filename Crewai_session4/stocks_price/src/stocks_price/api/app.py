import streamlit as st
from datetime import datetime
from stocks_price.crew import StocksPrice
import markdown

st.set_page_config(page_title=" Stock Analyst", page_icon="📈", layout="centered")

st.title("📊 Stocks Analyst")
st.subheader(" CrewAI حلل أي سهم في ثواني باستخدام الـ ")

with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        topic = st.text_input("أدخل رمز الشركة", placeholder="AAPL, NVDA, MSFT: مثلاً ")
    with col2:
        st.write("##") 
        run_button = st.button("بدء التحليل 🔥", use_container_width=True)

if run_button:
    if topic:
        with st.spinner(f"{topic.upper()} جاري تحضير  سهم ⏳"):
            try:
               
                inputs = {
                    'topic': topic.upper(),
                    'current_year': str(datetime.now().year)
                }

                crew_instance = StocksPrice().crew()
                result = crew_instance.kickoff(inputs=inputs)
                report_content = str(result.raw)
                st.success(f"تم الانتهاء من تحليل {topic.upper()}!")
                st.divider()
                
                st.markdown(report_content)

            except Exception as e:
                st.error(f"حدث خطأ أثناء التشغيل: {e}")
    else:
        st.warning("من فضلك أدخل اسم الشركة أولاً")

