import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Page Configuration with SEO
st.set_page_config(
    page_title="CHANGE Uttarakhand - Sustainable Agriculture & Environment",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to create base64 encoded logo (FIXED)
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

# Get logo base64 at the start
logo_base64 = get_base64_logo()

# Custom CSS for Modern Design with Logo support
st.markdown(f"""
<style>
    /* Main Styles */
    .main {{
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }}
    
    /* Header with Logo */
    .header-container {{
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 1rem 0;
        border-bottom: 3px solid #2E8B57;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }}
    
    .logo-container {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    
    .logo-img {{
        width: 60px;
        height: 60px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #2E8B57;
    }}
    
    .logo-title {{
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #2E8B57, #3CB371);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        font-family: 'Arial Black', sans-serif;
    }}
    
    .tagline {{
        font-size: 1.2rem;
        color: #666;
        font-weight: 300;
        margin-top: 0.5rem;
        font-style: italic;
    }}
    
    /* Hero Section */
    .hero-section {{
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(46, 139, 87, 0.3);
    }}
    
    .hero-title {{
        font-size: 3.2rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }}
    
    .hero-subtitle {{
        font-size: 1.4rem;
        font-weight: 300;
        margin-bottom: 2rem;
        opacity: 0.9;
    }}
    
    /* Card Styles */
    .feature-card {{
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-top: 4px solid #2E8B57;
        transition: all 0.3s ease;
        height: 100%;
        text-align: center;
    }}
    
    .feature-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }}
    
    .stat-card {{
        background: linear-gradient(135deg, #2E8B57, #3CB371);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(46, 139, 87, 0.3);
    }}
    
    /* Navigation */
    .nav-container {{
        background: rgba(255, 255, 255, 0.98);
        padding: 1rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
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
    
    /* Section Headers */
    .section-header {{
        text-align: center;
        margin: 3rem 0 2rem 0;
        padding: 2rem 0;
    }}
    
    .section-title {{
        font-size: 2.5rem;
        font-weight: 700;
        color: #2E8B57;
        margin-bottom: 1rem;
    }}
    
    .section-subtitle {{
        font-size: 1.2rem;
        color: #666;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
    }}
    
    /* AI Section */
    .ai-section {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
    }}
    
    /* Climate Alert */
    .climate-alert {{
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
    }}
    
    /* Footer */
    .footer {{
        background: linear-gradient(135deg, #2c3e50, #34495e);
        color: white;
        padding: 3rem 0;
        margin-top: 4rem;
        border-radius: 20px 20px 0 0;
    }}
</style>
""", unsafe_allow_html=True)

# Header Section with Logo
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

# Navigation
st.markdown("""
<div class="nav-container">
    <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 10px;">
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

# Home Section
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Transforming Rural Uttarakhand</h1>
    <p class="hero-subtitle">Sustainable Agriculture • Environmental Stewardship • Community Empowerment</p>
    <div style="margin-top: 3rem;">
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
    <div style="text-align: center; color: white;">
        <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">🤖 AI Climate Consultant</h2>
        <p style="font-size: 1.2rem; opacity: 0.9;">Advanced AI solutions for climate resilience and sustainable agriculture</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">
        <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 15px; border: 1px solid rgba(255,255,255,0.2);">
            <h4>🌦️ Climate Risk Forecasting</h4>
            <p>Real-time weather predictions and early warning systems for floods, landslides, and extreme weather events.</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 15px; border: 1px solid rgba(255,255,255,0.2);">
            <h4>🌱 Smart Farming Solutions</h4>
            <p>AI-powered crop recommendations, soil health analysis, and precision agriculture techniques.</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 15px; border: 1px solid rgba(255,255,255,0.2);">
            <h4>💰 Carbon Credit Management</h4>
            <p>Automated systems for carbon credit generation and international market access.</p>
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

# Climate Section
st.markdown('<div id="climate"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="climate-alert">
    <h3 style="font-size: 2rem; margin-bottom: 1rem;">🚨 Uttarakhand Climate Emergency</h3>
    <p style="font-size: 1.2rem; margin-bottom: 0.5rem;"><strong>2025 Data:</strong> 2,199+ disaster events | 260+ fatalities | 65% extreme weather days</p>
    <p style="font-size: 1.1rem; margin: 0;">Immediate AI-powered solutions needed for climate resilience in Himalayan region</p>
</div>
""", unsafe_allow_html=True)

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
            else:
                st.error("Please fill in all required fields (*)")

# Footer
st.markdown(f"""
<div class="footer">
    <div style="text-align: center;">
        <div class="logo-container" style="justify-content: center; margin-bottom: 1rem;">
            <img src="data:image/svg+xml;base64,{logo_base64}" class="logo-img" alt="CHANGE Logo">
            <h3 style="color: white; margin: 0; font-size: 2rem;">🌿 CHANGE Cooperative</h3>
        </div>
        <p style="font-size: 1.2rem; opacity: 0.9; margin-bottom: 2rem;">Empowering Rural Uttarakhand through Sustainable Development</p>
        
        <div style="margin-top: 2rem; opacity: 0.7; border-top: 1px solid rgba(255,255,255,0.3); padding-top: 2rem;">
            <p>© 2024 CHANGE - Centre for Himalaya Agriculture and Nature Group of Environment. All rights reserved.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
