import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="CHANGE - Centre for Himalaya Agriculture and Nature Group of Environment",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #8B4513;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E8B57;
        background-color: #FFF8E7;
        margin: 1rem 0;
    }
    .stats-card {
        background: linear-gradient(135deg, #2E8B57, #87CEEB);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    .objective-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .ai-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    .climate-alert {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .hindi-text {
        font-family: 'Arial Unicode MS', 'Nirmala UI', sans-serif;
        line-height: 1.8;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-header">CHANGE</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Centre for Himalaya Agriculture and Nature Group of Environment</div>', unsafe_allow_html=True)
st.markdown("### Empowering Rural Uttarakhand through Sustainable Agriculture, Nature Conservation & Community Enterprise")

# Navigation
st.sidebar.title("🌿 CHANGE Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "👥 About Us", 
    "🎯 Our Objectives",
    "🤖 AI Climate Consultant",
    "📊 Programs & Services",
    "🛍️ Products",
    "🏨 Enterprises",
    "🌧️ Uttarakhand Climate",
    "🤝 Get Involved",
    "📚 Resources",
    "📞 Contact"
])

# Home Page
if page == "🏠 Home":
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.image("https://images.unsplash.com/photo-1545208967-50e8c50d7deb?w=800", use_column_width=True)
    
    # Climate Alert Banner
    st.markdown("""
    <div class="climate-alert">
        <h3>🚨 उत्तराखंड जलवायु संकट</h3>
        <p>2025 में 65% दिन अत्यधिक मौसम की स्थिति | 2199+ आपदा घटनाएँ | AI सलाहकार से सहायता प्राप्त करें</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    st.subheader("📊 Our Impact")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="stats-card"><h3>5,000+</h3><p>Farmers Empowered</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stats-card"><h3>120+</h3><p>Organic Villages</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stats-card"><h3>15</h3><p>Cottage Industries</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stats-card"><h3>8 MW</h3><p>Solar Capacity Planned</p></div>', unsafe_allow_html=True)
    
    # AI Consultant Quick Section
    st.markdown("""
    <div class="ai-section">
        <h2>🤖 AI जलवायु सलाहकार</h2>
        <p>कृत्रिम बुद्धिमत्ता आधारित समाधान जलवायु परिवर्तन के प्रभावों से निपटने में</p>
        <p>✅ जलवायु जोखिम पूर्वानुमान | ✅ कार्बन क्रेडिट प्रबंधन | ✅ स्मार्ट कृषि सलाह</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Core Objectives Grid
    st.subheader("🎯 Our Core Objectives")
    objectives = [
        {"icon": "🌱", "title": "Organic Farming", "desc": "Promoting natural techniques"},
        {"icon": "💰", "title": "Fair Trade Marketing", "desc": "Eliminating middlemen"},
        {"icon": "🐄", "title": "Animal Protection", "desc": "Preventing exploitation"},
        {"icon": "👨‍🎓", "title": "Youth in Agriculture", "desc": "Smart tech integration"},
        {"icon": "🏨", "title": "Eco-Tourism", "desc": "Sustainable tourism"},
        {"icon": "⚡", "title": "Climate Resilience", "desc": "Disaster preparedness"}
    ]
    
    cols = st.columns(3)
    for idx, obj in enumerate(objectives):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="card">
                <div class="objective-icon">{obj['icon']}</div>
                <h4>{obj['title']}</h4>
                <p>{obj['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Featured Programs
    st.subheader("🚀 Featured Programs")
    programs = [
        "Personal Family Farmer Initiative",
        "Microfinance for Women SHGs", 
        "Contract Farming with Millets",
        "Organic Certification Support",
        "Solar Energy Projects"
    ]
    
    for program in programs:
        st.markdown(f"- **{program}**")
    
    # CTA Buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("👥 Join as Member", use_container_width=True):
            st.session_state.page = "🤝 Get Involved"
    with col2:
        if st.button("🤖 AI Consultant", use_container_width=True):
            st.session_state.page = "🤖 AI Climate Consultant"
    with col3:
        if st.button("📞 Contact Us", use_container_width=True):
            st.session_state.page = "📞 Contact"

# AI Climate Consultant Page
elif page == "🤖 AI Climate Consultant":
    st.header("🤖 AI जलवायु सलाहकार")
    st.subheader("कृत्रिम बुद्धिमत्ता आधारित समाधान जलवायु परिवर्तन अनुकूलन के लिए")
    
    # Introduction
    st.markdown("""
    <div class="card hindi-text">
        <h3>🌍 AI Consultant क्या कर सकता है?</h3>
        <p>एक AI Consultant (कृत्रिम बुद्धिमत्ता आधारित सलाहकार) जलवायु परिवर्तन के प्रभावों से निपटने और उससे अनुकूलन में किसानों, सरकारों और समुदायों को व्यावहारिक, तकनीकी और नीति-आधारित समाधान प्रदान कर सकता है।</p>
    </div>
    """, unsafe_allow_html=True)
    
    # AI Services Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌦️ जलवायु पूर्वानुमान", 
        "🌱 जलवायु अनुकूल खेती",
        "💰 कार्बन क्रेडिट", 
        "💧 संसाधन दक्षता",
        "🏛️ नीति सहायता"
    ])
    
    with tab1:
        st.subheader("🌦️ जलवायु जोखिम पूर्वानुमान और चेतावनी प्रणाली")
        st.markdown("""
        <div class="hindi-text">
        <h4>📊 कैसे काम करता है:</h4>
        <ul>
            <li>AI मॉडल तापमान, वर्षा, और फसल स्वास्थ्य के रियल-टाइम डेटा को विश्लेषित करके जलवायु जोखिमों की भविष्यवाणी करते हैं</li>
            <li>बाढ़, सूखा, या पाला पड़ने से पहले अलर्ट प्रणाली</li>
            <li>समय रहते फसल सुरक्षा, बीज चयन या सिंचाई योजना में बदलाव</li>
        </ul>
        
        <h4>🎯 उत्तराखंड के लिए लाभ:</h4>
        <ul>
            <li>पहाड़ी वर्षा और बर्फबारी से होने वाले नुकसान से समय पर निपटने में मदद</li>
            <li>भूस्खलन और बादल फटने की पूर्व चेतावनी</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Weather Alert Simulation
        st.subheader("🚨 मौसम चेतावनी सिमुलेशन")
        col1, col2 = st.columns(2)
        with col1:
            district = st.selectbox("जिला चुनें", [
                "टिहरी गढ़वाल", "पौड़ी", "रुद्रप्रयाग", "चमोली", "उत्तरकाशी"
            ])
        with col2:
            alert_type = st.selectbox("चेतावनी प्रकार", [
                "बाढ़ चेतावनी", "भूस्खलन चेतावनी", "बादल फटने की संभावना", "सूखा चेतावनी"
            ])
        
        if st.button("चेतावनी जनरेट करें"):
            st.warning(f"🚨 {district} में {alert_type} - अगले 24 घंटों में सतर्क रहें!")
            st.info("""
            **अनुशंसित कार्यवाही:**
            - फसलों को ढक कर रखें
            - पशुओं को सुरक्षित स्थान पर ले जाएं
            - स्थानीय अधिकारियों से संपर्क में रहें
            """)
    
    with tab2:
        st.subheader("🌱 जलवायु अनुकूल खेती के सुझाव")
        st.markdown("""
        <div class="hindi-text">
        <h4>🌾 AI-आधारित कृषि सलाह:</h4>
        <ul>
            <li>मिट्टी और मौसम के डेटा का विश्लेषण करके जलवायु-उपयुक्त फसल सुझाव</li>
            <li>मशीन लर्निंग एल्गोरिद्म फर्टिलाइज़र, सिंचाई और जल संरक्षण की आदर्श मात्रा बताते हैं</li>
            <li>Boomitra और Farmonaut जैसे प्लेटफ़ॉर्म के माध्यम से Carbon Farming</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Crop Recommendation Tool
        st.subheader("🌾 फसल सिफारिश उपकरण")
        col1, col2, col3 = st.columns(3)
        with col1:
            soil_type = st.selectbox("मिट्टी का प्रकार", [
                "दोमट मिट्टी", "चिकनी मिट्टी", "बलुई मिट्टी", "पहाड़ी मिट्टी"
            ])
        with col2:
            rainfall = st.selectbox("वार्षिक वर्षा", [
                "कम (500mm से कम)", "मध्यम (500-1000mm)", "अधिक (1000mm से अधिक)"
            ])
        with col3:
            altitude = st.selectbox("ऊंचाई", [
                "निचला क्षेत्र (1000m से कम)", 
                "मध्यम क्षेत्र (1000-2000m)", 
                "उच्च क्षेत्र (2000m से अधिक)"
            ])
        
        if st.button("फसल सिफारिश प्राप्त करें"):
            st.success("""
            **अनुशंसित फसलें:**
            - मंडुवा (Finger Millet)
            - झंगोरा (Barnyard Millet)
            - राजमा (Kidney Beans)
            - सेब (उच्च क्षेत्रों में)
            """)
            st.info("💡 **सलाह:** जैविक खाद का प्रयोग करें और फसल चक्र अपनाएं")
    
    with tab3:
        st.subheader("💰 कार्बन क्रेडिट प्रबंधन और आय बढ़त")
        st.markdown("""
        <div class="hindi-text">
        <h4>🌿 कार्बन फार्मिंग लाभ:</h4>
        <ul>
            <li>AI सलाहकार किसानों को कार्बन उत्सर्जन मापने, रिपोर्ट करने और वैरिफ़ाई करने में मदद</li>
            <li>ऑटोमेटेड MRV सिस्टम स्थापित करना</li>
            <li>अंतरराष्ट्रीय मानकों (Verra, Gold Standard) के अनुसार कार्बन क्रेडिट बेचकर आय</li>
        </ul>
        
        <h4>📈 सफलता की कहानी:</h4>
        <p>Boomitra प्लेटफ़ॉर्म के तहत भारत के किसानों ने मिट्टी में कार्बन बढ़ाकर प्रति वर्ष $300–$400 तक की अतिरिक्त आय अर्जित की</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Carbon Credit Calculator
        st.subheader("🧮 कार्बन क्रेडिट कैलकुलेटर")
        land_area = st.number_input("जमीन का क्षेत्रफल (हेक्टेयर में)", min_value=0.1, max_value=100.0, value=2.0)
        farming_type = st.selectbox("खेती का प्रकार", [
            "जैविक खेती", "पारंपरिक खेती", "वन-आधारित खेती"
        ])
        
        if st.button("आय का अनुमान लगाएं"):
            if farming_type == "जैविक खेती":
                income = land_area * 150
            elif farming_type == "वन-आधारित खेती":
                income = land_area * 200
            else:
                income = land_area * 100
                
            st.success(f"💰 अनुमानित वार्षिक अतिरिक्त आय: ${income:,.0f}")
            st.info("यह आय कार्बन क्रेडिट बिक्री से संभव है")
    
    with tab4:
        st.subheader("💧 संसाधन उपयोग में दक्षता")
        st.markdown("""
        <div class="hindi-text">
        <h4>🌊 स्मार्ट जल प्रबंधन:</h4>
        <ul>
            <li>AI नमी और तापमान सेंसरों से डेटा लेकर स्मार्ट सिंचाई प्रणाली</li>
            <li>जल की बचत और फसल उत्पादन दोनों बढ़ाना</li>
            <li>कृषि में ग्रीनहाउस गैस उत्सर्जन 10% तक घटाने की क्षमता</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Water Saving Calculator
        st.subheader("💧 जल बचत कैलकुलेटर")
        current_water_usage = st.number_input("वर्तमान जल उपयोग (लीटर/हेक्टेयर/दिन)", min_value=1000, max_value=10000, value=5000)
        
        if st.button("जल बचत विश्लेषण"):
            water_saved = current_water_usage * 0.3  # 30% saving with AI
            st.success(f"💧 AI सिस्टम से संभावित जल बचत: {water_saved:,.0f} लीटर/हेक्टेयर/दिन")
            st.info("यह 30% जल बचत के बराबर है!")
    
    with tab5:
        st.subheader("🏛️ नीति स्तर पर सहयोग")
        st.markdown("""
        <div class="hindi-text">
        <h4>📊 सरकारी सहयोग:</h4>
        <ul>
            <li>जलवायु नीतियों के प्रभाव मूल्यांकन में तकनीकी इनसाइट्स</li>
            <li>डेटा-संचालित नीति निर्माण</li>
            <li>राज्य और स्थानीय एजेंसियों को क्लाइमेट एक्शन प्लान में सहायता</li>
        </ul>
        
        <h4>👥 सामाजिक सशक्तिकरण:</h4>
        <ul>
            <li>जलवायु झटकों से प्रभावित समुदायों को AI आधारित सहायता</li>
            <li>Klarna और Milkywire का AI for Climate Resilience कार्यक्रम - $300,000 तक की ग्रांट</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # AI Benefits Summary Table
    st.subheader("📊 AI सलाहकार के लाभ - सारांश")
    benefits_data = {
        "योगदान क्षेत्र": [
            "जलवायु पूर्वानुमान",
            "टिकाऊ कृषि", 
            "कार्बन क्रेडिट",
            "नीति सहायता",
            "सामाजिक अनुकूलन"
        ],
        "AI Consultant की भूमिका": [
            "मौसम व फसल जोखिम चेतावनी",
            "मिट्टी आधारित फसल व जल सुझाव",
            "AI आधारित MRV और मार्केट लिंक",
            "प्रभाव मूल्यांकन व डेटा नीति",
            "प्रशिक्षण व स्थानीय क्षमताएँ"
        ],
        "लाभ": [
            "नुकसान में कमी",
            "उपज व आय वृद्धि", 
            "अतिरिक्त आय",
            "सटीक योजनाएँ",
            "जलवायु सहनशीलता"
        ]
    }
    
    st.table(pd.DataFrame(benefits_data))

# Uttarakhand Climate Page
elif page == "🌧️ Uttarakhand Climate":
    st.header("🌧️ उत्तराखंड जलवायु संकट")
    st.subheader("2025 के आंकड़े और विश्लेषण")
    
    # Critical Alert
    st.markdown("""
    <div class="climate-alert hindi-text">
        <h3>🚨 आपात स्थिति: उत्तराखंड जलवायु संकट</h3>
        <p><strong>2025 में उत्तराखंड ने पिछले 4 वर्षों का सबसे भीषण मौसम देखा है</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistics Section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("अत्यधिक मौसम के दिन", "65%", "43/66 दिन")
        st.caption("1 जून से 5 अगस्त 2025")
    
    with col2:
        st.metric("कुल आपदा घटनाएँ", "2,199+", "सितंबर 2025 तक")
    
    with col3:
        st.metric("मानव हानि", "260+", "मृत्यु, 566 घायल")
    
    # Detailed Breakdown
    st.subheader("📈 आपदा घटनाओं का विस्तृत विश्लेषण")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card hindi-text">
            <h4>🌧️ बादल फटना / फ्लैश फ्लड</h4>
            <p><strong>700+ मामले</strong></p>
            <p>तेज और केंद्रित वर्षा के कारण अचानक बाढ़</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card hindi-text">
            <h4>🏔️ भूस्खलन</h4>
            <p><strong>1,034 मामले</strong></p>
            <p>अवैज्ञानिक निर्माण और वनों की कटाई के कारण</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card hindi-text">
            <h4>❄️ ग्लेशियल लेक आउटबर्स्ट</h4>
            <p><strong>बढ़ता खतरा</strong></p>
            <p>हिमालयी ग्लेशियर तेज़ी से पिघल रहे हैं</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card hindi-text">
            <h4>🚧 अन्य आपदाएँ</h4>
            <p><strong>465+ मामले</strong></p>
            <p>बाढ़, मिट्टी का कटाव, और अन्य प्राकृतिक आपदाएँ</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Causes and Impacts
    st.subheader("🔍 मुख्य कारण और प्रभाव")
    
    tab1, tab2, tab3 = st.tabs(["कारण", "प्रभाव", "समाधान"])
    
    with tab1:
        st.markdown("""
        <div class="hindi-text">
        <h4>🌡️ जलवायु परिवर्तन:</h4>
        <ul>
            <li>औसत तापमान और वर्षा पैटर्न में बदलाव</li>
            <li>मॉनसून कम दिनों में ज़्यादा हिंसक और केंद्रित</li>
            <li>अचानक तेज बारिश के कारण बादल फटना और फ्लैश फ्लड</li>
        </ul>
        
        <h4>🏗️ अनियंत्रित विकास:</h4>
        <ul>
            <li>पहाड़ियों में अवैज्ञानिक सड़क निर्माण</li>
            <li>विशाल परियोजनाएँ और वनों की कटाई</li>
            <li>नदियों के किनारे बस्तियाँ और निर्माण</li>
        </ul>
        
        <h4>🏔️ ग्लेशियर पिघलना:</h4>
        <ul>
            <li>हिमालयी ग्लेशियर तेज़ी से पिघल रहे हैं</li>
            <li>Glacial Lake Outburst Floods (GLOF) का खतरा बढ़ गया</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="hindi-text">
        <h4>👥 लोगों का विस्थापन:</h4>
        <ul>
            <li><strong>245 गांव</strong> पिछले 14 वर्षों में आपदा का शिकार होकर अस्तित्व खो चुके</li>
            <li>बार-बार पूरे गांव खाली करने पड़ते हैं</li>
        </ul>
        
        <h4>💼 आजीविका पर प्रभाव:</h4>
        <ul>
            <li>किसानों, मजदूरों और सीमांत ग्रामीणों पर सबसे बड़ा असर</li>
            <li>कृषि और पर्यटन उद्योग बुरी तरह प्रभावित</li>
        </ul>
        
        <h4>🏗️ इंफ्रास्ट्रक्चर क्षति:</h4>
        <ul>
            <li>सड़क, पुल, बिजली-पानी व्यवस्था बार-बार टूटती है</li>
            <li>करोड़ों रुपये का नुकसान होता है</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="hindi-text">
        <h4>🚨 अर्ली वॉर्निंग सिस्टम:</h4>
        <ul>
            <li>हाईटेक मौसम और भूस्खलन पूर्वानुमान तंत्र</li>
            <li>समय से जागरूकता और सुरक्षा</li>
        </ul>
        
        <h4>🌳 सस्टेनेबल विकास:</h4>
        <ul>
            <li>वनों का संरक्षण और पुनर्वनरोपण</li>
            <li>पहाड़ों पर संयमित विकास</li>
            <li>परंपरागत जल-संरक्षण (चाल, नाला) को बढ़ावा</li>
        </ul>
        
        <h4>🏠 पुनर्वास योजनाएँ:</h4>
        <ul>
            <li>बार-बार आपदा भोग रहे गांवों का सुरक्षित स्थानों पर पुनर्वास</li>
            <li>सामूहिक और योजनाबद्ध पुनर्वास</li>
        </ul>
        
        <h4>🤖 AI तकनीक का उपयोग:</h4>
        <ul>
            <li>जलवायु जोखिम मॉडलिंग</li>
            <li>स्मार्ट कृषि सलाहकार</li>
            <li>रीयल-टाइम मॉनिटरिंग सिस्टम</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # AI Solutions for Uttarakhand
    st.subheader("🤖 उत्तराखंड के लिए AI समाधान")
    
    ai_solutions = [
        {
            "title": "भूस्खलन पूर्वानुमान",
            "description": "AI-आधारित भूस्खलन जोखिम मानचित्रण और चेतावनी प्रणाली",
            "benefit": "समय पर निकासी और जीवन बचाव"
        },
        {
            "title": "स्मार्ट कृषि सलाह",
            "description": "मौसम और मिट्टी डेटा के आधार पर फसल सिफारिश",
            "benefit": "फसल हानि में कमी और आय में वृद्धि"
        },
        {
            "title": "जल संसाधन प्रबंधन",
            "description": "AI-संचालित जल संरक्षण और वितरण प्रणाली",
            "benefit": "सूखे और बाढ़ दोनों से सुरक्षा"
        },
        {
            "title": "कार्बन क्रेडिट प्रबंधन",
            "description": "किसानों के लिए अतिरिक्त आय के अवसर",
            "benefit": "आर्थिक सशक्तिकरण और पर्यावरण संरक्षण"
        }
    ]
    
    cols = st.columns(2)
    for idx, solution in enumerate(ai_solutions):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card">
                <h4>🚀 {solution['title']}</h4>
                <p><strong>{solution['description']}</strong></p>
                <p>✅ {solution['benefit']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Call to Action
    st.markdown("""
    <div class="climate-alert hindi-text">
        <h3>📞 अभी कार्यवाही करें!</h3>
        <p>उत्तराखंड के जलवायु संकट से निपटने के लिए AI सलाहकार से संपर्क करें</p>
        <p>हमारे विशेषज्ञ आपको व्यक्तिगत समाधान प्रदान करेंगे</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🤖 AI सलाहकार से संपर्क करें", use_container_width=True):
            st.session_state.page = "🤖 AI Climate Consultant"
    with col2:
        if st.button("📞 तत्काल सहायता", use_container_width=True):
            st.session_state.page = "📞 Contact"

# Continue with other existing pages (About Us, Objectives, Programs, etc.)
# ... [Previous code for other pages remains the same]

# About Us Page (existing - keep as is)
elif page == "👥 About Us":
    st.header("👥 About CHANGE")
    # ... [Previous About Us content]

# Objectives Page (existing - keep as is)  
elif page == "🎯 Our Objectives":
    st.header("🎯 Our Objectives")
    # ... [Previous Objectives content]

# Programs Page (existing - keep as is)
elif page == "📊 Programs & Services":
    st.header("📊 Programs & Services")
    # ... [Previous Programs content]

# Products Page (existing - keep as is)
elif page == "🛍️ Products":
    st.header("🛍️ Our Products")
    # ... [Previous Products content]

# Enterprises Page (existing - keep as is)
elif page == "🏨 Enterprises":
    st.header("🏨 Our Enterprises")
    # ... [Previous Enterprises content]

# Get Involved Page (existing - keep as is)
elif page == "🤝 Get Involved":
    st.header("🤝 Get Involved")
    # ... [Previous Get Involved content]

# Resources Page (existing - keep as is)
elif page == "📚 Resources":
    st.header("📚 Resources")
    # ... [Previous Resources content]

# Contact Page (existing - keep as is)
elif page == "📞 Contact":
    st.header("📞 Contact CHANGE")
    # ... [Previous Contact content]

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**CHANGE Cooperative**")
    st.write("Empowering Rural Uttarakhand")

with col2:
    st.write("**Quick Links**")
    st.write("Privacy Policy | Terms of Service")

with col3:
    st.write("**Registered Under**")
    st.write("Uttarakhand Autonomous Cooperative Act, 2003")

st.markdown("<center>© 2024 CHANGE - Centre for Himalaya Agriculture and Nature Group of Environment. All rights reserved.</center>", unsafe_allow_html=True)