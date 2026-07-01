import os

md_path = 'decisoes_comissao.md'

new_content = """# Histórico de Decisões: Comissionamento

Este documento registra as definições matemáticas e operacionais adotadas na minuta do contrato e no HTML final, refletindo o modelo de "Margem Líquida da Operação".

## 1. Premissas Matemáticas e Conceituais

| Variável | Definição no Contrato |
|----------|-----------------------|
| **Receita NF Acumulada (Global)** | As faixas (R$ 150k / 300k / 500k) medem a Receita de NF Bruta acumulada de todas as operações da Explochip, definindo o "nível" ou "escala" da comissão. |
| **Margem Líquida da Operação** | O percentual da faixa vigente é multiplicado pelo **Lucro da Operação**, não pelo faturamento. Isso exige dedução contábil rigorosa de cada NF. |
| **Custos Deduzidos** | Impostos incidentes sobre a venda, custos com peças, placas, insumos e horas técnicas de mão de obra de engenharia/desenvolvimento. |
| **Degrau (taxa única vigente)** | O percentual da faixa em que se encontra o faturamento acumulado **no momento do faturamento** aplica-se ao lucro integral daquela operação. |
| Exemplo | Com faturamento acumulado global de R$ 180.000, novas operações geram **5%** de comissão, mas os 5% são multiplicados apenas pelo valor que sobrar após o desconto dos custos do projeto. |

---

## 2. Checklist de Validação do Contrato (Versão Atual)

Abaixo estão os parâmetros que **já estão programados** na minuta e nos anexos:

| Parâmetro | Pendente | Aplicado | Comentário |
|-----------|:--------:|:--------:|------------|
| Faixas balizadas por Faturamento Global acumulado | ☐ | ✅ | |
| Comissão calculada sobre a Margem Líquida | ☐ | ✅ | |
| Escalonamento por degrau (taxa única vigente) | ☐ | ✅ | |
| Necessidade de prestação de contas dos custos | ☐ | ✅ | |
| Fundo de marketing (pós-90 dias): 5% do faturamento global | ☐ | ✅ | Mantido em 5% do Faturamento (NF) conforme acordado |

"""

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("decisoes_comissao.md rewritten")
