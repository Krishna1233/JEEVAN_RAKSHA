
import streamlit as st
import requests
import urllib.parse
from supabase import create_client

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

st.set_page_config(
    page_title="JEEVANRAKSHA",
    page_icon="🛡️",
    layout="wide"
)

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

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Report",
        "Track Report",
        "Help & Benefits",
        "Emergency Help Center",
        "Dashboard",
        "Admin Panel"
    ]
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
    "Ladakh", "Lakshadweep", "Puducherry"
]

    state = st.selectbox("Select Your State / UT", states)

    districts = {
    "Gujarat": [
        "Ahmedabad", "Surat", "Vadodara",
        "Rajkot", "Anand"
    ],

    "Bihar": [
        "Patna", "Gaya", "Muzaffarpur",
        "Bhagalpur", "Darbhanga"
    ],

    "Uttar Pradesh": [
        "Prayagraj", "Lucknow", "Varanasi",
        "Kanpur", "Gorakhpur"
    ],

    "Maharashtra": [
        "Mumbai", "Pune", "Nagpur",
        "Nashik", "Thane"
    ],

    "Rajasthan": [
        "Jaipur", "Jodhpur", "Udaipur",
        "Kota", "Ajmer"
    ]
    }
    
    online_data =     get_india_districts()
    st.write("Online District Data:", online_data)
    if online_data:
        districts = {
            item["name"]: [
                district["name"]
                for district in    item["districts"]
            ]
            for item in online_data
        }
    district_list =       districts.get(state, [])

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

    search_text = f"{need} {selected_district} {state} site:gov.in"
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
        "🏛️ National Government Portal",
        "https://www.india.gov.in/"
    )

    st.info("Check the official government website "
        "for eligibility, documents and application details."
    )

     
elif page == "Emergency Help Center":
    st.title("🚨 Emergency Help Center")
    st.subheader("State & District Wise Emergency Contacts")

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

    selected_district = st.selectbox(
        "Select Your District",
         district_list if district_list else ["District list coming soon"]
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

elif page == "Dashboard":
    st.title("📊 Smart Relief Dashboard")
    st.write("Live overview of flood damage reports.")

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

            if reports:
                st.write("Total Reports:", len(reports))

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
  
