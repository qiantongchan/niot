import streamlit as st
st.set_page_config(page_title="CIMB Business Account Opening", page_icon="🏦", layout="wide")
# =========================================================
# STYLE
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"]  {
   font-family: 'Inter', sans-serif;
}
:root {
   --cimb-red: #D71920;
   --cimb-dark: #B31217;
   --cimb-light: #FDEBEC;
   --soft-gray: #F4F5F7;
   --mid-gray: #6B7280;
   --border: #E5E7EB;
   --text: #1F2937;
}
.stApp {
   background: #ffffff;
}
.topbar {
   background: white;
   border-bottom: 1px solid #eee;
   padding: 10px 8px 14px 8px;
   margin-bottom: 0;
}
.nav-pill {
   display: inline-block;
   margin-right: 10px;
   color: #374151;
   font-weight: 600;
   font-size: 14px;
}
.logo-wrap {
   text-align: center;
   font-size: 28px;
   font-weight: 800;
   color: var(--cimb-red);
   letter-spacing: 1px;
}
.top-actions {
   text-align: right;
   font-weight: 600;
   color: #374151;
   font-size: 14px;
}
.hero {
   background: linear-gradient(135deg, #d71920 0%, #b31217 60%, #8f0f13 100%);
   border-radius: 22px;
   padding: 0;
   overflow: hidden;
   margin-top: 14px;
   margin-bottom: 16px;
}
.hero-inner {
   display: grid;
   grid-template-columns: 1.1fr 1fr;
   min-height: 360px;
}
.hero-left {
   background:
       linear-gradient(rgba(0,0,0,0.18), rgba(0,0,0,0.18)),
       url('https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=1200&q=80');
   background-size: cover;
   background-position: center;
   min-height: 360px;
}
.hero-right {
   color: white;
   padding: 42px 38px;
   display: flex;
   flex-direction: column;
   justify-content: center;
}
.hero-kicker {
   font-size: 13px;
   letter-spacing: 0.12em;
   text-transform: uppercase;
   opacity: 0.9;
   margin-bottom: 10px;
   font-weight: 700;
}
.hero-title {
   font-size: 34px;
   line-height: 1.15;
   font-weight: 800;
   margin-bottom: 14px;
}
.hero-sub {
   font-size: 16px;
   line-height: 1.7;
   opacity: 0.95;
   margin-bottom: 18px;
}
.info-banner {
   background: white;
   border: 1px solid var(--border);
   border-radius: 18px;
   padding: 16px 18px;
   margin: 6px 0 18px 0;
   box-shadow: 0 6px 20px rgba(0,0,0,0.04);
}
.radio-card {
   background: white;
   border: 1px solid var(--border);
   border-radius: 18px;
   padding: 18px;
   margin-bottom: 18px;
   box-shadow: 0 6px 18px rgba(0,0,0,0.03);
}
.help-banner {
   background: #efefef;
   border-radius: 18px;
   padding: 24px;
   margin-top: 12px;
}
.help-title {
   font-size: 24px;
   font-weight: 800;
   margin-bottom: 18px;
   color: #1f2937;
}
.help-card {
   background: white;
   border-radius: 16px;
   border: 1px solid #ddd;
   padding: 18px;
   text-align: center;
   min-height: 150px;
}
.page-title {
   font-size: 30px;
   font-weight: 800;
   color: var(--cimb-red);
   margin-bottom: 4px;
}
.page-sub {
   color: var(--mid-gray);
   margin-bottom: 10px;
}
.form-card {
   background: white;
   border: 1px solid var(--border);
   border-radius: 18px;
   padding: 20px;
   margin-top: 12px;
   box-shadow: 0 8px 22px rgba(0,0,0,0.04);
}
.section-title {
   font-size: 20px;
   font-weight: 800;
   color: #111827;
   margin-bottom: 4px;
}
.section-subtitle {
   color: var(--mid-gray);
   margin-bottom: 16px;
   font-size: 14px;
}
.summary-box {
   background: #fff8f8;
   border: 1px solid #f3c6c8;
   border-radius: 16px;
   padding: 18px;
   margin-top: 16px;
}
.small-note {
   color: #6b7280;
   font-size: 13px;
}
.mandatory {
   color: var(--cimb-red);
   font-weight: 700;
}
.footer-space {
   height: 30px;
}
div[data-testid="stButton"] > button {
   border-radius: 12px;
   font-weight: 700;
   min-height: 44px;
}
div[data-testid="stButton"] > button[kind="primary"] {
   background: linear-gradient(90deg, #E23A40 0%, #D71920 50%, #B31217 100%) !important;
   color: white !important;
   border: none !important;
}
div[data-testid="stDownloadButton"] > button {
   border-radius: 12px;
}
.stProgress > div > div > div > div {
   background-color: #D71920;
}
</style>
""", unsafe_allow_html=True)
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
RISK_COUNTRY_TABLE = [
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
MANDATORY_KEYS = {
   "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "Q11", "Q12", "Q13"
}
# =========================================================
# SESSION STATE
# =========================================================
if "screen" not in st.session_state:
   st.session_state.screen = "landing"
if "step" not in st.session_state:
   st.session_state.step = 0
if "show_restricted_dialog" not in st.session_state:
   st.session_state.show_restricted_dialog = False
if "show_submit_dialog" not in st.session_state:
   st.session_state.show_submit_dialog = False
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
# =========================================================
# HELPERS
# =========================================================
def label_required(text: str):
   return f"{text} *"
def go_next():
   if st.session_state.step < len(PAGES) - 1:
       st.session_state.step += 1
def go_back():
   if st.session_state.step > 0:
       st.session_state.step -= 1
def top_header():
   left, center, right = st.columns([4, 2, 2])
   with left:
       st.markdown(
           """
<div class="topbar">
<span class="nav-pill">💼 Business Day to Day</span>
<span class="nav-pill">🚀 Business Solutions</span>
<span class="nav-pill">☪️ Islamic Banking</span>
<span class="nav-pill">🎁 Promotions</span>
<span class="nav-pill">📱 Digital Services</span>
<span class="nav-pill">🛟 Help & Support</span>
</div>
           """,
           unsafe_allow_html=True
       )
   with center:
       st.markdown('<div class="logo-wrap">CIMB</div>', unsafe_allow_html=True)
   with right:
       st.markdown(
           '<div class="top-actions">🔍 Search&nbsp;&nbsp;&nbsp;&nbsp;👤 Login</div>',
           unsafe_allow_html=True
       )
def render_progress():
   current = st.session_state.step
   pct = (current + 1) / len(PAGES)
   st.markdown(f'<div class="page-title">Open a Business Account</div>', unsafe_allow_html=True)
   st.markdown(
       '<div class="page-sub">Complete the form in a few simple steps. Fields marked with <span class="mandatory">*</span> are mandatory.</div>',
       unsafe_allow_html=True
   )
   st.progress(pct)
   c = st.columns(len(PAGES))
   for i, name in enumerate(PAGES):
       if i == current:
           c[i].markdown(f"**{i+1}. {name}**")
       else:
           c[i].caption(f"{i+1}. {name}")
def nav_buttons(next_label="Next", show_next=True):
   c1, c2, c3 = st.columns([1, 1, 5])
   with c1:
       if st.session_state.step > 0:
           if st.button("← Back", use_container_width=True):
               go_back()
               st.rerun()
   with c2:
       if show_next:
           if st.button(next_label, type="primary", use_container_width=True):
               go_next()
               st.rerun()
def yes_no(label, key):
   current = st.session_state.form.get(key)
   index = 0 if current in (None, "Yes") else 1
   val = st.radio(label, ["Yes", "No"], index=index, horizontal=True, key=f"widget_{key}")
   st.session_state.form[key] = val
   return val
def summary_value(v):
   if v is None or v == "":
       return "Not provided"
   return v
@st.dialog("Access Restricted")
def restricted_popup():
   st.error("Access restricted for Country of Registration: North Korea.")
   if st.button("Close", type="primary"):
       st.session_state.show_restricted_dialog = False
       st.rerun()
@st.dialog("Submission Successful")
def submitted_popup():
   st.success("Submitted.")
   if st.button("Close", type="primary"):
       st.session_state.show_submit_dialog = False
       st.rerun()
# =========================================================
# HEADER
# =========================================================
top_header()
# =========================================================
# LANDING PAGE
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
                       Check your eligibility, prepare your information, and submit online with ease.
</div>
</div>
</div>
</div>
       """,
       unsafe_allow_html=True
   )
   c1, c2, c3 = st.columns([4, 1.4, 1.2])
   with c2:
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
   c1, c2, c3 = st.columns([5, 1.2, 1])
   with c2:
       st.button("Login", type="primary", use_container_width=True, key="landing_login")
   st.markdown('<div class="radio-card">', unsafe_allow_html=True)
   nav = st.radio(
       "Navigate",
       ["FAQ", "Products and Packages", "First Time Login Guide", "User Guides and Forms"],
       horizontal=True,
       label_visibility="collapsed"
   )
   if nav == "FAQ":
       st.markdown("### Frequently Asked Questions")
       st.write("- Who is eligible to apply online for a business account?")
       st.write("- What documents should I prepare before starting?")
       st.write("- How long does the online application take?")
       st.write("- Can I continue later if I do not finish in one session?")
   elif nav == "Products and Packages":
       st.markdown("### Products and Packages")
       st.write("- Business Current Account")
       st.write("- SME banking solutions")
       st.write("- Payment and collection services")
       st.write("- Digital banking tools for day-to-day operations")
   elif nav == "First Time Login Guide":
       st.markdown("### First Time Login Guide")
       st.write("1. Register your profile")
       st.write("2. Verify your identity")
       st.write("3. Set up credentials")
       st.write("4. Log in to access your services")
   elif nav == "User Guides and Forms":
       st.markdown("### User Guides and Forms")
       st.write("- Account opening guide")
       st.write("- BizChannel onboarding guide")
       st.write("- Customer information forms")
       st.write("- Supporting document checklist")
   st.markdown('</div>', unsafe_allow_html=True)
   st.markdown(
       """
<div class="help-banner">
<div class="help-title">Need more information?</div>
</div>
       """,
       unsafe_allow_html=True
   )
   h1, h2, h3, h4 = st.columns(4)
   with h1:
       st.markdown('<div class="help-card"><div style="font-size:34px;">🛟</div><div style="font-weight:800; margin-top:6px;">Customer Help Centre</div><div style="color:#6B7280; margin-top:8px;">Find answers and self-service help.</div></div>', unsafe_allow_html=True)
   with h2:
       st.markdown('<div class="help-card"><div style="font-size:34px;">✉️</div><div style="font-weight:800; margin-top:6px;">Email Us</div><div style="color:#6B7280; margin-top:8px;">Reach out for general enquiries.</div></div>', unsafe_allow_html=True)
   with h3:
       st.markdown('<div class="help-card"><div style="font-size:34px;">📍</div><div style="font-weight:800; margin-top:6px;">Visit a Branch</div><div style="color:#6B7280; margin-top:8px;">Speak to our staff in person.</div></div>', unsafe_allow_html=True)
   with h4:
       st.markdown('<div class="help-card"><div style="font-size:34px;">📞</div><div style="font-weight:800; margin-top:6px;">Call Us at XX</div><div style="color:#6B7280; margin-top:8px;">Contact our support hotline.</div></div>', unsafe_allow_html=True)
# =========================================================
# FORM PAGE
# =========================================================
else:
   render_progress()
   # PAGE 1
   if st.session_state.step == 0:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Company Background</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Tell us about your business type and registration profile.</div>', unsafe_allow_html=True)
       st.session_state.form["Q1"] = st.selectbox(
           label_required("Q1. Type of Business"),
           BUSINESS_TYPES,
           index=BUSINESS_TYPES.index(st.session_state.form["Q1"]) if st.session_state.form["Q1"] in BUSINESS_TYPES else 0
       )
       if st.session_state.form["Q1"] != "Sole Proprietory":
           yes_no(
               label_required("Q1a. Is your company a subsidiary of a Public Listed company listed on the Main Board / Large Firms / MNCs / GLCs / MKDs / State owned enterprises?"),
               "Q1a"
           )
           if st.session_state.form["Q1a"] == "Yes":
               st.session_state.form["Q1b"] = st.text_input(
                   "Q1b. Name of Parent Company",
                   value=st.session_state.form["Q1b"]
               )
           else:
               st.session_state.form["Q1b"] = ""
       else:
           st.session_state.form["Q1a"] = None
           st.session_state.form["Q1b"] = ""
       yes_no(label_required("Q2. Malaysia Incorporated Business?"), "Q2")
       if st.session_state.form["Q2"] == "No":
           st.session_state.form["Q2a"] = st.selectbox(
               label_required("Q2a. Country of Registration"),
               COUNTRIES,
               index=COUNTRIES.index(st.session_state.form["Q2a"]) if st.session_state.form["Q2a"] in COUNTRIES else 0
           )
           if st.session_state.form["Q2a"] == "North Korea":
               st.session_state.show_restricted_dialog = True
       else:
           st.session_state.form["Q2a"] = None
       st.markdown('<div class="small-note"><span class="mandatory">*</span> is mandatory</div>', unsafe_allow_html=True)
       st.markdown('</div>', unsafe_allow_html=True)
       nav_buttons()
   # PAGE 2
   elif st.session_state.step == 1:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Compliance & Risk Screening</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Please answer the following compliance questions.</div>', unsafe_allow_html=True)
       st.markdown("**Q3. Listed higher-risk countries / jurisdictions**")
       st.table({"Countries / Jurisdictions": RISK_COUNTRY_TABLE})
       yes_no(label_required("Do you transact with or operate in the listed higher-risk countries / jurisdictions?"), "Q3")
       yes_no(label_required("Q4. Government / State Government Owned?"), "Q4")
       yes_no(label_required("Q5. Are any directors/shareholders/signatories politically exposed persons (PEPs)?"), "Q5")
       yes_no(label_required("Q6. Do you or your directors have ongoing legal cases related to fraud, insolvency or financial crimes?"), "Q6")
       yes_no(label_required("Q7. Has your business ever been subject to compliance actions or suspicious activity reporting?"), "Q7")
       st.markdown('<div class="small-note"><span class="mandatory">*</span> is mandatory</div>', unsafe_allow_html=True)
       st.markdown('</div>', unsafe_allow_html=True)
       nav_buttons()
   # PAGE 3
   elif st.session_state.step == 2:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Business Profile & Details</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Provide your business details below.</div>', unsafe_allow_html=True)
       st.session_state.form["Q8"] = st.selectbox(
           label_required("Q8. Nature of Business / Industry"),
           INDUSTRIES,
           index=INDUSTRIES.index(st.session_state.form["Q8"]) if st.session_state.form["Q8"] in INDUSTRIES else 0
       )
       c1, c2 = st.columns(2)
       with c1:
           st.session_state.form["Q9"] = st.text_input(
               label_required("Q9. Registered Business Name"),
               value=st.session_state.form["Q9"]
           )
       with c2:
           st.session_state.form["Q10"] = st.text_input(
               label_required("Q10. Business Registration Number"),
               value=st.session_state.form["Q10"]
           )
       c3, c4 = st.columns(2)
       with c3:
           options_owners = ["1", "2-10", "11-50", ">50"]
           st.session_state.form["Q11"] = st.selectbox(
               label_required("Q11. Number of shareholders / owners in the company"),
               options_owners,
               index=options_owners.index(st.session_state.form["Q11"]) if st.session_state.form["Q11"] in options_owners else 0
           )
       with c4:
           yes_no(label_required("Q12. Bumiputera-controlled Company? (>25% shareholding)"), "Q12")
       st.markdown('<div class="small-note"><span class="mandatory">*</span> is mandatory</div>', unsafe_allow_html=True)
       st.markdown('</div>', unsafe_allow_html=True)
       nav_buttons()
   # PAGE 4
   elif st.session_state.step == 3:
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Banking Relationship</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Let us know if you already bank with CIMB.</div>', unsafe_allow_html=True)
       yes_no(label_required("Q13. Does your company have an existing Business Current Account with CIMB?"), "Q13")
       if st.session_state.form["Q13"] == "Yes":
           st.session_state.form["Q13a"] = st.text_input(
               "Q13a. Existing CIMB Business Current Account Number",
               value=st.session_state.form["Q13a"],
               placeholder="Numeric account number"
           )
       else:
           st.session_state.form["Q13a"] = ""
       st.markdown('<div class="small-note"><span class="mandatory">*</span> is mandatory</div>', unsafe_allow_html=True)
       st.markdown('</div>', unsafe_allow_html=True)
       nav_buttons(next_label="Review")
   # PAGE 5
   elif st.session_state.step == 4:
       d = st.session_state.form
       st.markdown('<div class="form-card">', unsafe_allow_html=True)
       st.markdown('<div class="section-title">Review & Submit</div>', unsafe_allow_html=True)
       st.markdown('<div class="section-subtitle">Please review your information before submission.</div>', unsafe_allow_html=True)
       st.markdown('<div class="summary-box">', unsafe_allow_html=True)
       st.markdown("### Company Background")
       st.write({
           "Type of Business": summary_value(d["Q1"]),
           "Subsidiary of listed / state-linked entity": summary_value(d["Q1a"]),
           "Parent Company Name": summary_value(d["Q1b"]),
           "Malaysia Incorporated Business": summary_value(d["Q2"]),
           "Country of Registration": summary_value(d["Q2a"]),
       })
       st.markdown("### Compliance & Risk Screening")
       st.write({
           "Transacts / operates in listed higher-risk jurisdictions": summary_value(d["Q3"]),
           "Government / State Government Owned": summary_value(d["Q4"]),
           "Directors / shareholders / signatories are PEPs": summary_value(d["Q5"]),
           "Ongoing legal cases related to fraud / insolvency / financial crimes": summary_value(d["Q6"]),
           "Subject to compliance actions or suspicious activity reporting": summary_value(d["Q7"]),
       })
       st.markdown("### Business Profile & Details")
       st.write({
           "Nature of Business / Industry": summary_value(d["Q8"]),
           "Registered Business Name": summary_value(d["Q9"]),
           "Business Registration Number": summary_value(d["Q10"]),
           "Number of shareholders / owners": summary_value(d["Q11"]),
           "Bumiputera-controlled company": summary_value(d["Q12"]),
       })
       st.markdown("### Banking Relationship")
       st.write({
           "Existing CIMB Business Current Account": summary_value(d["Q13"]),
           "Existing CIMB Business Current Account Number": summary_value(d["Q13a"]),
       })
       st.markdown('</div>', unsafe_allow_html=True)
       c1, c2, c3 = st.columns([1, 1, 4])
       with c1:
           if st.button("← Back", use_container_width=True):
               go_back()
               st.rerun()
       with c2:
           if st.button("Submit", type="primary", use_container_width=True):
               st.session_state.show_submit_dialog = True
               st.rerun()
       st.markdown('</div>', unsafe_allow_html=True)
   if st.session_state.show_restricted_dialog:
       restricted_popup()
   if st.session_state.show_submit_dialog:
       submitted_popup()
st.markdown('<div class="footer-space"></div>', unsafe_allow_html=True)