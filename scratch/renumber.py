import re

def update_minuta():
    with open('minuta_contrato.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Clause 1
    content = re.sub(r'### CLÁUSULA PRIMEIRA – DAS DEFINIÇÕES\n\n.*?\n---\n\n', '', content, flags=re.DOTALL)
    
    # Update Objeto
    content = content.replace('em troca de participação percentual sobre o **Faturamento Total Bruto** da empresa.', 'em contrapartida à participação percentual sobre o faturamento da Explochip.')

    # Renumbering map
    num_map = {
        'SEGUNDA': 'PRIMEIRA',
        'TERCEIRA': 'SEGUNDA',
        'QUARTA': 'TERCEIRA',
        'QUINTA': 'QUARTA',
        'SEXTA': 'QUINTA',
        'SÉTIMA': 'SEXTA',
        'OITAVA': 'SÉTIMA',
        'NONA': 'OITAVA',
        'DÉCIMA PRIMEIRA': 'DÉCIMA',
        'DÉCIMA SEGUNDA': 'DÉCIMA PRIMEIRA',
        'DÉCIMA TERCEIRA': 'DÉCIMA SEGUNDA',
        'DÉCIMA QUARTA': 'DÉCIMA TERCEIRA',
        'DÉCIMA QUINTA': 'DÉCIMA QUARTA',
        'DÉCIMA SEXTA': 'DÉCIMA QUINTA',
        'DÉCIMA': 'NONA',
    }

    # First, we need to replace them carefully.
    # We should search for "CLÁUSULA X –" and replace
    for old, new in num_map.items():
        content = re.sub(rf'CLÁUSULA {old} –', f'CLÁUSULA {new} –', content)
        
    # Also fix any internal references like "Cláusula Sétima" -> "Cláusula Sexta", etc.
    for old, new in num_map.items():
        content = re.sub(rf'(?i)Cláusula {old}', f'Cláusula {new.capitalize()}', content)

    with open('minuta_contrato.md', 'w', encoding='utf-8') as f:
        f.write(content)


def update_html():
    with open('contrato_parceria.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Clause 1
    content = re.sub(r'<div class="clause">\s*<h3>I\. Das Definições</h3>.*?</ol>\s*</div>', '', content, flags=re.DOTALL)
    
    # Update Objeto
    content = content.replace('em contrapartida à participação percentual sobre o <strong>Faturamento Total Bruto</strong> da empresa.', 'em contrapartida à participação percentual sobre o <strong>faturamento da Explochip</strong>.')
    
    # Update Objeto if it was written without strong
    content = content.replace('em contrapartida à participação percentual sobre o Faturamento Total Bruto da empresa.', 'em contrapartida à participação percentual sobre o <strong>faturamento da Explochip</strong>.')

    num_map = {
        'XVI': 'XV',
        'XV': 'XIV',
        'XIV': 'XIII',
        'XIII': 'XII',
        'XII': 'XI',
        'XI': 'X',
        'X': 'IX',
        'IX': 'VIII',
        'VIII': 'VII',
        'VII': 'VI',
        'VI': 'V',
        'V': 'IV',
        'IV': 'III',
        'III': 'II',
        'II': 'I',
    }
    
    # Replace exactly <h3>X.
    for old, new in num_map.items():
        content = re.sub(rf'<h3>{old}\. ', f'<h3>{new}. ', content)

    with open('contrato_parceria.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_minuta()
update_html()
print("Done")
