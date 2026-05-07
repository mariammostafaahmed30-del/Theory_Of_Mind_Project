import streamlit as st
import requests

# إعدادات واجهة المستخدم الاحترافية
st.set_page_config(page_title="Empathetic AI Companion", page_icon="🧠", layout="centered")

# رابط الموديل من Hugging Face
API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
HEADERS = {"Authorization": "Bearer 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"}

def query_emotion(text):
    try:
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
        return response.json()
    except:
        return None

# التصميم الجمالي للواجهة
st.title("🧠 Developing Theory of Mind in AI")
st.markdown("### Empathetic UI: Understanding the Human Behind the Screen")
st.info("اكتبي كيف تشعرين اليوم وسيقوم الذكاء الاصطناعي بتعديل بيئته للتفاعل مع حالتك النفسية.")

user_input = st.text_input("How are you feeling today?", placeholder="Example: I've had such a long and exhausting day...")

if st.button("Connect with AI"):
    if user_input:
        with st.spinner('AI is analyzing the mental state...'):
            result = query_emotion(user_input)
            
            if isinstance(result, dict) and 'error' in result:
                st.warning("السيرفر يجهز الموديل.. من فضلك حاولي مرة أخرى بعد 5 ثوانٍ.")
            elif isinstance(result, list):
                emotion = result[0][0]['label']
                
                # منطق الـ Theory of Mind والتكيف البصري
                if emotion in ['joy', 'surprise']:
                    st.success(f"**Detected State: Positive ({emotion.upper()})** ✨")
                    st.balloons()
                    st.write("أنا سعيد جداً لسماع ذلك! طاقتك الإيجابية معدية. استمري في الإبداع!")
                elif emotion in ['sadness', 'fear']:
                    st.info(f"**Detected State: Vulnerable ({emotion.upper()})** 💙")
                    st.write("أنا هنا من أجلك. يبدو أنك تمرين بوقت صعب، خذي نفساً عميقاً، الأمور ستتحسن.")
                elif emotion in ['anger', 'disgust']:
                    st.error(f"**Detected State: Stressed ({emotion.upper()})** 🛑")
                    st.write("أشعر بمدى ضيقك. سأقوم بتهدئة الألوان قليلاً لمساعدتك على الاسترخاء.")
                else:
                    st.write(f"**Detected State: Balanced (NEUTRAL)** 🤖")
                    st.write("أنا أسمعك بوضوح.. أخبريني المزيد عما يدور في ذهنك.")
    else:
        st.warning("من فضلك اكتبي شيئاً أولاً.")
