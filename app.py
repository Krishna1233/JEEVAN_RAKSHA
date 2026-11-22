
import streamlit as st

st.set_page_config(
    page_title="JEEVANRAKSHA",
    page_icon="🛡️",
    layout="wide"
)

# Custom Design
st.markdown("""
<style>
.stApp {
    background-color: #f4f8fb;
}
.hero {
    background: linear-gradient(120deg, #102c46, #087e83);
    padding: 35px 22px;
    border-radius: 18px;
    color: white;
    text-align: center;
}
.hero h1 {
    color: white;
    font-size: 38px;
}
.hero p {
    color: #e1f5f3;
    font-size: 17px;
}
.feature {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #dce7ed;
    min-height: 150px;
}
.feature h3 {
    color: #123b50;
}
.feature p {
    color: #526575;
}
</style>
""", unsafe_allow_html=True)

# Language Selection
language = st.sidebar.selectbox(
    "Language / भाषा",
    ["English", "हिंदी"]
)

if language == "English":
    title = "Protect Lives. Connect Help."
    subtitle = "A Smart Flood Relief & Victim Support Platform"
    intro = "Helping flood-affected families and farmers connect with relief information."
    report = "Report Flood Damage"
    track = "Track My Report"
    benefits = "Government Help Finder"
    dashboard = "Relief Dashboard"
    safety = "Flood Safety Information"
else:
    title = "जीवन बचाएँ। सहायता पहुँचाएँ।"
    subtitle = "स्मार्ट बाढ़ राहत एवं पीड़ित सहायता प्लेटफॉर्म"
    intro = "बाढ़ प्रभावित परिवारों और किसानों को राहत की जानकारी से जोड़ने का प्रयास।"
    report = "बाढ़ नुकसान की रिपोर्ट"
    track = "अपनी रिपोर्ट देखें"
    benefits = "सरकारी सहायता योजनाएँ"
    dashboard = "राहत डैशबोर्ड"
    safety = "बाढ़ सुरक्षा जानकारी"

# Sidebar Navigation
st.sidebar.title("🛡️ JEEVANRAKSHA")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Report", "Track Report", "Help & Benefits", "Dashboard"]
)

# Home Page
if page == "Home":

    st.markdown(f"""
    <div class="hero">
        <h1>🛡️ JEEVANRAKSHA</h1>
        <h2>{title}</h2>
        <p>{subtitle}</p>
        <p>{intro}</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Our Services")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="feature">
            <h3>📝 {report}</h3>
            <p>Submit flood damage and assistance requests.</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown(f"""
        <div class="feature">
            <h3>🏛️ {benefits}</h3>
            <p>Explore relief schemes for families and farmers.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="feature">
            <h3>🔐 {track}</h3>
            <p>Access and update your report securely.</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown(f"""
        <div class="feature">
            <h3>📊 {dashboard}</h3>
            <p>View area-level relief information.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader(safety)

    st.info(
        "During a flood, move to safer higher ground. "
        "Avoid walking or driving through floodwater. "
        "Follow official government emergency instructions."
    )

    st.success(
        "JEEVANRAKSHA is a demonstration project, "
        "not an official government portal."
    )

elif page == "Report":
    st.title("📝 Report Flood Damage")
    st.write("Submit your flood damage and assistance request.")

    with st.form("flood_report_form"):
        district = st.text_input("District")
        village = st.text_input("Village / Area")

        damage_type = st.selectbox(
            "Type of Damage",
            ["House", "Crop", "Livestock", "Other"]
        )

        description = st.text_area("Describe your problem")

        submitted = st.form_submit_button("Submit Report")

        if submitted:
            if district.strip() and village.strip() and description.strip():
                st.success("Your report has been submitted successfully! (Demo only)")
            else:
                st.warning("Please fill in all required fields.")

elif page == "Track Report":
    st.title("🔐 " + track)
    st.info("Secure Ticket ID and Private Access Code feature is coming next.")

elif page == "Help & Benefits":
    st.title("🏛️ " + benefits)
    st.info("Verified government relief information will be added here.")

elif page == "Dashboard":
    st.title("📊 " + dashboard)
    st.info("Area-level relief dashboard will be developed next.")

st.divider()

st.caption(
    "JEEVANRAKSHA | Gujarat Pilot | "
    "Demo Version | Not an official government service"
      )
  
