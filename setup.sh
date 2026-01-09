#!/bin/bash

echo "🚀 Setting up FPL Analytics v1..."
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Check installation
echo ""
echo "✅ Checking installed packages..."
python3 << 'EOF'
packages = {
    'streamlit': 'Web Framework',
    'pandas': 'Data Processing', 
    'numpy': 'Numerical Computing',
    'plotly': 'Visualizations',
    'sklearn': 'Machine Learning',
    'xgboost': 'Advanced ML',
    'requests': 'HTTP Client',
    'beautifulsoup4': 'Web Scraping',
    'reportlab': 'PDF Generation',
    'openai': 'AI Integration',
    'streamlit_option_menu': 'Enhanced UI'
}

all_ok = True
for pkg, desc in packages.items():
    try:
        __import__(pkg.replace('-', '_'))
        print(f'  ✓ {pkg:<25} ({desc})')
    except ImportError:
        print(f'  ✗ {pkg:<25} MISSING!')
        all_ok = False

if all_ok:
    print('\n✅ All dependencies installed successfully!')
else:
    print('\n⚠️  Some packages are missing. Run: pip3 install -r requirements.txt')
EOF

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the application, run:"
echo "  streamlit run main_refactored.py"
echo ""
