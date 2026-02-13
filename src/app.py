from flask import Flask, jsonify, request

try:
    from content_optimizer import ContentAnalyzer
except ImportError:
    from src.content_optimizer import ContentAnalyzer

app = Flask(__name__)
analyzer = ContentAnalyzer()

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid or missing JSON body'}), 400
    content = data.get('content', '')
    target_keyword = data.get('target_keyword', None)
    analysis_result = analyzer.analyze(content, target_keyword)
    return jsonify(analysis_result)

@app.route('/api/suggestions', methods=['POST'])
def api_suggestions():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid or missing JSON body'}), 400
    analysis = data.get('analysis', {})
    target_keyword = data.get('target_keyword', None)
    suggestions = analyzer.get_optimization_suggestions(analysis, target_keyword)
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

