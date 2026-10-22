# Progresso de aprendizado

Data de início: 20/10/2026
Meta: 6 a 8 horas por semana, 12 semanas.

Atualize este arquivo no fim de cada aula e faça commit. O Claude (`/professor-tech`) lê este arquivo para saber onde você parou e o que revisar.

## Próximo passo
Aula 03: PROCX e SOMASES

## Aulas

| Aula | Tema | Concluída em | Checagem sem consultar? |
|---|---|---|---|
| 01 | Git e GitHub |20/10/2026 | parcial (commit × push) |
| 02 | Tabela dinâmica |21/10/2026 |sim |
| 03 | PROCX e SOMASES | | |
| 04 | Power Query | | |
| 05 | Média, mediana, outliers | | |
| 06 | Variação e correlação | | |
| 07 | SQL: SELECT e WHERE | | |
| 08 | SQL: GROUP BY | | |
| 09 | SQL: JOIN | | |
| 10 | SQL: CASE, CTE, janelas | | |
| 11 | pandas básico | | |
| 12 | groupby, merge, datas | | |
| 13 | Gráficos | | |
| 14 | Power BI: modelo estrela | | |
| 15 | DAX | | |
| 16 | Dashboard | | |
| 17 | Looker Studio | | |
| 18 | Macros | | |
| 19 | VBA com laços | | |
| 20 | Storytelling | | |
| 21 | Projeto final | | |

## Projetos

- [ ] P1: Análise de vendas em SQL
- [ ] P2: Conciliação de recebíveis em Python
- [ ] P3: Dashboard Power BI
- [ ] P4: Painel Looker Studio
- [ ] P5: Fechamento de caixa em VBA
- [ ] Projeto final: relatório e apresentação

## De "Em estudo" para Competências

- [ ] Git e GitHub
- [ ] Excel avançado
- [ ] Estatística descritiva
- [ ] SQL
- [ ] Python e pandas
- [ ] Power BI
- [ ] Looker Studio
- [ ] VBA
- [ ] Storytelling com dados

## Respostas das checagens

Escreva aqui, por aula, as respostas com suas palavras, antes de olhar o gabarito.

### Aula 01
1. Git e GitHub: ✅ certo. Um ajuste fino no vocabulário: o Git é a ferramenta (o programa) que faz o controle de versões, e o repositório é a pasta que ele acompanha. O GitHub é o site onde você publica e compartilha. Seu raciocínio estava certo.
2. Commit sem push: ❌ o recrutador não vê. Vou explicar de outro jeito:

🏠 Pense no fechamento de caixa. Você confere tudo e anota no seu caderno: isso é o commit, que fica registrado mas só com você. A gerência só fica sabendo quando você envia o relatório para o escritório: isso é o push. Até lá, o caderno pode estar perfeito, mas ninguém lá fora sabe o que tem nele.

Seu PC:   [commit] [commit] [commit]   ← só você vê
                       │
                     push
                       ▼
GitHub:   [commit] [commit] [commit]   ← o recrutador vê
3. Dados do hotel: ✅ certo. Dá para completar com mais dois pontos que pegam bem numa entrevista:

Esses dados têm informações de clientes (nomes, CPF, cartões), protegidas pela LGPD.
Publicar dados internos quebra a confidencialidade do seu contrato. Para um recrutador, isso é sinal de alerta, e não de experiência.

## Pontos fracos e dúvidas

Anote o que errou ou travou. Viram revisão nas aulas seguintes.

commit x push
duas pastas .git

### Aula 2

1. ✅ Certo, com um complemento. A Tabela é a base que alimenta a tabela dinâmica. O motivo principal de criá-la antes é que ela cresce sozinha: quando entram linhas novas (por exemplo, as vendas de 2026), elas passam a fazer parte de tbVendas automaticamente, e a tabela dinâmica enxerga os dados novos depois de um Atualizar. Com um intervalo comum (A1:H25316), as linhas novas ficariam de fora para sempre, sem ninguém perceber. Você viu isso na prática com a coluna dia_semana: ela só funcionou porque estava dentro da Tabela.

2. ✅ Certo. Um ajuste fino: o que se atualiza é a tabela dinâmica, porque é ela que tem a "foto" antiga. A Tabela de dados já está sempre em dia.

3. ✅ Muito boa resposta, com postura de analista. Você não concluiu "o Online fatura menos, então não vale a pena", e esse é exatamente o erro que o gerente esperaria de alguém sem experiência. Você percebeu que faltam dados (o custo do canal). E a sua tabela já traz um sinal importante. Veja o crescimento de 2024 para 2025:

Canal	 2024 →    2025	     Crescimento
Online	 95.963  → 106.130	   +10,6%
Recepção 169.012 → 179.449	   +6,2%
Loja	 967.119 → 1.023.873   +5,9%

O Online é o menor canal, mas é o que mais cresce, quase o dobro da Loja. Isso muda a conversa com o gerente: "O Online ainda é pequeno, mas está crescendo rápido. Para saber se vale a pena, preciso do custo dele (frete, taxa da plataforma)."


💡 Como você responderia ao gerente agora: "O Online é o canal que mais cresce (+10,6%), principalmente porque está atraindo mais clientes. Para saber se vale investir, preciso comparar com o custo do canal." Essa resposta é bem mais forte do que "ele fatura menos".

### Aula 3
