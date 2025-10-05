from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)
@app.route('/')
def read_root():
    return jsonify({"message": "API Analizador de Series", "status": "active"})

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy",  "service": "backend"})
                    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)                    