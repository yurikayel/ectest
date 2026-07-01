import os
import re

files_to_update = [
    'minuta_contrato.md',
    'contrato_parceria.html',
    'anexo_comissionamento.md',
    'anexo_prestacao_contas.md',
    'decisoes_comissao.md'
]

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Rename clause
    text = text.replace('Do Comissionamento e Comunicação Financeira', 'Do Comissionamento e Transparência Financeira')
    text = text.replace('DO COMISSIONAMENTO E COMUNICAÇÃO FINANCEIRA', 'DO COMISSIONAMENTO E TRANSPARÊNCIA FINANCEIRA')

    # 2. Remove the specific sentence
    # In Markdown: "* *Parágrafo primeiro (escalonamento):* Adota-se o método de **degrau**: o percentual da faixa vigente aplica-se integralmente ao Faturamento Bruto daquela operação faturada, até que a soma alcance o teto da faixa."
    text = re.sub(r'\* \*Parágrafo primeiro \(escalonamento\):\* Adota-se o método de \*\*degrau\*\*: o percentual da faixa vigente aplica-se integralmente ao Faturamento Bruto daquela operação faturada, até que a soma alcance o teto da faixa\.\n', '', text)
    # In HTML: "O percentual da faixa vigente aplica-se integralmente ao Faturamento Bruto daquela operação. "
    text = text.replace('O percentual da faixa vigente aplica-se integralmente ao Faturamento Bruto daquela operação. ', '')

    # 3. Replace Faturamento Total Bruto and Faturamento Bruto
    # Since we need to be redundant: "Faturamento Total Líquido (nunca Bruto) da Explochip do Brasil"
    target_phrase = "Faturamento Total Líquido (nunca Bruto) da Explochip do Brasil"
    
    text = re.sub(r'(?i)Faturamento Total Bruto', target_phrase, text)
    
    # After doing the Total Bruto, do any remaining Faturamento Bruto
    # We must be careful not to replace inside our target_phrase which has "(nunca Bruto)".
    # Our target phrase doesn't have "Faturamento Bruto", it has "Faturamento Total Líquido (nunca Bruto)".
    # So replacing "Faturamento Bruto" is safe.
    text = re.sub(r'Faturamento Bruto', target_phrase, text)
    text = re.sub(r'faturamento bruto', target_phrase, text)
    text = re.sub(r'faturamento da Explochip do Brasil', target_phrase, text)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print("Update complete")
