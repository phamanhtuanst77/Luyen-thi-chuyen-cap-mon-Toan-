import streamlit as st
import google.generativeai as genai

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Thầy Giáo Toán AI - Ôn thi vào 10", page_icon="🎓")
st.title("🎓 Thầy Giáo Toán AI: Ôn thi vào 10")
st.markdown("### Chuyên gia luyện thi dành cho học sinh trung bình")

# --- CẤU HÌNH API KEY ---
# Ở bước này, em có thể dán trực tiếp API Key vào đây hoặc nhập từ giao diện
api_key = st.sidebar.text_input("Nhập API Key của bạn:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # --- PROMPT VÀNG (SYSTEM INSTRUCTION) ---
    system_prompt = """
    Bạn là một chuyên gia sư phạm Toán hàng đầu tại Việt Nam... 
    (Em dán toàn bộ nội dung PHẦN 1 - SYSTEM INSTRUCTION ở câu trả lời trước vào đây)
    """

    # Khởi tạo Model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_prompt
    )

    # --- QUẢN LÝ TIN NHẮN ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Hiển thị lịch sử chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Ô nhập tin nhắn của học sinh
    if prompt := st.chat_input("Em muốn thầy giảng chuyên đề nào?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("Vui lòng nhập API Key ở cột bên trái để bắt đầu học nhé!")