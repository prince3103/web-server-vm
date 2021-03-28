"""
This module imports app instance from app module and runs it.
"""
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000,debug=True)
