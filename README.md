# Content Optimization Suite

[English](#english) | [Português](#português)

---

## English

### 🖼️ Hero Image

![Hero Image](assets/hero_image.png)

### Badges
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=flat-square&logo=flask&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-blueviolet?style=flat-square&logo=nltk&logoColor=white)
![TextStat](https://img.shields.io/badge/TextStat-orange?style=flat-square)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-green?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-1.x-red?style=flat-square&logo=pandas&logoColor=white)
![License](https://img.shields.io/github/license/galafis/Content-Optimization-Suite?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/galafis/Content-Optimization-Suite?style=flat-square)

### Overview
Comprehensive content optimization suite built with Python and Flask. Features advanced content analysis, SEO scoring, readability assessment, and optimization recommendations for creating search engine friendly content.

### Features
- **Content Analysis**: Detailed text analysis and metrics
- **SEO Scoring**: Content SEO score calculation
- **Readability Assessment**: Flesch-Kincaid and other readability scores
- **Keyword Optimization**: Keyword density and distribution analysis
- **Meta Tag Optimization**: Title and description optimization
- **Content Suggestions**: AI-powered content improvement recommendations
- **Competitor Analysis**: Compare content with competitors
- **Performance Tracking**: Monitor content performance over time

### Architecture Diagram
![Architecture Diagram](assets/architecture_diagram.png)

### Technologies Used
- **Python 3.8+**
- **Flask**: Web framework and dashboard
- **NLTK**: Natural language processing
- **TextStat**: Readability analysis
- **BeautifulSoup**: HTML content parsing
- **Pandas**: Data analysis and reporting

### Installation

1. Clone the repository:
```bash
git clone https://github.com/galafis/Content-Optimization-Suite.git
cd Content-Optimization-Suite
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/app.py
```

4. Open your browser to `http://localhost:5000`

### Usage

#### Web Interface
1. **Content Input**: Paste or upload content for analysis
2. **Target Keywords**: Specify primary and secondary keywords
3. **Analysis Options**: Select analysis depth and metrics
4. **Generate Report**: Create comprehensive optimization report
5. **Apply Suggestions**: Implement recommended improvements

#### API Endpoints

**Analyze Content**
```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"content": "Your content here", "keywords": ["SEO", "content optimization"]}'
```

**Get SEO Score**
```bash
curl -X POST http://localhost:5000/api/seo-score \
  -H "Content-Type: application/json" \
  -d '{"content": "Your content", "target_keyword": "SEO optimization"}'
```

#### Python API
```python
from content_optimizer import ContentOptimizer

# Initialize optimizer
optimizer = ContentOptimizer()

# Analyze content
content = "Your article content here..."
analysis = optimizer.analyze_content(
    content=content,
    target_keywords=["SEO", "content marketing"],
    url="https://example.com/article"
)

print(f"SEO Score: {analysis['seo_score']}/100")
print(f"Readability: {analysis['readability_score']}")
print(f"Word Count: {analysis['word_count']}")
```

### Content Analysis Features

#### Text Metrics
- **Word Count**: Total words in content
- **Character Count**: Total characters including spaces
- **Paragraph Count**: Number of paragraphs
- **Sentence Count**: Total sentences
- **Average Sentence Length**: Words per sentence
- **Reading Time**: Estimated reading time

#### SEO Analysis
- **Keyword Density**: Primary keyword frequency
- **Keyword Distribution**: Keyword placement analysis
- **Title Optimization**: Title tag SEO assessment
- **Meta Description**: Description optimization check
- **Header Structure**: H1, H2, H3 tag analysis
- **Internal Links**: Internal linking opportunities

#### Readability Assessment
- **Flesch Reading Ease**: Readability score (0-100)
- **Flesch-Kincaid Grade**: Grade level requirement
- **Gunning Fog Index**: Complexity measurement
- **SMOG Index**: Simple Measure of Gobbledygook
- **Automated Readability Index**: ARI score
- **Coleman-Liau Index**: Character-based readability

### Optimization Recommendations

#### Content Structure
- **Header Optimization**: Improve heading structure
- **Paragraph Length**: Optimize paragraph sizes
- **Sentence Variety**: Improve sentence length variation
- **Transition Words**: Add connecting phrases
- **Bullet Points**: Use lists for better readability
- **White Space**: Improve content formatting

#### SEO Improvements
- **Keyword Placement**: Optimize keyword positioning
- **Semantic Keywords**: Add related terms
- **Meta Tags**: Improve title and description
- **Image Alt Text**: Optimize image descriptions
- **URL Structure**: Improve URL readability
- **Schema Markup**: Add structured data

#### Content Quality
- **Depth Analysis**: Content comprehensiveness
- **Expertise Signals**: Authority and expertise indicators
- **Freshness**: Content update recommendations
- **User Intent**: Match content to search intent
- **Call-to-Action**: Improve conversion elements
- **Mobile Optimization**: Mobile-friendly content

### Competitor Analysis

#### Content Comparison
- **Content Length**: Compare word counts
- **Keyword Usage**: Competitor keyword analysis
- **Content Structure**: Header and formatting comparison
- **Topic Coverage**: Content depth analysis
- **Performance Metrics**: Ranking and traffic comparison

#### Gap Analysis
- **Missing Topics**: Identify content gaps
- **Keyword Opportunities**: Underused keywords
- **Content Formats**: Missing content types
- **User Questions**: Unanswered user queries
- **Semantic Coverage**: Related topic analysis

### Performance Tracking

#### Content Metrics
- **Search Rankings**: Track keyword positions
- **Organic Traffic**: Monitor traffic changes
- **Click-Through Rates**: CTR improvements
- **Bounce Rate**: User engagement metrics
- **Time on Page**: Content engagement time
- **Social Shares**: Social media performance

#### Optimization Impact
- **Before/After Analysis**: Pre and post optimization comparison
- **Score Improvements**: SEO score changes over time
- **Ranking Changes**: Position improvements
- **Traffic Growth**: Organic traffic increases
- **Conversion Rates**: Goal completion improvements

### Content Templates

#### Blog Posts
- **Introduction Structure**: Engaging opening templates
- **Body Organization**: Content flow templates
- **Conclusion Format**: Effective closing templates
- **CTA Placement**: Call-to-action positioning

#### Product Pages
- **Product Descriptions**: SEO-optimized descriptions
- **Feature Highlights**: Benefit-focused content
- **Technical Specifications**: Structured product details
- **Customer Reviews**: Review integration templates

#### Landing Pages
- **Headline Formulas**: High-converting headlines
- **Value Propositions**: Clear benefit statements
- **Social Proof**: Testimonial and review placement
- **Conversion Elements**: Form and button optimization

### Configuration
Configure optimization settings in `config.json`:
```json
{
  "analysis_settings": {
    "min_word_count": 300,
    "target_keyword_density": 2.5,
    "max_sentence_length": 20,
    "readability_target": 60
  },
  "seo_settings": {
    "title_length": [30, 60],
    "meta_description_length": [120, 160],
    "header_structure": true,
    "internal_links": true
  },
  "reporting": {
    "include_suggestions": true,
    "competitor_analysis": true,
    "export_format": "pdf"
  }
}
```

### Integration
- **WordPress**: Plugin for WordPress optimization
- **Google Analytics**: Performance tracking integration
- **Search Console**: Search performance data
- **Content Management**: CMS platform integration

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Português

### 🖼️ Imagem Hero

![Imagem Hero](assets/hero_image.png)

### Badges
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=flat-square&logo=flask&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-blueviolet?style=flat-square&logo=nltk&logoColor=white)
![TextStat](https://img.shields.io/badge/TextStat-orange?style=flat-square)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-green?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-1.x-red?style=flat-square&logo=pandas&logoColor=white)
![License](https://img.shields.io/github/license/galafis/Content-Optimization-Suite?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/galafis/Content-Optimization-Suite?style=flat-square)

### Visão Geral
Suite abrangente de otimização de conteúdo construída com Python e Flask. Apresenta análise avançada de conteúdo, pontuação SEO, avaliação de legibilidade e recomendações de otimização para criar conteúdo amigável aos mecanismos de busca.

### Funcionalidades
- **Análise de Conteúdo**: Análise detalhada de texto e métricas
- **Pontuação SEO**: Cálculo de score SEO do conteúdo
- **Avaliação de Legibilidade**: Scores Flesch-Kincaid e outros de legibilidade
- **Otimização de Palavras-chave**: Análise de densidade e distribuição de palavras-chave
- **Otimização de Meta Tags**: Otimização de título e descrição
- **Sugestões de Conteúdo**: Recomendações de melhoria de conteúdo com IA
- **Análise de Concorrentes**: Comparar conteúdo com concorrentes
- **Rastreamento de Performance**: Monitorar performance do conteúdo ao longo do tempo

### Diagrama de Arquitetura
![Diagrama de Arquitetura](assets/architecture_diagram.png)

### Tecnologias Utilizadas
- **Python 3.8+**
- **Flask**: Framework web e dashboard
- **NLTK**: Processamento de linguagem natural
- **TextStat**: Análise de legibilidade
- **BeautifulSoup**: Parsing de conteúdo HTML
- **Pandas**: Análise de dados e relatórios

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/galafis/Content-Optimization-Suite.git
cd Content-Optimization-Suite
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python src/app.py
```

4. Abra seu navegador em `http://localhost:5000`

### Uso

#### Interface Web
1. **Entrada de Conteúdo**: Cole ou faça upload de conteúdo para análise
2. **Palavras-chave Alvo**: Especifique palavras-chave primárias e secundárias
3. **Opções de Análise**: Selecione a profundidade e métricas de análise
4. **Gerar Relatório**: Crie um relatório abrangente de otimização
5. **Aplicar Sugestões**: Implemente as melhorias recomendadas

#### Endpoints da API

**Analisar Conteúdo**
```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"content": "Seu conteúdo aqui", "keywords": ["SEO", "otimização de conteúdo"]}'
```

**Obter Pontuação SEO**
```bash
curl -X POST http://localhost:5000/api/seo-score \
  -H "Content-Type: application/json" \
  -d '{"content": "Seu conteúdo", "target_keyword": "otimização SEO"}'
```

#### API Python
```python
from content_optimizer import ContentOptimizer

# Inicializar otimizador
otimizer = ContentOptimizer()

# Analisar conteúdo
content = "Seu artigo aqui..."
analysis = optimizer.analyze_content(
    content=content,
    target_keywords=["SEO", "marketing de conteúdo"],
    url="https://example.com/article"
)

print(f"Pontuação SEO: {analysis['seo_score']}/100")
print(f"Legibilidade: {analysis['readability_score']}")
print(f"Contagem de Palavras: {analysis['word_count']}")
```

### Recursos de Análise de Conteúdo

#### Métricas de Texto
- **Contagem de Palavras**: Total de palavras no conteúdo
- **Contagem de Caracteres**: Total de caracteres incluindo espaços
- **Contagem de Parágrafos**: Número de parágrafos
- **Contagem de Frases**: Total de frases
- **Comprimento Médio da Frase**: Palavras por frase
- **Tempo de Leitura**: Tempo estimado de leitura

#### Análise SEO
- **Densidade de Palavras-chave**: Frequência da palavra-chave primária
- **Distribuição de Palavras-chave**: Análise de posicionamento de palavras-chave
- **Otimização de Título**: Avaliação SEO da tag de título
- **Meta Descrição**: Verificação de otimização da descrição
- **Estrutura de Cabeçalho**: Análise de tags H1, H2, H3
- **Links Internos**: Oportunidades de linkagem interna

#### Avaliação de Legibilidade
- **Flesch Reading Ease**: Pontuação de legibilidade (0-100)
- **Flesch-Kincaid Grade**: Nível de escolaridade exigido
- **Gunning Fog Index**: Medida de complexidade
- **SMOG Index**: Medida Simples de Gíria
- **Automated Readability Index**: Pontuação ARI
- **Coleman-Liau Index**: Legibilidade baseada em caracteres

### Recomendações de Otimização

#### Estrutura de Conteúdo
- **Otimização de Cabeçalho**: Melhorar a estrutura de títulos
- **Comprimento do Parágrafo**: Otimizar o tamanho dos parágrafos
- **Variedade de Frases**: Melhorar a variação do comprimento das frases
- **Palavras de Transição**: Adicionar frases de conexão
- **Marcadores**: Usar listas para melhor legibilidade
- **Espaço em Branco**: Melhorar a formatação do conteúdo

#### Melhorias de SEO
- **Posicionamento de Palavras-chave**: Otimizar o posicionamento de palavras-chave
- **Palavras-chave Semânticas**: Adicionar termos relacionados
- **Meta Tags**: Melhorar título e descrição
- **Texto Alternativo de Imagem**: Otimizar descrições de imagem
- **Estrutura de URL**: Melhorar a legibilidade da URL
- **Marcação de Esquema**: Adicionar dados estruturados

#### Qualidade do Conteúdo
- **Análise de Profundidade**: Abrangência do conteúdo
- **Sinais de Expertise**: Indicadores de autoridade e expertise
- **Freshness**: Recomendações de atualização de conteúdo
- **Intenção do Usuário**: Corresponder conteúdo à intenção de busca
- **Chamada para Ação**: Melhorar elementos de conversão
- **Otimização Móvel**: Conteúdo amigável para dispositivos móveis

### Análise de Concorrentes

#### Comparação de Conteúdo
- **Comprimento do Conteúdo**: Comparar contagem de palavras
- **Uso de Palavras-chave**: Análise de palavras-chave de concorrentes
- **Estrutura de Conteúdo**: Comparação de cabeçalho e formatação
- **Cobertura de Tópicos**: Análise de profundidade do conteúdo
- **Métricas de Performance**: Comparação de ranking e tráfego

#### Análise de Lacunas
- **Tópicos Ausentes**: Identificar lacunas de conteúdo
- **Oportunidades de Palavras-chave**: Palavras-chave subutilizadas
- **Formatos de Conteúdo**: Tipos de conteúdo ausentes
- **Perguntas do Usuário**: Perguntas de usuários não respondidas
- **Cobertura Semântica**: Análise de tópicos relacionados

### Rastreamento de Performance

#### Métricas de Conteúdo
- **Rankings de Busca**: Rastrear posições de palavras-chave
- **Tráfego Orgânico**: Monitorar mudanças de tráfego
- **Taxas de Cliques**: Melhorias de CTR
- **Taxa de Rejeição**: Métricas de engajamento do usuário
- **Tempo na Página**: Tempo de engajamento do conteúdo
- **Compartilhamentos Sociais**: Performance em mídias sociais

#### Impacto da Otimização
- **Análise Antes/Depois**: Comparação pré e pós otimização
- **Melhorias de Pontuação**: Mudanças na pontuação SEO ao longo do tempo
- **Mudanças de Ranking**: Melhorias de posição
- **Tráfego Crescimento**: Aumentos de tráfego orgânico
- **Taxas de Conversão**: Melhorias na conclusão de metas

### Modelos de Conteúdo

#### Posts de Blog
- **Estrutura de Introdução**: Modelos de abertura envolventes
- **Organização do Corpo**: Modelos de fluxo de conteúdo
- **Formato de Conclusão**: Modelos de fechamento eficazes
- **Posicionamento de CTA**: Posicionamento de chamada para ação

#### Páginas de Produto
- **Descrições de Produto**: Descrições otimizadas para SEO
- **Destaques de Recursos**: Conteúdo focado em benefícios
- **Especificações Técnicas**: Detalhes estruturados do produto
- **Avaliações de Clientes**: Modelos de integração de avaliações

#### Páginas de Destino
- **Fórmulas de Títulos**: Títulos de alta conversão
- **Proposições de Valor**: Declarações claras de benefícios
- **Prova Social**: Posicionamento de depoimentos e avaliações
- **Elementos de Conversão**: Otimização de formulários e botões

### Configuração
Configure as configurações de otimização em `config.json`:
```json
{
  "analysis_settings": {
    "min_word_count": 300,
    "target_keyword_density": 2.5,
    "max_sentence_length": 20,
    "readability_target": 60
  },
  "seo_settings": {
    "title_length": [30, 60],
    "meta_description_length": [120, 160],
    "header_structure": true,
    "internal_links": true
  },
  "reporting": {
    "include_suggestions": true,
    "competitor_analysis": true,
    "export_format": "pdf"
  }
}
```

### Integração
- **WordPress**: Plugin para otimização de WordPress
- **Google Analytics**: Integração de rastreamento de performance
- **Search Console**: Dados de performance de busca
- **Gerenciamento de Conteúdo**: Integração com plataforma CMS

### Contribuindo
1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/nova-feature`)
3. Faça seus commits (`git commit -am 'Adicionar nova feature'`)
4. Envie para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

