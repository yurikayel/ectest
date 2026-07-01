import os
import re

# Update HTML File
html_path = 'contrato_parceria.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the formula and note
formula_old = "Comissão Devida = Valor Líquido da Nota Fiscal (Faturamento Total) × Percentual da Faixa Vigente"
formula_new = "Comissão Devida = Margem Líquida da Operação × Percentual da Faixa Vigente"

html = html.replace(formula_old, formula_new)

note_old = r"Nota: O valor líquido refere-se ao faturamento bruto deduzido dos impostos diretos incidentes sobre a venda. Não há dedução de custos de produção, peças ou mão de obra."
note_new = "Comissão devida: após dedução de custos de produção, peças, mão de obra e impostos."

html = re.sub(r'Nota: O valor líquido refere-se ao faturamento bruto deduzido dos impostos diretos incidentes sobre a venda\. Não há dedução de custos de produção, peças ou mão de obra\.', note_new, html)

# 2. Update Clause text
# "Comissão incidente diretamente sobre o Faturamento Total Líquido da Explochip do Brasil de cada operação"
html = re.sub(r'incidente diretamente sobre o <strong[^>]*>Faturamento Total Líquido da Explochip do Brasil</strong> de cada operação',
              'incidente diretamente sobre a <strong>Margem Líquida</strong> de cada operação', html)

# "incidirá sobre o Faturamento Total Líquido da Explochip do Brasil de todas as operações"
html = re.sub(r'incidirá sobre o <strong[^>]*>Faturamento Total Líquido da Explochip do Brasil de todas as operações e vendas da Explochip do Brasil</strong>',
              'incidirá sobre a <strong>Margem Líquida de todas as operações e vendas da Explochip do Brasil</strong>', html)

# 3. Rebuild the table in HTML
old_table = """                      <tr>
                          <th>Contexto</th>
                          <th class="text-right">Fat. Operação (R$)</th>
                          <th class="text-right">Fat. Acumulado (R$)</th>
                          <th>Escala</th>
                          <th class="text-right">Comissão DNA (R$)</th>
                      </tr>
                  </thead>
                  <tbody>
                      <tr>
                          <td><strong>Projeto 01</strong> (Faturamento Inicial)</td>
                          <td class="text-right">80.000,00</td>
                          <td class="text-right">80.000,00</td>
                          <td>3% (Faixa I)</td>
                          <td class="text-right"><strong>2.400,00</strong></td>
                      </tr>
                      <tr>
                          <td><strong>Projeto 02</strong> (Progressão)</td>
                          <td class="text-right">100.000,00</td>
                          <td class="text-right">180.000,00</td>
                          <td>5% (Faixa II)</td>
                          <td class="text-right"><strong>5.000,00</strong></td>
                      </tr>
                      <tr>
                          <td><strong>Projeto 03</strong> (Serviço ou Produto avulso)</td>
                          <td class="text-right">40.000,00</td>
                          <td class="text-right">220.000,00</td>
                          <td>5% (Faixa II - mantida)</td>
                          <td class="text-right"><strong>2.000,00</strong></td>
                      </tr>"""

new_table = """                      <tr>
                          <th>Contexto</th>
                          <th class="text-right">Receita NF</th>
                          <th class="text-right">Custos/Impostos</th>
                          <th class="text-right">Margem Líq.</th>
                          <th>Escala</th>
                          <th class="text-right">Comissão DNA</th>
                      </tr>
                  </thead>
                  <tbody>
                      <tr>
                          <td><strong>Proj 01</strong></td>
                          <td class="text-right">80.000,00</td>
                          <td class="text-right">-50.000,00</td>
                          <td class="text-right">30.000,00</td>
                          <td>3%</td>
                          <td class="text-right"><strong>900,00</strong></td>
                      </tr>
                      <tr>
                          <td><strong>Proj 02</strong></td>
                          <td class="text-right">100.000,00</td>
                          <td class="text-right">-60.000,00</td>
                          <td class="text-right">40.000,00</td>
                          <td>5%</td>
                          <td class="text-right"><strong>2.000,00</strong></td>
                      </tr>
                      <tr>
                          <td><strong>Proj 03</strong></td>
                          <td class="text-right">40.000,00</td>
                          <td class="text-right">-20.000,00</td>
                          <td class="text-right">20.000,00</td>
                          <td>5%</td>
                          <td class="text-right"><strong>1.000,00</strong></td>
                      </tr>"""
html = html.replace(old_table, new_table)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# Update minuta_contrato.md
md_path = 'minuta_contrato.md'
with open(md_path, 'r', encoding='utf-8') as f:
    md = f.read()

md = re.sub(r'incidente diretamente sobre o \*\*Faturamento Total Líquido da Explochip do Brasil\*\* de cada operação',
            'incidente diretamente sobre a **Margem Líquida** de cada operação', md)

md = re.sub(r'incidirá sobre o \*\*Faturamento Total Líquido da Explochip do Brasil de todas as operações e vendas da Explochip do Brasil\*\*',
            'incidirá sobre a **Margem Líquida de todas as operações e vendas da Explochip do Brasil**', md)

# We must explicitly define that the transparent accounting must include costs.
# Find: "Transparência Contábil: Disponibilização até o 10º"
# Replace with mention of costs.
md = re.sub(r'(2\. \*\*Transparência Contábil:\*\*.*?relatórios contábeis, notas fiscais emitidas no mês)',
            r'\1, incluindo o demonstrativo de custos de produção (peças, mão de obra e impostos)', md)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(md)

print("Updated HTML and MD main logic")
