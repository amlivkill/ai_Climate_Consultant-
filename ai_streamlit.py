import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import requests

# Page Configuration with SEO
st.set_page_config(
    page_title="CHANGE Uttarakhand - Sustainable Agriculture & Environment",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Modern Design with Logo support
st.markdown("""
<style>
    /* Main Styles */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Header with Logo */
    .header-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 1rem 0;
        border-bottom: 3px solid #2E8B57;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }
    
    .logo-container {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .logo-img {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #2E8B57;
    }
    
    .logo-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #2E8B57, #3CB371);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        font-family: 'Arial Black', sans-serif;
    }
    
    .tagline {
        font-size: 1.2rem;
        color: #666;
        font-weight: 300;
        margin-top: 0.5rem;
        font-style: italic;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(46, 139, 87, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,0 L100,0 L100,100 Z" fill="rgba(255,255,255,0.1)"/></svg>');
        background-size: cover;
    }
    
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        position: relative;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        font-weight: 300;
        margin-bottom: 2rem;
        opacity: 0.9;
        position: relative;
    }
    
    /* Card Styles */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-top: 4px solid #2E8B57;
        transition: all 0.3s ease;
        height: 100%;
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #2E8B57, #3CB371);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(46, 139, 87, 0.3);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: scale(1.05);
    }
    
    /* Navigation */
    .nav-container {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(10px);
        padding: 1rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        position: sticky;
        top: 10px;
        z-index: 100;
    }
    
    .nav-btn {
        background: linear-gradient(45deg, #2E8B57, #3CB371);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        margin: 0.3rem;
        font-weight: 600;
        transition: all 0.3s ease;
        cursor: pointer;
        font-size: 0.9rem;
    }
    
    .nav-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(46, 139, 87, 0.4);
    }
    
    /* Section Headers */
    .section-header {
        text-align: center;
        margin: 3rem 0 2rem 0;
        padding: 2rem 0;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2E8B57;
        margin-bottom: 1rem;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 4px;
        background: linear-gradient(45deg, #2E8B57, #3CB371);
        border-radius: 2px;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: #666;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* AI Section */
    .ai-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    /* Climate Alert */
    .climate-alert {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #2c3e50, #34495e);
        color: white;
        padding: 3rem 0;
        margin-top: 4rem;
        border-radius: 20px 20px 0 0;
    }
    
    /* Progress Bar */
    .progress-container {
        background: #f0f0f0;
        border-radius: 10px;
        margin: 1rem 0;
        overflow: hidden;
    }
    
    .progress-bar {
        background: linear-gradient(45deg, #2E8B57, #3CB371);
        height: 20px;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    /* Logo in Nav */
    .nav-logo {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #2E8B57;
        margin-right: 10px;
    }
    
    /* Mobile Responsive */
    @media (max-width: 768px) {
        .logo-title { font-size: 2rem; }
        .hero-title { font-size: 2.2rem; }
        .section-title { font-size: 2rem; }
        .nav-btn { 
            width: 100%; 
            margin: 0.2rem 0;
            font-size: 0.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Function to create base64 encoded logo (placeholder)
def get_base64_logo():
    # Create a simple SVG logo as base64
    logo_svg = """
    <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="40" fill="#2E8B57" opacity="0.8"/>
        <path d="M30,40 L50,20 L70,40 L60,40 L60,70 L40,70 L40,40 Z" fill="white"/>
        <circle cx="50" cy="35" r="8" fill="#3CB371"/>
    </svg>
    """
    return base64.b64encode(logo_svg.encode()).decode()

# Header Section with Logo
logo_base64 = get_base64_logo()
st.markdown(f"""
<div class="header-container">
    <div class="logo-container">
        <img src="data:image/svg+xml;base64,{logo_base64}" class="logo-img" alt="CHANGE Logo">
        <div>
            <div class="logo-title">🌿 CHANGE</div>
            <div class="tagline">Centre for Himalaya Agriculture and Nature Group of Environment</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation with Smooth Scrolling
st.markdown("""
<div class="nav-container">
    <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 8px; align-items: center;">
        <img src="data:image/svg+xml;base64,{}" class="nav-logo" alt="Logo">
        <button class="nav-btn" onclick="scrollToSection('home')">🏠 Home</button>
        <button class="nav-btn" onclick="scrollToSection('about')">👥 About</button>
        <button class="nav-btn" onclick="scrollToSection('programs')">🚀 Programs</button>
        <button class="nav-btn" onclick="scrollToSection('ai-consultant')">🤖 AI Consultant</button>
        <button class="nav-btn" onclick="scrollToSection('climate')">🌧️ Climate</button>
        <button class="nav-btn" onclick="scrollToSection('products')">🛍️ Products</button>
        <button class="nav-btn" onclick="scrollToSection('contact')">📞 Contact</button>
    </div>
</div>

<script>
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({behavior: "smooth", block: "start"});
    }
}
</script>
""".format(logo_base64), unsafe_allow_html=True)

# Home Section
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Transforming Rural Uttarakhand</h1>
    <p class="hero-subtitle">Sustainable Agriculture • Environmental Stewardship • Community Empowerment</p>
    <div style="margin-top: 3rem; position: relative;">
        <button class="nav-btn" style="font-size: 1.2rem; padding: 1rem 2rem; margin: 0.5rem;" onclick="scrollToSection('about')">Explore Our Mission</button>
        <button class="nav-btn" style="font-size: 1.2rem; padding: 1rem 2rem; margin: 0.5rem; background: rgba(255,255,255,0.2); border: 2px solid white;" onclick="scrollToSection('contact')">Join Our Movement</button>
    </div>
</div>
""", unsafe_allow_html=True)

# Impact Statistics
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Our Impact in Numbers</h2>
    <p class="section-subtitle">Creating sustainable change across Uttarakhand through community-driven initiatives</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <h3 style="font-size: 2.5rem; margin: 0;">5,000+</h3>
        <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0;">Farmers Empowered</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <h3 style="font-size: 2.5rem; margin: 0;">120+</h3>
        <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0;">Organic Villages</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <h3 style="font-size: 2.5rem; margin: 0;">15</h3>
        <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0;">Cottage Industries</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <h3 style="font-size: 2.5rem; margin: 0;">8 MW</h3>
        <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0;">Solar Capacity Planned</p>
    </div>
    """, unsafe_allow_html=True)

# About Section
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2 class="section-title">About CHANGE</h2>
    <p class="section-subtitle">Empowering communities through sustainable development in the Himalayan region</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🌿</div>
        <h3>Our Mission</h3>
        <p>CHANGE is an autonomous multi-purpose cooperative dedicated to holistic development of Uttarakhand. We work at the intersection of agriculture, environment, enterprise, and equity to transform rural livelihoods.</p>
        <div style="text-align: left; margin-top: 1.5rem;">
            <p>✅ Sustainable Agriculture Practices</p>
            <p>✅ Environmental Conservation</p>
            <p>✅ Community Empowerment</p>
            <p>✅ Youth Engagement</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
        <h3>Our Vision</h3>
        <p>To create self-reliant, sustainable rural communities where agriculture is profitable, environment is protected, and youth are empowered to build their futures in their homeland.</p>
        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
            <h4>Core Focus Areas:</h4>
            <p>🌱 Organic & Natural Farming</p>
            <p>🏭 Cottage Industries</p>
            <p>⚡ Renewable Energy</p>
            <p>🌍 Climate Resilience</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Programs Section
st.markdown('<div id="programs"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Our Programs & Services</h2>
    <p class="section-subtitle">Comprehensive solutions for sustainable rural development</p>
</div>
""", unsafe_allow_html=True)

programs = [
    {"icon": "🤝", "title": "Contract Farming", "desc": "Guaranteed buy-back at fair prices with technical support and market linkage"},
    {"icon": "📜", "title": "Organic Certification", "desc": "PGS and Organic India certification support for premium market access"},
    {"icon": "💰", "title": "Microfinance", "desc": "Financial services for women SHGs and farmers with low interest rates"},
    {"icon": "👨‍🌾", "title": "Personal Family Farmer", "desc": "Individualized farming enterprise support and mentorship"},
    {"icon": "🎓", "title": "Skill Development", "desc": "Training in modern agricultural techniques and entrepreneurship"},
    {"icon": "⚡", "title": "Disaster Preparedness", "desc": "Climate resilience training and risk management solutions"}
]

cols = st.columns(3)
for idx, program in enumerate(programs):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{program['icon']}</div>
            <h4>{program['title']}</h4>
            <p>{program['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# AI Consultant Section
st.markdown('<div id="ai-consultant"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="ai-section">
    <div class="section-header" style="color: white;">
        <h2 class="section-title" style="color: white;">🤖 AI Climate Consultant</h2>
        <p class="section-subtitle" style="color: rgba(255,255,255,0.9);">Advanced AI solutions for climate resilience and sustainable agriculture</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">
        <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <h4>🌦️ Climate Risk Forecasting</h4>
            <p>Real-time weather predictions and early warning systems for floods, landslides, and extreme weather events using AI algorithms.</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <h4>🌱 Smart Farming Solutions</h4>
            <p>AI-powered crop recommendations, soil health analysis, and precision agriculture techniques for optimal yield.</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <h4>💰 Carbon Credit Management</h4>
            <p>Automated MRV systems for carbon credit generation and international market access with blockchain technology.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Interactive AI Tools
st.markdown("""
<div class="section-header">
    <h2 class="section-title">AI Tools & Calculators</h2>
    <p class="section-subtitle">Practical AI-powered solutions for farmers and communities</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🌾 Crop Advisor", "💧 Water Calculator", "💰 Carbon Credits"])

with tab1:
    st.subheader("AI Crop Recommendation System")
    col1, col2 = st.columns(2)
    with col1:
        soil_type = st.selectbox("Soil Type", ["Loamy Soil", "Clay Soil", "Sandy Soil", "Mountain Soil", "Alluvial Soil"])
        rainfall = st.selectbox("Annual Rainfall", ["Low (<500mm)", "Medium (500-1000mm)", "High (>1000mm)"])
    with col2:
        altitude = st.selectbox("Altitude Zone", ["Lowland (<1000m)", "Mid-altitude (1000-2000m)", "Highland (>2000m)"])
        season = st.selectbox("Growing Season", ["Kharif (Monsoon)", "Rabi (Winter)", "Zaid (Summer)", "Annual"])
    
    if st.button("Get AI Crop Recommendations", use_container_width=True):
        st.success("""
        **🤖 AI Recommended Crops:**
        
        **Primary Crops:**
        • Manduwa (Finger Millet) - High nutrition value
        • Jhangora (Barnyard Millet) - Drought resistant
        • Rajma (Kidney Beans) - Good market demand
        
        **Secondary Crops:**
        • Organic Vegetables - For local markets
        • Medicinal Herbs - High value addition
        
        **💡 AI Advisory:**
        - Use organic manure and practice crop rotation
        - Implement drip irrigation for water efficiency
        - Consider intercropping with legumes
        """)

with tab2:
    st.subheader("Smart Water Management Calculator")
    col1, col2 = st.columns(2)
    with col1:
        crop_area = st.number_input("Crop Area (hectares)", min_value=0.1, value=2.0, step=0.1)
        crop_type = st.selectbox("Crop Type", ["Cereals (Rice/Wheat)", "Millets", "Pulses", "Vegetables", "Fruits", "Spices"])
    with col2:
        irrigation_type = st.selectbox("Irrigation System", ["Flood Irrigation", "Drip Irrigation", "Sprinkler System", "Traditional Methods"])
        soil_moisture = st.slider("Current Soil Moisture Level (%)", 0, 100, 50)
    
    if st.button("Calculate Water Optimization", use_container_width=True):
        base_water = crop_area * 1500
        if irrigation_type == "Drip Irrigation":
            water_saved = base_water * 0.4
            efficiency = "High (40% savings)"
        elif irrigation_type == "Sprinkler System":
            water_saved = base_water * 0.25
            efficiency = "Medium (25% savings)"
        else:
            water_saved = base_water * 0.1
            efficiency = "Low (10% savings)"
        
        st.success(f"💧 **Water Optimization Results:**")
        st.metric("Current Water Usage", f"{base_water:,.0f} liters/day")
        st.metric("Potential Savings", f"{water_saved:,.0f} liters/day")
        st.metric("System Efficiency", efficiency)
        
        st.info("""
        **💡 AI Recommendations:**
        - Switch to drip irrigation for maximum efficiency
        - Install soil moisture sensors
        - Implement rainwater harvesting
        - Use mulching to reduce evaporation
        """)

with tab3:
    st.subheader("Carbon Credit Income Calculator")
    st.info("Calculate your potential earnings from carbon farming")
    
    col1, col2 = st.columns(2)
    with col1:
        land_area = st.number_input("Land Area (hectares)", min_value=0.1, value=5.0, step=0.5)
        farming_practice = st.selectbox("Current Farming Practice", 
                                      ["Conventional Farming", "Organic Farming", "Conservation Agriculture", "Agroforestry", "Natural Farming"])
    with col2:
        trees_planted = st.number_input("Number of Trees Planted", min_value=0, value=100)
        practice_years = st.number_input("Years of Sustainable Practice", min_value=1, value=3)
    
    if st.button("Estimate Carbon Credit Income", use_container_width=True):
        base_credits = land_area * 2
        tree_credits = trees_planted * 0.1
        practice_bonus = practice_years * 0.5
        
        total_credits = base_credits + tree_credits + practice_bonus
        income = total_credits * 15
        
        st.success(f"💰 **Carbon Credit Analysis:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Carbon Credits", f"{total_credits:.1f} tCO2e")
        with col2:
            st.metric("Annual Income", f"${income:,.0f}")
        with col3:
            st.metric("Credit Value", "$15/credit")
        
        st.info("""
        **🌿 How to Increase Carbon Credits:**
        - Plant more native trees
        - Practice no-till farming
        - Use organic manure
        - Implement crop rotation
        - Maintain soil cover
        """)

# Climate Section
st.markdown('<div id="climate"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="climate-alert">
    <h3 style="font-size: 2rem; margin-bottom: 1rem;">🚨 Uttarakhand Climate Emergency</h3>
    <p style="font-size: 1.2rem; margin-bottom: 0.5rem;"><strong>2025 Data:</strong> 2,199+ disaster events | 260+ fatalities | 65% extreme weather days</p>
    <p style="font-size: 1.1rem; margin: 0;">Immediate AI-powered solutions needed for climate resilience in Himalayan region</p>
</div>
""", unsafe_allow_html=True)

# Climate Statistics
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Climate Impact Analysis</h2>
    <p class="section-subtitle">Understanding Uttarakhand's environmental challenges through data</p>
</div>
""", unsafe_allow_html=True)

# Create sample climate data
climate_data = {
    'Disaster Type': ['Cloudburst', 'Landslide', 'Floods', 'Drought', 'Others'],
    'Events': [700, 1034, 300, 100, 65],
    'Impact Score': [85, 90, 75, 60, 40]
}

df_climate = pd.DataFrame(climate_data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Disaster Distribution 2025")
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ['#ff6b6b', '#ffa726', '#42a5f5', '#66bb6a', '#ba68c8']
    wedges, texts, autotexts = ax.pie(df_climate['Events'], labels=df_climate['Disaster Type'], 
                                     autopct='%1.1f%%', colors=colors, startangle=90)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('Disaster Events Distribution', fontsize=14, fontweight='bold', pad=20)
    st.pyplot(fig)

with col2:
    st.subheader("Impact Severity Analysis")
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(df_climate['Disaster Type'], df_climate['Impact Score'], 
                   color=colors, alpha=0.8)
    
    for bar, value in zip(bars, df_climate['Impact Score']):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
                f'{value}%', va='center', fontweight='bold')
    
    ax.set_xlabel('Impact Score (%)', fontweight='bold')
    ax.set_title('Disaster Impact Severity', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3)
    st.pyplot(fig)

# Products Section
st.markdown('<div id="products"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Our Organic Products</h2>
    <p class="section-subtitle">Pure Himalayan goodness from our farms to your home</p>
</div>
""", unsafe_allow_html=True)

products = [
    {"name": "Organic Millets", "category": "Shri Anna", "features": ["GI Certified", "Rich in Nutrients", "Traditional Varieties"], "icon": "🌾"},
    {"name": "Himalayan Herbs", "category": "Medicinal Plants", "features": ["Ayurvedic", "Wild Harvested", "Therapeutic"], "icon": "🌿"},
    {"name": "Aroma Oils", "category": "Essential Oils", "features": ["Pure Extract", "Therapeutic", "Natural"], "icon": "💧"},
    {"name": "Vegan Products", "category": "Plant-based", "features": ["Cruelty-free", "Sustainable", "Healthy"], "icon": "🌱"},
    {"name": "Natural Preserves", "category": "Jams & Pickles", "features": ["No Preservatives", "Traditional Recipes", "Homemade"], "icon": "🍯"},
    {"name": "Puja Materials", "category": "Religious", "features": ["Natural", "Eco-friendly", "Traditional"], "icon": "🪔"}
]

cols = st.columns(3)
for idx, product in enumerate(products):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{product['icon']}</div>
            <h4>{product['name']}</h4>
            <p><strong>Category:</strong> {product['category']}</p>
            <div style="margin-top: 1rem; text-align: left;">
                {' '.join([f'<span style="background: #2E8B57; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin: 0.2rem; display: inline-block;">{feature}</span>' for feature in product['features']])}
            </div>
            <button class="nav-btn" style="margin-top: 1.5rem; width: 100%;" onclick="alert('{product['name']} details coming soon!')">View Details</button>
        </div>
        """, unsafe_allow_html=True)

# Contact Section
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Get Involved</h2>
    <p class="section-subtitle">Join our movement for sustainable development in Uttarakhand</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📞 Contact Information</h3>
        <div style="text-align: left; margin-top: 1.5rem;">
            <p><strong>📧 Email:</strong> thechangeuttarakhand@gmail.com</p>
            <p><strong>📱 Phone:</strong> +91-7668512325</p>
            <p><strong>🏠 Address:</strong> Village Badshahi Thaul, Tehri Garhwal, Uttarakhand - 249199</p>
            
            <div style="margin-top: 2rem;">
                <h4>🌐 Follow Us</h4>
                <p>📘 Facebook: @changeuttarakhand</p>
                <p>📷 Instagram: @changeuttarakhand</p>
                <p>🎬 YouTube: CHANGE Uttarakhand</p>
            </div>
            
            <div style="margin-top: 2rem; background: #f8f9fa; padding: 1.5rem; border-radius: 10px;">
                <h4>🏛️ Registered Under</h4>
                <p>Uttarakhand Autonomous Cooperative Act, 2003</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    with st.form("contact_form"):
        st.subheader("Send us a Message")
        
        name = st.text_input("Full Name *", placeholder="Enter your full name")
        email = st.text_input("Email Address *", placeholder="Enter your email")
        phone = st.text_input("Phone Number", placeholder="Enter your phone number")
        
        interest = st.selectbox("Area of Interest *", [
            "Select your interest", "Membership", "Volunteering", "Partnership", 
            "Product Information", "AI Consultation", "Training Programs", "Other"
        ])
        
        message = st.text_area("Your Message *", 
                             placeholder="Tell us how you'd like to get involved...",
                             height=120)
        
        submitted = st.form_submit_button("Send Message 📨", use_container_width=True)
        if submitted:
            if name and email and interest != "Select your interest" and message:
                st.success("""
                ✅ **Thank you for your message!** 
                
                We have received your inquiry and our team will get back to you within 24 hours. 
                Together, we can create sustainable change in Uttarakhand!
                """)
                
                # Show confirmation details
                st.info(f"""
                **Submission Details:**
                - Name: {name}
                - Email: {email}
                - Interest: {interest}
                - Status: ✅ Received
                - Response Time: 24 hours
                """)
            else:
                st.error("Please fill in all required fields (*)")

# Footer
st.markdown("""
<div class="footer">
    <div style="text-align: center;">
        <div class="logo-container" style="justify-content: center; margin-bottom: 1rem;">
            <img src="data:image/svg+xml;base64,{}" class="logo-img" alt="CHANGE Logo">
            <h3 style="color: white; margin: 0; font-size: 2rem;">🌿 CHANGE Cooperative</h3>
        </div>
        <p style="font-size: 1.2rem; opacity: 0.9; margin-bottom: 2rem;">Empowering Rural Uttarakhand through Sustainable Development</p>
        
        <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; flex-wrap: wrap;">
            <button class="nav-btn" onclick="scrollToSection('home')">Home</button>
            <button class="nav-btn" onclick="scrollToSection('about')">About</button>
            <button class="nav-btn" onclick="scrollToSection('programs')">Programs</button>
            <button class="nav-btn" onclick="scrollToSection('contact')">Contact</button>
        </div>
        
        <div style="margin-top: 2rem; opacity: 0.7; border-top: 1px solid rgba(255,255,255,0.3); padding-top: 2rem;">
            <p>© 2024 CHANGE - Centre for Himalaya Agriculture and Nature Group of Environment. All rights reserved.</p>
            <p style="font-size: 0.9rem; margin-top: 0.5rem;">Building a sustainable future for Uttarakhand, one community at a time.</p>
        </div>
    </div>
</div>
""".format(logo_base64), unsafe_allow_html=True)

# SEO Meta Tags
st.markdown("""
<!-- SEO Meta Tags -->
<meta name="description" content="CHANGE Uttarakhand - Sustainable agriculture, environmental conservation, and community empowerment in the Himalayas. Organic farming, AI climate solutions, rural development.">
<meta name="keywords" content="Uttarakhand agriculture, sustainable farming, climate change, AI consultant, organic products, rural development, Himalayas, CHANGE cooperative">
<meta name="author" content="CHANGE Cooperative">
<meta property="og:title" content="CHANGE Uttarakhand - Sustainable Agriculture & Environment">
<meta property="og:description" content="Empowering rural communities through sustainable agriculture and environmental conservation in Uttarakhand">
<meta property="og:type" content="website">
<!-- Structured Data for SEO -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "CHANGE Uttarakhand",
  "description": "Centre for Himalaya Agriculture and Nature Group of Environment",
  "url": "https://change-uttarakhand.streamlit.app",
  "logo": "data:image/svg+xml;base64,{}",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Tehri Garhwal",
    "addressRegion": "Uttarakhand",
    "postalCode": "249199",
    "addressCountry": "IN"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+91-7668512325",
    "contactType": "Customer service",
    "email": "thechangeuttarakhand@gmail.com"
  }
}
</script>
""".format(logo_base64), unsafe_allow_html=True)
