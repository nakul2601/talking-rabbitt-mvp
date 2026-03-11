import streamlit as st
import pandas as pd
import re

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
    
    # Professional header
    st.markdown("""
        <h1 style='text-align: center; color: #667eea; font-size: 3rem; margin-bottom: 0.5rem;'>🐰 Talking Rabbitt</h1>
        <p style='text-align: center; color: #666; font-size: 1.2rem; margin-bottom: 2rem;'>Enterprise-Grade Conversational Analytics Platform</p>
    """, unsafe_allow_html=True)
    
    # File uploader section (only show if data not loaded)
    if not st.session_state.data_loaded:
        st.markdown("""
            <div style='background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin: 1rem 0;'>
                <h2 style='color: #667eea; margin-bottom: 1.5rem;'>📊 Upload Your Dataset</h2>
                <p style='color: #666; margin-bottom: 1.5rem;'>Transform your CSV data into meaningful conversations with AI-powered insights</p>
            </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=['csv'],
            help="Upload a CSV file to analyze your data"
        )
        
        if uploaded_file is not None:
            try:
                # Read CSV file
                df = pd.read_csv(uploaded_file)
                
                # Store in session state
                st.session_state.data = df
                st.session_state.data_loaded = True
                
                # Welcome message
                welcome_msg = f"""
                    <div style='background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;'>
                        <h3>✅ Dataset Successfully Loaded!</h3>
                        <p><strong>File:</strong> {uploaded_file.name}</p>
                        <p><strong>Rows:</strong> {len(df):,}</p>
                        <p><strong>Columns:</strong> {len(df.columns)}</p>
                        <p><strong>Status:</strong> Ready for intelligent analysis</p>
                        <p>💬 Start asking questions about your data below!</p>
                    </div>
                """
                st.session_state.messages.append({"role": "assistant", "content": welcome_msg})
                
                # Rerun to refresh interface
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error reading the CSV file: {str(e)}")
                st.info("Please make sure the file is a valid CSV format.")
        else:
            st.info("� Upload a CSV file to get started")
    
    else:
        # Data is loaded, show chat interface
        st.markdown("""
            <div style='background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin: 1rem 0;'>
                <h2 style='color: #667eea; margin-bottom: 1.5rem;'>📊 Dataset Overview</h2>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📋 Dataset Details", expanded=False):
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
            
            st.markdown("**📝 Column Names:**")
            cols_str = ", ".join([f"`{col}`" for col in df.columns])
            st.markdown(cols_str)
        
        # Chat interface
        st.markdown("""
            <div style='background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin: 1rem 0;'>
                <h2 style='color: #667eea; margin-bottom: 1.5rem;'>💬 Intelligent Data Conversation</h2>
                <p style='color: #666;'>🤖 Ask me anything about your data in natural language</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Display chat messages
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
        
        # Chat input
        user_question = st.chat_input("🔍 Ask me anything about your data...")
        
        if user_question:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_question})
            
            # Process question
            with st.spinner("🤖 Analyzing your data..."):
                answer, metric_col, grouping_col = analyze_question(user_question, st.session_state.data)
            
            # Create assistant response
            assistant_response = f"""
                <div style='background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;'>
                    <h4>🎯 Analysis Result</h4>
                    <p>{answer}</p>
                    <p style='font-size: 0.9rem; opacity: 0.8;'>💡 <em>Ask follow-up questions to explore your data further!</em></p>
                </div>
            """
            
            # Add assistant message to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            
            # Rerun to display the new messages
            st.rerun()

if __name__ == "__main__":
    main()
