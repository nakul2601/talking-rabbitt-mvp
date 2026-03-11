import streamlit as st
import pandas as pd
import re

# Custom CSS for professional styling
def load_css():
    st.markdown("""
    <style>
        /* Import modern fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global styles */
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            font-family: 'Inter', sans-serif;
        }
        
        /* Main container */
        .main {
            padding: 0;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Title styling */
        .title {
            font-size: 4rem !important;
            font-weight: 800 !important;
            color: white !important;
            text-align: center;
            margin-bottom: 0.5rem;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
            letter-spacing: -1px;
            animation: fadeInDown 1s ease-out;
        }
        
        /* Subtitle styling */
        .subtitle {
            font-size: 1.3rem !important;
            color: rgba(255, 255, 255, 0.9) !important;
            text-align: center;
            margin-bottom: 3rem;
            font-weight: 400;
            animation: fadeInUp 1s ease-out 0.3s both;
        }
        
        /* Premium card styling */
        .card {
            background: rgba(255, 255, 255, 0.98);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.3);
            margin: 1.5rem 0;
            position: relative;
            overflow: hidden;
            animation: slideUp 0.6s ease-out;
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
            border-radius: 20px 20px 0 0;
        }
        
        /* Enhanced upload area */
        .upload-area {
            border: 3px dashed rgba(102, 126, 234, 0.6);
            border-radius: 15px;
            padding: 3rem;
            text-align: center;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.08), rgba(118, 75, 162, 0.12));
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        
        .upload-area::before {
            content: '📁';
            font-size: 4rem;
            display: block;
            margin-bottom: 1rem;
            animation: bounce 2s infinite;
        }
        
        .upload-area:hover {
            border-color: #f093fb;
            background: linear-gradient(135deg, rgba(240, 147, 251, 0.15), rgba(102, 126, 234, 0.2));
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(240, 147, 251, 0.3);
        }
        
        /* Premium chat container */
        .chat-container {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            max-height: 500px;
            overflow-y: auto;
            box-shadow: 0 15px 50px rgba(0,0,0,0.12);
            scrollbar-width: thin;
            scrollbar-color: rgba(102, 126, 234, 0.3) transparent;
        }
        
        .chat-container::-webkit-scrollbar {
            width: 6px;
        }
        
        .chat-container::-webkit-scrollbar-track {
            background: rgba(102, 126, 234, 0.1);
            border-radius: 10px;
        }
        
        .chat-container::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 10px;
        }
        
        /* Enhanced success box */
        .success-box {
            background: linear-gradient(135deg, #10b981, #059669, #047857);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            border-left: 5px solid #065f46;
            position: relative;
            overflow: hidden;
            animation: slideInLeft 0.5s ease-out;
        }
        
        .success-box::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
            animation: shimmer 3s infinite;
        }
        
        /* Enhanced info box */
        .info-box {
            background: linear-gradient(135deg, #3b82f6, #2563eb, #1d4ed8);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            border-left: 5px solid #1e3a8a;
            position: relative;
            animation: slideInRight 0.5s ease-out;
        }
        
        /* Hide streamlit branding */
        .stDeployButton {
            display: none !important;
        }
        
        /* Streamlit header */
        .stHeader {
            background: transparent !important;
        }
        
        /* Enhanced button styling */
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2, #f093fb) !important;
            color: white !important;
            border: none !important;
            padding: 0.75rem 2.5rem !important;
            border-radius: 50px !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3) !important;
            position: relative !important;
            overflow: hidden !important;
        }
        
        .stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.6s;
        }
        
        .stButton > button:hover::before {
            left: 100%;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px) scale(1.05) !important;
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5) !important;
        }
        
        /* Enhanced expander */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #667eea, #764ba2, #f093fb) !important;
            border-radius: 15px !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 1rem !important;
            border: none !important;
        }
        
        /* Premium metric styling */
        div[data-testid="metric-container"] {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 147, 251, 0.05)) !important;
            padding: 1.5rem !important;
            border-radius: 15px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
            border: 1px solid rgba(102, 126, 234, 0.2) !important;
            transition: all 0.3s ease !important;
        }
        
        div[data-testid="metric-container"]:hover {
            transform: translateY(-5px) !important;
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2) !important;
        }
        
        /* Enhanced file uploader */
        .stFileUploader {
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
        }
        
        .stFileUploader > div > div {
            background: rgba(255, 255, 255, 0.1) !important;
            border: 2px solid rgba(102, 126, 234, 0.3) !important;
            border-radius: 15px !important;
            padding: 1rem !important;
            transition: all 0.3s ease !important;
        }
        
        .stFileUploader > div > div:hover {
            border-color: #f093fb !important;
            background: rgba(240, 147, 251, 0.1) !important;
        }
        
        /* Chat input styling */
        .stChatInput {
            background: rgba(255, 255, 255, 0.98) !important;
            border: 2px solid rgba(102, 126, 234, 0.3) !important;
            border-radius: 50px !important;
            padding: 1rem 1.5rem !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
        }
        
        .stChatInput:focus {
            border-color: #f093fb !important;
            box-shadow: 0 0 0 3px rgba(240, 147, 251, 0.2) !important;
        }
        
        /* Animations */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-20px);
            }
            60% {
                transform: translateY(-10px);
            }
        }
        
        @keyframes shimmer {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .title {
                font-size: 2.5rem !important;
            }
            
            .subtitle {
                font-size: 1.1rem !important;
            }
            
            .card {
                padding: 1.5rem;
                margin: 1rem 0;
            }
            
            .upload-area {
                padding: 2rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

def analyze_question(question, df):
    """
    Analyze the user's question and provide an answer based on the dataset.
    Currently handles questions about highest and lowest values.
    Returns both the answer text and the detected columns for visualization.
    """
    question_lower = question.lower()
    
    # Check for highest/lowest keywords
    if any(word in question_lower for word in ['highest', 'maximum', 'max', 'top', 'largest', 'greatest']):
        answer, metric_col, grouping_col = find_extreme_value(question, df, 'highest')
        return answer, metric_col, grouping_col
    elif any(word in question_lower for word in ['lowest', 'minimum', 'min', 'bottom', 'smallest', 'least']):
        answer, metric_col, grouping_col = find_extreme_value(question, df, 'lowest')
        return answer, metric_col, grouping_col
    else:
        answer = "I'm sorry, I can only understand questions about the highest or lowest values right now. Please try asking something like 'Which region has the highest revenue?' or 'What is the lowest sales amount?'"
        return answer, None, None

def find_extreme_value(question, df, extreme_type):
    """
    Find the highest or lowest value based on the question.
    Returns answer text and detected columns for visualization.
    """
    # Extract column names from the question
    columns = df.columns.tolist()
    
    # Try to identify the target column (numeric) and grouping column (categorical)
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    
    # Look for column names mentioned in the question
    question_lower = question.lower()
    
    # Find the metric column (what we're measuring)
    metric_column = None
    for col in numeric_columns:
        if col.lower() in question_lower:
            metric_column = col
            break
    
    # Find the grouping column (what we're comparing)
    grouping_column = None
    for col in categorical_columns:
        if col.lower() in question_lower:
            grouping_column = col
            break
    
    # If we can't find specific columns, try to infer
    if not metric_column and numeric_columns:
        metric_column = numeric_columns[0]  # Use first numeric column
    
    if not grouping_column and categorical_columns:
        grouping_column = categorical_columns[0]  # Use first categorical column
    
    if not metric_column:
        answer = "I couldn't find a numeric column to analyze. Please make sure your dataset has numerical data."
        return answer, None, None
    
    # Perform the analysis
    if grouping_column:
        # Group by the categorical column and find extreme
        grouped = df.groupby(grouping_column)[metric_column].sum()
        if extreme_type == 'highest':
            result = grouped.idxmax()
            value = grouped.max()
        else:
            result = grouped.idxmin()
            value = grouped.min()
        
        answer = f"The {grouping_column} with the {extreme_type} {metric_column} is {result} with total {metric_column} of {value:,.2f}."
        return answer, metric_column, grouping_column
    else:
        # No grouping, just find extreme in the entire dataset
        if extreme_type == 'highest':
            value = df[metric_column].max()
            row_index = df[metric_column].idxmax()
        else:
            value = df[metric_column].min()
            row_index = df[metric_column].idxmin()
        
        # Get some context from the row
        row_data = df.loc[row_index]
        context = []
        for col in df.columns:
            if col != metric_column and pd.notna(row_data[col]):
                context.append(f"{col}: {row_data[col]}")
        
        context_str = ", ".join(context[:3])  # Limit to first 3 context items
        answer = f"The {extreme_type} {metric_column} is {value:,.2f} ({context_str})."
        return answer, metric_column, None

def main():
    # Load custom CSS
    load_css()
    
    # Set page configuration
    st.set_page_config(
        page_title="Talking Rabbitt – Conversational Data Analytics",
        page_icon="🐰",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state for conversation history and data
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    
    # Professional header with enhanced branding
    st.markdown("""
        <div class='title'>
            🐰 Talking Rabbitt
        </div>
        <div class='subtitle'>
            🚀 Enterprise-Grade Conversational Analytics Platform
        </div>
    """, unsafe_allow_html=True)
    
    # File uploader section (only show if data not loaded)
    if not st.session_state.data_loaded:
        st.markdown("""
            <div class='card'>
                <h2 style='color: #667eea; margin-bottom: 2rem; font-size: 2rem;'>� Upload Your Dataset</h2>
                <div class='upload-area'>
                    <h3 style='color: #764ba2; margin-bottom: 1.5rem; font-size: 1.5rem;'>🎯 Ready for Intelligent Analysis</h3>
                    <p style='color: #666; margin-bottom: 2rem; font-size: 1.1rem;'>Transform your CSV data into meaningful conversations with AI-powered insights</p>
                    <div style='display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;'>
                        <div style='text-align: center;'>
                            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📁</div>
                            <div style='font-size: 0.9rem; color: #666;'>Drag & Drop</div>
                        </div>
                        <div style='text-align: center;'>
                            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📂</div>
                            <div style='font-size: 0.9rem; color: #666;'>or Browse</div>
                        </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=['csv'],
            help="Upload a CSV file to analyze your data",
            label_visibility="collapsed"
        )
        
        if uploaded_file is not None:
            try:
                # Read CSV file
                df = pd.read_csv(uploaded_file)
                
                # Store in session state
                st.session_state.data = df
                st.session_state.data_loaded = True
                
                # Premium welcome message
                welcome_msg = f"""
                    <div class='success-box'>
                        <div style='display: flex; align-items: center; margin-bottom: 1.5rem;'>
                            <div style='font-size: 3rem; margin-right: 1rem;'>🎉</div>
                            <div>
                                <h3 style='margin: 0; font-size: 1.5rem;'>Dataset Successfully Loaded!</h3>
                                <p style='margin: 0.5rem 0; opacity: 0.9;'>Your data is ready for intelligent analysis</p>
                            </div>
                        </div>
                        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;'>
                            <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;'>
                                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📄</div>
                                <div style='font-weight: 600; margin-bottom: 0.25rem;'>{uploaded_file.name}</div>
                                <div style='font-size: 0.9rem; opacity: 0.8;'>File Name</div>
                            </div>
                            <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;'>
                                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📏</div>
                                <div style='font-weight: 600; margin-bottom: 0.25rem;'>{len(df):,}</div>
                                <div style='font-size: 0.9rem; opacity: 0.8;'>Total Rows</div>
                            </div>
                            <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;'>
                                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📋</div>
                                <div style='font-weight: 600; margin-bottom: 0.25rem;'>{len(df.columns)}</div>
                                <div style='font-size: 0.9rem; opacity: 0.8;'>Total Columns</div>
                            </div>
                            <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;'>
                                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>✅</div>
                                <div style='font-weight: 600; margin-bottom: 0.25rem;'>Ready</div>
                                <div style='font-size: 0.9rem; opacity: 0.8;'>Status</div>
                            </div>
                        </div>
                        <div style='margin-top: 2rem; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: center;'>
                            <p style='margin: 0; font-weight: 600;'>💬 Start asking questions about your data below!</p>
                        </div>
                    </div>
                """
                st.session_state.messages.append({"role": "assistant", "content": welcome_msg})
                
                # Rerun to refresh interface
                st.rerun()
                
            except Exception as e:
                error_msg = f"""
                    <div class='info-box'>
                        <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                            <div style='font-size: 3rem; margin-right: 1rem;'>⚠️</div>
                            <div>
                                <h3 style='margin: 0; font-size: 1.5rem;'>Upload Error</h3>
                                <p style='margin: 0.5rem 0; opacity: 0.9;'>Unable to process the uploaded file</p>
                            </div>
                        </div>
                        <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-top: 1rem;'>
                            <p><strong>Error Details:</strong> {str(e)}</p>
                            <p><strong>Solution:</strong> Please ensure your file is a valid CSV format and try again.</p>
                        </div>
                    </div>
                """
                st.markdown(error_msg, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class='card'>
                    <h2 style='color: #667eea; margin-bottom: 2rem; font-size: 2rem;'>👋 Welcome to Talking Rabbitt</h2>
                    <div style='text-align: center; margin: 2rem 0;'>
                        <div style='font-size: 4rem; margin-bottom: 1rem; animation: bounce 2s infinite;'>🐰</div>
                        <h3 style='color: #764ba2; margin-bottom: 1rem;'>Your Intelligent Data Assistant</h3>
                        <p style='font-size: 1.1rem; color: #666; margin-bottom: 2rem;'>Upload any CSV file to unlock powerful AI-driven data insights through natural conversation</p>
                        
                        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; margin: 2rem 0;'>
                            <div style='text-align: center; padding: 1rem; background: rgba(102, 126, 234, 0.1); border-radius: 10px;'>
                                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📊</div>
                                <div style='font-weight: 600; margin-bottom: 0.25rem;'>Analyze</div>
                                <div style='font-size: 0.8rem; opacity: 0.8;'>Data Patterns</div>
                            </div>
                            <div style='text-align: center; padding: 1rem; background: rgba(118, 75, 162, 0.1); border-radius: 10px;'>
                                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>💬</div>
                                <div style='font-weight: 600; margin-bottom: 0.25rem;'>Chat</div>
                                <div style='font-size: 0.8rem; opacity: 0.8;'>Natural Language</div>
                            </div>
                            <div style='text-align: center; padding: 1rem; background: rgba(240, 147, 251, 0.1); border-radius: 10px;'>
                                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🎯</div>
                                <div style='font-weight: 600; margin-bottom: 0.25rem;'>Discover</div>
                                <div style='font-size: 0.8rem; opacity: 0.8;'>Insights</div>
                            </div>
                        </div>
                    </div>
                    
                    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(240, 147, 251, 0.1)); padding: 1.5rem; border-radius: 15px; margin-top: 2rem; text-align: center;'>
                        <h4 style='color: #667eea; margin-bottom: 1rem;'>🚀 Getting Started</h4>
                        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; text-align: left;'>
                            <div>
                                <p style='margin: 0 0 0.5rem 0;'><strong>📁 Supported Formats:</strong> CSV files</p>
                                <p style='margin: 0 0 0.5rem 0;'><strong>📏 Max File Size:</strong> 200MB</p>
                                <p style='margin: 0;'><strong>🔒 Security:</strong> Local processing only</p>
                            </div>
                            <div>
                                <p style='margin: 0 0 0.5rem 0;'><strong>💬 Natural Language:</strong> Ask questions in plain English</p>
                                <p style='margin: 0 0 0.5rem 0;'><strong>🎯 Smart Analysis:</strong> Automatic pattern detection</p>
                                <p style='margin: 0;'><strong>⚡ Instant Results:</strong> Real-time insights</p>
                            </div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    else:
        # Data is loaded, show professional chat interface
        # Show data info in a professional card
        st.markdown("""
            <div class='card'>
                <h2 style='color: #667eea; margin-bottom: 1.5rem;'>📊 Dataset Overview</h2>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("� Dataset Details", expanded=False):
            df = st.session_state.data
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📏 Total Rows", f"{len(df):,}")
            with col2:
                st.metric("📋 Total Columns", len(df.columns))
            with col3:
                st.metric("📊 Data Points", f"{len(df) * len(df.columns):,}")
            
            st.markdown("**👁️ Data Preview:**")
            st.dataframe(df.head(), use_container_width=True)
            
            st.markdown("**� Column Names:**")
            cols_str = ", ".join([f"`{col}`" for col in df.columns])
            st.markdown(cols_str)
        
        # Professional chat interface
        st.markdown("""
            <div class='card'>
                <h2 style='color: #667eea; margin-bottom: 1.5rem; font-size: 2rem;'>💬 Intelligent Data Conversation</h2>
                <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(240, 147, 251, 0.1)); padding: 1rem; border-radius: 10px; margin-bottom: 1.5rem; text-align: center;'>
                    <p style='margin: 0; color: #667eea; font-weight: 600;'>🤖 Ask me anything about your data in natural language</p>
                    <p style='margin: 0.5rem 0 0 0; color: #666; font-size: 0.9rem;'>I'll provide instant insights and analysis</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Display chat messages with custom styling
        chat_container = st.container()
        with chat_container:
            if not st.session_state.messages:
                st.markdown("""
                    <div style='text-align: center; padding: 2rem; opacity: 0.6;'>
                        <div style='font-size: 3rem; margin-bottom: 1rem;'>💬</div>
                        <p style='color: #666; font-style: italic;'>Start a conversation about your data...</p>
                    </div>
                """, unsafe_allow_html=True)
            
            for message in st.session_state.messages:
                with st.chat_message(message["role"], avatar="🐰" if message["role"] == "assistant" else "👤"):
                    st.markdown(message["content"], unsafe_allow_html=True)
        
        # Enhanced chat input
        user_question = st.chat_input("� Ask me anything about your data...", key="chat_input")
        
        if user_question:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_question})
            
            # Process question
            with st.spinner("🤖 Analyzing your data..."):
                answer, metric_col, grouping_col = analyze_question(user_question, st.session_state.data)
            
            # Create premium assistant response
            assistant_response = f"""
                <div class='success-box'>
                    <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                        <div style='font-size: 2.5rem; margin-right: 1rem;'>🎯</div>
                        <div>
                            <h4 style='margin: 0; font-size: 1.3rem; color: white;'>Analysis Result</h4>
                            <p style='margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 1rem;'>Here's what I found in your data:</p>
                        </div>
                    </div>
                    <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-top: 1rem;'>
                        <p style='margin: 0; font-size: 1.1rem; color: white; font-weight: 500;'>{answer}</p>
                    </div>
                    <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.2);'>
                        <p style='margin: 0; font-size: 0.9rem; opacity: 0.8;'>💡 <em>Ask follow-up questions to explore your data further!</em></p>
                    </div>
                </div>
            """
            
            # Add assistant message to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            
            # Rerun to display the new messages
            st.rerun()

if __name__ == "__main__":
    main()
