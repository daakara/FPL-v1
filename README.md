# FPL Analytics v1

Advanced Fantasy Premier League Analytics Application

## Features

- 📊 **Live Data Dashboard** - Real-time FPL statistics and player data
- 🤖 **AI Recommendations** - ML-powered player suggestions  
- 📈 **Advanced Analytics** - Predictive models and performance analysis
- 🎯 **Team Builder** - Optimize your FPL squad
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 💡 **Smart Insights** - Data-driven transfer suggestions

## Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/daakara/FPL-v1.git
cd FPL-v1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main_refactored.py
```

The app will open in your browser at `http://localhost:8501`

## Streamlit Cloud Deployment

The app is deployed at: **https://fpl-v1-xryauzckbnbq3snyg29tnv.streamlit.app/**

### Restarting the Cloud App

If you see errors after pushing changes to GitHub:
1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click on your app
3. Click "Reboot app" in the menu (⋮)
4. Wait for the app to restart with new dependencies

### Running Diagnostics

Visit the diagnostics page to check system health:
```
https://fpl-v1-xryauzckbnbq3snyg29tnv.streamlit.app/?diagnostics=true
```

Or run locally:
```bash
streamlit run diagnostics.py
```

## Troubleshooting

### "No FPL Data Available" Error

This error occurs when the app cannot connect to the FPL API. Try these solutions:

**On Streamlit Cloud:**
1. **Reboot the app** from Streamlit Cloud dashboard
2. **Check app logs** for specific errors
3. **Run diagnostics** by adding `?diagnostics=true` to URL

**Locally:**
1. **Check your internet connection**
2. **Verify FPL API is accessible**:
   ```bash
   curl https://fantasy.premierleague.com/api/bootstrap-static/
   ```
3. **Clear cache** and restart the app:
   ```bash
   rm -rf fpl_cache/ cache/
   streamlit run main_refactored.py
   ```

### Missing Dependencies

If you encounter import errors, reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### SSL Certificate Errors

If you see SSL/certificate errors:
```bash
pip install --upgrade certifi urllib3
```

## Configuration

The app uses secure configuration for API keys. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_key_here  # Optional, for AI features
```

## Project Structure

```
FPL-v1/
├── main_refactored.py       # Main application entry point
├── requirements.txt         # Python dependencies
├── components/             # UI components
├── services/              # Business logic services
├── views/                 # Page views
├── utils/                 # Utility functions
├── models/                # Data models
├── config/                # Configuration
└── middleware/            # Application middleware
```

## Technologies

- **Streamlit** - Web framework
- **Pandas** - Data processing
- **Plotly** - Interactive visualizations
- **scikit-learn** - Machine learning
- **XGBoost** - Advanced ML models
- **OpenAI** - AI integrations (optional)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is for educational and personal use.

## Support

For issues and questions, please open an issue on GitHub.
