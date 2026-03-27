import streamlit as st
import base64
from pathlib import Path
st.set_page_config(page_title="CIMB Business Account Opening", page_icon="🏦", layout="wide")
# =========================================================
# LOCAL IMAGE PATHS
# =========================================================
CIMB_LOGO_PATH = r"C:\Users\MX446RB\OneDrive - EY\Documents\04 Project (local folder)\CIMB NIOT\prototype\assets\CIMB-Logo.png"
HERO_IMAGE_PATH = r"C:\Users\MX446RB\OneDrive - EY\Documents\04 Project (local folder)\CIMB NIOT\prototype\assets\June-2023-BizChannel-hero-banner-image.png"

def image_to_base64(path: str) -> str:
   p = Path(path)
   if not p.exists():
       return ""
   return base64.b64encode(p.read_bytes()).decode()

logo_b64 = image_to_base64(CIMB_LOGO_PATH)
hero_b64 = image_to_base64(HERO_IMAGE_PATH)
# =========================================================
# DATA
# =========================================================
BUSINESS_TYPES = [
   "Sole Proprietory",
   "Partnership",
   "LLP",
   "Professional Firm",
   "Association/Club/Society",
   "Company (Sdn Bhd)",
   "Company (Bhd)",
]
COUNTRIES = [
   "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
   "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
   "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
   "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
   "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
   "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
   "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica",
   "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti",
   "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
   "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
   "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
   "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
   "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
   "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo",
   "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
   "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
   "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
   "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
   "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
   "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman",
   "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru",
   "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
   "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
   "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
   "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
   "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain",
   "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan",
   "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga",
   "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
   "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America",
   "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
   "Yemen", "Zambia", "Zimbabwe"
]
RISK_COUNTRY_LIST = [
   "Afghanistan", "Belarus", "Central African Republic",
   "Crimea Region (including Donetsk People’s Republic, Luhansk People’s Republic, and non-government-controlled areas of Zaporizhzhia and Kherson region of Ukraine)",
   "Democratic Republic of Congo", "Haiti", "Iran", "Iraq", "Lebanon", "Libya",
   "Myanmar", "North Korea", "Russia", "Somalia", "South Sudan", "Sudan", "Syria",
   "Venezuela", "Yemen", "Zimbabwe"
]
INDUSTRIES = [
   "Manufacturing",
   "Trading / Wholesale",
   "Retail",
   "Construction",
   "Healthcare",
   "Technology",
   "Education",
   "Professional Services",
   "Food & Beverage",
   "Transportation / Logistics",
   "Real Estate",
   "Money Changer",
   "Gaming",
   "Gold / Precious Metals",
   "Pawn",
   "Remittance",
   "Others",
]
PAGES = [
   "Company Background",
   "Compliance & Risk Screening",
   "Business Profile & Details",
   "Banking Relationship",
   "Review & Submit",
]
TAB_OPTIONS = {
   "FAQ": "❓",
   "Products & Packages": "💼",
   "First Time Login Guide": "🔐",
   "User Guides & Forms": "📄",
}
MENU_ITEMS = [
   "💼 Business Day to Day",
   "🚀 Business Solutions",
   "☪️ Islamic Banking",
   "🎁 Promotions",
   "📱 Digital Services",
   "🛟 Help & Support",
]
# =========================================================
# SESSION
# =========================================================
if "screen" not in st.session_state:
   st.session_state.screen = "landing"
if "step" not in st.session_state:
   st.session_state.step = 0
if "show_restricted_dialog" not in st.session_state:
   st.session_state.show_restricted_dialog = False
if "show_submit_dialog" not in st.session_state:
   st.session_state.show_submit_dialog = False
if "show_menu" not in st.session_state:
   st.session_state.show_menu = False
if "active_tab" not in st.session_state:
   st.session_state.active_tab = "FAQ"
if "form" not in st.session_state:
   st.session_state.form = {
       "Q1": None,
       "Q1a": None,
       "Q1b": "",
       "Q2": None,
       "Q2a": None,
       "Q3": None,
       "Q4": None,
       "Q5": None,
       "Q6": None,
       "Q7": None,
       "Q8": None,
       "Q9": "",
       "Q10": "",
       "Q11": None,
       "Q12": None,
       "Q13": None,
       "Q13a": "",
   }
if "field_errors" not in st.session_state:
   st.session_state.field_errors = set()
# =========================================================
# STYLE
# =========================================================
hero_bg_css = ""
if hero_b64:
   hero_bg_css = f'url("data:image/png;base64,{hero_b64}")'
else:
   hero_bg_css = "linear-gradient(135deg,#d71920 0%,#b31217 60%,#8f0f13 100%)"
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {{
   font-family: 'Poppins', sans-serif;
}}
:root {{
   --cimb-red: #D71920;
   --cimb-dark: #B31217;
   --cimb-light: #FDEBEC;
   --soft-gray: #F4F5F7;
   --mid-gray: #6B7280;
   --border: #E5E7EB;
   --text: #1F2937;
   --danger: #d71920;
}}
.stApp {{
   background: #ffffff;
}}
.top-actions {{
   text-align: right;
   font-weight: 600;
   color: #374151;
   font-size: 14px;
   padding-top: 10px;
}}
.hero {{
   background: linear-gradient(135deg, #d71920 0%, #b31217 60%, #8f0f13 100%);
   border-radius: 24px;
   overflow: hidden;
   margin-top: 12px;
   margin-bottom: 18px;
}}
.hero-inner {{
   display: grid;
   grid-template-columns: 1.05fr 1fr;
   min-height: 380px;
}}
.hero-left {{
   background-image: {hero_bg_css};
   background-size: cover;
   background-position: center;
   min-height: 380px;
}}
.hero-right {{
   color: white;
   padding: 42px 40px;
   display: flex;
   flex-direction: column;
   justify-content: center;
}}
.hero-kicker {{
   font-size: 13px;
   letter-spacing: 0.12em;
   text-transform: uppercase;
   opacity: 0.92;
   margin-bottom: 10px;
   font-weight: 700;
}}
.hero-title {{
   font-size: 34px;
   line-height: 1.15;
   font-weight: 800;
   margin-bottom: 14px;
}}
.hero-sub {{
   font-size: 16px;
   line-height: 1.7;
   opacity: 0.96;
   margin-bottom: 20px;
}}
.info-banner {{
   background: white;
   border: 1px solid var(--border);
   border-radius: 18px;
   padding: 18px;
   margin: 6px 0 18px 0;
   box-shadow: 0 6px 20px rgba(0,0,0,0.04);
}}
.tabs-area {{
   background: white;
   border: 1px solid var(--border);
   border-radius: 18px;
   padding: 18px;
   margin-bottom: 18px;
   box-shadow: 0 6px 18px rgba(0,0,0,0.03);
}}
.tab-panel {{
   margin-top: 16px;
   border: 1px solid #f0d6d8;
   background: #fff8f8;
   border-radius: 16px;
   padding: 18px;
}}
.help-banner {{
   background: #eeeeee;
   border-radius: 20px;
   padding: 24px;
   margin-top: 12px;
}}
.help-title {{
   font-size: 24px;
   font-weight: 800;
   margin-bottom: 18px;
   color: #1f2937;
}}
.help-card {{
   background: white;
   border-radius: 16px;
   border: 1px solid #ddd;
   padding: 18px;
   text-align: center;
   min-height: 150px;
}}
.page-title {{
   font-size: 30px;
   font-weight: 800;
   color: var(--cimb-red);
   margin-bottom: 4px;
}}
.page-sub {{
   color: var(--mid-gray);
   margin-bottom: 10px;
}}
.form-card {{
   background: white;
   border: 1px solid var(--border);
   border-radius: 18px;
   padding: 20px;
   margin-top: 12px;
   box-shadow: 0 8px 22px rgba(0,0,0,0.04);
}}
.section-title {{
   font-size: 20px;
   font-weight: 800;
   color: #111827;
   margin-bottom: 4px;
}}
.section-subtitle {{
   color: var(--mid-gray);
   margin-bottom: 16px;
   font-size: 14px;
}}
.summary-box {{
   background: #fff8f8;
   border: 1px solid #f3c6c8;
   border-radius: 16px;
   padding: 18px;
   margin-top: 16px;
}}
.summary-block {{
   background: white;
   border: 1px solid #f0d4d6;
   border-radius: 14px;
   padding: 16px;
   margin-bottom: 14px;
}}
.summary-row {{
   display: flex;
   justify-content: space-between;
   gap: 20px;
   padding: 8px 0;
   border-bottom: 1px solid #f3f4f6;
}}
.summary-row:last-child {{
   border-bottom: none;
}}
.summary-label {{
   color: #6b7280;
   font-weight: 600;
   min-width: 280px;
}}
.summary-value {{
   color: #111827;
   font-weight: 500;
   text-align: right;
}}
.step-pill {{
   padding: 10px 12px;
   border-radius: 999px;
   border: 1px solid #f0c7ca;
   color: #8f1d22;
   background: white;
   font-size: 13px;
   font-weight: 700;
   text-align: center;
}}
.step-pill.active {{
   background: var(--cimb-red);
   color: white;
   border-color: var(--cimb-red);
}}
.step-pill.done {{
   background: #fdebec;
   color: var(--cimb-dark);
   border-color: #f2b8bc;
}}
.menu-item {{
   padding: 12px 10px;
   border-radius: 10px;
   border: 1px solid #efefef;
   margin-bottom: 10px;
   font-weight: 600;
   background: #fff;
}}
.red-star {{
   color: var(--cimb-red);
   font-weight: 700;
}}
.field-error-box {{
   border: 2px solid var(--danger);
   border-radius: 14px;
   padding: 10px 12px 2px 12px;
   margin-bottom: 10px;
   background: #fff5f5;
}}
.field-error-text {{
   color: var(--danger);
   font-size: 12px;
   font-weight: 600;
   margin-top: -4px;
   margin-bottom: 8px;
}}
div[data-testid="stButton"] > button {{
   border-radius: 12px;
   font-weight: 700;
   min-height: 44px;
}}
div[data-testid="stButton"] > button[kind="primary"] {{
   background: linear-gradient(90deg, #E23A40 0%, #D71920 50%, #B31217 100%) !important;
   color: white !important;
   border: none !important;
}}
.stProgress > div > div > div > div {{
   background-color: #D71920;
}}
</style>
""", unsafe_allow_html=True)
# =========================================================
# HELPERS
# =========================================================
def go_home():
   st.session_state.screen = "landing"
   st.session_state.step = 0
   st.session_state.field_errors = set()
def label_required(text: str):
   return f"{text} *"
def go_next():
   if st.session_state.step < len(PAGES) - 1:
       st.session_state.step += 1
def go_back():
   if st.session_state.step > 0:
       st.session_state.step -= 1
def summary_value(v):
   if v is None or v == "":
       return None
   return str(v)
def begin_error_box(key: str):
   if key in st.session_state.field_errors:
       st.markdown('<div class="field-error-box">', unsafe_allow_html=True)
       return True
   return False
def end_error_box(key: str, message: str):
   if key in st.session_state.field_errors:
       st.markdown(f'<div class="field-error-text">{message}</div></div>', unsafe_allow_html=True)
def yes_no(label, key):
   started = begin_error_box(key)
   current = st.session_state.form.get(key)
   options = ["Yes", "No"]
   index = options.index(current) if current in options else None
   value = st.radio(label, options, index=index, horizontal=True, key=f"widget_{key}")
   st.session_state.form[key] = value
   end_error_box(key, "This field is required.")
   return value
def validate_step(step: int):
   d = st.session_state.form
   errors = set()
   if step == 0:
       if not d["Q1"]:
           errors.add("Q1")
       if d["Q1"] != "Sole Proprietory":
           if not d["Q1a"]:
               errors.add("Q1a")
           if d["Q1a"] == "Yes" and not d["Q1b"].strip():
               errors.add("Q1b")
       if not d["Q2"]:
           errors.add("Q2")
       if d["Q2"] == "No":
           if not d["Q2a"]:
               errors.add("Q2a")
           if d["Q2a"] == "North Korea":
               st.session_state.show_restricted_dialog = True
               st.session_state.field_errors = set()
               return False
   elif step == 1:
       for k in ["Q3", "Q4", "Q5", "Q6", "Q7"]:
           if not d[k]:
               errors.add(k)
   elif step == 2:
       if not d["Q8"]:
           errors.add("Q8")
       if not d["Q9"].strip():
           errors.add("Q9")
       if not d["Q10"].strip():
           errors.add("Q10")
       if not d["Q11"]:
           errors.add("Q11")
       if not d["Q12"]:
           errors.add("Q12")
   elif step == 3:
       if not d["Q13"]:
           errors.add("Q13")
       if d["Q13"] == "Yes":
           if not d["Q13a"].strip():
               errors.add("Q13a")
           elif not d["Q13a"].strip().isdigit():
               errors.add("Q13a")
   st.session_state.field_errors = errors
   return len(errors) == 0
@st.dialog("Access Restricted")
def restricted_popup():
   st.error("Access restricted for Country of Registration: North Korea.")
   c1, c2 = st.columns(2)
   with c1:
       if st.button("Back to home", type="primary", use_container_width=True):
           st.session_state.show_restricted_dialog = False
           go_home()
           st.rerun()
   with c2:
       if st.button("Close", use_container_width=True):
           st.session_state.show_restricted_dialog = False
           st.rerun()
@st.dialog("Submitted")
def submitted_popup():
   st.success("Submitted.")
   if st.button("Close", type="primary"):
       st.session_state.show_submit_dialog = False
       st.rerun()
# =========================================================
# TOP HEADER
# =========================================================
c1, c2, c3 = st.columns([1.2, 3, 2])
with c1:
   if st.session_state.screen == "landing":
       if st.button("☰", key="hamburger_btn"):
           st.session_state.show_menu = not st.session_state.show_menu
           st.rerun()
with c2:
   if logo_b64:
       st.markdown(
           f"""
<div style="text-align:center;">
<img src="data:image/png;base64,{logo_b64}" style="height:48px; margin-bottom:8px;">
</div>
           """,
           unsafe_allow_html=True
       )
   if st.button("Home", key="go_home_logo"):
       go_home()
       st.rerun()
with c3:
   st.markdown('<div class="top-actions">🔍 Search&nbsp;&nbsp;&nbsp;&nbsp;👤 Login</div>', unsafe_allow_html=True)
if st.session_state.screen == "landing" and st.session_state.show_menu:
   with st.sidebar:
       st.markdown("## Menu")
       for item in MENU_ITEMS:
           st.markdown(f'<div class="menu-item">{item}</div>', unsafe_allow_html=True)
       if st.button("Close menu", use_container_width=True):
           st.session_state.show_menu = False
           st.rerun()
# =========================================================
# LANDING
# =========================================================
if st.session_state.screen == "landing":
   st.markdown(
       """
<div class="hero">
<div class="hero-inner">
<div class="hero-left"></div>
<div class="hero-right">
<div class="hero-kicker">Digital Services</div>
<div class="hero-title">Save time to check eligibility and apply online for your account in a few clicks.</div>
<div class="hero-sub">
                       Start your business banking journey with a simpler digital onboarding experience.
                       Check eligibility, prepare your information, and submit online with ease.
</div>
</div>
</div>
</div>
       """,
       unsafe_allow_html=True
   )
   hero_btn_cols = st.columns([5, 2.0, 0.8])
   with hero_btn_cols[1]:
       if st.button("I'm interested", type="primary", use_container_width=True):
           st.session_state.screen = "form"
           st.rerun()
   st.markdown(
       """
<div class="info-banner">
<div style="display:flex; justify-content:space-between; align-items:center; gap:20px;">
<div>
<div style="font-weight:800; font-size:18px; color:#111827;">Already an existing user?</div>
<div style="color:#6B7280;">Access your accounts on BizChannel@CIMB</div>
</div>
</div>
</div>
       """,
       unsafe_allow_html=True
   )
   login_cols = st.columns([5, 1.3, 0.7])
   with login_cols[1]:
       st.button("Login", type="primary", use_container_width=True, key="existing_user_login")
   st.markdown('<div class="tabs-area">', unsafe_allow_html=True)
   tab_cols = st.columns(4)
   for idx, (label, icon) in enumerate(TAB_OPTIONS.items()):
       with tab_cols[idx]:
           is_active = st.session_state.active_tab == label
           button_label = f"{icon} {label}"
           if st.button(button_label, key=f"tab_{label}", use_container_width=True, type="primary" if is_active else "secondary"):
               st.session_state.active_tab = label
               st.rerun()
   st.markdown('<div class="tab-panel">', unsafe_allow_html=True)
   if st.session_state.active_tab == "FAQ":
       st.markdown("### Frequently Asked Questions")
       st.write("Find answers on eligibility, required documents, application turnaround time, and the onboarding journey.")
   elif st.session_state.active_tab == "Products & Packages":
       st.markdown("### Products & Packages")
       st.write("Explore business current accounts, SME solutions, cash management options, and digital banking packages.")
   elif st.session_state.active_tab == "First Time Login Guide":
       st.markdown("### First Time Login Guide")
       st.write("Learn how to register, verify your business profile, create credentials, and access BizChannel securely.")
   elif st.session_state.active_tab == "User Guides & Forms":
       st.markdown("### User Guides & Forms")
       st.write("Access onboarding guides, reference documents, user guides, and required forms for account application.")
   st.markdown('</div></div>', unsafe_allow_html=True)
   st.markdown('<div class="help-banner">', unsafe_allow_html=True)
   st.markdown('<div class="help-title">Need more information?</div>', unsafe_allow_html=True)
   h1, h2, h3, h4 = st.columns(4)
   with h1:
       st.markdown('<div class="help-card"><div style="font-size:34px;">🛟</div><div style="font-weight:800; margin-top:6px;">Customer Help Centre</div><div style="color:#6B7280; margin-top:8px;">Find answers and self-service help.</div></div>', unsafe_allow_html=True)
   with h2:
       st.markdown('<div class="help-card"><div style="font-size:34px;">✉️</div><div style="font-weight:800; margin-top:6px;">Email Us</div><div style="color:#6B7280; margin-top:8px;">Reach out for general enquiries.</div></div>', unsafe_allow_html=True)
   with h3:
       st.markdown('<div class="help-card"><div style="font-size:34px;">📍</div><div style="font-weight:800; margin-top:6px;">Visit a Branch</div><div style="color:#6B7280; margin-top:8px;">Speak to our staff in person.</div></div>', unsafe_allow_html=True)
   with h4:
       st.markdown('<div class="help-card"><div style="font-size:34px;">📞</div><div style="font-weight:800; margin-top:6px;">Call Us at XX</div><div style="color:#6B7280; margin-top:8px;">Contact our support hotline.</div></div>', unsafe_allow_html=True)
   st.markdown('</div>', unsafe_allow_html=True)
# =========================================================
# FORM
# =========================================================
else:
   st.markdown('<div class="page-title">Pre-screening questionnaire</div>', unsafe_allow_html=True)
   st.markdown(
       '<div class="page-sub">Complete each section and click Next to continue. Fields marked with <span class="red-star">*</span> are mandatory.</div>',
       unsafe_allow_html=True
   )
   st.progress((st.session_state.step + 1) / len(PAGES))
   step_cols = st.columns(len(PAGES))
   for i, page in enumerate(PAGES):
       cls = "step-pill"
       if i < st.session_state.step:
           cls += " done"
       elif i == st.session_state.step:
           cls += " active"
       step_cols[i].markdown(f'<div class="{cls}">{i+1}. {page}</div>', unsafe_allow_html=True)
   d = st.session_state.form
   if st.session_state.step == 0:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Company Background</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Tell us about your business type and registration profile.</div>', unsafe_allow_html=True)
       begin_error_box("Q1")
       d["Q1"] = st.selectbox(
           label_required("Q1. Type of Business"),
           BUSINESS_TYPES,
           index=BUSINESS_TYPES.index(d["Q1"]) if d["Q1"] in BUSINESS_TYPES else None,
           placeholder="Select one"
       )
       end_error_box("Q1", "This field is required.")
       if d["Q1"] != "Sole Proprietory":
           yes_no(label_required("Q1a. Is your company a subsidiary of a Public Listed company listed on the Main Board / Large Firms / MNCs / GLCs / MKDs / State owned enterprises?"), "Q1a")
           begin_error_box("Q1b")
           if d["Q1a"] == "Yes":
               d["Q1b"] = st.text_input(label_required("Q1b. Name of Parent Company"), value=d["Q1b"])
           else:
               d["Q1b"] = ""
           end_error_box("Q1b", "This field is required.")
       else:
           d["Q1a"] = None
           d["Q1b"] = ""
       yes_no(label_required("Q2. Malaysia Incorporated Business?"), "Q2")
       if d["Q2"] == "No":
           begin_error_box("Q2a")
           d["Q2a"] = st.selectbox(
               label_required("Q2a. Country of Registration"),
               COUNTRIES,
               index=COUNTRIES.index(d["Q2a"]) if d["Q2a"] in COUNTRIES else None,
               placeholder="Select country"
           )
           end_error_box("Q2a", "This field is required.")
           if d["Q2a"] == "North Korea":
               st.session_state.show_restricted_dialog = True
       else:
           d["Q2a"] = None
       st.markdown('</div>', unsafe_allow_html=True)
   elif st.session_state.step == 1:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Compliance & Risk Screening</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Please answer the following compliance questions.</div>', unsafe_allow_html=True)
       st.markdown("**Q3. Listed higher-risk countries / jurisdictions**")
       with st.expander("View listed countries / jurisdictions"):
           st.write(", ".join(RISK_COUNTRY_LIST))
       yes_no(label_required("Do you transact with or operate in the listed higher-risk countries / jurisdictions?"), "Q3")
       yes_no(label_required("Q4. Government / State Government Owned?"), "Q4")
       yes_no(label_required("Q5. Are any directors/shareholders/signatories politically exposed persons (PEPs)?"), "Q5")
       yes_no(label_required("Q6. Do you or your directors have ongoing legal cases related to fraud, insolvency or financial crimes?"), "Q6")
       yes_no(label_required("Q7. Has your business ever been subject to compliance actions or suspicious activity reporting?"), "Q7")
       st.markdown('</div>', unsafe_allow_html=True)
   elif st.session_state.step == 2:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Business Profile & Details</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Provide your business details below.</div>', unsafe_allow_html=True)
       begin_error_box("Q8")
       d["Q8"] = st.selectbox(
           label_required("Q8. Nature of Business / Industry"),
           INDUSTRIES,
           index=INDUSTRIES.index(d["Q8"]) if d["Q8"] in INDUSTRIES else None,
           placeholder="Select one"
       )
       end_error_box("Q8", "This field is required.")
       c1, c2 = st.columns(2)
       with c1:
           begin_error_box("Q9")
           d["Q9"] = st.text_input(label_required("Q9. Registered Business Name"), value=d["Q9"])
           end_error_box("Q9", "This field is required.")
       with c2:
           begin_error_box("Q10")
           d["Q10"] = st.text_input(label_required("Q10. Business Registration Number"), value=d["Q10"])
           end_error_box("Q10", "This field is required.")
       c3, c4 = st.columns(2)
       with c3:
           begin_error_box("Q11")
           owner_options = ["1", "2-10", "11-50", ">50"]
           d["Q11"] = st.selectbox(
               label_required("Q11. Number of shareholders / owners in the company"),
               owner_options,
               index=owner_options.index(d["Q11"]) if d["Q11"] in owner_options else None,
               placeholder="Select one"
           )
           end_error_box("Q11", "This field is required.")
       with c4:
           yes_no(label_required("Q12. Bumiputera-controlled Company? (>25% shareholding)"), "Q12")
       st.markdown('</div>', unsafe_allow_html=True)
   elif st.session_state.step == 3:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Banking Relationship</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Let us know if you already bank with CIMB.</div>', unsafe_allow_html=True)
       yes_no(label_required("Q13. Does your company have an existing Business Current Account with CIMB?"), "Q13")
       if d["Q13"] == "Yes":
           begin_error_box("Q13a")
           d["Q13a"] = st.text_input(
               label_required("Q13a. Existing CIMB Business Current Account Number"),
               value=d["Q13a"],
               placeholder="Numeric account number"
           )
           if "Q13a" in st.session_state.field_errors and d["Q13a"].strip() and not d["Q13a"].strip().isdigit():
               end_error_box("Q13a", "Account number must be numeric.")
           else:
               end_error_box("Q13a", "This field is required.")
       else:
           d["Q13a"] = ""
       st.markdown('</div>', unsafe_allow_html=True)
   elif st.session_state.step == 4:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Review & Submit</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Please review your information before submission.</div>', unsafe_allow_html=True)
       st.markdown('<div class="summary-box">', unsafe_allow_html=True)
       def section_block(title, rows):
           filtered_rows = [(label, value) for label, value in rows if summary_value(value) is not None]
           if not filtered_rows:
               return
           st.markdown(f'<div class="summary-block"><div style="font-weight:800; font-size:18px; margin-bottom:10px;">{title}</div>', unsafe_allow_html=True)
           for label, value in filtered_rows:
               st.markdown(
                   f'''
<div class="summary-row">
<div class="summary-label">{label}</div>
<div class="summary-value">{summary_value(value)}</div>
</div>
                   ''',
                   unsafe_allow_html=True
               )
           st.markdown('</div>', unsafe_allow_html=True)
       section_block("Company Background", [
           ("Type of Business", d["Q1"]),
           ("Subsidiary of listed / state-linked entity", d["Q1a"]),
           ("Parent Company Name", d["Q1b"]),
           ("Malaysia Incorporated Business", d["Q2"]),
           ("Country of Registration", d["Q2a"]),
       ])
       section_block("Compliance & Risk Screening", [
           ("Transacts / operates in listed higher-risk jurisdictions", d["Q3"]),
           ("Government / State Government Owned", d["Q4"]),
           ("Directors / shareholders / signatories are PEPs", d["Q5"]),
           ("Ongoing legal cases related to fraud / insolvency / financial crimes", d["Q6"]),
           ("Subject to compliance actions or suspicious activity reporting", d["Q7"]),
       ])
       section_block("Business Profile & Details", [
           ("Nature of Business / Industry", d["Q8"]),
           ("Registered Business Name", d["Q9"]),
           ("Business Registration Number", d["Q10"]),
           ("Number of shareholders / owners", d["Q11"]),
           ("Bumiputera-controlled company", d["Q12"]),
       ])
       section_block("Banking Relationship", [
           ("Existing CIMB Business Current Account", d["Q13"]),
           ("Existing CIMB Business Current Account Number", d["Q13a"]),
       ])
       st.markdown('</div></div>', unsafe_allow_html=True)
   # nav
   c1, c2, c3 = st.columns([1, 1, 5])
   with c1:
       if st.session_state.step > 0:
           if st.button("← Back", use_container_width=True):
               st.session_state.field_errors = set()
               go_back()
               st.rerun()
   with c2:
       if st.session_state.step < len(PAGES) - 1:
           if st.button("Next", type="primary", use_container_width=True):
               if validate_step(st.session_state.step):
                   go_next()
                   st.rerun()
               else:
                   st.rerun()
       else:
           if st.button("Submit", type="primary", use_container_width=True):
               if validate_step(3):
                   st.session_state.show_submit_dialog = True
                   st.rerun()
               else:
                   st.rerun()
# dialogs
if st.session_state.show_restricted_dialog:
   restricted_popup()
if st.session_state.show_submit_dialog:
   submitted_popup()