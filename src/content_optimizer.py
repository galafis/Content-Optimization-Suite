# -*- coding: utf-8 -*-
"""
Content Optimization Suite

Comprehensive content optimization and SEO analysis tool.
"""

import re
from collections import Counter

class ContentAnalyzer:
    """A class to analyze content for various metrics."""

    def __init__(self):
        """Initializes the ContentAnalyzer with a set of English stop words."""
        self.stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
        }

    def analyze(self, content, target_keyword=None):
        """
        Analyzes the given content and returns a dictionary of metrics.

        Args:
            content (str): The text content to analyze.
            target_keyword (str, optional): The target keyword for SEO analysis. Defaults to None.

        Returns:
            dict: A dictionary containing various content metrics.
        """
        if not content:
            return {'error': 'No content provided'}

        words = re.findall(r'\b\w+\b', content.lower())
        word_count = len(words)

        sentence_count = len(re.findall(r'[.!?]+', content))

        analysis_result = {
            'word_count': word_count,
            'char_count': len(content),
            'char_count_no_spaces': len(content.replace(' ', '')),
            'paragraph_count': len([p for p in content.split('\n\n') if p.strip()]),
            'sentence_count': sentence_count,
            'avg_words_per_sentence': round(word_count / max(sentence_count, 1), 1),
            'readability_score': self.calculate_readability(word_count, sentence_count),
            'seo_score': self.calculate_seo_score(content, target_keyword, word_count),
            'top_keywords': self.get_top_keywords(content),
            'keyword_density': self.calculate_keyword_density(content, target_keyword) if target_keyword else 0
        }
        return analysis_result

    def get_top_keywords(self, content):
        """
        Identifies the most common keywords in the content.

        Args:
            content (str): The text content.

        Returns:
            list: A list of tuples with the top 10 keywords and their frequencies.
        """
        words = re.findall(r'\b\w+\b', content.lower())
        filtered_words = [word for word in words if word not in self.stop_words and len(word) > 2]
        return Counter(filtered_words).most_common(10)

    def calculate_readability(self, word_count, sentence_count):
        """
        Calculates a simplified Flesch Reading Ease score.

        Args:
            word_count (int): The total number of words.
            sentence_count (int): The total number of sentences.

        Returns:
            float: The readability score.
        """
        if sentence_count == 0:
            return 0.0
        avg_sentence_length = word_count / sentence_count
        # Simplified Flesch Reading Ease formula
        score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * 1.5) 
        return round(max(0, min(100, score)), 1)

    def calculate_seo_score(self, content, target_keyword, word_count):
        """
        Calculates an SEO score based on various content attributes.

        Args:
            content (str): The text content.
            target_keyword (str): The target keyword.
            word_count (int): The total number of words.

        Returns:
            int: The calculated SEO score (0-100).
        """
        score = 0
        if 300 <= word_count <= 2000:
            score += 25
        elif word_count > 100:
            score += 15

        if len([p for p in content.split('\n\n') if p.strip()]) >= 3:
            score += 20

        if len(re.findall(r'[.!?]+', content)) > 5:
            score += 15

        if target_keyword:
            keyword_density = self.calculate_keyword_density(content, target_keyword)
            if 1 <= keyword_density <= 3:
                score += 25
            elif keyword_density > 0:
                score += 10
        else:
            score += 15

        if re.search(r'\n#+\s', content):
            score += 15

        return min(100, score)

    def calculate_keyword_density(self, content, keyword):
        """
        Calculates the density of a keyword in the content.

        Args:
            content (str): The text content.
            keyword (str): The keyword to analyze.

        Returns:
            float: The keyword density in percentage.
        """
        if not keyword:
            return 0
        
        all_words = re.findall(r'\b\w+\b', content.lower())
        keyword_count = all_words.count(keyword.lower())
        total_words = len(all_words)
        return round((keyword_count / max(total_words, 1)) * 100, 2)

    def get_optimization_suggestions(self, analysis, target_keyword=None):
        """
        Generates optimization suggestions based on the content analysis.

        Args:
            analysis (dict): The analysis results from the `analyze` method.
            target_keyword (str, optional): The target keyword. Defaults to None.

        Returns:
            list: A list of dictionaries, each representing a suggestion.
        """
        suggestions = []
        if analysis['word_count'] < 300:
            suggestions.append({
                'type': 'Content Length',
                'priority': 'High',
                'suggestion': 'Increase content length to at least 300 words for better SEO',
                'current': f"{analysis['word_count']} words",
                'target': '300+ words'
            })

        if analysis['readability_score'] < 60:
            suggestions.append({
                'type': 'Readability',
                'priority': 'Medium',
                'suggestion': 'Improve readability by using shorter sentences and simpler words',
                'current': f"{analysis['readability_score']} score",
                'target': '60+ score'
            })

        if target_keyword and analysis['keyword_density'] < 1:
            suggestions.append({
                'type': 'Keyword Optimization',
                'priority': 'High',
                'suggestion': f'Increase usage of target keyword "{target_keyword}"',
                'current': f"{analysis['keyword_density']}% density",
                'target': '1-3% density'
            })

        if analysis['paragraph_count'] < 3:
            suggestions.append({
                'type': 'Content Structure',
                'priority': 'Medium',
                'suggestion': 'Break content into more paragraphs for better readability',
                'current': f"{analysis['paragraph_count']} paragraphs",
                'target': '3+ paragraphs'
            })

        return suggestions

