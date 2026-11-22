"""
Flask application entry point.

Loads the dataset and database, registers all routes, and runs the
development server. The analysis logic lives in the sibling modules
(analyzer, features, model_service, dataset, db).
"""

# ════════════════════════════════════════════════════════════════
# IMPORTS
# ════════════════════════════════════════════════════════════════

import os
from flask import Flask

# Local imports
import config
import dataset
import db
from routes import register_routes

# ════════════════════════════════════════════════════════════════
# APPLICATION INITIALIZATION
# ════════════════════════════════════════════════════════════════

app = Flask(__name__, static_folder=config.FRONTEND_DIR, static_url_path='')

# ════════════════════════════════════════════════════════════════
# STARTUP INITIALIZATION
# ════════════════════════════════════════════════════════════════

# Load the email dataset
dataset.load_dataset()

# Initialize database and schema
db.init_db()

# Register all HTTP routes
register_routes(app)

# ════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
