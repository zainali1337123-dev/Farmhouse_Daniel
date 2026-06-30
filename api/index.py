import subprocess
import sys
import os

# Set environment variables for Streamlit
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_SERVER_PORT"] = "8501"
os.environ["STREAMLIT_SERVER_RUNONSAVE"] = "false"
os.environ["STREAMLIT_LOGGER_LEVEL"] = "info"

def handler(request):
    """Vercel serverless function to run Streamlit app"""
    
    # Get the directory where app.py is located
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_path = os.path.join(app_dir, "app.py")
    
    # Run Streamlit
    try:
        subprocess.Popen([
            sys.executable, 
            "-m", 
            "streamlit", 
            "run", 
            app_path,
            "--logger.level=error"
        ])
        
        return {
            "statusCode": 200,
            "body": "Streamlit app started"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
