from flask import Flask, jsonify, request
from flask_cors import CORS
from bson.objectid import ObjectId
from .models import NumberSeries, AnalysisResult
from .utils import calculate_gcd, calculate_mean_std, find_primes
from .database import mongodb

app = Flask(__name__) 
CORS(app)

mongodb.connect()
    
@app.route('/')
def read_root():
    return jsonify({"message": "API Analizador de Series", "status": "active"})

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy",  "service": "backend"})

@app.route('/series', methods=['POST'])
def create_series():
    data = request.get_json()
    
    if not data or 'numbers' not in data:
        return jsonify({"error": "Datos inválidos"}), 400
    
    numbers = data['numbers']
    
    if not isinstance(numbers, list) or len(numbers) < 2:
        return jsonify({"error": "Se requieren al menos 2 números"}), 400
    
    for num in numbers:
        if not isinstance(num, int):
            return jsonify({"error": "Todos los elementos deben ser números enteros"}), 400
    
    series_obj = NumberSeries(numbers)
    
    result = mongodb.db.series.insert_one({
        "numbers": series_obj.numbers,
        "count": series_obj.count,
        "created_at": series_obj.created_at
    })
    
    return jsonify({
        "id": str(result.inserted_id),
        "numbers": series_obj.numbers,
        "message": "Serie creada exitosamente"
    })

@app.route('/series', methods=['GET'])
def get_all_series():
    series = list(mongodb.db.series.find().sort("created_at", -1))
    
    response = []
    for s in series:
        response.append({
            "id": str(s["_id"]),
            "numbers": s["numbers"],
            "count": s["count"],
            "created_at": s["created_at"].isoformat()
        })
    
    return jsonify(response)

@app.route('/series/<series_id>/analyze', methods=['GET'])
def analyze_series(series_id):
    if not ObjectId.is_valid(series_id):
        return jsonify({"error": "ID inválido"}), 400
    
    series = mongodb.db.series.find_one({"_id": ObjectId(series_id)})
    if not series:
        return jsonify({"error": "Serie no encontrada"}), 404
    
    numbers = series["numbers"]
    
    gcd = calculate_gcd(numbers)
    mean, std_dev = calculate_mean_std(numbers)
    primes = find_primes(numbers)
    
    result = AnalysisResult(series_id, gcd, mean, std_dev, primes)
    
    return jsonify({
        "series_id": result.series_id,
        "gcd": result.gcd,
        "mean": result.mean,
        "std_dev": result.std_dev,
        "primes": result.primes
    })
                    

                    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)                    