# Aula 21: Projeto final e portfólio pronto para recrutador

**Objetivo:** deixar o repositório com cara de portfólio profissional, ensaiar a apresentação de 5 minutos e mover as ferramentas de "Em estudo" para Competências no currículo.

**Tempo:** cerca de 4 horas.

## Revisão espaçada

Responda sem consultar. Errou alguma? Volte na aula indicada antes de continuar.

1. Diferença entre WHERE e HAVING. (Aula 08)
2. Diferença entre JOIN e LEFT JOIN. (Aula 09)
3. O que `CALCULATE` faz. (Aula 15)
4. Por que a mediana é melhor que a média nesta loja. (Aula 05)
5. Quando usar Power Query e quando usar VBA. (Aula 18)

## Analogia

O repositório é a **vitrine** da loja. O recrutador passa em frente com pressa: ele olha a vitrine por 30 segundos e decide se entra. A vitrine precisa mostrar os melhores produtos, com preço (resultado) à vista, e uma porta fácil de abrir.

Onde a analogia quebra: na vitrine não dá para provar o produto. No GitHub dá: o recrutador técnico vai abrir o código. Por isso ele precisa estar organizado e funcionando.

## Mão na massa

### Eu faço: o que o recrutador olha, em ordem

1. **README da raiz**: quem é você, o que sabe fazer, links dos projetos com uma frase de resultado cada.
2. **Um projeto**, geralmente o primeiro da lista: o README dele, as imagens, e talvez um arquivo de código.
3. **Histórico de commits**: constância (commits em várias semanas) conta mais que volume.

Ele raramente vai além disso. Então capriche nesses três.

### Fazemos juntos: o README da raiz

O `README.md` da raiz já tem uma estrutura pronta. Preencha:

- [ ] Uma frase de apresentação: quem você é e o que busca.
- [ ] Tabela de projetos: troque cada "a fazer" pelo resultado em uma frase. Ex.: "Encontrei R$ 27 mil em recebíveis não pagos pelas operadoras".
- [ ] Imagem de destaque do Projeto 3 (print do dashboard).
- [ ] Links para o Looker Studio e (se tiver) o Power BI publicado.
- [ ] Seu LinkedIn e e-mail.
- [ ] Apague a seção "Sobre este curso" ou mova-a para o fim.

Também no GitHub:
- [ ] No seu perfil (github.com/SEU-USUARIO), **fixe** (*pin*) este repositório.
- [ ] Na página do repositório, clique na engrenagem de **About** e escreva uma descrição curta e os *topics*: `sql`, `power-bi`, `python`, `pandas`, `data-analysis`, `excel`.

### Você faz

1. **Projeto final**: o `relatorio-2025.md` da Aula 20 junto com um link para cada projeto que sustenta os números.
2. **Apresentação de 5 minutos** (`projetos/projeto-final/roteiro-apresentacao.md`): o roteiro de uma fala que você usaria numa entrevista. Estrutura:
   - 30 s: quem você é e por que dados (a transição do hotel para dados é uma ótima história).
   - 3 min: um projeto, no formato **Problema → O que fiz → Resultado → O que aprendi**. A conciliação de recebíveis (Projeto 2) é forte, porque você conhece o problema por dentro.
   - 1 min: o que faria a seguir.
   - 30 s: perguntas.
3. Grave-se no celular apresentando. Assista uma vez e anote o que melhorar.

### Atualizar o currículo

Para cada ferramenta com projeto publicado, mova de "Em estudo" para Competências, usando a frase da tabela em `COMECE-AQUI.md`. Acrescente no cabeçalho o link do GitHub. Acrescente uma seção **Projetos** com 2 ou 3 linhas, por exemplo:

> **Conciliação de recebíveis (Python, pandas):** script que cruza 21 mil transações com os repasses das operadoras e identifica R$ 27 mil não pagos. github.com/SEU-USUARIO/analise-de-dados

Peça ajuda ao Claude para atualizar o arquivo `Curriculo_Natan_Donato_Analista_de_Dados.docx` com os projetos concluídos.

## Checagem final

Responda como se fosse numa entrevista (em voz alta, de preferência):

1. "Me conta um projeto de dados que você fez." (Use o roteiro.)
2. "Como você garante que os números estão certos?" (Dica: você conferiu o mesmo número em Excel, SQL, pandas e Power BI.)
3. "Qual ferramenta você mais gostou e por quê?"

## No seu portfólio

Commit: `Projeto final: relatório executivo e README do portfólio`. Marque tudo no `progresso-aprendizado.md`.

Parabéns: agora o "Em estudo" virou "Sei fazer, e aqui está a prova".
