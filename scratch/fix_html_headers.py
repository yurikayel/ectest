import re

def fix_html():
    with open('contrato_parceria.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # The headers currently look like:
    # <h3>XIV. Disposições Gerais</h3> -> the text inside is Inadimplemento e Força Maior
    # Wait, let's just restore the correct headers based on their paragraph content.
    
    # We can use regex to match the paragraph content to identify the clause.
    replacements = [
        (r'<h3>.*?</h3>\s*<p>O presente contrato estabelece uma parceria', r'<h3>I. Do Objeto</h3>\n            <p>O presente contrato estabelece uma parceria'),
        (r'<h3>.*?</h3>\s*<ol>\s*<li><strong>Segmento I', r'<h3>II. Dos Segmentos de Atuação</h3>\n            <ol>\n                <li><strong>Segmento I'),
        (r'<h3>.*?</h3>\s*<ol>\s*<li>Gestão integral da estrutura e canais de marketing digital', r'<h3>III. Das Obrigações da DNA Network</h3>\n            <ol>\n                <li>Gestão integral da estrutura e canais de marketing digital'),
        (r'<h3>.*?</h3>\s*<ol>\s*<li>Execução de engenharia, garantia técnica', r'<h3>IV. Das Obrigações da Explochip</h3>\n            <ol>\n                <li>Execução de engenharia, garantia técnica'),
        (r'<h3>.*?</h3>\s*<p>Como contraprestação pelo acordo de parceria, a DNA Network receberá comissão', r'<h3>V. Do Comissionamento e Financeiro</h3>\n            <p>Como contraprestação pelo acordo de parceria, a DNA Network receberá comissão'),
        (r'<h3>.*?</h3>\s*<p>Fica pactuado que a comissão incidirá', r'<h3>VI. Da Universalidade do Faturamento</h3>\n            <p>Fica pactuado que a comissão incidirá'),
        (r'<h3>.*?</h3>\s*<p>A Explochip concorda em não contratar agências ou parceiros concorrentes', r'<h3>VII. Da Exclusividade</h3>\n            <p>A Explochip concorda em não contratar agências ou parceiros concorrentes'),
        (r'<h3>.*?</h3>\s*<p>A titularidade da marca "Explochip" permanece sob o domínio da Explochip', r'<h3>VIII. Propriedade Intelectual</h3>\n            <p>A titularidade da marca "Explochip" permanece sob o domínio da Explochip'),
        (r'<h3>.*?</h3>\s*<p>Compromisso de absoluto sigilo sobre informações tecnológicas', r'<h3>IX. Proteção de Dados (LGPD) e Sigilo</h3>\n            <p>Compromisso de absoluto sigilo sobre informações tecnológicas'),
        (r'<h3>.*?</h3>\s*<ol>\s*<li><strong>Duração:</strong> Fica estabelecido um período inicial de <strong>90 \(noventa\) dias', r'<h3>X. Do Período Inicial e de Alinhamento</h3>\n            <ol>\n                <li><strong>Duração:</strong> Fica estabelecido um período inicial de <strong>90 (noventa) dias'),
        (r'<h3>.*?</h3>\s*<p>O ciclo total da parceria é fixado em <strong>24 \(vinte e quatro\) meses', r'<h3>XI. Vigência e Revisões</h3>\n            <p>O ciclo total da parceria é fixado em <strong>24 (vinte e quatro) meses'),
        (r'<h3>.*?</h3>\s*<ol>\s*<li><strong>Livre Rescisão:</strong> O presente contrato', r'<h3>XII. Da Rescisão e Ausência de Multas</h3>\n            <ol>\n                <li><strong>Livre Rescisão:</strong> O presente contrato'),
        (r'<h3>.*?</h3>\s*<ol>\s*<li><strong>Inadimplemento:</strong> Em caso de descumprimento material', r'<h3>XIII. Do Inadimplemento e Força Maior</h3>\n            <ol>\n                <li><strong>Inadimplemento:</strong> Em caso de descumprimento material'),
        (r'<h3>.*?</h3>\s*<p>Modificações nas premissas contratuais apenas são reconhecidas por meio de aditivos', r'<h3>XIV. Disposições Gerais</h3>\n            <p>Modificações nas premissas contratuais apenas são reconhecidas por meio de aditivos'),
        (r'<h3>.*?</h3>\s*<p>Determina-se o <strong>Foro Regional I - Santana</strong>', r'<h3>XV. Foro e Mediação</h3>\n            <p>Determina-se o <strong>Foro Regional I - Santana</strong>'),
    ]
    
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text, count=1)
        
    with open('contrato_parceria.html', 'w', encoding='utf-8') as f:
        f.write(text)

fix_html()
print("Fixed!")
