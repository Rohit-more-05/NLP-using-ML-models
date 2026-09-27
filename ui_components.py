import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="NLP Models Explorer",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def apply_custom_styles():
    st.markdown("""
        <style>
        .main {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .metric-card {
            background: linear-gradient(135deg, #1E2530 0%, #151A22 100%);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            text-align: center;
            border: 1px solid #2B3544;
            transition: transform 0.2s;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: #4CAF50;
        }
        .metric-title {
            font-size: 1.1rem;
            color: #A0AEC0;
            margin-bottom: 10px;
        }
        .metric-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #4CAF50;
            margin: 0;
        }
        .info-box {
            background-color: #1E2530;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #3B82F6;
            margin-bottom: 20px;
        }
        .pros-cons-box {
            background-color: #1E2530;
            padding: 15px;
            border-radius: 8px;
            height: 100%;
        }
        .mock-prediction {
            background: linear-gradient(to right, #1a2a6c, #b21f1f, #fdbb2d);
            padding: 2px;
            border-radius: 12px;
            margin-top: 20px;
        }
        .mock-prediction-inner {
            background-color: #0E1117;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.title("🧠 Natural Language Processing: Model Explorer")
    st.markdown("""
    Welcome! This dashboard allows you to explore different machine learning models trained for text classification. 
    Compare how different algorithms (Naive Bayes, Logistic Regression) and text vectorization techniques (BoW, TF-IDF) perform.
    """)
    st.divider()

def render_model_details(details):
    st.header(f"📊 {details['type']} with {details['vectorizer']}")
    
    # Accuracy Metric Card
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Model Accuracy Score</div>
            <div class="metric-value">{details['accuracy'] * 100:.2f}%</div>
        </div>
        <br>
    """, unsafe_allow_html=True)
    
    # Description
    st.markdown(f"""
        <div class="info-box">
            <h4>About this Model</h4>
            <p>{details['description']}</p>
            <p><strong>Best for:</strong> {details['best_for']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Pros & Cons
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="pros-cons-box">', unsafe_allow_html=True)
        st.subheader("✅ Advantages")
        for pro in details['pros']:
            st.markdown(f"- {pro}")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="pros-cons-box">', unsafe_allow_html=True)
        st.subheader("⚠️ Limitations")
        for con in details['cons']:
            st.markdown(f"- {con}")
        st.markdown('</div>', unsafe_allow_html=True)

def render_simulation_section(model_name):
    st.divider()
    st.subheader("🧪 Try it out (Simulation)")
    st.markdown(f"Enter some text below to simulate how the **{model_name}** model would process it.")
    
    user_input = st.text_area("Enter text for classification:", placeholder="e.g., I absolutely loved this movie, the acting was phenomenal!")
    
    if st.button("Simulate Prediction", type="primary"):
        if user_input.strip():
            with st.spinner("Processing text..."):
                import time
                time.sleep(1.5) # Simulate processing time
                
                # Mock result logic
                result = "Positive" if len(user_input) % 2 == 0 else "Negative"
                confidence = 0.75 + (min(len(user_input), 100) / 400) # Fake confidence
                
                st.markdown(f"""
                <div class="mock-prediction">
                    <div class="mock-prediction-inner">
                        <h3>Simulated Result</h3>
                        <p>Predicted Class: <strong>{result}</strong></p>
                        <p>Confidence: <strong>{confidence * 100:.1f}%</strong></p>
                        <p style="color: #888; font-size: 0.8em; margin-top: 15px;">
                            *Note: This is a simulated prediction for UI demonstration purposes, as the original vectorizers were not provided.
                        </p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to simulate a prediction.")
