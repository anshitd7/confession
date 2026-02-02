import streamlit as st
import time

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="Read Carefully",
    page_icon="📩",
    layout="centered"
)

# =========================
# ADVANCED STYLING (CSS)
# =========================
st.markdown("""
<style>
/* IMPORT FONTS */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lora:ital,wght@0,400;0,500;1,400&family=Share+Tech+Mono&display=swap');

/* GLOBAL ANIMATIONS */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* FORCE DARK BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at center, #264653 0%, #102027 100%) !important;
    background-attachment: fixed !important;
    background-size: cover !important;
    color: #e0e0e0 !important;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0) !important;
}

/* HIDE DEFAULT STREAMLIT ELEMENTS */
#MainMenu, footer {visibility: hidden;}

/* ============================
   UI COMPONENT: TITLES
   ============================ */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 700;
    text-align: center;
    color: #FFD700; /* Gold */
    text-shadow: 0 4px 15px rgba(0,0,0,0.5);
    margin-top: 20px;
    margin-bottom: 10px;
    letter-spacing: 1px;
    animation: fadeIn 1.5s ease-out;
}

.subtitle {
    font-family: 'Lora', serif;
    text-align: center;
    font-size: 1.2rem;
    font-style: italic;
    color: #A7F3D0; /* Soft Mint */
    margin-bottom: 40px;
    opacity: 0.8;
    font-weight: 300;
    animation: fadeIn 2s ease-out;
}

/* ============================
   UI COMPONENT: THE LETTER
   ============================ */
.letter-paper {
    background: rgba(20, 25, 30, 0.6); /* Dark Glass */
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border-radius: 12px;
    padding: 50px;
    
    /* Subtle Gold Glow Border */
    border: 1px solid rgba(255, 215, 0, 0.15);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    
    margin-top: 10px;
    margin-bottom: 50px;
    animation: fadeIn 2.5s ease-in;
}

.story-text {
    font-family: 'Lora', serif;
    font-size: 1.15rem;
    line-height: 1.8;
    color: #e0e0e0;
    white-space: pre-wrap; /* Preserves line breaks */
    text-align: justify;
}

.signature {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    text-align: right;
    margin-top: 50px;
    color: #00FF9D;
    font-style: italic;
    opacity: 0.9;
    text-shadow: 0 0 10px rgba(0, 255, 157, 0.2);
}

/* DECORATIVE LINE */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #FFD700, transparent);
    margin: 20px 0;
    opacity: 0.5;
}

/* LINK STYLE */
.final-link {
    text-align: center;
    margin-top: 30px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.9rem;
    opacity: 0.8;
}
.final-link a {
    color: #FFD700 !important;
    text-decoration: none;
    border-bottom: 1px dotted #FFD700;
    transition: all 0.3s ease;
}
.final-link a:hover {
    color: #fff !important;
    border-bottom: 1px solid #fff;
    opacity: 1;
}

</style>
""", unsafe_allow_html=True)

# =========================
# MAIN CONTENT
# =========================

# Title Section
st.markdown("<div class='main-title'>Read carefully</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A story that needs to be told...</div>", unsafe_allow_html=True)

# The Message Content
MESSAGE_BODY = """Hello Vaibhavi,
Abhi intern khatam ho gayi hai aomost toh vo password dene ka time aa gaya tereko. Mai shayad de bhi doonga bahut jald.
Ye message bss ek reminder hai ki jab tu vo sab padh legi toh mereko bss galat mat samjhna aur baakiyo ki tarah mat samjhna.
Ab vaise bhi tereko aage sabhi life me dikkato ka saamna khudse karna hoga, isliye acche se padhai karna, plzacment le aur daffa hoja mere saamne se!
"""

# Render the Letter with the Link (NO INDENTATION FIX)
st.markdown(f"""
<div class='letter-paper'>
<div class='story-text'>{MESSAGE_BODY}</div>
<div class='divider'></div>
<div class='signature'>— Anshit</div>
<div class='final-link'>
<a href='https://last-message-vaibhavi.streamlit.app/' target='_blank'>
https://last-message-vaibhavi.streamlit.app/
</a>
</div>
</div>
""", unsafe_allow_html=True)

# Subtle animation on load
time.sleep(0.5)
st.balloons()