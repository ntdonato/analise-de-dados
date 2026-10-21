# Projeto 3: Dashboard de vendas e metas no Power BI

> **Status:** a fazer. Depois de concluir, coloque aqui o print do dashboard e o resultado principal.

## Contexto
A gerência acompanhava metas numa planilha preenchida à mão. Este dashboard mostra, em uma página, se a meta está sendo batida, o que vende e quando vende, com filtros por ano e canal.

## O que o dashboard responde
- Estamos batendo a meta do mês e do ano?
- Como estamos em relação ao ano passado?
- Quais categorias e produtos puxam o faturamento? Com que margem?
- Em que dias e canais a loja vende mais?

## Modelo de dados
Modelo estrela com `fVendas`, `fItens` e `fMetas` ligadas a `dCalendario` e `dProdutos`.

![Modelo](modelo-estrela.png)

## Medidas DAX
Ver [`medidas.dax`](medidas.dax): Faturamento, Ticket Médio, % Meta, Faturamento AA, Var % AA, Acumulado Mês, Margem %.

## Ferramentas
Power BI Desktop · Power Query · DAX

## Arquivos
- `dashboard-vendas.pbix`: o arquivo do Power BI
- `dashboard.pdf`: exportação para quem não tem o Power BI
- `medidas.dax`: todas as medidas em texto

---
### Checklist antes de publicar
- [ ] Print do dashboard (`dashboard.png`) aqui no README
- [ ] `modelo-estrela.png` e `medidas.dax`
- [ ] `dashboard.pdf` exportado
- [ ] Títulos dos visuais com conclusões
- [ ] (Opcional) link do Publicar na Web
