# 🤖 Agente de Análise de Viabilidade Licitatória

Sistema automatizado para decisão de participação em licitações baseado em percentuais de prêmio.

---

## 📊 Visão Geral

Este projeto contém um agente inteligente que analisa licitações e decide automaticamente se a empresa deve participar, baseado em critérios objetivos de percentual de prêmio para equipes de background.

### 🎯 Regras de Negócio

| Faixa de Valor | Percentual Mínimo |
|----------------|-------------------|
| R$ 1M - R$ 5M | ≥ 7% |
| R$ 5M - R$ 10M | ≥ 6% |
| Acima de R$ 10M | ≥ 5% |

**Decisão:** Se percentual oferecido < mínimo → **NÃO PARTICIPA**

---

## 📁 Arquivos do Projeto

### 📄 Documentação

- **[RESPOSTAS_PERGUNTAS.md](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/RESPOSTAS_PERGUNTAS.md)** - Respostas às perguntas principais
  - ✅ Qual o objetivo do fluxo?
  - ✅ Qual problema ele resolve?
  - ✅ O que cada etapa faria?

- **[DOCUMENTACAO_AGENTE_PREMIO.md](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/DOCUMENTACAO_AGENTE_PREMIO.md)** - Documentação técnica completa
  - Detalhamento de cada etapa
  - 12 cenários demonstrativos
  - Justificativas dos percentuais

### 💻 Código Executável

- **[agente_premio_simplificado.py](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/agente_premio_simplificado.py)** - Código Python
  - Análise em < 1 segundo
  - 12 casos de teste
  - Relatórios automáticos

- **[agente_premio_simplificado.ipynb](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/agente_premio_simplificado.ipynb)** - Jupyter Notebook
  - Versão interativa
  - Pronto para Google Colab

### 🎨 Visualizações

- **[bpmn_agente_premio_simplificado.html](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/bpmn_agente_premio_simplificado.html)** - Diagrama BPMN
  - Fluxo visual interativo
  - Notação padrão BPMN 2.0

- **[dashboard_premio_percentual.html](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/dashboard_premio_percentual.html)** - Dashboard
  - 12 cenários demonstrados
  - Gráficos e métricas
  - Design profissional

---

## 🚀 Como Usar

### Opção 1: Python

```bash
# Clonar repositório
git clone https://github.com/laerciosantos09/Senac-SAPDPE.git

# Navegar para a pasta
cd Senac-SAPDPE

# Executar agente
python agente_premio_simplificado.py
```

### Opção 2: Jupyter Notebook

```bash
# Abrir notebook
jupyter notebook agente_premio_simplificado.ipynb
```

### Opção 3: Google Colab

1. Acesse: [agente_premio_simplificado.ipynb](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/agente_premio_simplificado.ipynb)
2. Clique em "Open in Colab"
3. Execute as células

### Opção 4: Ver Visualizações

Para ver os arquivos HTML (Dashboard e BPMN), você tem duas opções:

**A) Baixar e abrir localmente:**
1. Clique no arquivo HTML
2. Botão "Download" (ou Raw)
3. Abra no seu navegador

**B) Usar GitHub Pages (se ativado):**
- Dashboard: `https://laerciosantos09.github.io/Senac-SAPDPE/dashboard_premio_percentual.html`
- BPMN: `https://laerciosantos09.github.io/Senac-SAPDPE/bpmn_agente_premio_simplificado.html`

---

## 📊 Resultados Demonstrados

- **Total Analisado:** 12 licitações
- **✅ Aprovadas:** 9 (75%)
- **❌ Rejeitadas:** 3 (25%)
- **💰 Valor em Prêmios:** R$ 4.976.500

### Cenários por Faixa

#### 🟦 Faixa 1M-5M (Mínimo 7%)
- 4 licitações analisadas
- 3 aprovadas | 1 rejeitada
- Taxa de aprovação: 75%

#### 🟩 Faixa 5M-10M (Mínimo 6%)
- 4 licitações analisadas
- 3 aprovadas | 1 rejeitada
- Taxa de aprovação: 75%

#### 🟪 Faixa 10M+ (Mínimo 5%)
- 4 licitações analisadas
- 3 aprovadas | 1 rejeitada
- Taxa de aprovação: 75%

---

## 🎯 Funcionalidades

- ✅ Análise automatizada em < 1 segundo
- ✅ Critérios objetivos e transparentes
- ✅ Relatórios detalhados em JSON
- ✅ 100% executável e testado
- ✅ Documentação completa
- ✅ Dashboard interativo
- ✅ Diagrama BPMN visual

---

## 📖 Documentação Completa

### 📝 Respostas às Perguntas
👉 **[RESPOSTAS_PERGUNTAS.md](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/RESPOSTAS_PERGUNTAS.md)**

Contém respostas detalhadas para:
1. **Qual o objetivo do fluxo?**
2. **Qual problema ele resolve?**
3. **O que cada etapa do fluxo faria?**

### 📚 Documentação Técnica
👉 **[DOCUMENTACAO_AGENTE_PREMIO.md](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/DOCUMENTACAO_AGENTE_PREMIO.md)**

Inclui:
- Detalhamento de cada etapa do BPMN
- 12 cenários demonstrativos completos
- Justificativas dos percentuais mínimos
- Exemplos de uso
- Limitações e recomendações

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **Dataclasses** - Estruturas de dados
- **JSON** - Formato de relatórios
- **BPMN 2.0** - Notação de processos
- **HTML5/CSS3/JavaScript** - Dashboard e visualizações
- **Jupyter Notebook** - Ambiente interativo

---

## 📞 Informações do Projeto

**Projeto:** LicitBrain  
**Sistema:** Agente Simplificado de Análise por Percentual  
**Instituição:** Senac - SAPDPE  
**Versão:** 1.0  
**Data:** Novembro 2025  
**Autor:** Laércio Santos

---

## 🔗 Links Rápidos

| Recurso | Link |
|---------|------|
| 📦 Repositório | https://github.com/laerciosantos09/Senac-SAPDPE |
| 📝 Respostas | [RESPOSTAS_PERGUNTAS.md](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/RESPOSTAS_PERGUNTAS.md) |
| 📚 Documentação | [DOCUMENTACAO_AGENTE_PREMIO.md](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/DOCUMENTACAO_AGENTE_PREMIO.md) |
| 💻 Código Python | [agente_premio_simplificado.py](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/agente_premio_simplificado.py) |
| 📓 Jupyter | [agente_premio_simplificado.ipynb](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/agente_premio_simplificado.ipynb) |
| 🎨 Dashboard | [dashboard_premio_percentual.html](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/dashboard_premio_percentual.html) |
| 📊 BPMN | [bpmn_agente_premio_simplificado.html](https://github.com/laerciosantos09/Senac-SAPDPE/blob/main/bpmn_agente_premio_simplificado.html) |

---

## 📄 Licença

Este projeto é fornecido para fins educacionais e pode ser usado livremente com devida atribuição.

---

## ⭐ Próximos Passos

1. **Clone o repositório** e explore os arquivos
2. **Leia a documentação completa** para entender o funcionamento
3. **Execute os exemplos** para ver o agente em ação
4. **Customize** os percentuais conforme sua necessidade
5. **Adapte** para seu caso de uso específico

---

## 💡 Contribuições

Este projeto foi desenvolvido como parte do curso Senac SAPDPE. Sugestões e melhorias são bem-vindas!

---

**Happy Analyzing! 🎯**

---

## 📸 Preview

### Dashboard
![Dashboard Preview](https://via.placeholder.com/800x400/667eea/ffffff?text=Dashboard+Interativo)

### Fluxo BPMN
![BPMN Preview](https://via.placeholder.com/800x400/764ba2/ffffff?text=Diagrama+BPMN)

*Obs: Para visualizar os dashboards reais, acesse os arquivos HTML no repositório.*
