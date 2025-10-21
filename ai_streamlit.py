import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64

# Page Configuration
st.set_page_config(
    page_title="CHANGE Uttarakhand - Sustainable Agriculture & Environment",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Logo Function
def get_base64_logo():
    logo_svg = """
    <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="40" fill="#2E8B57" opacity="0.8"/>
        <path d="M30,40 L50,20 L70,40 L60,40 L60,70 L40,70 L40,40 Z" fill="white"/>
        <circle cx="50" cy="35" r="8" fill="#3CB371"/>
    </svg>
    """
    return base64.b64encode(logo_svg.encode()).decode()

logo_base64 = get_base64_logo()

# Custom CSS
st.markdown(f"""
<style>
    .main {{ background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }}
    .header-container {{ 
        background: rgba(255, 255, 255, 0.95);
        padding: 1rem 0;
        border-bottom: 3px solid #2E8B57;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        text-align: center;
    }}
    .logo-title {{
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #2E8B57, #3CB371);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }}
    .tagline {{ font-size: 1.2rem; color: #666; margin-top: 0.5rem; }}
    .hero-section {{
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 20px;
        margin: 2rem 0;
    }}
    .hero-title {{ font-size: 3rem; font-weight: 800; margin-bottom: 1rem; }}
    .feature-card {{
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-top: 4px solid #2E8B57;
        height: 100%;
        text-align: center;
    }}
    .stat-card {{
        background: linear-gradient(135deg, #2E8B57, #3CB371);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
    }}
    .nav-container {{
        background: rgba(255, 255, 255, 0.98);
        padding: 1rem;
        border-radius: 15px;
        margin: 1rem 0;
        text-align: center;
    }}
    .nav-btn {{
        background: linear-gradient(45deg, #2E8B57, #3CB371);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        margin: 0.3rem;
        font-weight: 600;
        cursor: pointer;
    }}
    .section-header {{ text-align: center; margin: 3rem 0 2rem 0; padding: 2rem 0; }}
    .section-title {{ font-size: 2.5rem; font-weight: 700; color: #2E8B57; margin-bottom: 1rem; }}
    .ai-section {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
    }}
    .climate-alert {{
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
    }}
    .footer {{
        background: linear-gradient(135deg, #2c3e50, #34495e);
        color: white;
        padding: 3rem 0;
        margin-top: 4rem;
        border-radius: 20px 20px 0 0;
        text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
<div class="header-container">
    <div class="logo-title">🌿 CHANGE</div>
    <div class="tagline">Centre for Himalaya Agriculture and Nature Group of Environment</div>
</div>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="nav-container">
    <button class="nav-btn" onclick="scrollToSection('home')">🏠 Home</button>
    <button class="nav-btn" onclick="scrollToSection('about')">👥 About</button>
    <button class="nav-btn" onclick="scrollToSection('programs')">🚀 Programs</button>
    <button class="nav-btn" onclick="scrollToSection('ai-consultant')">🤖 AI Consultant</button>
    <button class="nav-btn" onclick="scrollToSection('contact')">📞 Contact</button>
</div>

<script>
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) element.scrollIntoView({behavior: "smooth"});
}
</script>
""", unsafe_allow_html=True)

# Home Section
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Transforming Rural Uttarakhand</h1>
    <p style="font-size: 1.4rem; margin-bottom: 2rem;">Sustainable Agriculture • Environmental Stewardship • Community Empowerment</p>
</div>
""", unsafe_allow_html=True)

# Impact Stats
col1, col2, col3, col4 = st.columns(4)
with col1: st.markdown("""<div class="stat-card"><h3>5,000+</h3><p>Farmers Empowered</p></div>""", unsafe_allow_html=True)
with col2: st.markdown("""<div class="stat-card"><h3>120+</h3><p>Organic Villages</p></div>""", unsafe_allow_html=True)
with col3: st.markdown("""<div class="stat-card"><h3>15</h3><p>Cottage Industries</p></div>""", unsafe_allow_html=True)
with col4: st.markdown("""<div class="stat-card"><h3>8 MW</h3><p>Solar Capacity</p></div>""", unsafe_allow_html=True)

# About Section
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("""<div class="section-header"><h2 class="section-title">About CHANGE</h2></div>""", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1: st.markdown("""<div class="feature-card"><h3>🌿 Our Mission</h3><p>Holistic development of Uttarakhand through sustainable agriculture and environmental conservation.</p></div>""", unsafe_allow_html=True)
with col2: st.markdown("""<div class="feature-card"><h3>🎯 Our Vision</h3><p>Self-reliant, sustainable rural communities where agriculture is profitable and environment is protected.</p></div>""", unsafe_allow_html=True)

# Programs Section
st.markdown('<div id="programs"></div>', unsafe_allow_html=True)
st.markdown("""<div class="section-header"><h2 class="section-title">Our Programs</h2></div>""", unsafe_allow_html=True)
cols = st.columns(3)
programs = [
    {"icon": "🤝", "title": "Contract Farming", "desc": "Guaranteed buy-back at fair prices"},
    {"icon": "📜", "title": "Organic Certification", "desc": "PGS and Organic India certification support"},
    {"icon": "💰", "title": "Microfinance", "desc": "Financial services for women SHGs and farmers"},
    {"icon": "👨‍🌾", "title": "Personal Family Farmer", "desc": "Individualized farming enterprise support"},
    {"icon": "🎓", "title": "Skill Development", "desc": "Training in modern agricultural techniques"},
    {"icon": "⚡", "title": "Disaster Preparedness", "desc": "Climate resilience training"}
]
for idx, program in enumerate(programs):
    with cols[idx % 3]:
        st.markdown(f"""<div class="feature-card"><div style="font-size: 3rem;">{program['icon']}</div><h4>{program['title']}</h4><p>{program['desc']}</p></div>""", unsafe_allow_html=True)

# AI Consultant Section
st.markdown('<div id="ai-consultant"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="ai-section">
    <h2 style="text-align: center; color: white; font-size: 2.5rem;">🤖 AI Climate Consultant</h2>
    <p style="text-align: center; color: white; font-size: 1.2rem;">Advanced AI solutions for climate resilience</p>
</div>
""", unsafe_allow_html=True)

# AI Tools
tab1, tab2, tab3 = st.tabs(["🌾 Crop Advisor", "💧 Water Calculator", "💰 Carbon Credits"])
with tab1:
    st.subheader("AI Crop Recommendation")
    col1, col2 = st.columns(2)
    with col1:
        soil_type = st.selectbox("Soil Type", ["Loamy Soil", "Clay Soil", "Sandy Soil", "Mountain Soil"])
        rainfall = st.selectbox("Rainfall", ["Low", "Medium", "High"])
    with col2:
        altitude = st.selectbox("Altitude", ["Lowland", "Mid-altitude", "Highland"])
        season = st.selectbox("Season", ["Kharif", "Rabi", "Zaid"])
    if st.button("Get Recommendations"):
        st.success("Recommended: Manduwa, Jhangora, Rajma - Use organic manure and drip irrigation")

with tab2:
    st.subheader("Water Management")
    crop_area = st.number_input("Crop Area (hectares)", 1.0, 10.0, 2.0)
    irrigation = st.selectbox("Irrigation", ["Flood", "Drip", "Sprinkler"])
    if st.button("Calculate"):
        base_water = crop_area * 1500
        st.metric("Water Usage", f"{base_water:,.0f} liters/day")
        st.info("Switch to drip irrigation for 40% savings")

with tab3:
    st.subheader("Carbon Credits")
    land_area = st.number_input("Land Area (hectares)", 1.0, 20.0, 5.0)
    trees = st.number_input("Trees Planted", 0, 500, 100)
    if st.button("Calculate Income"):
        credits = land_area * 2 + trees * 0.1
        income = credits * 15
        st.metric("Annual Income", f"${income:,.0f}")

# Climate Alert
st.markdown("""
<div class="climate-alert">
    <h3>🚨 Uttarakhand Climate Emergency</h3>
    <p><strong>2025 Data:</strong> 2,199+ disaster events | 260+ fatalities</p>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""<div class="section-header"><h2 class="section-title">Contact Us</h2></div>""", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📞 Contact Information</h3>
        <p><strong>Email:</strong> thechangeuttarakhand@gmail.com</p>
        <p><strong>Phone:</strong> +91-7668512325</p>
        <p><strong>Address:</strong> Village Badshahi Thaul, Tehri Garhwal</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Send Message"):
            st.success("Thank you for your message!")

# Footer
st.markdown("""
<div class="footer">
    <h3 style="color: white;">🌿 CHANGE Cooperative</h3>
    <p>Empowering Rural Uttarakhand through Sustainable Development</p>
    <p>© 2024 CHANGE - All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
