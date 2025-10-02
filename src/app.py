from flask import Flask, send_from_directory, jsonify, request
from content_optimizer import ContentAnalyzer

app = Flask(__name__, static_folder=\'../docs\', static_url_path=\'\')
analyzer = ContentAnalyzer()

@app.route(\'/\')
def index():
    return send_from_directory(app.static_folder, \'index.html\')

@app.route(\'/api/analyze\', methods=[\'POST\'])
def api_analyze():
    data = request.get_json()
    content = data.get(\'content\', \'\')
    target_keyword = data.get(\'target_keyword\', None)
    analysis_result = analyzer.analyze(content, target_keyword)
    return jsonify(analysis_result)

@app.route(\'/api/suggestions\', methods=[\'POST\'])
def api_suggestions():
    data = request.get_json()
    analysis = data.get(\'analysis\', {})
    target_keyword = data.get(\'target_keyword\', None)
    suggestions = analyzer.get_optimization_suggestions(analysis, target_keyword)
    return jsonify(suggestions)

if __name__ == \'__main__\':
    app.run(debug=True, host=\'0.0.0.0\', port=5000)

