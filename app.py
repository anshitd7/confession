import streamlit as st
from datetime import datetime, timedelta
import time

# =========================
# CONFIGuration
# =========================
PASSWORD = "byebyevaibhavi"
COUNTDOWN_MINUTES = 15

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="The Last Message",
    page_icon="🕰️",
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

@keyframes pulseGlow {
    0% { box-shadow: 0 0 5px rgba(255, 215, 0, 0.2); }
    50% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.5); }
    100% { box-shadow: 0 0 5px rgba(255, 215, 0, 0.2); }
}

/* APP BACKGROUND */
.stApp {
    /* Deep Cinematic Teal Gradient */
    background: radial-gradient(circle at center, #264653 0%, #102027 100%);
    background-attachment: fixed;
    color: #e0e0e0;
}

/* HIDE DEFAULT STREAMLIT JUNK */
#MainMenu, footer, header {visibility: hidden;}

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
    margin-bottom: 0px;
    letter-spacing: 1px;
}

.subtitle {
    font-family: 'Lora', serif;
    text-align: center;
    font-size: 1.1rem;
    font-style: italic;
    color: #A7F3D0; /* Soft Mint */
    margin-bottom: 40px;
    opacity: 0.7;
    font-weight: 300;
}

/* ============================
   UI COMPONENT: ACCESS SCREEN
   ============================ */
.access-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 60px;
    animation: fadeIn 1.5s ease-out;
}

.access-clock {
    font-family: 'Playfair Display', serif;
    font-size: 6rem;
    color: #FFD700;
    text-shadow: 0 0 25px rgba(255, 215, 0, 0.5); 
    font-weight: 700;
    margin-bottom: 25px;
    line-height: 1;
}

.access-status-box {
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(10px);
    padding: 15px 40px;
    border-radius: 12px;
    border: 1px solid rgba(0, 255, 157, 0.3);
    box-shadow: 0 0 20px rgba(0, 255, 157, 0.1);
    width: 100%;
    max-width: 400px;
    text-align: center;
}

.access-text {
    color: #00FF9D; /* NEON GREEN */
    font-family: 'Share Tech Mono', monospace;
    font-size: 1.8rem;
    letter-spacing: 3px;
    text-shadow: 0 0 10px rgba(0, 255, 157, 0.6);
    text-transform: uppercase;
}

/* ============================
   UI COMPONENT: INPUTS & FORMS
   ============================ */
/* Style the input box to look invisible/sleek */
div[data-testid="stTextInput"] {
    margin-top: 20px;
}

div[data-testid="stTextInput"] input {
    background-color: rgba(255, 255, 255, 0.05) !important;
    color: #FFD700 !important;
    border: 1px solid rgba(255, 215, 0, 0.3) !important;
    border-radius: 8px !important;
    padding: 15px !important;
    font-family: 'Share Tech Mono', monospace !important;
    text-align: center;
    font-size: 1.2rem !important;
    transition: all 0.3s ease;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #00FF9D !important;
    box-shadow: 0 0 15px rgba(0, 255, 157, 0.2) !important;
}

/* Style the Button */
div.stButton > button {
    width: 100%;
    background: transparent;
    border: 1px solid #FFD700;
    color: #FFD700;
    padding: 10px 20px;
    font-family: 'Lora', serif;
    font-size: 1.1rem;
    letter-spacing: 1px;
    border-radius: 8px;
    transition: all 0.4s ease;
    margin-top: 10px;
}

div.stButton > button:hover {
    background: rgba(255, 215, 0, 0.1);
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
    border-color: #FFD700;
    color: #fff;
    transform: translateY(-2px);
}

/* ============================
   UI COMPONENT: THE LETTER
   ============================ */
.letter-paper {
    background: rgba(20, 25, 30, 0.7); /* Dark Glass */
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border-radius: 12px;
    padding: 50px;
    
    /* Subtle Gold Glow Border */
    border: 1px solid rgba(255, 215, 0, 0.15);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    
    margin-top: 30px;
    margin-bottom: 50px;
    animation: fadeIn 2.5s ease-in;
}

.story-text {
    font-family: 'Lora', serif;
    font-size: 1.15rem;
    line-height: 2; /* More breathing room */
    color: #e0e0e0;
    white-space: pre-wrap;
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

/* ============================
   UI COMPONENT: NOTICES
   ============================ */
.notice-box {
    background: rgba(255, 107, 107, 0.08);
    border-left: 4px solid #ff6b6b;
    border-radius: 4px;
    padding: 20px;
    text-align: center;
    color: #ffcccc;
    font-family: 'Lora', serif;
    margin-bottom: 25px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

.countdown-container {
    text-align: center;
    margin-top: 50px;
    padding: 30px;
    background: rgba(0,0,0,0.2);
    border-radius: 15px;
    border: 1px solid rgba(255, 215, 0, 0.1);
}

.countdown-timer {
    font-family: 'Share Tech Mono', monospace;
    font-size: 4.5rem;
    color: #FFD700;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
}

</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE MANAGEMENT
# =========================
if "authorized" not in st.session_state:
    st.session_state.authorized = False

if "show_success_screen" not in st.session_state:
    st.session_state.show_success_screen = False

if "timer_start" not in st.session_state:
    st.session_state.timer_start = None

# =========================
# MAIN APP LOGIC
# =========================

# -------------------------
# PHASE 1: PASSWORD LOCK
# -------------------------
if not st.session_state.authorized:
    # Spacer
    st.write("")
    st.write("")
    
    st.markdown("<div class='main-title'>Hello Vaibhavi</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>There is a story that needs to be told...</div>",
        unsafe_allow_html=True
    )
    
    # Centered Form
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown(
            "<div class='notice-box'>🔒 <b>Secure Archive</b><br>This file is password protected. <br>Anshit will share the password the night the intenrship work is over.</div>",
            unsafe_allow_html=True
        )
        
        with st.form("password_form"):
            password_input = st.text_input("", type="password", placeholder="Enter Access Key...")
            submit = st.form_submit_button("UNLOCK ARCHIVE")

    if submit:
        if password_input == PASSWORD:
            # Transition Logic
            st.session_state.authorized = True
            st.session_state.show_success_screen = True
            st.session_state.timer_start = datetime.now()
            st.rerun()
        else:
            st.error("Access Denied. Dont Guess! Anshit will share the password at the right time, Trust please.")

# -------------------------
# PHASE 2: ACCESS GRANTED ANIMATION
# -------------------------
elif st.session_state.show_success_screen:
    
    current_time = datetime.now().strftime("%H:%M")
    
    # This renders the "Cyber/Neon" look you wanted
    st.markdown(f"""
        <div class="access-container">
            <div class="access-clock">{current_time}</div>
            <div class="access-status-box">
                <div class="access-text">Access Granted</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Hold the screen for effect
    time.sleep(3.5)
    st.session_state.show_success_screen = False
    st.rerun()

# -------------------------
# PHASE 3: THE COUNTDOWN
# -------------------------
elif datetime.now() < st.session_state.timer_start + timedelta(minutes=COUNTDOWN_MINUTES):
    
    st.markdown("<div class='main-title' style='font-size: 2.5rem;'>One Last Thing</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='notice-box' style='border-left: 4px solid #FFD700; color: #fffacd; background: rgba(255, 215, 0, 0.05);'>
    <b>Important Notice</b><br>
    Please read carefully. This might be the last message from Anshit. You may never see Anshit again.<br>
    The archive will open shortly.
    </div>
    """, unsafe_allow_html=True)

    remaining = (
        st.session_state.timer_start
        + timedelta(minutes=COUNTDOWN_MINUTES)
        - datetime.now()
    )
    mins, secs = divmod(int(remaining.total_seconds()), 60)

    st.markdown(
        f"<div class='countdown-container'><div class='countdown-timer'>{mins:02d}:{secs:02d}</div></div>",
        unsafe_allow_html=True
    )
    
    time.sleep(1)
    st.rerun()

# -------------------------
# PHASE 4: THE CONFESSION LETTER
# -------------------------
else:
    st.markdown("<div class='main-title' style='font-size:3rem; margin-bottom: 20px;'>The Confession</div>", unsafe_allow_html=True)
    
    # The Text Content (Unchanged)
    MESSAGE_BODY = """ Hello Vaibhavi,
Tereko romantic novels pasand hain na, aaj ek kahani sunata hoon.

Ek ladka tha, uska naam Yash. Uska breakup bahut kharaab hua tha—itna kharaab ki vo mentally kaafi down rehne laga. Usne apne kisi dost ko breakup ka asli reason nahi bataya. Uske andar ek toofan sa ban gaya tha. Uparwale ki kripa se uski ek dost thi, jisko usne sab bata diya, aur dheere-dheere usse baatein karte-karte vo thoda theek hone laga.

Us phase mein usne life ke baare mein bahut kuch seekha. Apna mann bhatakane ke liye usne kaafi cheezein try ki—dating apps, dates par jaana—par phir bhi dil ke kisi kone mein ye umeed thi ki shayad uski ex kabhi wapas aa jaaye, kabhi contact kare. Par aisa kabhi nahi hua. Apni dost ki help aur uski advice ki wajah se, vo dheere-dheere mentally strong banne laga, apni ex ko bhoolta gaya, aur wapas ek normal insaan ban gaya.

Lekin is waqt ek change aa chuka tha. Usne khud se promise kiya ki college mein vo kisi bhi ladki ko apna dil nahi dega, kisi se attach nahi hoga. Kyunki use lagta tha ki jisse bhi vo attach hoga, vo aakhir mein chhod ke chali jaayegi, aur use phir se usi dard se guzarna padega. Isi soch ke saath vo apni zindagi mein aage badhne laga. Dheere-dheere, vo phir se life enjoy karne laga—thanks to his friend as well.

Phir ek din campus mein uski mulaqat ek ladki se hui. Haalaat aise the ki vo dono saath kaam karne lage the. Dheere-dheere ye casual teammates ya colleagues wali baat dosti mein badal gayi. Ladke ko bhi accha lagne laga ki campus mein uski ek acchi female friend ban gayi hai jiske sang vo khulke baat kar sakke.

Time ke saath-saath vo dono kaafi ache dost ban gaye. Ladke ko samajh aane laga ki ladki ki life me itne struggles hai, family problems, silent struggles. Vo dono lagbhag sab kuch share karte the. Par dheere-dheere ladke ko lagne laga ki shayad vo ladki ke kaafi close aa raha hai. Uske andar vo purana darr wapas aa gaya—ki he shouldn’t fall for her.

Thoda confuse hoke, ladke ne decide kiya ki vo kuch din ladki se baat nahi karega, taaki use thoda time mile aur confusion kam ho jaaye. Par aisa ho nahi paaya. Circumstances aise the ki baat karni hi padi, aur ladki ke liye bhi fair nahi tha ki uska accha dost achanak se baat karna band kar de.

Toh phir dono wapas baat karne lage, kaam karne lage—sab normal hi tha. Ladke ko laga ki itna bhi kuch serious nahi hai, sab theek hi rahega. Lekin use bilkul andaza nahi tha ki aage kya hone wala hai.

Time ke saath-saath, jis ladki ka vo itna mazaak udaata tha, jiske saath hasta tha, shayad usse vo pasand karne laga tha. Use thoda-thoda bura lagne laga, sirf ye soch kar bhi ki uski dost kisi aur ke saath date par jaa sakti hai, ya kisi aur ke saath future me relation mein aa sakti hai. Usne khud ko samjhane ki bahut koshish ki—khud se kehta raha ki vo hota kaun hai use rokne wala, plz mat soch uske baare me!

Usne decide kiya ki ab vo apni dost se nafrat karega—chhoti-chhoti baaton par gussa karega, daantega, chillayega—taaki ek baar kaam khatam hone ke baad vo dono kabhi baat hi na karein, aur kabhi ek-dusre ka chehra bhi na dekhein.

Par jab bhi vo apni dost ka masoom sa chehra dekhta, vo gussa reh hi nahi paata tha. Uska koi plan kaam nahi kar raha tha. Ek saal baad phir se uske andar ek toofan paida ho gaya. Usne kisi ko kuch nahi bataya aur akele hi suffer karta raha.

Kabhi-kabhi vo shaant ho jaata tha, kabhi ajeeb sa behave karne lagta tha achanak. Uski dost ko bhi pareshani hone lagi ki use kya ho gaya hai. Kaash vo ladka bata paata… par vo nahi chahta tha ki vo kabhi us par burden bane. Vo bilkul nahi chahta tha ki uski dost kabhi is topic par soche, ya unki itni pyaari dosti par koi asar pade.

Vo ladka roz Bhagwan se pray karta tha ki sab theek ho jaaye, kyunki ab usse sambhala nahi ja raha tha. Vo is had tak tayaar tha ki uski dost ka koi boyfriend ban jaaye, aur fir uski dost usse kabhi baat hi na kare—sirf isliye taaki uski dost khush rahe, aur shayad time ke saath vo khud bhi theek ho jaaye.

Par uske andar itni himmat nahi thi ki vo khud uski dost ke liye koi ladka dhundh ke laaye, kyunki andar se vo ye bilkul nahi chahta tha ki vo kisi aur ke saath chali jaaye.

Vo ladka, jo khud ko mentally strong samajhta tha, phir se weak hone laga. Vo us din ka wait karne laga jab saara kaam khatam ho jaayega, jab shayad baat karne ke liye kuch bachega hi nahi. Vo bahut sad aur dara hua rehta tha ki vo din jaldi aa jaayega—but ek side se thoda relief bhi tha, ki shayad usse time mil jaayega use bhool paane ka.

Uske andar bahut dard tha. Vo ladka apni dost se itna pyaar kar baitha tha ki uski bhalaai ke liye use chhodne ko bhi tayaar tha. Par vo kabhi khud se ye baat usse keh nahi paaya. Ye ek baat hamesha uske dil mein reh gayi—jo vo kabhi bahar nahi nikaal paaya.

Vaibhavi, is kahani ka ladka koi aur nahi, balki main hoon.
Aur vo ladki… tu hai.

Mujhe pata hai shayad ye ajeeb lage, par sach yahi hai.
I am sorry.

Main ye sab face-to-face nahi keh paaya, aur yahi baat mujhe andar se khaaye ja rahi thi. Maine socha tha ki tujhe kabhi pata hi nahi chalna chahiye—but shayad tujhe jaanne ka thoda haq tha.

I am sorry ki main hamari itni pyaari dosti ko is situation tak le aaya. Tune mujhe itni khoobsurat memories di hain—main hamesha yaad rakhunga tujhe, aur tera “Jerry” wala gusse ka face. Ab koi nahi hai jisko main gussa dila paun… I will miss you.

I really love you.

Mai dua karta hoon ki tujhe ek bahut accha ladka mile—jo teri har baat maane, aur bilkul teri type ka ho, jiske sang tu khush aur safe rahe.
Mujhe ek acche insaan ki tarah yaad rkhna, jo shayad teri help karne aaya tha… par tujhse hi itna pyaar kar baitha.

Aur bhi bahut si baatein reh gayi hain jo kehni thi, par shayad ab aur nhi..
You are very lucky tere aur bhi dost hai, acche se rehna unke sang.

Pehli baar likhte-likhte meri aankhen moist ho gayi hain.
Shayad ab mera kaam bhi khatam ho gaya hai… aur mujhe chale jaana chahiye.

Please apna dhyan rakhna, koi aise vaise pagal se ladke ke peeche MTT pad jaana! Mujhe hamesha Teri chinta rahegi.
Dil se bata raha hu, maine Terese jyda cute creature aj tak nhi dekha…maine zaroor koi accha kaam kiya hoga jiske vajah tere se jaisa dost mil paaya mereko. 
Mai hamesha bolta tha mai jyda cute hu, but sachai yehi hai I JUST ADORE YOU SO MUCH, itna pyaara koi kaise ho sakta hai , tu itni pyaari kaise hai!
Tu bahut pyaari si squirrel jo hamesha mere yaado me rahegi. 

Mai Tera call naa uthau ajse toh please gussa mat karna, maaf kar dena aakhri baar.

Bye, Vaibhavi.
I am sorry.
Main teri saheli banke nahi reh paaya."""

    # Render with the paper effect
    st.markdown(f"""
    <div class='letter-paper'>
        <div class='story-text'>{MESSAGE_BODY}</div>
        <div class='signature'>— Anshit</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.balloons()