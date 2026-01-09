"""
System Diagnostics and Health Check for FPL Analytics
"""
import streamlit as st
import sys
import requests
from datetime import datetime


def show_diagnostics():
    """Display system diagnostics"""
    st.title("🔍 System Diagnostics")
    
    # Python Environment
    st.header("1. Python Environment")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Python Version", f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    with col2:
        st.metric("Platform", sys.platform)
    
    # Check Dependencies
    st.header("2. Dependencies Check")
    dependencies = {
        'streamlit': 'Web Framework',
        'pandas': 'Data Processing',
        'numpy': 'Numerical Computing',
        'plotly': 'Visualizations',
        'sklearn': 'Machine Learning',
        'xgboost': 'Advanced ML',
        'requests': 'HTTP Client',
        'bs4': 'Web Scraping (beautifulsoup4)',
        'reportlab': 'PDF Generation',
        'openai': 'AI Integration',
        'streamlit_option_menu': 'Enhanced UI',
        'aiohttp': 'Async HTTP',
        'websockets': 'WebSocket Support'
    }
    
    missing = []
    installed = []
    
    for pkg, desc in dependencies.items():
        try:
            __import__(pkg)
            installed.append((pkg, desc))
        except ImportError:
            missing.append((pkg, desc))
    
    if installed:
        st.success(f"✅ {len(installed)} packages installed")
        with st.expander("View installed packages"):
            for pkg, desc in installed:
                st.write(f"✓ **{pkg}** - {desc}")
    
    if missing:
        st.error(f"❌ {len(missing)} packages missing")
        for pkg, desc in missing:
            st.write(f"✗ **{pkg}** - {desc}")
        st.code(f"pip install {' '.join([p[0] for p in missing])}")
    
    # FPL API Connection Test
    st.header("3. FPL API Connection")
    
    with st.spinner("Testing FPL API connection..."):
        try:
            start_time = datetime.now()
            response = requests.get(
                "https://fantasy.premierleague.com/api/bootstrap-static/",
                timeout=10,
                verify=True
            )
            end_time = datetime.now()
            response_time = (end_time - start_time).total_seconds()
            
            if response.status_code == 200:
                data = response.json()
                players_count = len(data.get('elements', []))
                teams_count = len(data.get('teams', []))
                
                st.success("✅ FPL API is accessible")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Response Time", f"{response_time:.2f}s")
                with col2:
                    st.metric("Players", players_count)
                with col3:
                    st.metric("Teams", teams_count)
                
                with st.expander("API Response Sample"):
                    st.json({
                        'status_code': response.status_code,
                        'players': players_count,
                        'teams': teams_count,
                        'events': len(data.get('events', [])),
                        'headers': dict(response.headers)
                    })
            else:
                st.error(f"❌ FPL API returned status code: {response.status_code}")
                
        except requests.exceptions.Timeout:
            st.error("❌ Connection timeout - FPL API not responding")
        except requests.exceptions.SSLError as e:
            st.error(f"❌ SSL Certificate Error: {str(e)}")
            st.info("💡 Try: `pip install --upgrade certifi urllib3`")
        except requests.exceptions.ConnectionError as e:
            st.error(f"❌ Connection Error: {str(e)}")
        except Exception as e:
            st.error(f"❌ Unexpected error: {str(e)}")
            st.exception(e)
    
    # Session State
    st.header("4. Application State")
    
    if hasattr(st.session_state, '__dict__'):
        state_keys = [k for k in st.session_state.keys() if not k.startswith('_')]
        st.metric("Session Variables", len(state_keys))
        
        if state_keys:
            with st.expander("View session state"):
                for key in state_keys:
                    value = st.session_state[key]
                    if isinstance(value, (str, int, float, bool)):
                        st.write(f"**{key}**: {value}")
                    else:
                        st.write(f"**{key}**: {type(value).__name__}")
    
    # Quick Actions
    st.header("5. Quick Actions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Clear Cache"):
            st.cache_data.clear()
            st.cache_resource.clear()
            st.success("Cache cleared!")
            st.rerun()
    
    with col2:
        if st.button("🗑️ Reset Session"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.success("Session reset!")
            st.rerun()
    
    # Environment Info
    st.header("6. Environment Information")
    import os
    
    env_vars = {
        'STREAMLIT_SERVER_PORT': os.getenv('STREAMLIT_SERVER_PORT', 'Not set'),
        'STREAMLIT_SERVER_HEADLESS': os.getenv('STREAMLIT_SERVER_HEADLESS', 'Not set'),
        'HOME': os.getenv('HOME', 'Not set'),
    }
    
    for var, value in env_vars.items():
        st.text(f"{var}: {value}")


if __name__ == "__main__":
    show_diagnostics()
