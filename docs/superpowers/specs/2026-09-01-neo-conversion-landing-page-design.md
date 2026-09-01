# NEO — Landing Page de Conversão | Design

Data: 2026-09-01

## Objetivo

Reconstruir a landing page de tráfego pago da NEO para maximizar cliques qualificados no WhatsApp oficial **+55 61 99874-5357**, usando como referência o que já funciona na página atual da clínica, mas com mensagem mais direta, hierarquia mais clara, menos distrações, melhor performance e instrumentação de conversão.

O sucesso não será tratado como promessa de aumento de conversão. A página será desenhada para melhorar a probabilidade de conversão e preparada para medição real por eventos e, futuramente, teste A/B.

## Diagnóstico da página atual de referência

A página de referência acerta em pontos importantes para tráfego:

- usa a intenção de busca exata “Otorrino na Asa Sul” já no topo;
- explicita consultas, exames, cirurgias e atendimento adulto/pediátrico;
- repete CTA de WhatsApp várias vezes;
- reforça Ed. Talento / Asa Sul / Brasília;
- dedica blocos a dores de alta intenção, como labirintite, tontura e cirurgia coclear;
- reduz a distância entre conteúdo e ação com botões “Agende Aqui / Quero Agendar”.

Problemas observados:

- texto excessivo e repetitivo;
- afirmações de superioridade que não devem ser reproduzidas sem comprovação;
- pouco uso de hierarquia visual orientada à conversão;
- pouca segmentação das mensagens de WhatsApp por dor/intenção;
- navegação que pode dispersar o usuário;
- ausência de instrumentação clara para comparar desempenho dos CTAs;
- oportunidade de melhorar velocidade e experiência mobile.

## Princípio da nova página

A landing page será tratada como **funil de agendamento**, não como site institucional.

Objetivo primário: clique no WhatsApp.

Objetivos secundários: consultar convênios, entender serviços, localizar a clínica e ligar para o telefone fixo.

## Estrutura proposta

### 1. Hero acima da dobra

Mensagem principal:

**Otorrino na Asa Sul, Brasília**

Subtítulo orientado à decisão:

**Consultas, exames e cirurgias em otorrinolaringologia para adultos e crianças. Atendimento na Asa Sul, no Ed. Talento.**

Faixa de confiança imediatamente abaixo:

- Adulto e Pediátrico
- Consultas, Exames e Cirurgias
- Particular e Convênios
- Ed. Talento · Asa Sul

CTA principal:

**Agendar pelo WhatsApp**

CTA secundário discreto:

**Consultar convênio**

O CTA principal deve aparecer sem necessidade de rolagem em desktop e mobile.

### 2. Seletor por sintoma/intenção

Título: **O que você precisa avaliar?**

Cards de alta intenção:

- Tontura e vertigem
- Zumbido e audição
- Ouvido tampado ou dor
- Rinite, sinusite e nariz entupido
- Garganta e voz
- Ronco e sono
- Atendimento infantil

Cada card abre WhatsApp com mensagem pré-preenchida específica.

### 3. Prova de capacidade de atendimento

Bloco curto e objetivo:

- Otorrinolaringologia
- Fonoaudiologia quando pertinente ao atendimento divulgado pela clínica
- Exames relacionados a audição e equilíbrio
- Cirurgias conforme indicação médica

Não usar frases como “melhor”, “maior”, “líder absoluto” ou promessa de resultado sem comprovação documental e validação da clínica.

### 4. Bloco principal de consulta

Mostrar claramente o que acontece na consulta e o que o paciente pode resolver a partir dela.

CTA: **Quero agendar uma consulta**.

### 5. Tontura / equilíbrio

Bloco de alta prioridade porque a página atual dá forte destaque ao tema.

Mensagem:

**Tontura não é tudo igual.**

Explicar de forma breve que vertigem, desequilíbrio e instabilidade podem ter causas distintas e exigem avaliação individualizada.

CTA com mensagem específica de tontura/vertigem.

### 6. Audição / zumbido

Sinais de alta intenção:

- dificuldade para compreender conversas;
- aumento frequente do volume;
- ouvido tampado;
- zumbido;
- perda auditiva percebida.

CTA específico.

### 7. Exames

Exibir os exames/áreas confirmados pela clínica. Não inventar nomes de exames não validados.

A seção deve reforçar conveniência e integração entre consulta e investigação diagnóstica, sem prometer diagnóstico imediato.

### 8. Cirurgia coclear

Conteúdo educativo curto, com linguagem condicional e indicação individualizada.

CTA: **Falar com a equipe sobre avaliação**.

### 9. Convênios

Trazer esta seção para antes da parte institucional final, porque cobertura é objeção de conversão.

CTA: **Confirmar meu convênio no WhatsApp**.

### 10. Sobre a NEO / confiança

Bloco curto, não institucional demais.

Usar apenas fatos confirmados pela clínica. Caso seja validado documentalmente que a NEO atua desde 2016, incluir a informação.

Incluir identificação obrigatória do estabelecimento e do diretor técnico conforme exigências do CFM quando os dados forem fornecidos/validados.

### 11. Localização

Mostrar:

**Ed. Talento — SEP/SUL, EQ 714/914 · Brasília — DF**

Telefone fixo atual: **(61) 3547-3607**

WhatsApp: **(61) 99874-5357**

Botões:

- Agendar pelo WhatsApp
- Como chegar

### 12. CTA final

Repetir a intenção de busca:

**Procurando otorrino na Asa Sul?**

CTA único e forte para WhatsApp.

## Navegação e distrações

A página não terá menu tradicional com múltiplos links externos. O objetivo é manter o usuário no fluxo de conversão.

No desktop poderá haver uma barra compacta com marca, telefone e CTA.

No mobile haverá CTA fixo de WhatsApp na parte inferior, sem cobrir conteúdo relevante.

## WhatsApp

Número oficial para todos os CTAs:

`5561998745357`

Mensagens devem ser específicas por origem do clique, por exemplo:

- consulta geral;
- tontura/vertigem;
- audição/zumbido;
- convênios;
- cirurgia coclear;
- pediatria;
- CTA final.

Isso reduz fricção e permite identificar a intenção do lead no primeiro contato.

## Instrumentação

Todos os CTAs terão identificador próprio em `data-track`.

Evento padrão:

`neo_cta_click`

Campos mínimos:

- `cta`
- `section`
- `pathname`
- `destination`

Preparar estrutura compatível com `dataLayer` para futura integração com Google Tag Manager / Google Ads, sem exigir a integração para a primeira publicação.

## SEO e tráfego pago

Título e H1 devem manter a correspondência com a intenção principal:

**Otorrino na Asa Sul | NEO**

A expressão “Otorrino na Asa Sul” deve aparecer de maneira natural no hero, conteúdo e CTA final, sem keyword stuffing.

Manter meta description local e objetiva.

## Performance

Requisitos:

- nenhuma imagem quebrada;
- hero carregado prioritariamente;
- imagens abaixo da dobra com lazy loading;
- ativos em formatos seguros para GitHub Pages;
- evitar arquivos binários corrompidos/truncados;
- CSS e JS mínimos;
- sem frameworks desnecessários;
- layout responsivo;
- ausência de dependências que bloqueiem renderização.

## Estratégia de imagens

As imagens existentes serão reaproveitadas somente se puderem ser publicadas e abertas corretamente pelo GitHub Pages.

Como o fluxo anterior corrompeu JPEGs durante upload pelo conector, a implementação deverá usar um formato de publicação verificado antes do deploy final. SVG com JPEG incorporado é aceitável como fallback técnico se preservar visual adequado e carregar corretamente no navegador.

## Compliance médico

A página deverá respeitar a Resolução CFM nº 2.336/2023.

Regras relevantes para o projeto:

- clínica deve exibir identificação do estabelecimento e diretor técnico em local visível quando esses dados forem disponibilizados;
- médicos identificados devem ter CRM e RQE quando aplicável;
- não atribuir superioridade, garantia de resultado ou capacidade privilegiada a médico/equipamento;
- linguagem sobre cirurgia e tratamentos deve ser educativa e condicional;
- imagens não devem induzir garantia de resultado.

Até que os dados regulatórios sejam validados pela clínica, não inventar CRM, RQE ou cadastro do estabelecimento.

## Testes obrigatórios antes de declarar publicação concluída

1. Abrir a URL pública do GitHub Pages e confirmar HTTP/HTML carregando.
2. Abrir diretamente cada ativo usado pela página.
3. Confirmar que nenhum `img` utilizado aponta para arquivo quebrado.
4. Confirmar que nenhum CTA de WhatsApp usa o número antigo `556135473607`.
5. Confirmar que todos os CTAs usam `5561998745357` e mantêm mensagem pré-preenchida.
6. Testar âncoras internas e botão de mapa.
7. Verificar layout em larguras mobile e desktop.
8. Confirmar presença de H1 único e estrutura de headings coerente.
9. Confirmar ausência de links vazios ou placeholders.
10. Verificar que a página pública corresponde ao commit da `main` após propagação.

## Critério de conclusão

A página só será considerada publicada quando o HTML público estiver acessível, as imagens carregarem diretamente pela URL pública e os CTAs de WhatsApp apontarem para o número oficial.

O desempenho de conversão deverá ser medido após início do tráfego. Não haverá alegação de “converte mais” sem dados comparativos; a implementação será otimizada para conversão e preparada para mensuração e teste A/B.