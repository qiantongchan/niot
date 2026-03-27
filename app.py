import streamlit as st
st.set_page_config(page_title="CIMB Business Onboarding", page_icon="🏦", layout="wide")
# =========================
# STYLE
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"]  {
   font-family: 'Inter', sans-serif;
}
:root {
   --cimb-red: #D71920;
   --cimb-dark-red: #B31217;
   --cimb-soft-red: #FDEBEC;
   --cimb-bg: #F8F9FB;
   --text-dark: #1F2937;
   --muted: #6B7280;
   --card-border: #E5E7EB;
}
.stApp {
   background: linear-gradient(180deg, #fff 0%, #fff7f7 100%);
}
.main-title {
   font-size: 2rem;
   font-weight: 700;
   color: var(--cimb-red);
   margin-bottom: 0.2rem;
}
.subtle {
   color: var(--muted);
   font-size: 0.95rem;
   margin-bottom: 1rem;
}
.form-card {
   background: white;
   border: 1px solid var(--card-border);
   border-radius: 18px;
   padding: 1.25rem 1.25rem 1rem 1.25rem;
   box-shadow: 0 8px 24px rgba(0,0,0,0.04);
   margin-bottom: 1rem;
}
.section-title {
   font-size: 1.1rem;
   font-weight: 700;
   color: var(--text-dark);
   margin-bottom: 0.25rem;
}
.section-subtitle {
   color: var(--muted);
   margin-bottom: 1rem;
   font-size: 0.92rem;
}
.milestone-wrap {
   margin: 0.8rem 0 1.2rem 0;
}
.milestone-row {
   display: flex;
   gap: 12px;
   flex-wrap: wrap;
   margin-top: 0.75rem;
}
.milestone {
   padding: 8px 12px;
   border-radius: 999px;
   border: 1px solid #f1c4c6;
   background: #fff;
   color: #8B1E22;
   font-size: 0.85rem;
   font-weight: 600;
}
.milestone.active {
   background: var(--cimb-red);
   color: white;
   border-color: var(--cimb-red);
}
.milestone.done {
   background: #FDEBEC;
   color: var(--cimb-dark-red);
   border-color: #f3b4b7;
}
.summary-kpi {
   background: #fff;
   border: 1px solid var(--card-border);
   border-radius: 14px;
   padding: 1rem;
   text-align: center;
}
.summary-kpi h3 {
   margin: 0;
   color: var(--cimb-red);
}
.summary-kpi p {
   margin: 0.3rem 0 0 0;
   color: var(--muted);
}
.stButton > button {
   border-radius: 12px;
   font-weight: 600;
   padding: 0.6rem 1rem;
   border: 1px solid var(--cimb-red);
}
.primary-btn button,
div[data-testid="column"] .stButton > button[kind="primary"] {
   background: var(--cimb-red) !important;
   color: white !important;
   border: 1px solid var(--cimb-red) !important;
}
.note-box {
   background: #fff7e6;
   border: 1px solid #f5d38c;
   color: #8a5a00;
   padding: 0.9rem 1rem;
   border-radius: 12px;
   margin-top: 0.75rem;
}
.blocked-box {
   background: #fff0f1;
   border: 1px solid #f5a2a7;
   color: #9f1239;
   padding: 1rem;
   border-radius: 14px;
   font-weight: 600;
   margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)
# =========================
# DATA
# =========================
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
RESTRICTED_COUNTRY = "North Korea"
SANCTIONED_COUNTRIES = [
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
# =========================
# SESSION STATE
# =========================
if "step" not in st.session_state:
   st.session_state.step = 0
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
       "Q9": None,
       "Q10": "",
       "Q11": None,
       "Q12": None,
       "Q13": None,
       "Q13a": "",
   }
# =========================
# HELPERS
# =========================
def go_next():
   if st.session_state.step < len(PAGES) - 1:
       st.session_state.step += 1
def go_back():
   if st.session_state.step > 0:
       st.session_state.step -= 1
def progress_header():
   current = st.session_state.step
   pct = (current + 1) / len(PAGES)
   st.markdown('<div class="main-title">🏦 CIMB Business Onboarding</div>', unsafe_allow_html=True)
   st.markdown(
       '<div class="subtle">Pre-screening for non-individual onboarding. Complete each section and click Next to continue.</div>',
       unsafe_allow_html=True,
   )
   st.markdown('<div class="milestone-wrap">', unsafe_allow_html=True)
   st.progress(pct)
   pills = []
   for i, page in enumerate(PAGES):
       cls = "milestone"
       if i < current:
           cls += " done"
       elif i == current:
           cls += " active"
       pills.append(f'<span class="{cls}">{i+1}. {page}</span>')
   st.markdown(f'<div class="milestone-row">{"".join(pills)}</div>', unsafe_allow_html=True)
   st.markdown('</div>', unsafe_allow_html=True)
def nav_buttons(show_next=True, next_label="Next"):
   c1, c2, c3 = st.columns([1, 1, 4])
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
def yes_no(label, key, horizontal=True):
   current = st.session_state.form.get(key)
   idx = 0 if current in (None, "Yes") else 1
   value = st.radio(label, ["Yes", "No"], index=idx, horizontal=horizontal, key=f"widget_{key}")
   st.session_state.form[key] = value
   return value
def summary_value(val):
   if val is None or val == "":
       return "-"
   return val
# =========================
# UI
# =========================
progress_header()
# -------------------------
# PAGE 1
# -------------------------
if st.session_state.step == 0:
   st.markdown('<div class="form-card">', unsafe_allow_html=True)
   st.markdown('<div class="section-title">🏢 Company Background</div>', unsafe_allow_html=True)
   st.markdown('<div class="section-subtitle">Basic entity classification and registration routing.</div>', unsafe_allow_html=True)
   st.session_state.form["Q1"] = st.selectbox(
       "Q1. Type of Business",
       BUSINESS_TYPES,
       index=BUSINESS_TYPES.index(st.session_state.form["Q1"]) if st.session_state.form["Q1"] in BUSINESS_TYPES else 0
   )
   needs_q1a = st.session_state.form["Q1"] != "Sole Proprietory"
   if needs_q1a:
       yes_no(
           "Q1a. Is your company a subsidiary of a Public Listed company listed on the Main Board / Large Firms / MNCs / GLCs / MKDs / State owned enterprises?",
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
   yes_no("Q2. Malaysia Incorporated Business?", "Q2")
   restricted = False
   if st.session_state.form["Q2"] == "No":
       st.session_state.form["Q2a"] = st.selectbox(
           "Q2a. Country of Registration",
           COUNTRIES,
           index=COUNTRIES.index(st.session_state.form["Q2a"]) if st.session_state.form["Q2a"] in COUNTRIES else 0
       )
       if st.session_state.form["Q2a"] == RESTRICTED_COUNTRY:
           restricted = True
           st.markdown(
               '<div class="blocked-box">⛔ Access restricted due to country of registration.</div>',
               unsafe_allow_html=True
           )
   else:
       st.session_state.form["Q2a"] = None
   st.markdown('</div>', unsafe_allow_html=True)
   if restricted:
       c1, c2 = st.columns([1, 5])
       with c1:
           if st.button("← Back", use_container_width=True):
               go_back()
               st.rerun()
   else:
       nav_buttons()
# -------------------------
# PAGE 2
# -------------------------
elif st.session_state.step == 1:
   st.markdown('<div class="form-card">', unsafe_allow_html=True)
   st.markdown('<div class="section-title">🛡️ Compliance & Risk Screening</div>', unsafe_allow_html=True)
   st.markdown('<div class="section-subtitle">High-level risk filters and red-flag declarations.</div>', unsafe_allow_html=True)
   yes_no(
       "Q3. Do you transact with or operate in the listed higher-risk countries/jurisdictions?",
       "Q3"
   )
   with st.expander("View listed countries / jurisdictions"):
       st.write(", ".join(SANCTIONED_COUNTRIES))
   yes_no("Q4. Government / State Government Owned?", "Q4")
   yes_no("Q5. Are any directors/shareholders/signatories politically exposed persons (PEPs)?", "Q5")
   yes_no("Q6. Do you or your directors have ongoing legal cases related to fraud, insolvency or financial crimes?", "Q6")
   yes_no("Q7. Has your business ever been subject to compliance actions or suspicious activity reporting?", "Q7")
   flags = []
   if st.session_state.form["Q3"] == "Yes":
       flags.append("Jurisdiction exposure declared")
   if st.session_state.form["Q4"] == "Yes":
       flags.append("Government-linked ownership")
   if st.session_state.form["Q5"] == "Yes":
       flags.append("PEP declared")
   if st.session_state.form["Q6"] == "Yes":
       flags.append("Legal / financial crime case declared")
   if st.session_state.form["Q7"] == "Yes":
       flags.append("Compliance / SAR history declared")
   if flags:
       st.markdown('<div class="note-box">⚠️ Screening flags detected: ' + "; ".join(flags) + '</div>', unsafe_allow_html=True)
   st.markdown('</div>', unsafe_allow_html=True)
   nav_buttons()
# -------------------------
# PAGE 3
# -------------------------
elif st.session_state.step == 2:
   st.markdown('<div class="form-card">', unsafe_allow_html=True)
   st.markdown('<div class="section-title">📋 Business Profile & Details</div>', unsafe_allow_html=True)
   st.markdown('<div class="section-subtitle">Core company information and ownership profile.</div>', unsafe_allow_html=True)
   st.session_state.form["Q8"] = st.selectbox(
       "Q8. Nature of Business / Industry",
       INDUSTRIES,
       index=INDUSTRIES.index(st.session_state.form["Q8"]) if st.session_state.form["Q8"] in INDUSTRIES else 0
   )
   c1, c2 = st.columns(2)
   with c1:
       st.session_state.form["Q9"] = st.text_input(
           "Q9. Registered Business Name",
           value=st.session_state.form["Q9"]
       )
   with c2:
       st.session_state.form["Q10"] = st.text_input(
           "Q10. Business Registration Number",
           value=st.session_state.form["Q10"]
       )
   c3, c4 = st.columns(2)
   with c3:
       st.session_state.form["Q11"] = st.selectbox(
           "Q11. Number of shareholders / owners in the company",
           ["1", "2-10", "11-50", ">50"],
           index=["1", "2-10", "11-50", ">50"].index(st.session_state.form["Q11"]) if st.session_state.form["Q11"] in ["1", "2-10", "11-50", ">50"] else 0
       )
   with c4:
       yes_no("Q12. Bumiputera-controlled Company? (>25% shareholding)", "Q12", horizontal=True)
   st.markdown('</div>', unsafe_allow_html=True)
   nav_buttons()
# -------------------------
# PAGE 4
# -------------------------
elif st.session_state.step == 3:
   st.markdown('<div class="form-card">', unsafe_allow_html=True)
   st.markdown('<div class="section-title">🏦 Banking Relationship</div>', unsafe_allow_html=True)
   st.markdown('<div class="section-subtitle">Existing banking relationship check.</div>', unsafe_allow_html=True)
   yes_no("Q13. Does your company have an existing Business Current Account with CIMB?", "Q13")
   if st.session_state.form["Q13"] == "Yes":
       st.session_state.form["Q13a"] = st.text_input(
           "Q13a. Existing CIMB Business Current Account Number",
           value=st.session_state.form["Q13a"],
           placeholder="Numeric account number"
       )
   else:
       st.session_state.form["Q13a"] = ""
   st.markdown('</div>', unsafe_allow_html=True)
   nav_buttons(next_label="Review")
# -------------------------
# PAGE 5
# -------------------------
elif st.session_state.step == 4:
   data = st.session_state.form
   st.markdown('<div class="form-card">', unsafe_allow_html=True)
   st.markdown('<div class="section-title">✅ Review & Submit</div>', unsafe_allow_html=True)
   st.markdown('<div class="section-subtitle">Check the captured answers before submission.</div>', unsafe_allow_html=True)
   score = 0
   flags = []
   if data["Q3"] == "Yes":
       score += 25
       flags.append("Jurisdiction exposure")
   if data["Q4"] == "Yes":
       score += 15
       flags.append("Government ownership")
   if data["Q5"] == "Yes":
       score += 30
       flags.append("PEP declared")
   if data["Q6"] == "Yes":
       score += 30
       flags.append("Legal / financial crime case")
   if data["Q7"] == "Yes":
       score += 25
       flags.append("Compliance action / SAR history")
   if data["Q2a"] == "North Korea":
       score += 100
       flags.append("Restricted jurisdiction")
   risk_level = "Low"
   if score >= 60:
       risk_level = "High"
   elif score >= 25:
       risk_level = "Medium"
   k1, k2, k3 = st.columns(3)
   with k1:
       st.markdown(f'<div class="summary-kpi"><h3>{score}</h3><p>Risk Score</p></div>', unsafe_allow_html=True)
   with k2:
       st.markdown(f'<div class="summary-kpi"><h3>{risk_level}</h3><p>Risk Level</p></div>', unsafe_allow_html=True)
   with k3:
       st.markdown(f'<div class="summary-kpi"><h3>{len(flags)}</h3><p>Flags Triggered</p></div>', unsafe_allow_html=True)
   st.markdown("### Company Background")
   st.write({
       "Q1 Type of Business": summary_value(data["Q1"]),
       "Q1a Subsidiary of listed / state-linked entity": summary_value(data["Q1a"]),
       "Q1b Parent Company": summary_value(data["Q1b"]),
       "Q2 Malaysia Incorporated": summary_value(data["Q2"]),
       "Q2a Country of Registration": summary_value(data["Q2a"]),
   })
   st.markdown("### Compliance & Risk Screening")
   st.write({
       "Q3 High-risk country exposure": summary_value(data["Q3"]),
       "Q4 Government owned": summary_value(data["Q4"]),
       "Q5 PEP": summary_value(data["Q5"]),
       "Q6 Legal / fraud / insolvency cases": summary_value(data["Q6"]),
       "Q7 Compliance / suspicious activity history": summary_value(data["Q7"]),
   })
   st.markdown("### Business Profile & Details")
   st.write({
       "Q8 Industry": summary_value(data["Q8"]),
       "Q9 Registered Business Name": summary_value(data["Q9"]),
       "Q10 Registration Number": summary_value(data["Q10"]),
       "Q11 Number of Shareholders/Owners": summary_value(data["Q11"]),
       "Q12 Bumiputera-controlled": summary_value(data["Q12"]),
   })
   st.markdown("### Banking Relationship")
   st.write({
       "Q13 Existing CIMB Business Current Account": summary_value(data["Q13"]),
       "Q13a Existing Account Number": summary_value(data["Q13a"]),
   })
   if flags:
       st.markdown("### 🚩 Screening Flags")
       for f in flags:
           st.warning(f)
   st.download_button(
       "⬇️ Download Submission JSON",
       data=str(data),
       file_name="cimb_onboarding_prescreening.json",
       mime="application/json",
       use_container_width=False
   )
   c1, c2, c3 = st.columns([1, 1, 4])
   with c1:
       if st.button("← Back", use_container_width=True):
           go_back()
           st.rerun()
   with c2:
       if st.button("Submit", type="primary", use_container_width=True):
           st.success("Pre-screening submitted.")
           st.balloons()
   st.markdown('</div>', unsafe_allow_html=True)