import streamlit as st
import random
import time

st.set_page_config(page_title="Surpresa de Aniversário!", page_icon="💛", layout="centered")

# CSS global para visual igual ao print
st.markdown("""
<style>
body, .stApp {
    background: #f9ecec !important;
}
.titulo-festa {
    text-align: center;
    font-size: 2.6em;
    font-weight: bold;
    color: #8B5C00;
    font-family: 'Segoe UI', sans-serif;
    margin-top: 24px;
    margin-bottom: 0.15em;
    letter-spacing: 1px;
}
.emoji-cima {
    text-align: center;
    font-size: 2.2em;
    margin-bottom: 0.30em;
}
.texto-normal {
    text-align: center;
    font-size: 1.18em;
    color: #8B5C00;
    font-family: 'Segoe UI', sans-serif;
    margin-bottom: 0.36em;
}
.texto-sub {
    text-align: center;
    font-size: 1.13em;
    color: #8B5C00;
    margin-bottom: 1.15em;
}
.destaque {
    color: #ffe066 !important;
    font-weight: bold;
}
.stButton > button {
    background: linear-gradient(90deg,#ffe066 15%,#f4c6b4 100%);
    color: #8B5C00 !important;
    border-radius: 32px !important;
    font-size: 1.14em !important;
    font-weight: bold;
    height: 55px !important;
    width: 260px !important;
    box-shadow: 0 2px 12px #c97b6344;
    border: none !important;
    transition: 0.3s;
    letter-spacing: 0.5px;
    margin: 0 !important;
    display: block !important;
}
.stButton > button:hover {
    background: linear-gradient(90deg,#fff5ba,#ffe6c6 95%);
    color: #a36800 !important;
}
.caixinha {
    background: #fffbe7;
    border-radius: 18px;
    border: 3px solid #ffe066;
    padding: 26px 22px;
    min-height: 108px;
    min-width: 310px;
    max-width: 410px;
    width: 100%;
    font-size: 1.14em;
    color: #8B5C00 !important;
    text-align: center;
    box-shadow: 0 6px 20px #ffe06638;
    font-weight: bold;
    margin: 12px auto 15px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    line-height: 1.35;
}
.centraliza-btn {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 18px;
    margin-bottom: 13px;
}
.centraliza {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# Título e textos igual à imagem
st.markdown('<div class="titulo-festa">Feliz aniversário, minha princesa!</div>', unsafe_allow_html=True)
#st.markdown('<div class="emoji-cima">💛</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="texto-normal">Hoje é dia de comemorar do jeito que a gente gosta: com uma surpresa pra guardar pra sempre na memória.</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '''<div class="texto-sub">
    Escolha até <span class="destaque">3 caixinhas</span> misteriosas abaixo e descubra quais mimos especiais você vai ganhar por ser a esposa mais incrível do universo! 🚀💛
    </div>''',
    unsafe_allow_html=True
)

prizes = [
    "💋 Vale Beijinho — resgatável quando quiser!",
    "☕🌹 Vale Café na Cama — em breve, uma manhã especial só pra você!",
    "🏙️ Vale Passeio Surpresa — uma experiência inesquecível está vindo aí!",
    "🔄 Tente novamente!"
]

# Estado
if "embaralhado" not in st.session_state:
    st.session_state.embaralhado = False
if "embaralhando" not in st.session_state:
    st.session_state.embaralhando = False
if "final_prizes" not in st.session_state:
    st.session_state.final_prizes = prizes.copy()
if "revealed" not in st.session_state:
    st.session_state.revealed = [False, False, False, False]
if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0
if "msg_tente" not in st.session_state:
    st.session_state.msg_tente = ""

def embaralhar_animado():
    st.session_state.embaralhando = True
    st.session_state.embaralhado = False

# --- CENTRALIZAÇÃO do botão usando COLUMNS do Streamlit ---
if not st.session_state.embaralhado and not st.session_state.embaralhando:
    cols = st.columns([2, 3, 2])
    with cols[1]:
        st.button("Embaralhar as caixinhas!", on_click=embaralhar_animado)

elif st.session_state.embaralhando:
    placeholder = st.empty()
    for _ in range(24):
        temp_prizes = prizes.copy()
        random.shuffle(temp_prizes)
        with placeholder.container():
            st.markdown(
                f"""
                <div style='
                    display:flex; 
                    flex-direction:column; 
                    align-items:center; 
                    justify-content:center; 
                    height:285px; 
                    background:linear-gradient(90deg,#fff9e2 48%,#f9ecec 100%);
                    border-radius: 32px;
                    box-shadow: 0 0 40px #ffe06633;
                    margin: 24px 0 8px 0;
                '>
                    <div style='font-size:2.1em; font-weight:bold; color:#f3bb28; margin-bottom:7px; letter-spacing:1px;'>
                        <span style="font-size:1.09em; margin-right:12px;"></span>
                        Embaralhando as surpresas...
                    </div>
                    <div style='font-size:1.88em; margin-bottom:8px; color:#c97b63; font-weight:bold; letter-spacing:4px;'>
                        {" ".join(['🎁' for _ in temp_prizes])}
                    </div>
                    <div style='font-size:1.14em; color:#8B5C00; margin-top:16px; opacity:0.9;'>
                        Preparando as caixas misteriosas para você!
                    </div>
                </div>
                """, unsafe_allow_html=True
            )
        time.sleep(0.085)
    placeholder.empty()
    shuffled = prizes.copy()
    random.shuffle(shuffled)
    st.session_state.final_prizes = shuffled
    st.session_state.embaralhado = True
    st.session_state.embaralhando = False
    st.session_state.revealed = [False, False, False, False]
    st.session_state.tentativas = 0
    st.session_state.msg_tente = ""
    st.rerun()

# Escolha das caixinhas/prêmios (botões das caixinhas um embaixo do outro e centralizados!)
else:
    st.markdown(
        "<div class='texto-sub' style='margin-bottom:0.45em;'><b>Escolha até <span class='destaque'>3 caixinhas</span> para revelar seu prêmio!</b></div>",
        unsafe_allow_html=True
    )
    num_reveladas = sum(st.session_state.revealed)
    st.markdown("<div style='display:flex; justify-content:center; gap:22px; margin-bottom:14px;'>", unsafe_allow_html=True)
    for idx, revealed in enumerate(st.session_state.revealed):
        if revealed:
            st.markdown(
                f"<div class='caixinha'>{st.session_state.final_prizes[idx]}</div>",
                unsafe_allow_html=True
            )
    st.markdown("</div>", unsafe_allow_html=True)
    # Botões das caixinhas: CADA UM CENTRALIZADO EM SUA PRÓPRIA LINHA
    if num_reveladas < 3:
        for idx, revealed in enumerate(st.session_state.revealed):
            if not revealed:
                cols_btn = st.columns([2, 3, 2])
                with cols_btn[1]:
                    if st.button(f"🎁 Caixa Misteriosa {idx+1}", key=f"btn_{idx}"):
                        prize = st.session_state.final_prizes[idx]
                        if prize == "🔄 Tente novamente!":
                            st.session_state.tentativas += 1
                            if st.session_state.tentativas < 3:
                                st.session_state.msg_tente = f"<div style='color:#c97b63; font-size:1.05em; text-align:center;'><b>Ops! Você pegou o 'Tente novamente'.<br>Como é seu aniversário, você ainda pode tentar mais {3 - st.session_state.tentativas} vez(es)!</b></div>"
                            else:
                                st.session_state.revealed[idx] = True
                                st.session_state.msg_tente = "<div style='color:#c97b63; font-size:1.08em; text-align:center;'><b>Que azar mozinho! Você chegou ao limite de tentativas! Agora só restam os prêmios 🏆</b></div>"
                        else:
                            st.session_state.revealed[idx] = True
        if st.session_state.msg_tente:
            st.markdown(st.session_state.msg_tente, unsafe_allow_html=True)
    if num_reveladas == 3:
        st.balloons()
        st.markdown(
            "<div style='text-align:center; font-size:1.23em; margin-top:1.25em; color:#8B5C00; font-weight:bold;'>Eu te amo! Prepare-se para viver todas essas surpresas grudadinhas.💛</div>",
            unsafe_allow_html=True
        )
        # Centraliza o botão "Jogar de novo"
        cols = st.columns([2, 3, 2])
        with cols[1]:
            if st.button("Jogar de novo"):
                st.session_state.embaralhado = False
                st.session_state.revealed = [False, False, False, False]
                st.session_state.tentativas = 0
                st.session_state.msg_tente = ""
