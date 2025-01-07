import streamlit as st

from agent import handle_chat

if "history" not in st.session_state:
    st.session_state["history"] = []

# Configuração da página
st.set_page_config(page_title="Chatbot Inteligente", page_icon="🤖", layout="wide")

# Estilos CSS
st.markdown("""
<style>
    .stTextInput>div>div>input {
        border-radius: 20px;
        padding: 10px 20px;
    }
    .stButton>button {
        border-radius: 20px;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
    }
    .user-message {
        background-color: #e3f2fd;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
    .ai-message {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# Layout principal
st.title("🤖 Chatbot Inteligente")
st.markdown("""
**Funcionalidades:**
- Consulta a banco de dados
- Cálculos matemáticos
- Buscas na web
""")

# Área de chat
chat_container = st.container()

def send_message():
    if st.session_state.user_input:
        with st.spinner("Processando..."):
            user_message = st.session_state.user_input
            response = handle_chat(user_message)
            st.session_state["history"].append(("Você", user_message))
            st.session_state["history"].append(("AI", response))
            st.session_state.user_input = ""

# Input e botão
col1, col2 = st.columns([6, 1])
with col1:
    user_input = st.text_input(
        "Digite sua mensagem:",
        key="user_input",
        on_change=send_message,
        placeholder="Escreva sua mensagem aqui..."
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    send_button = st.button("Enviar")

# Exibir histórico
with chat_container:
    for idx, (user, message) in enumerate(reversed(st.session_state["history"])):
        if user == "Você":
            st.markdown(f"""
            <div class="user-message">
                <strong>Você:</strong><br>
                {message}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="ai-message">
                <strong>AI:</strong><br>
                {message}
            </div>
            """, unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("""
**Desenvolvido com:**
- LangChain
- OpenAI GPT-3.5
- Streamlit
""")
st.markdown("---")
