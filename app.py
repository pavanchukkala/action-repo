#!/usr/bin/env python3
"""
Sample Python Application for GitHub Webhook Testing
This file is used to demonstrate push events and code changes.
"""

import json
from datetime import datetime

class SampleApp:
    def __init__(self, name="GitHub Webhook Test App"):
        self.name = name
        self.version = "1.0.0"
        self.created_at = datetime.now().isoformat()
    
    def get_info(self):
        """Return application information"""
        return {
            "name": self.name,
            "version": self.version,
            "created_at": self.created_at,
            "status": "running"
        }
    
    def process_data(self, data):
        """Process incoming data"""
        if not data:
            return {"error": "No data provided"}
        
        return {
            "processed": True,
            "data_type": type(data).__name__,
            "timestamp": datetime.now().isoformat()
        }

def main():
    """Main application entry point"""
    app = SampleApp()
    print(f"Starting {app.name} v{app.version}")
    
    # Sample data processing
    sample_data = {"message": "Hello from GitHub webhook test!"}
    result = app.process_data(sample_data)
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

