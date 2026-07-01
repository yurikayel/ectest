import os
import re

files_to_update = [
    'decisoes_comissao.md',
    'anexo_comissionamento.md',
    'anexo_prestacao_contas.md'
]

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace residual "valor bruto" to "valor líquido"
    text = re.sub(r'(?i)valor bruto', 'valor líquido', text)
    # Also "Valor Bruto"
    text = re.sub(r'Valor Bruto', 'Valor Líquido', text)
    
    # In anexo_comissionamento.md
    # "Comissão Devida = Valor Bruto da Nota Fiscal (Faturamento Total) × Percentual da Faixa Vigente"
    # -> "Comissão Devida = Valor Líquido da Nota Fiscal (Faturamento Total) × Percentual da Faixa Vigente"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

# Also update the HTML formula box
with open('contrato_parceria.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'(?i)Valor Bruto da Nota Fiscal', 'Valor Líquido da Nota Fiscal', text)
with open('contrato_parceria.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Anexos update complete")
