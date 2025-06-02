#!/usr/bin/env python3
"""
Content Optimization Suite
Comprehensive content optimization and SEO analysis tool.
"""

from flask import Flask, render_template_string, jsonify, request
import re
from collections import Counter
import json

app = Flask(__name__)

class ContentOptimizer:
    def __init__(self):
        self.stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
        }
    
    def analyze_content(self, content, target_keyword=None):
        if not content:
            return {'error': 'No content provided'}
        
        # Basic metrics
        word_count = len(content.split())
        char_count = len(content)
        char_count_no_spaces = len(content.replace(' ', ''))
        paragraph_count = len([p for p in content.split('\n\n') if p.strip()])
        sentence_count = len(re.findall(r'[.!?]+', content))
        
        # Reading metrics
        avg_words_per_sentence = word_count / max(sentence_count, 1)
        
        # Keyword analysis
        words = re.findall(r'\b\w+\b', content.lower())
        filtered_words = [word for word in words if word not in self.stop_words and len(word) > 2]
        word_frequency = Counter(filtered_words)
        
        # SEO analysis
        seo_score = self.calculate_seo_score(content, target_keyword)
        
        # Readability score (simplified Flesch Reading Ease)
        avg_sentence_length = word_count / max(sentence_count, 1)
        readability_score = max(0, min(100, 206.835 - (1.015 * avg_sentence_length) - (84.6 * 1.5)))  # Simplified
        
        return {
            'word_count': word_count,
            'char_count': char_count,
            'char_count_no_spaces': char_count_no_spaces,
            'paragraph_count': paragraph_count,
            'sentence_count': sentence_count,
            'avg_words_per_sentence': round(avg_words_per_sentence, 1),
            'readability_score': round(readability_score, 1),
            'seo_score': seo_score,
            'top_keywords': word_frequency.most_common(10),
            'keyword_density': self.calculate_keyword_density(content, target_keyword) if target_keyword else 0
        }
    
    def calculate_seo_score(self, content, target_keyword=None):
        score = 0
        
        # Word count score (300-2000 words is optimal)
        word_count = len(content.split())
        if 300 <= word_count <= 2000:
            score += 25
        elif word_count > 100:
            score += 15
        
        # Paragraph structure
        paragraphs = [p for p in content.split('\n\n') if p.strip()]
        if len(paragraphs) >= 3:
            score += 20
        
        # Sentence variety
        sentences = re.findall(r'[.!?]+', content)
        if len(sentences) > 5:
            score += 15
        
        # Target keyword optimization
        if target_keyword:
            keyword_density = self.calculate_keyword_density(content, target_keyword)
            if 1 <= keyword_density <= 3:
                score += 25
            elif keyword_density > 0:
                score += 10
        else:
            score += 15  # Bonus for having content even without target keyword
        
        # Content structure indicators
        if re.search(r'\n#+\s', content):  # Headers
            score += 15
        
        return min(100, score)
    
    def calculate_keyword_density(self, content, keyword):
        if not keyword:
            return 0
        
        words = content.lower().split()
        keyword_count = content.lower().count(keyword.lower())
        total_words = len(words)
        
        return round((keyword_count / max(total_words, 1)) * 100, 2)
    
    def get_optimization_suggestions(self, analysis, target_keyword=None):
        suggestions = []
        
        # Word count suggestions
        if analysis['word_count'] < 300:
            suggestions.append({
                'type': 'Content Length',
                'priority': 'High',
                'suggestion': 'Increase content length to at least 300 words for better SEO',
                'current': f"{analysis['word_count']} words",
                'target': '300+ words'
            })
        elif analysis['word_count'] > 2000:
            suggestions.append({
                'type': 'Content Length',
                'priority': 'Medium',
                'suggestion': 'Consider breaking long content into multiple pages',
                'current': f"{analysis['word_count']} words",
                'target': '300-2000 words'
            })
        
        # Readability suggestions
        if analysis['readability_score'] < 60:
            suggestions.append({
                'type': 'Readability',
                'priority': 'Medium',
                'suggestion': 'Improve readability by using shorter sentences and simpler words',
                'current': f"{analysis['readability_score']} score",
                'target': '60+ score'
            })
        
        # Keyword density suggestions
        if target_keyword and analysis['keyword_density'] < 1:
            suggestions.append({
                'type': 'Keyword Optimization',
                'priority': 'High',
                'suggestion': f'Increase usage of target keyword "{target_keyword}"',
                'current': f"{analysis['keyword_density']}% density",
                'target': '1-3% density'
            })
        elif target_keyword and analysis['keyword_density'] > 3:
            suggestions.append({
                'type': 'Keyword Optimization',
                'priority': 'Medium',
                'suggestion': f'Reduce keyword stuffing for "{target_keyword}"',
                'current': f"{analysis['keyword_density']}% density",
                'target': '1-3% density'
            })
        
        # Structure suggestions
        if analysis['paragraph_count'] < 3:
            suggestions.append({
                'type': 'Content Structure',
                'priority': 'Medium',
                'suggestion': 'Break content into more paragraphs for better readability',
                'current': f"{analysis['paragraph_count']} paragraphs",
                'target': '3+ paragraphs'
            })
        
        if analysis['avg_words_per_sentence'] > 20:
            suggestions.append({
                'type': 'Sentence Length',
                'priority': 'Low',
                'suggestion': 'Use shorter sentences for better readability',
                'current': f"{analysis['avg_words_per_sentence']} words/sentence",
                'target': '15-20 words/sentence'
            })
        
        return suggestions

optimizer = ContentOptimizer()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Content Optimization Suite</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        .header { background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; }
        .content-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; }
        .card { background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        .full-width { grid-column: 1 / -1; }
        .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px; margin-bottom: 20px; }
        .metric-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; padding: 20px; text-align: center; }
        .metric-value { font-size: 1.8rem; font-weight: bold; margin-bottom: 5px; }
        .metric-label { font-size: 0.9rem; opacity: 0.9; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: 600; }
        .form-group input, .form-group textarea { width: 100%; padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 14px; }
        .form-group textarea { min-height: 200px; resize: vertical; font-family: inherit; }
        .btn { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: 600; margin: 5px 0; }
        .btn:hover { opacity: 0.9; }
        .suggestion-item { padding: 15px; border-left: 4px solid #667eea; margin-bottom: 15px; background: #f8f9fa; border-radius: 0 8px 8px 0; }
        .priority-high { border-left-color: #e74c3c; }
        .priority-medium { border-left-color: #f39c12; }
        .priority-low { border-left-color: #27ae60; }
        .keyword-item { display: inline-block; background: #e9ecef; padding: 5px 10px; margin: 3px; border-radius: 15px; font-size: 14px; }
        .score-circle { width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; margin: 0 auto 10px; }
        .score-excellent { background: linear-gradient(135deg, #27ae60, #2ecc71); color: white; }
        .score-good { background: linear-gradient(135deg, #f39c12, #e67e22); color: white; }
        .score-poor { background: linear-gradient(135deg, #e74c3c, #c0392b); color: white; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📝 Content Optimization Suite</h1>
            <p>Comprehensive content optimization and SEO analysis tool</p>
        </div>
        
        <div class="content-grid">
            <div class="card">
                <h3>✍️ Content Input</h3>
                <div class="form-group">
                    <label for="targetKeyword">Target Keyword (optional):</label>
                    <input type="text" id="targetKeyword" placeholder="e.g., digital marketing tips">
                </div>
                <div class="form-group">
                    <label for="contentText">Content to Analyze:</label>
                    <textarea id="contentText" placeholder="Paste your content here for analysis...">Digital marketing has become an essential component of modern business strategy. In today's competitive landscape, companies must leverage various digital channels to reach their target audience effectively.

Search engine optimization (SEO) plays a crucial role in digital marketing success. By optimizing content for search engines, businesses can improve their online visibility and attract more organic traffic to their websites.

Content marketing is another vital aspect of digital marketing. Creating valuable, relevant content helps establish brand authority and builds trust with potential customers. This approach focuses on providing useful information rather than directly promoting products or services.

Social media marketing allows businesses to engage with their audience on platforms where they spend significant time. Through strategic social media campaigns, companies can increase brand awareness and foster customer relationships.

Email marketing remains one of the most effective digital marketing channels, offering high ROI when executed properly. Personalized email campaigns can nurture leads and convert prospects into loyal customers.</textarea>
                </div>
                <button onclick="analyzeContent()" class="btn">🔍 Analyze Content</button>
                <button onclick="clearContent()" class="btn" style="background: #6c757d;">🗑️ Clear</button>
            </div>
            
            <div class="card">
                <h3>📊 Content Metrics</h3>
                <div id="metricsContainer">
                    <p style="text-align: center; color: #666; padding: 40px;">Enter content and click "Analyze Content" to see metrics</p>
                </div>
            </div>
        </div>
        
        <div class="content-grid">
            <div class="card">
                <h3>🎯 SEO Score</h3>
                <div id="seoScoreContainer" style="text-align: center;">
                    <div class="score-circle score-poor" id="scoreCircle">--</div>
                    <p id="scoreDescription">No analysis yet</p>
                </div>
            </div>
            
            <div class="card">
                <h3>🔤 Top Keywords</h3>
                <div id="keywordsContainer">
                    <p style="text-align: center; color: #666;">Keywords will appear after analysis</p>
                </div>
            </div>
        </div>
        
        <div class="card full-width">
            <h3>💡 Optimization Suggestions</h3>
            <div id="suggestionsContainer">
                <p style="text-align: center; color: #666; padding: 20px;">Suggestions will appear after content analysis</p>
            </div>
        </div>
    </div>

    <script>
        async function analyzeContent() {
            const content = document.getElementById('contentText').value.trim();
            const targetKeyword = document.getElementById('targetKeyword').value.trim();
            
            if (!content) {
                alert('Please enter content to analyze');
                return;
            }
            
            try {
                const response = await fetch('/api/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        content: content,
                        target_keyword: targetKeyword || null
                    })
                });
                
                const analysis = await response.json();
                displayAnalysis(analysis);
                
                // Get suggestions
                const suggestionsResponse = await fetch('/api/suggestions', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        analysis: analysis,
                        target_keyword: targetKeyword || null
                    })
                });
                
                const suggestions = await suggestionsResponse.json();
                displaySuggestions(suggestions);
                
            } catch (error) {
                console.error('Analysis error:', error);
                alert('Analysis failed. Please try again.');
            }
        }
        
        function displayAnalysis(analysis) {
            // Display metrics
            document.getElementById('metricsContainer').innerHTML = `
                <div class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-value">${analysis.word_count}</div>
                        <div class="metric-label">Words</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${analysis.char_count}</div>
                        <div class="metric-label">Characters</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${analysis.paragraph_count}</div>
                        <div class="metric-label">Paragraphs</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${analysis.sentence_count}</div>
                        <div class="metric-label">Sentences</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${analysis.avg_words_per_sentence}</div>
                        <div class="metric-label">Words/Sentence</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${analysis.readability_score}</div>
                        <div class="metric-label">Readability</div>
                    </div>
                </div>
            `;
            
            // Display SEO score
            const scoreCircle = document.getElementById('scoreCircle');
            const scoreDescription = document.getElementById('scoreDescription');
            
            scoreCircle.textContent = analysis.seo_score;
            
            if (analysis.seo_score >= 80) {
                scoreCircle.className = 'score-circle score-excellent';
                scoreDescription.textContent = 'Excellent SEO optimization';
            } else if (analysis.seo_score >= 60) {
                scoreCircle.className = 'score-circle score-good';
                scoreDescription.textContent = 'Good SEO optimization';
            } else {
                scoreCircle.className = 'score-circle score-poor';
                scoreDescription.textContent = 'Needs SEO improvement';
            }
            
            // Display keywords
            document.getElementById('keywordsContainer').innerHTML = analysis.top_keywords.map(([keyword, count]) => 
                `<span class="keyword-item">${keyword} (${count})</span>`
            ).join('');
        }
        
        function displaySuggestions(suggestions) {
            if (suggestions.length === 0) {
                document.getElementById('suggestionsContainer').innerHTML = 
                    '<p style="text-align: center; color: #27ae60; padding: 20px;">✅ Great! No major optimization issues found.</p>';
                return;
            }
            
            document.getElementById('suggestionsContainer').innerHTML = suggestions.map(suggestion => `
                <div class="suggestion-item priority-${suggestion.priority.toLowerCase()}">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <strong>${suggestion.type}</strong>
                        <span style="background: #667eea; color: white; padding: 2px 8px; border-radius: 12px; font-size: 12px;">
                            ${suggestion.priority} Priority
                        </span>
                    </div>
                    <div style="margin-bottom: 10px;">${suggestion.suggestion}</div>
                    <div style="font-size: 14px; color: #666;">
                        <strong>Current:</strong> ${suggestion.current} → <strong>Target:</strong> ${suggestion.target}
                    </div>
                </div>
            `).join('');
        }
        
        function clearContent() {
            document.getElementById('contentText').value = '';
            document.getElementById('targetKeyword').value = '';
            document.getElementById('metricsContainer').innerHTML = '<p style="text-align: center; color: #666; padding: 40px;">Enter content and click "Analyze Content" to see metrics</p>';
            document.getElementById('scoreCircle').textContent = '--';
            document.getElementById('scoreCircle').className = 'score-circle score-poor';
            document.getElementById('scoreDescription').textContent = 'No analysis yet';
            document.getElementById('keywordsContainer').innerHTML = '<p style="text-align: center; color: #666;">Keywords will appear after analysis</p>';
            document.getElementById('suggestionsContainer').innerHTML = '<p style="text-align: center; color: #666; padding: 20px;">Suggestions will appear after content analysis</p>';
        }
        
        // Auto-analyze demo content on page load
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(() => {
                document.getElementById('targetKeyword').value = 'digital marketing';
                analyzeContent();
            }, 1000);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/analyze', methods=['POST'])
def analyze_content():
    data = request.get_json()
    content = data.get('content', '')
    target_keyword = data.get('target_keyword')
    
    analysis = optimizer.analyze_content(content, target_keyword)
    return jsonify(analysis)

@app.route('/api/suggestions', methods=['POST'])
def get_suggestions():
    data = request.get_json()
    analysis = data.get('analysis', {})
    target_keyword = data.get('target_keyword')
    
    suggestions = optimizer.get_optimization_suggestions(analysis, target_keyword)
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

