
import streamlit as st
import requests
import urllib.parse
from supabase import create_client

def calculate_priority(damage_type, description):

    text = (str(damage_type) + " " + str(description)).lower()

    high_keywords = [
        "trapped", "life danger", "rescue",
        "people stranded", "house flooded",
        "पानी में फंसे", "जान का खतरा",
        "बचाव", "घर में पानी"
    ]

    medium_keywords = [
        "crop", "livestock", "house damage",
        "फसल", "पशुधन", "मकान क्षति"
    ]

    if any(word in text for word in high_keywords):
        return "High"

    elif any(word in text for word in medium_keywords):
        return "Medium"

    return "Low"

st.set_page_config(
    page_title="JEEVANRAKSHA",
    page_icon="🛡️",
    layout="wide"
)


@st.cache_data(ttl=86400)
def get_india_districts():
    url = "https://raw.githubusercontent.com/CodingMation/indian-states-districts/main/data/india_states_districts.json"

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data:
            return data

        return None

    except Exception as e:
        st.error(f"District API Error: {e}")
        return None

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_SECRET_KEY"]
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

page_names = {
    "Home": "Home",
    "Report": "Report",
    "Track Report": "Track Report",
    "Help & Benefits": "Help & Benefits",
    "Donation & Support":"Donation & Support",
    "Emergency Help Center": "Emergency Help Center",
    "Resource Matching":"Resource Matching",
    "Dashboard": "Dashboard",
    "Admin Panel": "Admin Panel"
}

if language == "हिंदी":
    page_names = {
        "Home": "होम",
        "Report": "रिपोर्ट दर्ज करें",
        "Track Report": "रिपोर्ट ट्रैक करें",
        "Help & Benefits": "सहायता और लाभ",
        "Emergency Help Center": "आपातकालीन सहायता",
        "Dashboard": "राहत डैशबोर्ड",
        "Admin Panel": "एडमिन पैनल"
    }
def go_to_page(target):
    st.session_state["navigation"] = page_names[target]
page = st.sidebar.radio(
    "Navigation / नेविगेशन",
    list(page_names.values()),
    key="navigation"
)

page = {
    display: original
    for original, display in page_names.items()
}[page]
 
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

    st.button(
        "📊 Open Dashboard",
        use_container_width=True,
        on_click=go_to_page,
        args=("Dashboard",)
    )

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

        st.button(
            "📝 Open Report Page",
            use_container_width=True,
            on_click=go_to_page,
            args=("Report",)
        )

        st.markdown(f"""
        <div class="feature">
            <h3>🏛️ {benefits}</h3>
            <p>Explore relief schemes for families and farmers.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "🏛️ Open Help & Benefits",
            use_container_width=True,
            on_click=go_to_page,
            args=("Help & Benefits",)
        )

    with col2:
        st.markdown(f"""
        <div class="feature">
            <h3>🔐 {track}</h3>
            <p>Access and update your report securely.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "🔐 Track Your Report",
            use_container_width=True,
            on_click=go_to_page,
            args=("Track Report",)
        )

        st.markdown(f"""
        <div class="feature">
            <h3>📊 {dashboard}</h3>
            <p>View area-level relief information.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "📊 View Dashboard",
            use_container_width=True,
            on_click=go_to_page,
            args=("Dashboard",)
        )

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
            import uuid
            import hashlib
            import secrets

            ticket_id = "JVR-" + uuid.uuid4().hex[:12].upper()
            access_code = secrets.token_urlsafe(12)

            access_hash = hashlib.sha256(
                access_code.encode()
            ).hexdigest()

            try:
                supabase.table("reports").insert({
                    "ticket_id": ticket_id,
                    "access_code_hash": access_hash,
                    "district": district.strip(),
                    "village": village.strip(),
                    "damage_type": damage_type,
                    "description": description.strip(),
                    "status": "Submitted"
                }).execute()

                st.success("Report saved successfully!")
                st.write("Ticket ID:", ticket_id)
                st.write("Private Access Code:", access_code)
                st.warning("Save both details safely. Access Code will be shown only once.")

            except Exception as e:
                st.error("Report could not be saved.")
                st.code(str(e))

        else:
            st.warning("Please fill in all required fields.")
             

elif page == "Track Report":
    st.title("🔐 " + track)
    st.write("Enter your Ticket ID and Private Access Code.")
    ticket = st.text_input("Ticket ID")
    access = st.text_input(
        "Private Access Code",
        type="password"
    )

    if st.button("Track My Report"):
        if ticket.strip() and access.strip():
            import hashlib

            access_hash = hashlib.sha256(
                access.strip().encode()
            ).hexdigest()

            try:
                result = supabase.table("reports").select(
                    "ticket_id, district, village, damage_type, status, created_at"
                ).eq(
                    "ticket_id", ticket.strip()
                ).eq(
                    "access_code_hash", access_hash
                ).execute()

                if result.data:
                    report = result.data[0]

                    st.success("Report found successfully!")

                    st.write("Ticket ID:", report["ticket_id"])
                    st.write("District:", report["district"])
                    st.write("Village / Area:", report["village"])
                    st.write("Damage Type:", report["damage_type"])
                    st.write("Current Status:", report["status"])

                    st.subheader("📍 Report Status Timeline")

                    status = report["status"]

                    steps = ["Submitted", "Under Review", "Resolved"]

                    for step in steps:
                        if step == "Submitted":
                            st.success("✅ Submitted")
                        elif step == "Under Review" and status in ["Under Review", "Resolved"]:
                            st.success("✅ Under Review")
                        elif step == "Resolved" and status == "Resolved":
                            st.success("✅ Resolved")
       
                else:                                     

                    st.error( 
"Invalid Ticket ID or Private Access Code."
                    )

            except Exception:
                st.error("Unable to track report. Please try again.")

        else:
            st.warning("Please enter both Ticket ID and Access Code.")

elif page == "Help & Benefits":
    st.title("🏛️ Government Help Finder")
    st.subheader("🆘 SOS Quick Access")
    st.warning("Emergency में तुरंत सहायता के लिए कॉल करें।")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.link_button("🚨 Call 112", "tel:112")

    with col2:
        st.link_button("🚑 Call 102", "tel:102")

    with col3:
        st.link_button("🔥 Call 101", "tel:101")
    st.subheader("Find Government Relief Schemes Across India")

     
    states = [
    "Andhra Pradesh", "Arunachal Pradesh",
    "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh",
    "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha",
    "Punjab", "Rajasthan", "Sikkim",
    "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand",
    "West Bengal", "Andaman and Nicobar Islands",
    "Chandigarh", "Delhi", "Jammu and Kashmir",
    "Ladakh", "Lakshadweep", "Puducherry","Dadra and Nagar Haveli and Daman and Diu"
    ]


    state = st.selectbox("Select Your State / UT", states)

    online_data = get_india_districts()

    if online_data:
        districts = {
            item["name"]: [
                district["name"]
                for district in item["districts"]
            ]
            for item in online_data
        }
    else:
        districts = {
            "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Anand"],
            "Bihar": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur", "Darbhanga"],
            "Uttar Pradesh": ["Prayagraj", "Lucknow", "Varanasi", "Kanpur", "Gorakhpur"],
            "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Thane"],
            "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer"]
        }

    district_list = districts.get(state, [])

    selected_district =            st.selectbox(
        "Help District",
        district_list if district_list else ["District list coming soon"]
    )
    
    district_list = districts.get(state, [])

    selected_district = st.selectbox(
        "Select Your District",
        district_list if district_list else ["District list coming soon"]
    )

    need = st.selectbox(
        "What kind of help do you need?",
        [
            "Flood Damage",
            "Crop Damage",
            "House Damage",
            "Livestock Loss",
            "Food Assistance",
            "Medical Assistance",
            "Financial Assistance"
        ]
    )

    st.write("### Government Information")
    
    search_text =f"{need} {selected_district} {state}site:gov.in"

    search_url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote(search_text)
    )

    st.link_button("🔎 Search Government Information", search_url)

    st.link_button(
        "🇮🇳 myScheme Portal",
        "https://www.myscheme.gov.in/"
    )

    st.link_button(
        "🇮🇳 National Portal of India",
        "https://www.india.gov.in/"
    )


    st.link_button(
        "🏛️ National Government Portal",
       "https://www.india.gov.in/"
    )

    st.info("Check the official government website "
        "for eligibility, documents and application details."
    )


elif page == "Donation & Support":

    st.title("❤️ Donation & Support")
    st.subheader("Help Every Victim. Support Every Life.")

    st.write(
        "JEEVANRAKSHA aims to connect kind-hearted people "
        "with victims and families who need support."
    )

    st.info(
        "Every contribution, whether financial or in the form "
        "of essential supplies, can make a difference."
    )

    st.subheader("🤝 Who Can We Support?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🌊 Disaster Victims")
        st.write("Flood, earthquake and other natural disaster victims.")

        st.markdown("### 🔥 Accident & Fire Victims")
        st.write("People affected by accidents and fire incidents.")

        st.markdown("### 🏥 Medical Support")
        st.write("Poor families needing medical assistance.")

        st.markdown("### 🌾 Farmers")
        st.write("Farmers facing financial loss and hardship.")

    with col2:
        st.markdown("### 👨‍👩‍👧 Needy Families")
        st.write("Poor and economically vulnerable families.")

        st.markdown("### 👵 Elderly & Disabled")
        st.write("Elderly and disabled people needing assistance.")

        st.markdown("### 🏚️ Homeless People")
        st.write("People needing food, shelter and essential supplies.")

        st.markdown("### 🆘 Other Victims")
        st.write("People facing unexpected emergencies.")

    st.divider()

    st.subheader("💝 Ways to Contribute")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💰 Financial Donation")
        st.write("Support verified relief funds and organizations.")

    with col2:
        st.markdown("### 📦 Essential Supplies")
        st.write("Contribute food, clothes, medicines and other essentials.")

    st.warning(
        "Donation collection is not active yet. "
        "Please contribute only through verified organizations "
        "and official relief funds."
    )

    st.success(
        "Together, we can bring hope, support and dignity "
        "to people in difficult situations."
    )


    st.divider()

    st.title("🙋 Volunteer Registration")

    st.write(
        "Join JEEVANRAKSHA and help people in need. "
        "You can register without providing a mobile number."
    )

    with st.form("volunteer_registration"):

        volunteer_name = st.text_input("Full Name")

        volunteer_state = st.text_input("State")

        volunteer_district = st.text_input("District")

        volunteer_email = st.text_input(
            "Email (Optional)"
        )

        volunteer_skills = st.multiselect(
            "How would you like to help?",
            [
                "Food Distribution",
                "Medical Assistance",
                "Rescue Support",
                "Clothes & Essential Supplies",
                "Shelter Support",
                "Fundraising",
                "Other"
            ]
        )

        volunteer_availability = st.selectbox(
            "Availability",
            [
                "Available Anytime",
                "Weekends",
                "Part Time",
                "Only During Emergencies"
            ]
        )

        volunteer_submit = st.form_submit_button(
            "🙋 Register as Volunteer",
            use_container_width=True
        )

        if volunteer_submit:

            if (
                volunteer_name.strip()
                and volunteer_state.strip()
                and volunteer_district.strip()
                and volunteer_skills
            ):
                st.success(
                    "Thank you for your interest! "
                    "Your volunteer details are ready."
                )

            else:
                st.error(
                    "Please fill Name, State, District "
                    "and select at least one helping skill."
                )

elif page == "Emergency Help Center":
    st.title("🚨 Emergency Help Center")
    st.subheader("State & District Wise Emergency Contacts")
    with st.expander("🛡️ Flood Emergency Safety Checklist"):
        st.warning("बाढ़ के दौरान अपनी सुरक्षा का ध्यान रखें।")

        st.checkbox("बिजली के खंभों और खुले तारों से दूर रहें")
        st.checkbox("गहरे बाढ़ के पानी में न उतरें")
        st.checkbox("जरूरी दवाइयाँ और दस्तावेज सुरक्षित रखें")
        st.checkbox("बच्चों और बुजुर्गों को सुरक्षित स्थान पर रखें")
        st.checkbox("पीने के लिए सुरक्षित पानी इस्तेमाल करें")
        st.checkbox("आपातकाल में 112 पर कॉल करें")

    states =["Andhra Pradesh",     "Arunachal Pradesh", "Assam",
"Bihar", "Chhattisgarh", "Goa", "Gujarat","Haryana", 
"Himachal Pradesh","Jharkhand",
"Karnataka", "Kerala", 
"Madhya Pradesh",
"Maharashtra", "Manipur", "Meghalaya", "Mizoram",
"Nagaland", "Odisha",  "Punjab", "Rajasthan","Sikkim", 
"Tamil Nadu", "Telangana", "Tripura",
"Uttar Pradesh", "Uttarakhand", "West Bengal",
"Andaman and Nicobar Islands", "Chandigarh","Delhi", 
"Jammu and Kashmir", "Ladakh",
"Lakshadweep", "Puducherry"
    ]
    
    selected_state = st.selectbox(
        "Select Your State / UT", states
    )

    online_data = get_india_districts()

    if online_data:
        districts = {
            item["name"]: [
                district["name"]
                for district in item["districts"]
            ]
            for item in online_data
        }
     
    else:
        districts = {
            "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
            "Bihar": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur"],
            "Uttar Pradesh": ["Lucknow", "Varanasi", "Prayagraj", "Kanpur"],
            "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik"],
            "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota"]
        }

    district_list = districts.get(selected_state, [])

    selected_district=(
        st.selectbox(
       "Emergency District",
         district_list if district_list else ["District list coming soon"],key="emergency_district"
        )
    )
    st.error("🚨 National Emergency Number: 112")
    st.link_button("📞 Call Emergency 112", "tel:112")

    st.subheader("📞 Other Emergency Helplines")

    st.write("🌊 Disaster Relief: 1070")
    st.link_button("Call Disaster Helpline", "tel:1070")

    st.write("🚑 National Ambulance: 102")
    st.link_button("Call Ambulance", "tel:102")

    st.write("🔥 Fire Emergency: 101")
    st.link_button("Call Fire Service", "tel:101")
    st.link_button(
        "🇮🇳 NDMA Official Help Desk",
        "https://sachet.ndma.gov.in/"
    )
    
    st.markdown("---")
    st.subheader("🏛️ District Government Help")

    search_query = (
        f"{selected_district} {selected_state} "
        "official district administration website"
    )

    search_url = (
      "https://www.google.com/search?q="
        + urllib.parse.quote(search_query)
    )
    st.link_button(
        "🔎 Find District Government Website",
        search_url
    )

    st.link_button(
        "🌐 NDMA State Helpdesk",
        "https://sachet.ndma.gov.in/HelpDesk"
    )

    st.caption(
        "Verify contact details on official government websites."
    )


    st.divider()

    st.subheader("🎒 Emergency Ready Checklist")

    st.write(
        "Prepare these essential items before an emergency."
    )

    emergency_items = [
        "Drinking Water",
        "Dry Food & Biscuits",
        "First Aid Kit",
        "Essential Medicines",
        "Torch & Extra Batteries",
        "Mobile Phone & Power Bank",
        "Important Documents",
        "Clothes & Blankets",
        "Cash & Emergency Contacts"
    ]

    st.write("Check the items you have prepared:")

    for item in emergency_items:
        st.checkbox(item, key=f"emergency_{item}")

    st.info(
        "Keep emergency supplies in a safe, waterproof bag "
        "and follow official safety instructions."
    )


elif page == "Resource Matching":

    st.title("🤝 Need & Resource Matching")
    st.write("Connect people in need with available relief resources.")

    st.subheader("📢 Register a Need")

    need = st.selectbox(
        "What support is needed?",
        ["Food", "Drinking Water", "Clothes",
         "Medicines", "Shelter", "Other"]
    )

    district = st.text_input("Enter District")
    quantity = st.number_input(
        "Required Quantity",
        min_value=1,
        step=1
    )

    if st.button("Submit Need"):
        if district.strip():
            st.success(
                f"Need recorded: {quantity} units of {need} in {district}."
            )
            st.info(
                "This is a demo entry. It is not yet saved "
                "or matched with a real donor."
            )
        else:
            st.warning("Please enter your district.")

    st.divider()

    st.subheader("🎁 Register Available Resources")

    resource = st.selectbox(
        "What can you provide?",
        ["Food", "Drinking Water", "Clothes",
         "Medicines", "Shelter", "Other"],
        key="resource_type"
    )

    resource_district = st.text_input(
        "Your District",
        key="resource_district"
    )

    available_quantity = st.number_input(
        "Available Quantity",
        min_value=1,
        step=1,
        key="available_quantity"
    )

    if st.button("Submit Available Resource"):
        if resource_district.strip():
            st.success(
                f"{available_quantity} units of {resource} "
                f"offered in {resource_district}."
            )
            st.info(
                "This is a demo entry. It is not yet saved "
                "or matched with a real person."
            )
        else:
            st.warning("Please enter your district.")

elif page == "Dashboard":
    st.title("📊 Smart Relief Dashboard")
    st.write("Live overview of flood damage reports.")
    st.subheader("🚀 Quick Access")

    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "📝 Report Damage",
            use_container_width=True,
            on_click=go_to_page,
            args=("Report",)
        )

        st.button(
            "🔍 Track Report",
            use_container_width=True,
            on_click=go_to_page,
            args=("Track Report",)
        )

    with col2:
        st.button(
            "🆘 Emergency Help",
            use_container_width=True,
            on_click=go_to_page,
            args=("Emergency Help Center",)
        )

        st.button(
            "🤝 Help & Benefits",
            use_container_width=True,
            on_click=go_to_page,
            args=("Help & Benefits",)
        )  


    st.divider()
    st.subheader("📊 Relief Transparency Board")

    try:
        transparency_result = (
            supabase.table("reports")
            .select("status")
            .execute()
        )

        transparency_reports = transparency_result.data or []

        total_reports = len(transparency_reports)

        pending_reports = sum(
            1 for r in transparency_reports
            if r.get("status") == "Submitted"
        )

        review_reports = sum(
            1 for r in transparency_reports
            if r.get("status") == "Under Review"
        )

        resolved_reports = sum(
            1 for r in transparency_reports
            if r.get("status") == "Resolved"
        )

        resolution_rate = (
            resolved_reports / total_reports * 100
            if total_reports > 0 else 0
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total Reports", total_reports)
        c2.metric("Pending", pending_reports)
        c3.metric("Under Review", review_reports)
        c4.metric("Resolved", resolved_reports)

        st.progress(resolution_rate / 100)

        st.caption(
            f"Resolution Rate: {resolution_rate:.1f}%"
        )

    except Exception:
        st.warning("Transparency data is currently unavailable.")
  
    try:
        result = supabase.table("reports").select(
            "district, damage_type, status"
        ).execute()

        reports = result.data

        total = len(reports)

        submitted_count = sum(
            1 for r in reports if r["status"] == "Submitted"
        )

        under_review = sum(
            1 for r in reports if r["status"] == "Under Review"
        )

        verified = sum(
            1 for r in reports if r["status"] == "Verified"
        )

        resolved = sum(
            1 for r in reports if r["status"] == "Resolved"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Reports", total)
        col2.metric("Submitted", submitted_count)
        col3.metric("Under Review", under_review)

        col4, col5 = st.columns(2)

        col4.metric("Verified", verified)
        col5.metric("Resolved", resolved)


        st.divider()

        st.subheader("Damage Type Overview")

        damage_counts = {}

        for r in reports:
            damage = r["damage_type"]
            damage_counts[damage] = damage_counts.get(damage, 0) + 1

        if damage_counts:
            st.bar_chart(damage_counts)
        else:
            st.info("No reports available yet.")

        st.divider()

        st.subheader("District-wise Reports")

        district_counts = {}

        for r in reports:
            district = r["district"]
            district_counts[district] = district_counts.get(district, 0) + 1

        if district_counts:
            st.bar_chart(district_counts)

    except Exception:
        st.error("Dashboard data could not be loaded.")

elif page == "Admin Panel":
    st.title("🔐 Admin Report Management")

    if not st.session_state.get("admin_logged_in", False):
        st.subheader("Admin Login")

        admin_password = st.text_input(
            "Enter Admin Password",
            type="password"
        )

        if st.button("Login"):
            if admin_password == st.secrets["ADMIN_PASSWORD"]:
                st.session_state["admin_logged_in"] = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Incorrect Admin Password.")

    else:
        st.success("Welcome, Admin!")

        if st.button("Logout"):
            st.session_state["admin_logged_in"] = False
            st.rerun()

        st.divider()
        st.subheader("📋 All Flood Reports")

        try:
            result = supabase.table("reports").select(
                "ticket_id, district, village, damage_type, description, status, created_at"
            ).order("created_at", desc=True).execute()

            reports = result.data
            for report in reports:
                priority = calculate_priority(
                    report.get("damage_type", ""),
                    report.get("description", "")
                )

                report["priority"] = priority

            priority_order = {
                "High": 1,
                "Medium": 2,
                "Low": 3
            }

            reports.sort(
                key=lambda r: priority_order.get(
                    r["priority"], 3
                )
            )

            if reports:
                st.write("Total Reports:", len(reports))

                st.subheader("📍 District-wise Priority Dashboard")

                district_data = {}

                for r in reports:
                    district = r.get("district", "Unknown")
                    priority = r.get("priority", "Low")

                    if district not in district_data:
                        district_data[district] = {
                            "High": 0,
                            "Medium": 0,
                            "Low": 0
                        }

                    district_data[district][priority] += 1

                for district, counts in district_data.items():
                    st.write(
                        f"**{district}** | "
                        f"🔴 High: {counts['High']} | "
                        f"🟠 Medium: {counts['Medium']} | "
                        f"🟢 Low: {counts['Low']}"
                    )

                st.subheader("📊 District-wise Reports Chart")

                chart_data = {
                    district: sum(counts.values())
                    for district, counts in district_data.items()
                }       

                st.bar_chart(
chart_data)

                high_count = sum(
                    1 for r in reports if r["priority"] == "High"
                )

                medium_count = sum(
                    1 for r in reports if r["priority"] == "Medium"
                )

                low_count = sum(
                    1 for r in reports if r["priority"] == "Low"
                )

                col1, col2, col3 = st.columns(3)

                col1.metric("🔴 High Priority", high_count)
                col2.metric("🟠 Medium Priority", medium_count)
                col3.metric("🟢 Low Priority", low_count)

                ticket_options = [
                    r["ticket_id"] for r in reports
                ]

                selected_ticket = st.selectbox(
                    "Select Ticket ID",
                    ticket_options
                )

                selected_report = next(
                    r for r in reports
                    if r["ticket_id"] == selected_ticket
                )

                st.subheader("Report Details")
                priority = selected_report["priority"]

                if priority == "High":
                    st.error("🔴 HIGH PRIORITY — Immediate Attention Suggested")

                elif priority == "Medium":
                    st.warning("🟠 MEDIUM PRIORITY — Review Required")

                else:
                    st.success("🟢 LOW PRIORITY — Normal Review")


                st.write("District:", selected_report["district"])
                st.write("Village:", selected_report["village"])
                st.write("Damage Type:", selected_report["damage_type"])
                st.write("Description:", selected_report["description"])
                st.write("Current Status:", selected_report["status"])

                st.divider()
                st.subheader("Update Report Status")

                new_status = st.selectbox(
                    "Choose New Status",
                    [
                        "Submitted",
                        "Under Review",
                        "Verified",
                        "Resolved"
                    ],
                    index=[
                        "Submitted",
                        "Under Review",
                        "Verified",
                        "Resolved"
                    ].index(selected_report["status"])
                )

        
                if st.button("Update Status"):
                    if new_status != selected_report["status"]:
                        from datetime import datetime, timezone

                        supabase.table("reports").update({
                            "status": new_status,
                            "updated_at": datetime.now(timezone.utc).isoformat()
                        }).eq(
                            "ticket_id", selected_ticket
                        ).execute()

                        st.success("Report status updated successfully!")
                        st.rerun()
                    else:
                        st.info("This report already has the selected status.")
       

        except Exception as e:
            st.error("Unable to load or update reports.")
            st.code(str(e))

st.divider()

st.caption(
    "JEEVANRAKSHA | all India | "
    "Demo Version | Not an official government service"
      )
  
