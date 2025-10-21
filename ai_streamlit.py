import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import requests
from PIL import Image
import io

# Page Configuration
st.set_page_config(
    page_title="CHANGE Uttarakhand - Sustainable Agriculture & Environment",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Modern Design
st.markdown("""
<style>
    /* Main Styles */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header Styles */
    .header-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 1rem 0;
        border-bottom: 3px solid #2E8B57;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    .logo-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #2E8B57, #3CB371);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 0;
    }
    
    .tagline {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        font-weight: 300;
        margin-top: 0.5rem;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url('https://images.unsplash.com/photo-1545208967-50e8c50d7deb');
        background-size: cover;
        background-position: center;
        color: white;
        padding: 6rem 2rem;
        text-align: center;
        border-radius: 0 0 30px 30px;
        margin-bottom: 3rem;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    /* Card Styles */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 5px solid #2E8B57;
        transition: transform 0.3s ease;
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #2E8B57, #3CB371);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(46, 139, 87, 0.3);
    }
    
    /* Navigation */
    .nav-container {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(10px);
        padding: 1rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
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
    }
    
    .nav-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(46, 139, 87, 0.4);
    }
    
    /* Section Headers */
    .section-header {
        text-align: center;
        margin: 4rem 0 2rem 0;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2E8B57;
        margin-bottom: 1rem;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: #666;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* AI Section */
    .ai-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
    }
    
    /* Climate Alert */
    .climate-alert {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
    }
    
    /* Footer */
    .footer {
        background: #2c3e50;
        color: white;
        padding: 3rem 0;
        margin-top: 4rem;
        border-radius: 30px 30px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header-container">
    <div class="logo-title">🌿 CHANGE</div>
    <div class="tagline">Centre for Himalaya Agriculture and Nature Group of Environment</div>
</div>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="nav-container">
    <div style="display: flex; justify-content: center; flex-wrap: wrap;">
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
        element.scrollIntoView({behavior: "smooth"});
    }
}
</script>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section" id="home">
    <h1 class="hero-title">Transforming Rural Uttarakhand</h1>
    <p class="hero-subtitle">Sustainable Agriculture • Environmental Stewardship • Community Empowerment</p>
    <div style="margin-top: 2rem;">
        <button class="nav-btn" style="font-size: 1.2rem; padding: 1rem 2rem;" onclick="scrollToSection('about')">Explore Our Mission</button>
        <button class="nav-btn" style="font-size: 1.2rem; padding: 1rem 2rem; background: rgba(255,255,255,0.2); border: 2px solid white;" onclick="scrollToSection('contact')">Join Our Movement</button>
    </div>
</div>
""", unsafe_allow_html=True)

# Impact Statistics
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Our Impact in Numbers</h2>
    <p class="section-subtitle">Creating sustainable change across Uttarakhand</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <h3>5,000+</h3>
        <p>Farmers Empowered</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <h3>120+</h3>
        <p>Organic Villages</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <h3>15</h3>
        <p>Cottage Industries</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <h3>8 MW</h3>
        <p>Solar Capacity Planned</p>
    </div>
    """, unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="section-header" id="about">
    <h2 class="section-title">About CHANGE</h2>
    <p class="section-subtitle">Empowering communities through sustainable development</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🌿 Our Mission</h3>
        <p>CHANGE is an autonomous multi-purpose cooperative dedicated to holistic development of Uttarakhand. We work at the intersection of agriculture, environment, enterprise, and equity to transform rural livelihoods.</p>
        <ul>
            <li>Sustainable Agriculture Practices</li>
            <li>Environmental Conservation</li>
            <li>Community Empowerment</li>
            <li>Youth Engagement</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Our Vision</h3>
        <p>To create self-reliant, sustainable rural communities where agriculture is profitable, environment is protected, and youth are empowered to build their futures in their homeland.</p>
        <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin-top: 1rem;">
            <h4>Core Focus Areas:</h4>
            <p>• Organic & Natural Farming<br>• Cottage Industries<br>• Renewable Energy<br>• Climate Resilience</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Programs Section
st.markdown("""
<div class="section-header" id="programs">
    <h2 class="section-title">Our Programs & Services</h2>
    <p class="section-subtitle">Comprehensive solutions for rural development</p>
</div>
""", unsafe_allow_html=True)

programs = [
    {"icon": "🤝", "title": "Contract Farming", "desc": "Guaranteed buy-back at fair prices with technical support"},
    {"icon": "📜", "title": "Organic Certification", "desc": "PGS and Organic India certification support"},
    {"icon": "💰", "title": "Microfinance", "desc": "Financial services for women SHGs and farmers"},
    {"icon": "👨‍🌾", "title": "Personal Family Farmer", "desc": "Individualized farming enterprise support"},
    {"icon": "🎓", "title": "Skill Development", "desc": "Training in modern agricultural techniques"},
    {"icon": "⚡", "title": "Disaster Preparedness", "desc": "Climate resilience and risk management"}
]

cols = st.columns(3)
for idx, program in enumerate(programs):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">{program['icon']}</div>
            <h4>{program['title']}</h4>
            <p>{program['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# AI Consultant Section
st.markdown("""
<div class="ai-section" id="ai-consultant">
    <div class="section-header">
        <h2 class="section-title" style="color: white;">🤖 AI Climate Consultant</h2>
        <p class="section-subtitle" style="color: rgba(255,255,255,0.9);">Advanced AI solutions for climate resilience</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">
        <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 15px; backdrop-filter: blur(10px);">
            <h4>🌦️ Climate Risk Forecasting</h4>
            <p>Real-time weather predictions and early warning systems for floods, landslides, and extreme weather events.</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 15px; backdrop-filter: blur(10px);">
            <h4>🌱 Smart Farming Solutions</h4>
            <p>AI-powered crop recommendations, soil health analysis, and precision agriculture techniques.</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 15px; backdrop-filter: blur(10px);">
            <h4>💰 Carbon Credit Management</h4>
            <p>Automated MRV systems for carbon credit generation and international market access.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Interactive AI Tools
st.markdown("""
<div class="section-header">
    <h2 class="section-title">AI Tools & Calculators</h2>
    <p class="section-subtitle">Practical solutions for farmers and communities</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🌾 Crop Advisor", "💧 Water Calculator", "💰 Carbon Credits"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        soil_type = st.selectbox("Soil Type", ["Loamy", "Clay", "Sandy", "Mountain Soil"])
        rainfall = st.selectbox("Annual Rainfall", ["Low (<500mm)", "Medium (500-1000mm)", "High (>1000mm)"])
    with col2:
        altitude = st.selectbox("Altitude", ["Lowland (<1000m)", "Mid-altitude (1000-2000m)", "Highland (>2000m)"])
        season = st.selectbox("Season", ["Kharif", "Rabi", "Zaid"])
    
    if st.button("Get Crop Recommendations", use_container_width=True):
        st.success("""
        **Recommended Crops:**
        - Manduwa (Finger Millet)
        - Jhangora (Barnyard Millet)
        - Rajma (Kidney Beans)
        - Organic Vegetables
        
        **Advisory:** Use organic manure and practice crop rotation
        """)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        crop_area = st.number_input("Crop Area (hectares)", min_value=0.1, value=2.0)
        crop_type = st.selectbox("Crop Type", ["Cereals", "Pulses", "Vegetables", "Fruits"])
    with col2:
        irrigation_type = st.selectbox("Irrigation Type", ["Flood", "Drip", "Sprinkler", "Traditional"])
        soil_moisture = st.slider("Soil Moisture Level", 0, 100, 50)
    
    if st.button("Calculate Water Savings", use_container_width=True):
        water_saved = crop_area * 1500
        st.success(f"💧 Potential water savings: {water_saved:,.0f} liters per day")
        st.info("Switch to drip irrigation for maximum efficiency")

with tab3:
    st.info("Calculate your potential carbon credit earnings")
    col1, col2 = st.columns(2)
    with col1:
        land_area = st.number_input("Land Area (hectares)", min_value=0.1, value=5.0)
        farming_practice = st.selectbox("Farming Practice", ["Organic", "Traditional", "Agroforestry", "Conservation Agriculture"])
    with col2:
        trees_planted = st.number_input("Trees Planted", min_value=0, value=100)
        practice_years = st.number_input("Years of Sustainable Practice", min_value=1, value=3)
    
    if st.button("Estimate Carbon Credits", use_container_width=True):
        credits = land_area * 2 + trees_planted * 0.1
        income = credits * 15  # $15 per credit
        st.success(f"💰 Estimated annual carbon credit income: ${income:,.0f}")
        st.metric("Carbon Credits Generated", f"{credits:.1f} tCO2e")

# Climate Section
st.markdown("""
<div class="climate-alert" id="climate">
    <h3>🚨 Uttarakhand Climate Emergency</h3>
    <p><strong>2025 Data:</strong> 2,199+ disaster events | 260+ fatalities | 65% extreme weather days</p>
    <p>Immediate AI-powered solutions needed for climate resilience</p>
</div>
""", unsafe_allow_html=True)

# Climate Statistics
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Climate Impact Analysis</h2>
    <p class="section-subtitle">Understanding Uttarakhand's environmental challenges</p>
</div>
""", unsafe_allow_html=True)

# Create sample data for visualization
climate_data = pd.DataFrame({
    'Disaster Type': ['Cloudburst', 'Landslide', 'Floods', 'Others'],
    'Events': [700, 1034, 300, 165],
    'Impact Score': [85, 90, 75, 40]
})

col1, col2 = st.columns(2)

with col1:
    fig = px.pie(climate_data, values='Events', names='Disaster Type', 
                 title='Disaster Distribution 2025',
                 color_discrete_sequence=px.colors.sequential.Emrld)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.bar(climate_data, x='Disaster Type', y='Impact Score',
                  title='Impact Severity Analysis',
                  color='Impact Score',
                  color_continuous_scale='Viridis')
    st.plotly_chart(fig2, use_container_width=True)

# Products Section
st.markdown("""
<div class="section-header" id="products">
    <h2 class="section-title">Our Organic Products</h2>
    <p class="section-subtitle">Pure Himalayan goodness from our farms to your home</p>
</div>
""", unsafe_allow_html=True)

products = [
    {"name": "Organic Millets", "category": "Shri Anna", "features": ["GI Certified", "Rich in Nutrients"]},
    {"name": "Himalayan Herbs", "category": "Medicinal Plants", "features": ["Ayurvedic", "Wild Harvested"]},
    {"name": "Aroma Oils", "category": "Essential Oils", "features": ["Pure Extract", "Therapeutic"]},
    {"name": "Vegan Products", "category": "Plant-based", "features": ["Cruelty-free", "Sustainable"]},
    {"name": "Natural Preserves", "category": "Jams & Pickles", "features": ["No Preservatives", "Traditional Recipes"]},
    {"name": "Puja Materials", "category": "Religious", "features": ["Natural", "Eco-friendly"]}
]

cols = st.columns(3)
for idx, product in enumerate(products):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <h4>🌿 {product['name']}</h4>
            <p><strong>Category:</strong> {product['category']}</p>
            <div style="margin-top: 1rem;">
                {' '.join([f'<span style="background: #2E8B57; color: white; padding: 0.2rem 0.5rem; border-radius: 15px; font-size: 0.8rem; margin-right: 0.5rem;">{feature}</span>' for feature in product['features']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="section-header" id="contact">
    <h2 class="section-title">Get Involved</h2>
    <p class="section-subtitle">Join our movement for sustainable development</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📞 Contact Information</h3>
        <p><strong>Email:</strong> thechangeuttarakhand@gmail.com</p>
        <p><strong>Phone:</strong> +91-7668512325</p>
        <p><strong>Address:</strong> Village Badshahi Thaul, Tehri Garhwal, Uttarakhand</p>
        
        <div style="margin-top: 2rem;">
            <h4>Follow Us</h4>
            <p>📱 Facebook: @changeuttarakhand</p>
            <p>📸 Instagram: @changeuttarakhand</p>
            <p>🎬 YouTube: CHANGE Uttarakhand</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    with st.form("contact_form"):
        st.subheader("Send us a Message")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        interest = st.selectbox("Area of Interest", [
            "Membership", "Volunteering", "Partnership", "Products", "AI Consultation", "Other"
        ])
        message = st.text_area("Message")
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        if submitted:
            st.success("Thank you for your message! We'll get back to you within 24 hours.")

# Footer
st.markdown("""
<div class="footer">
    <div style="text-align: center;">
        <h3 style="color: white; margin-bottom: 1rem;">🌿 CHANGE Cooperative</h3>
        <p style="opacity: 0.8;">Empowering Rural Uttarakhand through Sustainable Development</p>
        <div style="margin-top: 2rem; opacity: 0.6;">
            <p>Registered under Uttarakhand Autonomous Cooperative Act, 2003</p>
            <p>© 2024 CHANGE - Centre for Himalaya Agriculture and Nature Group of Environment. All rights reserved.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# SEO Meta Tags (for when deployed as proper website)
st.markdown("""
<!-- SEO Meta Tags -->
<meta name="description" content="CHANGE Uttarakhand - Sustainable agriculture, environmental conservation, and community empowerment in the Himalayas. Organic farming, AI climate solutions, rural development.">
<meta name="keywords" content="Uttarakhand agriculture, sustainable farming, climate change, AI consultant, organic products, rural development, Himalayas">
<meta name="author" content="CHANGE Cooperative">
""", unsafe_allow_html=True)
