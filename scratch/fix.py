import re

def fix_minuta():
    with open('minuta_contrato.md', 'r', encoding='utf-8') as f:
        text = f.read()

    # The headers currently look like:
    # ### CLÁUSULA PRIMEIRA – DO OBJETO
    # ### Cláusula Primeira – DOS SEGMENTOS DE ATUAÇÃO
    # ### Cláusula Segunda – DAS OBRIGAÇÕES DA DNA NETWORK
    # ...
    # ### Cláusula Nona primeira – DA RESCISÃO E AUSÊNCIA DE MULTAS
    
    # Let's extract all sections starting with ###
    
    # Actually, let's just do a manual replacement list for the exact headers.
    headers = [
        ("### CLÁUSULA PRIMEIRA – DO OBJETO", "### CLÁUSULA PRIMEIRA – DO OBJETO"),
        ("### Cláusula Primeira – DOS SEGMENTOS DE ATUAÇÃO", "### CLÁUSULA SEGUNDA – DOS SEGMENTOS DE ATUAÇÃO"),
        ("### Cláusula Segunda – DAS OBRIGAÇÕES DA DNA NETWORK", "### CLÁUSULA TERCEIRA – DAS OBRIGAÇÕES DA DNA NETWORK"),
        ("### Cláusula Terceira – DAS OBRIGAÇÕES DA EXPLOCHIP", "### CLÁUSULA QUARTA – DAS OBRIGAÇÕES DA EXPLOCHIP"),
        ("### Cláusula Quarta – DO COMISSIONAMENTO E COMUNICAÇÃO FINANCEIRA", "### CLÁUSULA QUINTA – DO COMISSIONAMENTO E COMUNICAÇÃO FINANCEIRA"),
        ("### Cláusula Quinta – DA UNIVERSALIDADE DO FATURAMENTO", "### CLÁUSULA SEXTA – DA UNIVERSALIDADE DO FATURAMENTO"),
        ("### Cláusula Sexta – DA EXCLUSIVIDADE", "### CLÁUSULA SÉTIMA – DA EXCLUSIVIDADE"),
        ("### Cláusula Sétima – DA PROPRIEDADE INTELECTUAL E ATIVOS DIGITAIS", "### CLÁUSULA OITAVA – DA PROPRIEDADE INTELECTUAL E ATIVOS DIGITAIS"),
        ("### Cláusula Oitava – DA CONFIDENCIALIDADE E PROTEÇÃO DE DADOS (LGPD)", "### CLÁUSULA NONA – DA CONFIDENCIALIDADE E PROTEÇÃO DE DADOS (LGPD)"),
        ("### Cláusula Oitava – DO PERÍODO INICIAL E DE ALINHAMENTO", "### CLÁUSULA DÉCIMA – DO PERÍODO INICIAL E DE ALINHAMENTO"),
        ("### Cláusula Nona – DA VIGÊNCIA E REVISÕES", "### CLÁUSULA DÉCIMA PRIMEIRA – DA VIGÊNCIA E REVISÕES"),
        ("### Cláusula Nona primeira – DA RESCISÃO E AUSÊNCIA DE MULTAS", "### CLÁUSULA DÉCIMA SEGUNDA – DA RESCISÃO E AUSÊNCIA DE MULTAS"),
        ("### Cláusula Nona segunda – DO INADIMPLEMENTO E FORÇA MAIOR", "### CLÁUSULA DÉCIMA TERCEIRA – DO INADIMPLEMENTO E FORÇA MAIOR"),
        ("### Cláusula Nona terceira – DAS DISPOSIÇÕES GERAIS", "### CLÁUSULA DÉCIMA QUARTA – DAS DISPOSIÇÕES GERAIS"),
        ("### Cláusula Nona quarta – DO FORO E MEDIAÇÃO", "### CLÁUSULA DÉCIMA QUINTA – DO FORO E MEDIAÇÃO")
    ]
    
    for old, new in headers:
        text = text.replace(old, new)
        
    with open('minuta_contrato.md', 'w', encoding='utf-8') as f:
        f.write(text)

def fix_html():
    with open('contrato_parceria.html', 'r', encoding='utf-8') as f:
        text = f.read()
        
    headers = [
        "I. Do Objeto",
        "II. Dos Segmentos de Atuação",
        "III. Das Obrigações da DNA Network",
        "IV. Das Obrigações da Explochip",
        "V. Do Comissionamento e Financeiro",
        "VI. Da Universalidade do Faturamento",
        "VII. Da Exclusividade",
        "VIII. Propriedade Intelectual",
        "IX. Proteção de Dados (LGPD) e Sigilo",
        "X. Do Período Inicial e de Alinhamento",
        "XI. Vigência e Revisões",
        "XII. Da Rescisão e Ausência de Multas",
        "XIII. Do Inadimplemento e Força Maior",
        "XIV. Disposições Gerais",
        "XV. Foro e Mediação"
    ]
    
    # We know the current HTML has <h3>I. For all of them.
    # Let's replace <h3>I. sequentially.
    
    for header in headers:
        # replace the first occurrence of <h3>I. (Anything)
        text = re.sub(r'<h3>I\.\s*(.*?)</h3>', r'<h3>' + header + r'</h3>', text, count=1)
        
    with open('contrato_parceria.html', 'w', encoding='utf-8') as f:
        f.write(text)

fix_minuta()
fix_html()
print("Fixed!")
