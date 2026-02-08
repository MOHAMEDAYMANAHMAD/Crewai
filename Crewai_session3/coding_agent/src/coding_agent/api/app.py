import streamlit as st
from datetime import datetime
from coding_agent.crew import CodingAgent
import time

st.set_page_config(
    page_title="Software Architect Agent | CrewAI",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Software Architect Agent")
st.markdown("### حول فكرتك إلى واقع - تحليل، تخطيط، وهيكلة برمجية")
st.divider()

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/606/606259.png", width=100)
    st.header("إعدادات الوكيل المهندس")
    st.info("هذا الوكيل يستخدم CrewAI لتحليل الأفكار البرمجية وتحديد التقنيات المطلوبة ورسم خطوات التنفيذ.")
    if st.button("مسح البيانات 🧹"):
        st.rerun()

with st.container():
    col1, col2 = st.columns([4, 1])
    with col1:
        topic = st.text_input("💡 وصف فكرة التطبيق:", placeholder="مثلاً: تطبيق توصيل طلبات، موقع يشبه فيسبوك، نظام إدارة مخازن...")
    with col2:
        st.write("##")
        run_button = st.button("بدء التخطيط 🚀")

if run_button:
    if topic:
        tab1, tab2 = st.tabs(["⚙️ كواليس التفكير", "📋 خطة العمل النهائية"])
        
        with tab1:
            with st.status(f"🧠 جاري تحليل فكرة: {topic}...", expanded=True) as status:
                st.write("🕵️ تحليل المتطلبات الأساسية (Requirements)...")
                time.sleep(1)
                st.write("🏗️ تصميم الهيكلية البرمجية (Architecture)...")
                time.sleep(1)
                st.write("🛠️ اختيار أفضل التقنيات (Tech Stack)...")
                time.sleep(1)
                st.write("📝 كتابة خطوات التنفيذ (Roadmap)...")
                
                try:
                    inputs = {
                        'topic': topic, 
                        'current_year': str(datetime.now().year)
                    }

                    crew_instance = CodingAgent().crew()
                    result = crew_instance.kickoff(inputs=inputs)
                    
                    status.update(label="✅ تم رسم الخطط بنجاح!", state="complete", expanded=False)
                    
                    report_content = str(result.raw)

                    with tab2:
                        st.success(f"✅ إليك الخطة الكاملة لمشروع: {topic}")
                        st.divider()
                        st.markdown(report_content)
                        

                except Exception as e:
                    st.error(f"❌ حدث خطأ: {e}")
                    status.update(label="💥 فشلت المهمة", state="error")
    else:
        st.warning("⚠️ من فضلك اشرح لي فكرة التطبيق اللي عايز تبنيه!")

# Footer
st.divider()
st.caption("برمجة محمد أيمن | مدعوم بذكاء CrewAI 🚀")