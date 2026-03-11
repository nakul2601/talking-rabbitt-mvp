# 🐰 Talking Rabbitt – Conversational Data Analytics

A professional, enterprise-grade conversational analytics platform that transforms CSV data exploration through natural language conversations.

## ✨ Features

### 🎯 Core Functionality
- **📁 CSV Upload**: Drag-and-drop or browse file upload
- **💬 Natural Language Chat**: Ask questions in plain English
- **🤖 Smart Analysis**: Automatic pattern detection and insights
- **📊 Data Preview**: Real-time dataset overview
- **💾 Session Persistence**: Maintains conversation history

### 🎨 Premium UI/UX
- **Modern Gradient Design**: Professional purple-blue-pink theme
- **Glass Morphism**: Frosted glass effects with backdrop blur
- **Smooth Animations**: FadeIn, SlideUp, Bounce, Shimmer effects
- **Responsive Layout**: Optimized for all screen sizes
- **Interactive Elements**: Hover effects and micro-interactions
- **Professional Typography**: Inter font for optimal readability

### 🚀 Technical Stack
- **Frontend**: Streamlit with custom CSS
- **Backend**: Python with Pandas for data processing
- **Styling**: Advanced CSS3 animations and transitions
- **Icons**: Emoji-based visual communication

## 📋 Requirements

- Python 3.7+
- Streamlit >= 1.28.0
- Pandas >= 1.5.0
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🛠️ Installation

### Clone and Setup
```bash
git clone https://github.com/yourusername/talking-rabbitt.git
cd talking-rabbitt
pip install -r requirements.txt
```

### Run Locally
```bash
streamlit run app.py
```

## 📖 Usage Guide

### 1. Upload Dataset
- Click "Browse files" or drag & drop CSV file
- Supported formats: CSV files up to 200MB
- Automatic data validation and preview

### 2. Start Conversation
- Ask questions in natural language
- Example queries:
  - "Which region has the highest revenue?"
  - "What is the lowest sales amount?"
  - "Show me top performing products"

### 3. Get Insights
- Real-time data analysis
- Automatic column detection
- Context-aware responses
- Visual data summaries

## 🎯 Supported Query Types

### Highest/Lowest Analysis
- **Keywords**: highest, maximum, max, top, largest, greatest
- **Keywords**: lowest, minimum, min, bottom, smallest, least
- **Auto-detection**: Numeric and categorical columns
- **Grouping**: Automatic aggregation by categories

## 📊 Sample Dataset Format

```csv
Region,Product,Sales,Date
North,Laptop,15000,2024-01-15
South,Phone,12000,2024-01-16
East,Tablet,8000,2024-01-17
West,Laptop,18000,2024-01-18
```

## 🎨 Customization

### Branding
Modify the CSS in `load_css()` function to customize:
- **Colors**: Gradient themes and color schemes
- **Typography**: Font families and sizes
- **Animations**: Transition effects and timings
- **Layout**: Spacing and component styling

### Features
Extend functionality in `analyze_question()` function:
- **New query types**: Average, sum, count operations
- **Advanced analysis**: Trend detection, correlations
- **Export options**: CSV, JSON, or visual formats

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set custom port
STREAMLIT_SERVER_PORT=8501

# Optional: Enable debug mode
STREAMLIT_LOGGER_LEVEL=debug
```

## 📱 Deployment

### Local Deployment
```bash
streamlit run app.py --server.port 8501
```

### Cloud Deployment
- **Streamlit Cloud**: Direct deployment to cloud.streamlit.io
- **Docker**: Containerized deployment with Dockerfile
- **Heroku**: PaaS deployment with Procfile

## 🐛 Troubleshooting

### Common Issues
- **CSV Upload Error**: Ensure valid CSV format
- **Memory Issues**: Reduce dataset size or increase resources
- **Port Conflicts**: Change server port with `--server.port`
- **Font Loading**: Check internet connection for Google Fonts

### Debug Mode
```bash
streamlit run app.py --logger.level debug
```

## 🤝 Contributing

### Development Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
```

### Code Style
- Follow PEP 8 guidelines
- Use descriptive variable names
- Add comprehensive docstrings
- Include type hints

## 📄 License

MIT License - Feel free to use, modify, and distribute

## 🙏 Acknowledgments

- **Streamlit**: Foundation framework for web apps
- **Pandas**: Powerful data manipulation library
- **Google Fonts**: Inter font family
- **CSS3**: Modern styling and animations

---

## 📞 Support

For issues, questions, or feature requests:
- 📧 **GitHub Issues**: Create an issue in the repository
- 💬 **Discussions**: Start a GitHub discussion
- 📧 **Pull Requests**: Submit improvements via PR

---

**🐰 Talking Rabbitt** - Transform data into conversations, one insight at a time.
