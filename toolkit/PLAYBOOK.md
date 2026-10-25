# GAP Mobile — Playbook de operação do Instagram (@gapcel)

Este é o roteiro que Claude segue para produzir e agendar os posts da GAP Mobile.
O briefing completo do cliente está em `BRIEFING.md` e tem prioridade sobre este arquivo.

## Objetivo
Vender eSIMs em **gapsim.com**. Toda publicação existe para levar a pessoa ao site.

## Contas
- Metricool: brand id **6967327** (Instagram @gapcel), fuso **America/New_York**.
- Plano gratuito da Metricool: **20 publicações por mês** — nunca ultrapassar.
- Hospedagem das artes: este repositório (`md1orlandoarts-netizen/gap_arts`, público).
  URL pública: `https://raw.githubusercontent.com/md1orlandoarts-netizen/gap_arts/main/<AAAA-MM>/<arquivo>.jpg`

## Calendário (regra fixa)
- 20 posts por mês no padrão **"posta, posta, folga"**: em um mês de 30 dias, publicar em todo dia `d` em que `d % 3 != 0`
  (1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29). Nunca dois dias seguidos sem post.
  Meses de 31 dias: o mesmo padrão; o dia 31 também é folga se o total já chegou a 20. Fevereiro: ajustar para 20 sem dois dias vazios seguidos.
- Horários alternados: **10:00** e **18:00** America/New_York (picos medidos na Metricool; = 12h/20h Brasília no horário padrão).
- Criar os posts de um mês **somente a partir do dia 1º desse mês** (a cota pode contar pela data de criação).
- Antes de criar, conferir com `getScheduledPosts` o que já existe no mês para não duplicar nem estourar o limite.

## Preços (obrigatório antes de cada arte com preço)
- Rodar `python3 check_prices.py` (lê os preços exibidos em gapsim.com).
- O gapsim.com busca os preços na loja Shopify md1travel.com. Se md1travel.com estiver acessível, conferir lá também.
- Referência lida em 25/10/2026: Pro USA $40 · Pro Europa $45 · Pro Global $65 · Controle USA $31 · Controle Europa $31 (USD).
  Planos Pro: "internet sem corte — 1GB por dia em alta velocidade*" com a nota
  "*Após o consumo diário de 1GB, a navegação continua conforme as condições do serviço."
  Controle USA: 5GB/15 dias ou 10GB/30 dias. Controle Europa: 5GB/10 dias ou 10GB/30 dias. Site: "1 a 30 dias", "+180 países",
  "não muda o número do WhatsApp", "ativação simples ao chegar".
- Se um preço mudou, usar o novo. Se não der para verificar, não publicar preço — usar um gancho sem preço.
- Nunca inventar desconto, oferta, cobertura ou compatibilidade.

## Padrão visual APROVADO pelo cliente (ver `2026-10/` e `variants_2026-10_ref.json`)
- Foto REAL em tela cheia (Pexels/Unsplash, uso comercial livre), pessoas felizes, céu azul, destinos variados
  (EUA, Europa, praia, neve, cidades, natureza, família, casal, amigos, viajante solo). Nada com aparência de IA.
- Tratamento de cor: `python3 grade.py foto.jpg photos/g_foto.jpg` (saturação realçada, céu mais azul).
- Moldura arco-íris nas cores da GAP, logo original no canto (arquivo `gap_logo_original.png`, nunca alterar),
  selo amarelo de preço, título Montserrat 900 com segunda linha em amarelo, subtítulo, 2–3 tags, botão branco com CTA, "gapsim.com".
- Gerar com `python3 make_art.py variants.json saida/` — cada variante: IMG, POS (object-position), SHADEH, H1 (tamanho),
  SEALB (altura do selo, ~700), CHIP, SEALTOP, PRICE, H1TXT, SUB, TAGS, CTA.
- Conferir visualmente cada arte (texto não pode encostar no selo nem cortar). O selo precisa bater com o plano citado
  (ex.: "Global" → $65; não usar $31 com Global).
- Evitar marcas registradas em destaque (castelo da Disney, logos de parques) principalmente em anúncios.
- O cliente detestou artes "duras"/tipográficas sem foto e o layout claro tipo site. Manter o padrão aprovado.

### Como achar fotos
- `WebSearch` com `allowed_domains: ["pexels.com"]`, ex.: "happy family beach vacation", "couple New York sunny".
- Baixar: `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=2000`
- Montar uma folha de contato e escolher as melhores (rostos felizes, luz bonita, céu azul). Não repetir fotos de meses anteriores.

## Variedade de ganchos (rodar entre eles; não repetir a mesma mensagem no mês)
Desembarque conectado · compartilhar ao vivo com quem ficou · família segura e conectada · mapa/transporte/Uber sem Wi-Fi ·
WhatsApp não muda de número (objeção nº 1) · como funciona em 3 passos · Europa vários países · Global +180 países ·
viagem a trabalho · férias escolares/fim de ano · "compre antes de embarcar" · Wi-Fi público inseguro/instável ·
dúvidas frequentes do site (troca de aparelho, mais de 30 dias → suporte).

## Legenda (PT-BR)
Gancho emocional → benefício concreto → lista curta (✓) com dados verificados → "A partir de US$ X" →
CTA para o **link da bio: gapsim.com** (links na legenda não são clicáveis) → nota do 1GB/dia quando citar plano Pro →
8–9 hashtags relevantes (sempre #eSIM e #GAPMobile). Nunca usar Direct como canal principal de venda.

## Agendamento
1. Salvar as artes em `<AAAA-MM>/gap_<AAAA-MM>_<NN>.jpg`, `git add`, commit, `git push origin main`.
2. Conferir que a URL raw responde 200 (image/jpeg).
3. `createScheduledPost` (blogId 6967327) com providers instagram, `instagramData.type = "POST"`, `autoPublish: true`,
   `isAiGenerated: false`, `publicationDate` em America/New_York, `mediaAltText` descritivo.
4. Ao final, mandar ao cliente um resumo: datas/horários, ganchos, preços usados e quantos dos 20 foram usados.

## Proibido
Alterar logotipo · inventar preços/descontos · estética de IA · misturar com agência de viagens · passar de 20 posts/mês ·
contratar planos pagos · mexer em campanhas Meta Ads, no site ou no checkout sem autorização expressa do cliente.
