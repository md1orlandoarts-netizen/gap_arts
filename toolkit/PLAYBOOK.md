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
- **Limite: 20 publicações por mês** (plano gratuito da Metricool) — nunca ultrapassar.
- Padrão **"posta, posta, folga"**: publicar em todo dia `d` do mês em que `d % 3 != 0`
  (1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29) até completar 20. Nunca dois dias seguidos sem post.
  Fevereiro: ajustar para 20 sem dois dias vazios seguidos.
- Horários alternados: **10:00** e **18:00** America/New_York.
- Outubro/2026 foi planejado à mão (ver `calendario/2026-10.csv`); o padrão começa em 2026-11-01.
- **Registro oficial dos posts: `calendario/AAAA-MM.csv`** (data,hora,peca,fonte_imagem,gancho,metricool_uuid).
  `getScheduledPosts` só mostra posts ainda não publicados, então o total do mês é contado por este arquivo.
- **Produção diária (rolante):** toda manhã, agendar os posts de hoje e dos próximos 2 dias que ainda não estiverem no
  calendário do mês, usando as imagens mais recentes do Drive (o ChatGPT envia ~5 por semana). Nunca criar posts de um mês
  antes do dia 1º desse mês. Se não houver nada a fazer, encerrar sem mensagem.

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
- Imagem em tela cheia, linda e emocional: pessoas felizes, céu azul, destinos variados.
- **Duas fontes, ALTERNADAS ao longo do mês** (decisão do cliente): imagens do ChatGPT em `banco/ia/` e fotos reais de bancos
  gratuitos (Pexels, Pixabay, Unsplash). Alternar post a post (IA, real, IA, real…), cerca de metade de cada.
- **Imagens do ChatGPT: pasta "Gap arts" no Google Drive** (fluxo ChatGPT → Google Drive → Claude; validado em 25/10/2026).
  - Pasta: id `1lK0Qnaq0zqMDYtQBCtb-TljKDEcU5_Tc` (conta md1orlandoarts@gmail.com), compartilhada como "qualquer pessoa com o link: leitor".
  - Listar com o conector Google Drive: `search_files` com `parentId = '1lK0Qnaq0zqMDYtQBCtb-TljKDEcU5_Tc' and mimeType contains 'image/'`.
  - Baixar cada arquivo com:
    `curl -sS -L -o arquivo "https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t"`
    e conferir com PIL (tamanho ≥ 1000 px de largura). Converter PNG para JPEG (qualidade 95) antes de usar no `make_art.py`.
  - `banco/ia/` no GitHub continua aceito como fonte secundária (o envio do GPT pelo GitHub corrompeu o primeiro teste).
  - Nomes esperados: `AAAA-MM-NN-tema.png/jpg`, fotografias puras (sem texto/logos), verticais, espaço livre no terço inferior.
  - **Nunca alterar, mover, renomear ou apagar** arquivos da pasta do Drive nem de `banco/ia/`. Registrar o uso em `banco/uso.csv`
    (colunas: arquivo,data_post,hora_post,gancho — para o Drive, use `drive:<FILE_ID>:<nome>` em "arquivo") e nunca reutilizar
    um arquivo já listado ali. Ignorar arquivos com "teste" no nome, exceto se o cliente pedir.
  - Usar primeiro os arquivos do mês corrente; depois os de meses anteriores ainda não usados.
  - Conferir cada imagem antes de usar: rejeitar rostos plásticos, mãos erradas, texto/logos visíveis ou baixa resolução
    (registrar a rejeição em `banco/uso.csv` com gancho = "REJEITADA: motivo").
  - Post com imagem do banco de IA: `instagramData.isAiGenerated = true` (exigência do Instagram).
  - Imagens de Disney/parques: evitar castelos, personagens e logos reconhecíveis em anúncios pagos; em posts orgânicos o cliente aceita.
- `banco/fotos/`: fotos próprias da GAP (isAiGenerated = false).
- Fotos reais de bancos gratuitos (Pexels, Pixabay, Unsplash): fazem parte da alternância (isAiGenerated = false).
  Nunca apresentar uma foto de banco como se fosse imagem entregue pelo ChatGPT, nem fingir que o banco de IA foi abastecido.
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
- `WebSearch` com `allowed_domains: ["pexels.com"]` ou `["pixabay.com"]`, ex.: "happy family beach vacation", "couple New York sunny".
- Baixar: `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=2000`
- Montar uma folha de contato e escolher as melhores (rostos felizes, luz bonita, céu azul). Não repetir fotos de meses anteriores.

## Falta de imagens do ChatGPT
Se `banco/ia/` tiver menos imagens válidas do que as vagas de IA do mês, completar essas vagas com fotos reais de bancos
gratuitos para manter os 20 posts bem distribuídos, e informar no resumo ao cliente quantas imagens de IA faltaram.
Ignorar arquivos de teste (ex.: `teste-upload-miniatura.jpg`).

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
