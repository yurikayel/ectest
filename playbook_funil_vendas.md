# Playbook — Funil de Vendas DNA Network × Explochip

Operação comercial da parceria. Complementa a Cláusula Quarta da [minuta do contrato](./minuta_contrato.md).

---

## 1. Visão geral do funil

```mermaid
flowchart LR
  A[Captação] --> B[Qualificação]
  B --> C[Diagnóstico]
  C --> D[Proposta]
  D --> E[Negociação]
  E --> F[Fechamento]
  F --> G[Handoff Engenharia]
  G --> H[Entrega e Pós-venda]
```

| Etapa | Responsável principal | SLA |
|-------|----------------------|-----|
| Captação | DNA Network | — |
| Qualificação | DNA Network | 24h úteis após lead |
| Diagnóstico técnico inicial | DNA + Explochip | 48h úteis |
| Proposta comercial | Explochip (valores) + DNA (formato) | 5 dias úteis |
| Negociação | DNA Network (comercial) | 48h entre contatos |
| Fechamento | DNA Network | Registro no CRM em 24h |
| Handoff engenharia | Explochip | Kick-off em 3 dias úteis |
| Pós-venda | DNA (relacionamento) + Explochip (técnico) | Follow-up 7/30/90 dias |

---

## 2. Critérios de qualificação (BANT simplificado)

Lead **qualificado** quando atender **mínimo 3 de 4**:

| Critério | Pergunta-chave |
|----------|----------------|
| **Budget** | Existe orçamento ou faixa de investimento definida? |
| **Authority** | Contato tem poder de decisão ou acesso ao decisor? |
| **Need** | Necessidade clara em um dos Segmentos I–IV? |
| **Timeline** | Projeto com início em até 6 meses? |

Leads **desqualificados** (arquivar com motivo): fora dos segmentos, sem orçamento em 12 meses, concorrente disfarçado, solicitação sem dados de contato válidos.

---

## 3. Qualificação por segmento

### Segmento I — Equipamentos (explosivos/defesa)

* **Perfil:** indústria de defesa, mineração, demolição, órgãos públicos.
* **Sinais:** equipamento customizado, requisitos civis/militares, firmware dedicado.
* **Handoff:** obrigatório engenheiro Explochip antes de proposta; verificar restrições de exportação/confidencialidade.

### Segmento II — Retrofit industrial

* **Perfil:** indústrias com máquinas obsoletas, painéis legados sem reposição nacional.
* **Sinais:** máquina parada, peça importada indisponível, manutenção recorrente cara.
* **Handoff:** fotos/vídeos do equipamento, modelo, ano, sintoma; visita técnica se ticket > R$ 30k.

### Segmento III — Automação e painéis

* **Perfil:** fábricas, integradores, OEMs que precisam de painel/comando eletrônico.
* **Sinais:** projeto elétrico/eletrônico, sem alteração mecânica concorrente ao cliente.
* **Atenção:** confirmar que a Explochip **não** competirá na parte mecânica do cliente.

### Segmento IV — Robotização (exclusivo)

* **Perfil:** linhas de produção, manipuladores, integração robótica ou similar.
* **Sinais:** automação de pick-and-place, redução de mão de obra, layout de célula robótica.
* **Prioridade:** segmento com exclusividade reforçada — priorizar no pipeline.

---

## 4. Handoff DNA → Explochip

Ao qualificar lead, DNA registra no CRM:

1. Dados do contato e empresa (CNPJ, segmento, cidade)
2. Resumo da necessidade (máx. 500 caracteres)
3. Segmento (I / II / III / IV)
4. Urgência e faixa de budget estimada
5. Anexos (fotos, PDFs, especificações)

**Explochip retorna:**

* Viabilidade técnica (sim / não / condicional)
* Prazo estimado de proposta
* Necessidade de visita técnica

Template de e-mail de handoff: assunto `[EXPLOCHIP-LEAD] {Empresa} — Seg {I-IV}`.

---

## 5. Atribuição e CRM

* Todo lead de campanha DNA deve ter **origem** e **data** no CRM antes do primeiro contato Explochip.
* Clientes da **base ativa Explochip** (lista na assinatura) não geram comissão se contato for direto — ver Cláusula Sétima da minuta.
* Renovações de projetos originados da parceria: mantêm comissão.

**CRM sugerido:** planilha compartilhada na fase inicial; migrar para ferramenta dedicada (HubSpot, Pipedrive ou similar) na revisão de 90 dias.

---

## 6. SLAs de comunicação

| Canal | Horário comercial | Tempo de resposta |
|-------|-------------------|-------------------|
| WhatsApp comercial | Seg–Sex 8h–18h | 4h úteis |
| E-mail | Seg–Sex | 24h úteis |
| Proposta técnica | — | 5 dias úteis após dados completos |
| Emergência (máquina parada) | Acordo prévio | 2h úteis (Explochip) |

---

## 7. Métricas do funil (reportar mensalmente)

* Leads captados por canal
* Taxa de qualificação (%)
* Propostas enviadas
* Taxa de conversão proposta → fechamento
* Ticket médio por segmento
* Ciclo médio de venda (dias)
* Pipeline aberto (valor estimado)

Relatório entregue até o **5º dia útil** de cada mês à Explochip.

---

## 8. Papéis resumidos

| Função | DNA Network | Explochip |
|--------|:-----------:|:---------:|
| Tráfego pago e conteúdo | ✓ | |
| Qualificação de leads | ✓ | Apoio técnico |
| Proposta comercial (preço) | Formatação | ✓ |
| Proposta técnica | | ✓ |
| Negociação comercial | ✓ | Suporte |
| Contrato com cliente final | | ✓ |
| Execução e entrega | | ✓ |
| NF e faturamento | | ✓ |
| Prestação de contas à DNA | | ✓ |
