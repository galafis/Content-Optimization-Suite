        async function analyzeContent() {
            const content = document.getElementById(\'contentText\').value.trim();
            const targetKeyword = document.getElementById(\'targetKeyword\').value.trim();
            
            if (!content) {
                alert(\'Please enter content to analyze\');
                return;
            }
            
            try {
                const response = await fetch(\'/api/analyze\', {
                    method: \'POST\',
                    headers: { \'Content-Type\': \'application/json\' },
                    body: JSON.stringify({ 
                        content: content,
                        target_keyword: targetKeyword || null
                    })
                });
                
                const analysis = await response.json();
                displayAnalysis(analysis);
                
                const suggestionsResponse = await fetch(\'/api/suggestions\', {
                    method: \'POST\',
                    headers: { \'Content-Type\': \'application/json\' },
                    body: JSON.stringify({ 
                        analysis: analysis,
                        target_keyword: targetKeyword || null
                    })
                });
                
                const suggestions = await suggestionsResponse.json();
                displaySuggestions(suggestions);
                
            } catch (error) {
                console.error(\'Analysis error:\', error);
                alert(\'Analysis failed. Please try again.\');
            }
        }
        
        function displayAnalysis(analysis) {
            document.getElementById(\'metricsContainer\').innerHTML = `
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
                        <div class="metric-label">Readability Score</div>
                    </div>
                </div>
            `;

            const seoScore = analysis.seo_score;
            let scoreClass = \'score-poor\';
            let scoreDescription = \'Needs significant improvement\';

            if (seoScore >= 80) {
                scoreClass = \'score-excellent\';
                scoreDescription = \'Excellent SEO Score!\';
            } else if (seoScore >= 50) {
                scoreClass = \'score-good\';
                scoreDescription = \'Good SEO Score, some improvements possible\';
            } else {
                scoreClass = \'score-poor\';
                scoreDescription = \'Needs significant SEO improvement\';
            }

            document.getElementById(\'seoScoreContainer\').innerHTML = `
                <div class="score-circle ${scoreClass}">${seoScore}</div>
                <p>${scoreDescription}</p>
            `;

            document.getElementById(\'keywordsContainer\').innerHTML = analysis.top_keywords.map(kw => `
                <span class="keyword-item">${kw[0]} (${kw[1]})</span>
            `).join(\'\');
        }

        function displaySuggestions(suggestions) {
            const suggestionsContainer = document.getElementById(\'suggestionsContainer\');
            if (suggestions.length === 0) {
                suggestionsContainer.innerHTML = 
                    \' <p style="text-align: center; color: #666; padding: 20px;">No specific suggestions at this time. Content looks good!</p>\';
                return;
            }
            suggestionsContainer.innerHTML = suggestions.map(s => `
                <div class="suggestion-item priority-${s.priority.toLowerCase()}">
                    <strong>${s.type}:</strong> ${s.suggestion} <br>
                    <small>Current: ${s.current} | Target: ${s.target}</small>
                </div>
            `).join(\'\');
        }

        function clearContent() {
            document.getElementById(\'contentText\').value = \'\';
            document.getElementById(\'targetKeyword\').value = \'\';
            document.getElementById(\'metricsContainer\').innerHTML = \'<p style="text-align: center; color: #666; padding: 40px;">Enter content and click "Analyze Content" to see metrics</p>\';
            document.getElementById(\'seoScoreContainer\').innerHTML = \'<div class="score-circle score-poor" id="scoreCircle">--</div><p id="scoreDescription">No analysis yet</p>\';
            document.getElementById(\'keywordsContainer\').innerHTML = \'<p style="text-align: center; color: #666;">Keywords will appear after analysis</p>\';
            document.getElementById(\'suggestionsContainer\').innerHTML = \'<p style="text-align: center; color: #666; padding: 20px;">Suggestions will appear after content analysis</p>\';
        }
