#!/usr/bin/env python
"""FileGuard FIM - File Integrity Monitoring System"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app import create_app

app = create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
