import pandas as pd

# TODAS AS 65 TRTs OFICIAIS REGISTRADAS NO CFT (2018 - 2026) + PROJETOS EXECUTIVOS
todos_os_registros = [
    # --- PÁGINA 1 ---
    {
        "id_doc": "2018110811440", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Força",
        "titulo": "Projeto Elétrico de Alimentação de Motobombas e Iluminação (86 kW)",
        "cliente_empresa": "M.R. Comercial & Logística Ltda", "cidade": "Santos/SP", "ano": 2018,
        "descricao": "Dimensionamento de alimentadores para motobombas, diagramas unifilar e multifilar, memorial de cálculo, bayface do painel elétrico e lista de materiais.",
        "normas_atendidas": "NBR 5410 / NR-10", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "2018110812061", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Luminotécnica",
        "titulo": "Projeto Luminotécnico Industrial (340.529 LM)",
        "cliente_empresa": "M.R. Comercial & Logística Ltda", "cidade": "Santos/SP", "ano": 2018,
        "descricao": "Cálculo luminotécnico para quantitativo de luminárias com lâmpadas a vapor metálico de 250W de sobrepor.",
        "normas_atendidas": "NBR ISO/CIE 8995-1", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20190030992", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Construção e Execução de Fachada em Alvenaria",
        "cliente_empresa": "Deise Will de Melo Mendes", "cidade": "São Vicente/SP", "ano": 2019,
        "descricao": "Condução e execução de alvenaria estrutural e revestimento de fachada frontal em residência unifamiliar (45 m²).",
        "normas_atendidas": "NBR 6118 / NBR 16280", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20190128359", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Hospitalar",
        "titulo": "Projeto Elétrico de Unidade Hospitalar USAFA Princesa (73 kVA)",
        "cliente_empresa": "M.R. Comercial & Logística", "cidade": "Praia Grande/SP", "ano": 2019,
        "descricao": "Projeto elétrico para área da saúde: planta baixa, diagrama unifilar/multifilar, memorial de cálculo e distribuição trifásica T4.",
        "normas_atendidas": "NBR 5410 / NBR 13534", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 2 ---
    {
        "id_doc": "BR20190144516", "tipo": "TRT", "conselho": "CFT", "disciplina": "Telecomunicações",
        "titulo": "Projeto de Cabeamento Estruturado e Rede Lógica (740m)",
        "cliente_empresa": "M.R. Comercial & Logística", "cidade": "Praia Grande/SP", "ano": 2019,
        "descricao": "Detalhamento de salas de telecomunicações (ER, MC, TR), distribuição de pontos de rede, eletrocalhas e diagrama lógico para CFTV e dados.",
        "normas_atendidas": "ANSI/TIA-568 / ISO 11801", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20190148180", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Infraestrutura",
        "titulo": "Projeto Elétrico de Praça Pública e Iluminação Urbana (36.14 kVA)",
        "cliente_empresa": "M.R. Comercial & Logística", "cidade": "Itanhaém/SP", "ano": 2019,
        "descricao": "Elaboração de projeto elétrico de praça pública: entrada de energia em baixa tensão trifásica (T2), diagramas e distribuição.",
        "normas_atendidas": "NBR 5410 / NBR 5101", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20190195872", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Laudos",
        "titulo": "Relatório Técnico e Levantamento de Infraestrutura Elétrica (600A)",
        "cliente_empresa": "Secretaria Municipal da Educação", "cidade": "Praia Grande/SP", "ano": 2019,
        "descricao": "Coleta de dados técnicos, memorial de carga, vistoria em quadros de medição e aterramento de 600A.",
        "normas_atendidas": "NBR 5410 / NR-10", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 3 ---
    {
        "id_doc": "BR20190213976", "tipo": "TRT", "conselho": "CFT", "disciplina": "Hidráulica / Saneamento",
        "titulo": "Projeto Hidrossanitário de Água Fria e Esgoto",
        "cliente_empresa": "M.R. Comercial & Logística", "cidade": "Itapetininga/SP", "ano": 2019,
        "descricao": "Projeto técnico de rede de esgoto sanitário, ligação de água fria e instalação de medidores de água (20 m³).",
        "normas_atendidas": "NBR 5626 / NBR 8160", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20190235911", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Impermeabilização com Manta Asfáltica Líquida",
        "cliente_empresa": "OGMO - Porto de Santos", "cidade": "Santos/SP", "ano": 2019,
        "descricao": "Reforma e recuperação de telhado com aplicação de manta asfáltica líquida para garantia de estanqueidade.",
        "normas_atendidas": "NBR 9575 / NR-35", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20190251994", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Hospitalar",
        "titulo": "Projeto Elétrico Executivo - Unidade USAFA Princesa",
        "cliente_empresa": "Prefeitura de Praia Grande", "cidade": "Praia Grande/SP", "ano": 2019,
        "descricao": "Projeto executivo elétrico de baixa tensão (73 kVA), painel elétrico geral e padrão de medição hospitalar.",
        "normas_atendidas": "NBR 5410 / NBR 13534", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20190332718", "tipo": "TRT", "conselho": "CFT", "disciplina": "Hidráulica / Predial",
        "titulo": "Projeto Hidráulico, Sanitário e Pluvial - Unidade CEMAS",
        "cliente_empresa": "Prefeitura de Praia Grande", "cidade": "Praia Grande/SP", "ano": 2019,
        "descricao": "Projeto hidráulico executivo para o Centro de Especializações Médicas de Praia Grande (Água, Esgoto e Drenagem Pluvial).",
        "normas_atendidas": "NBR 5626 / NBR 10844", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 4 ---
    {
        "id_doc": "BR20190383456", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Reforma e Adequação Estrutural de Ambientes Internos (78.49 m²)",
        "cliente_empresa": "OGMO - Porto de Santos", "cidade": "Santos/SP", "ano": 2019,
        "descricao": "Execução de demolição controlada, reforma de salas administrativas e adequação de alvenaria em equipe.",
        "normas_atendidas": "NBR 16280 / NR-18", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20200510390", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Execução de Fachada de Residência Multifamiliar",
        "cliente_empresa": "Eduardo Ferreira Leite", "cidade": "São Vicente/SP", "ano": 2020,
        "descricao": "Condução e execução de alvenaria e revestimento externo de fachada residencial multifamiliar (38 m²).",
        "normas_atendidas": "NBR 6118 / NBR 13755", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20200593216", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Medidas de Segurança Contra Incêndio - Centro Esportivo / Academia",
        "cliente_empresa": "Jessica Flavio dos Santos", "cidade": "Praia Grande/SP", "ano": 2020,
        "descricao": "Dimensionamento de extintores, sinalização de rota de fuga e blocos autônomos de iluminação de emergência.",
        "normas_atendidas": "IT Bombeiros SP / NBR 12693", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 5 ---
    {
        "id_doc": "BR20200700390", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Entrada de Energia",
        "titulo": "Construção e Dimensionamento de Padrão de Entrada (18 kW)",
        "cliente_empresa": "Elvis Presley Pontes da Silva", "cidade": "Itariri/SP", "ano": 2020,
        "descricao": "Dimensionamento de carga, cálculo de condutores de entrada e instalação de padrão de energia homologado.",
        "normas_atendidas": "NBR 5410 / Normas da Concessionária", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20200725209", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Aplicação de Material Antichamas em Portas e Áreas Comuns (126.72 m²)",
        "cliente_empresa": "Condomínio Edifício Pamphilli", "cidade": "Santos/SP", "ano": 2020,
        "descricao": "Reforma condominial com pintura e aplicação de verniz retardante de chamas nas portas de acesso e rotas de escape.",
        "normas_atendidas": "IT-10 Bombeiros SP / NBR 9442", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20200759506", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Projeto de Segurança Contra Incêndio - Oficina Mecânica",
        "cliente_empresa": "Raimundo Carlos da Silva Goncalves", "cidade": "Praia Grande/SP", "ano": 2020,
        "descricao": "Projeto técnico de PPCI para oficina mecânica: extintores de pó químico e CO2, blocos de iluminação e sinalização fotoluminescente.",
        "normas_atendidas": "IT-11 / IT-20 Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20200844746", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Entrada de Energia",
        "titulo": "Projeto de Reforma de Padrão de Entrada Agrupado (39.5 kW)",
        "cliente_empresa": "Jean Paulo Monks das Neves", "cidade": "Santos/SP", "ano": 2020,
        "descricao": "Dimensionamento de medição agrupada em baixa tensão (34.36 kVA), malha de aterramento e verificação das instalações.",
        "normas_atendidas": "GED-13 CPFL / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 6 ---
    {
        "id_doc": "BR20200862481", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Reforma Residencial e Assentamento de Revestimentos",
        "cliente_empresa": "Carolina Scarelli Costa Pitombeira", "cidade": "Barueri/SP", "ano": 2020,
        "descricao": "Execução de reforma em alvenaria e substituição de revestimentos cerâmicos e bancadas de cozinha.",
        "normas_atendidas": "NBR 16280 / NBR 13753", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "BR20211520062", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Predial",
        "titulo": "Lançamento de Prumada Elétrica Predial - Residencial Marati",
        "cliente_empresa": "JN Marques Participações Societárias", "cidade": "São Vicente/SP", "ano": 2021,
        "descricao": "Substituição e lançamento de nova prumada elétrica de condutores unifilares para alimentação de unidade residencial.",
        "normas_atendidas": "NBR 5410 / NR-10", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2201882822", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Construção de Fachada e Padrão de Entrada Tipo C1 (23 kVA)",
        "cliente_empresa": "Icaro Nunes de Andrade", "cidade": "Santos/SP", "ano": 2022,
        "descricao": "Execução técnica de alvenaria de fachada e padrão de entrada de energia homologado CPFL Tipo C1.",
        "normas_atendidas": "GED-13 CPFL / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2201909430", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Padrão de Entrada Tipo C1 com Ancoragem de Roldana 200 DAN",
        "cliente_empresa": "Icaro Nunes de Andrade", "cidade": "Santos/SP", "ano": 2022,
        "descricao": "Substituição de TRT com cálculo de carga de tração mecânica para roldana olhal de 200 DAN em fachada comercial.",
        "normas_atendidas": "GED-13 CPFL", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 7 ---
    {
        "id_doc": "CFT2202257362", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Regularização Contra Incêndio - Comércio Varejista Pet Shop (C-2)",
        "cliente_empresa": "Comércio Varejista de Animais Vivos", "cidade": "Praia Grande/SP", "ano": 2022,
        "descricao": "Projeto de regularização para carga de incêndio de 600 MJ/m²: extintores, sinalização, iluminação e saídas de emergência.",
        "normas_atendidas": "IT Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2202313928", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Projeto e Execução Elétrica Coletiva Residencial (34.97 kVA)",
        "cliente_empresa": "Éder Santos Cirino", "cidade": "Praia Grande/SP", "ano": 2022,
        "descricao": "Projeto e instalação de quadro de medição coletivo para 3 unidades residenciais, painel elétrico e malha de aterramento.",
        "normas_atendidas": "GED-13 CPFL / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302453809", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Adequação de PPCI Comercial Misto (222.47 m²)",
        "cliente_empresa": "Comércio Varejista de Animais Vivos", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Regularização de medidas de segurança contra incêndio para imóvel misto comercial/residencial.",
        "normas_atendidas": "Decreto Estadual 63.911/SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 8 ---
    {
        "id_doc": "CFT2302464320", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Instalação de Equipamentos de Proteção Contra Incêndio",
        "cliente_empresa": "Comércio Varejista de Animais Vivos", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Instalação física e manutenção de extintores, sinalização fotoluminescente e rotas de escape em edificação comercial.",
        "normas_atendidas": "IT-20 / IT-21 Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302528984", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Segurança Contra Incêndio - Local de Reunião Religiosa (F-2)",
        "cliente_empresa": "Ile Axe Tope Caboclo Sultan das Matas", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Dimensionamento de saídas de emergência e extintores para local de concentração pública de 132 m².",
        "normas_atendidas": "IT-11 / IT-20 Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302549974", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Cálculo de Fluxo de População e Portas de Escape (158 Pessoas)",
        "cliente_empresa": "Ile Axe Tope Caboclo Sultan das Matas", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Cálculo de Unidades de Passagem (UP) conforme IT-11 com dimensionamento de 3 portas de 2,70m para evacuação rápida.",
        "normas_atendidas": "IT-11 Tabela 1 / NBR 9077", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 9 ---
    {
        "id_doc": "CFT2302563683", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Segurança Contra Incêndio - Distribuidora de Químicos (C-2)",
        "cliente_empresa": "B R Piscinas Distribuidora Ltda", "cidade": "Guarujá/SP", "ano": 2023,
        "descricao": "Instalação e laudo de medidas de combate a incêndio para distribuidora de produtos de tratamento de piscinas (500 MJ/m²).",
        "normas_atendidas": "IT Bombeiros SP / NBR 12693", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302599503", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "PPCI e Dimensionamento de Saídas - Restaurante (F-8)",
        "cliente_empresa": "Lanchonete Marabarba Ltda", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Dimensionamento de saídas de emergência e extintores para restaurante/costelaria com salão e cozinha comercial.",
        "normas_atendidas": "IT-11 / IT-20 Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 10 ---
    {
        "id_doc": "CFT2302606312", "tipo": "TRT", "conselho": "CFT", "disciplina": "Mecânica / Gás Combustível",
        "titulo": "Teste de Estanqueidade e Rede de Gás GLP Comercial",
        "cliente_empresa": "Lanchonete Marabarba Ltda", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Instalação de tubulação de GLP comercial e realização de ensaio hidrostático/pneumático de estanqueidade para obtenção de alvará.",
        "normas_atendidas": "NBR 15526 / IT-28 Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302624259", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Reforma e Impermeabilização de 03 Sanitários Residenciais",
        "cliente_empresa": "Fernando Pierini Costa", "cidade": "Santos/SP", "ano": 2023,
        "descricao": "Demolição, regularização de base, impermeabilização de piso e paredes, assentamento cerâmico e pintura (72 m²).",
        "normas_atendidas": "NBR 16280 / NBR 9575", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302678615", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Instalação de Sistema Contra Incêndio em Academia (E-3)",
        "cliente_empresa": "Jessica Flavio dos Santos", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Instalação de iluminação de emergência, extintores de água e CO2 e rota de fuga para academia de musculação.",
        "normas_atendidas": "IT Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 11 ---
    {
        "id_doc": "CFT2302786087", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Reforma Residencial com Ampliação de Vãos e Revestimentos",
        "cliente_empresa": "Sueli Aparecida Santos da Silva", "cidade": "Santos/SP", "ano": 2023,
        "descricao": "Demolição de alvenaria para passagem de ambiente, assentamento de bancada de granito e piso cerâmico.",
        "normas_atendidas": "NBR 16280", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302837376", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Fachada Comercial e Padrão de Entrada Tipo B1 (18 kW)",
        "cliente_empresa": "Claudia Virgínia Federico Breuel", "cidade": "Santos/SP", "ano": 2023,
        "descricao": "Construção de alvenaria de fachada para suporte de padrão bifásico B1 da CPFL com ancoragem de roldana olhal de 200 DAN.",
        "normas_atendidas": "GED-13 CPFL", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302847818", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Medidas de Segurança Contra Incêndio - Serviços Automotivos (G-4)",
        "cliente_empresa": "Raimundo Carlos da Silva Goncalves", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Instalação física de extintores e sinalização de emergência em oficina de manutenção de motocicletas.",
        "normas_atendidas": "IT-11 / IT-20 Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 12 ---
    {
        "id_doc": "CFT2302941759", "tipo": "TRT", "conselho": "CFT", "disciplina": "Civil / Arquitetura",
        "titulo": "Projeto Arquitetônico e Memorial Técnico Descritivo",
        "cliente_empresa": "Valdeci Ribeiro Silva Lima", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Elaboração de plantas baixas, cortes, fachadas e memorial descritivo completo para regularização municipal.",
        "normas_atendidas": "NBR 6492", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2302975791", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Fachada e Padrão de Entrada Agrupado Tipo B1 e C1 (43 kW)",
        "cliente_empresa": "Edson Francisco de Santana", "cidade": "Praia Grande/SP", "ano": 2023,
        "descricao": "Execução técnica de alvenaria e instalação de quadro de medição agrupado comercial/residencial com roldana de 200 DAN.",
        "normas_atendidas": "GED-13 CPFL / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2303085000", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Reforma Residencial com Cobertura em Estrutura de Alumínio e Vidro",
        "cliente_empresa": "José Luiz Xavier Filho", "cidade": "Santos/SP", "ano": 2023,
        "descricao": "Reforma sem acréscimo de área, novos pontos elétricos, instalação hidráulica e montagem de toldo em alumínio e vidro.",
        "normas_atendidas": "NBR 16280 / NBR 7199", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2403192794", "tipo": "TRT", "conselho": "CFT", "disciplina": "Mecânica / Climatização",
        "titulo": "Laudo e Limpeza de Sistemas de Exaustão de Cozinhas Profissionais",
        "cliente_empresa": "Praia Grande Boliche e Bar Eireli", "cidade": "Praia Grande/SP", "ano": 2024,
        "descricao": "Inspeção técnica e manutenção preventiva do sistema de ventilação e exaustão mecânica com emissão de laudo de limpeza.",
        "normas_atendidas": "NBR 14518 / Portaria 3.523 MS", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 13 ---
    {
        "id_doc": "CFT2403309430", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Segurança Contra Incêndio - Manutenção de Motores Elétricos (I-1)",
        "cliente_empresa": "Boaventura Aquecedores Ltda", "cidade": "Guarujá/SP", "ano": 2024,
        "descricao": "Instalação de portas corta-fogo, extintores de alta capacidade e iluminação de emergência para unidade de reparo de motores.",
        "normas_atendidas": "IT Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2403312354", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Instalação de Poste Homologado com Medição Frontal Tipo C1 (23 kVA)",
        "cliente_empresa": "2A Comercio de Roupas e Acessórios", "cidade": "Santos/SP", "ano": 2024,
        "descricao": "Montagem de poste de concreto, caixa de medição voltada para a rua, malha de aterramento e ligação junto à CPFL.",
        "normas_atendidas": "GED-13 CPFL / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2403353127", "tipo": "TRT", "conselho": "CFT", "disciplina": "Estrutural / Civil",
        "titulo": "Cálculo Estrutural e Instalação de SPA Externo (Jacuzzi)",
        "cliente_empresa": "José Luiz Xavier Filho", "cidade": "Santos/SP", "ano": 2024,
        "descricao": "Cálculo de sobrecarga sobre laje existente para assentamento de banheira de hidromassagem tipo SPA e adequações hidrossanitárias.",
        "normas_atendidas": "NBR 6120 / NBR 6118", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 14 ---
    {
        "id_doc": "CFT2403452428", "tipo": "TRT", "conselho": "CFT", "disciplina": "Engenharia Legal / Laudos",
        "titulo": "Laudo Pericial de Estabilidade Estrutural e Acessibilidade PCD",
        "cliente_empresa": "Mathaius Comércio e Confecção Ltda", "cidade": "Santos/SP", "ano": 2024,
        "descricao": "Perícia técnica atestando solidez de fundações superficiais, alvenarias, SPDA, controle de acabamentos e rotas acessíveis PCD.",
        "normas_atendidas": "NBR 9050 / NBR 13752", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2403513370", "tipo": "TRT", "conselho": "CFT", "disciplina": "Mecânica / Climatização",
        "titulo": "Manutenção Preventiva e Laudo em Lavadores e Dutos de Exaustão",
        "cliente_empresa": "Praia Grande Boliche e Bar Eireli", "cidade": "Praia Grande/SP", "ano": 2024,
        "descricao": "Execução de higienização profunda e verificação de rotação/vazão de coifas e exaustores mecânicos em cozinha industrial.",
        "normas_atendidas": "NBR 14518", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 15 ---
    {
        "id_doc": "CFT2403553476", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Laudos",
        "titulo": "Vistoria e Laudo Técnico de Instalações Elétricas de Baixa Tensão",
        "cliente_empresa": "Albino Dietrich Garcia", "cidade": "Guarujá/SP", "ano": 2024,
        "descricao": "Vistoria técnica final em barramentos, condutores e quadros de força de 30 kVA com medições de continuidade.",
        "normas_atendidas": "NBR 5410 / NR-10", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2403570419", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Fachada Residencial para Padrão de Entrada Tipo B1 (18 kW)",
        "cliente_empresa": "Gabriel Pérez de Santiago", "cidade": "Santos/SP", "ano": 2024,
        "descricao": "Condução da execução de fachada em alvenaria estruturada para suporte de ramal de ligação aérea CPFL com roldana de 200 DAN.",
        "normas_atendidas": "GED-13 CPFL", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2403573737", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Remoção de Prumada Externa e Impermeabilização em Fachada Sul",
        "cliente_empresa": "Condomínio Blue Moon Blue Sky", "cidade": "São Vicente/SP", "ano": 2024,
        "descricao": "Trabalho técnico especializado em altura para desmontagem de tubulação horizontal externa e estanqueidade de fachada.",
        "normas_atendidas": "NR-35 / NBR 16280", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 16 ---
    {
        "id_doc": "CFT2403670665", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Poste com Medição Agrupada Frontal para 02 Unidades Comerciais (46 kVA)",
        "cliente_empresa": "2A Comercio de Roupas e Acessórios", "cidade": "Santos/SP", "ano": 2024,
        "descricao": "Instalação e comissionamento de poste com 2 caixas Tipo C1, malha de terra e distribuição de condutores subterrâneos.",
        "normas_atendidas": "GED-13 CPFL / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2403744964", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Entrada de Energia Comercial de Alta Demanda - Padrão C6 (76 kVA)",
        "cliente_empresa": "Organização Social de Ataúdes Novoa Ltda", "cidade": "São Vicente/SP", "ano": 2024,
        "descricao": "Instalação de padrão de medição indireta/direta Tipo C6, montagem de disjuntor em caixa blindada e aterramento.",
        "normas_atendidas": "GED-13 CPFL / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2404047414", "tipo": "TRT", "conselho": "CFT", "disciplina": "Manutenção Predial",
        "titulo": "Coordenação Técnica em Manutenção e Conservação de Fachadas (100 m²)",
        "cliente_empresa": "Residencial Marhermar III", "cidade": "Praia Grande/SP", "ano": 2024,
        "descricao": "Coordenação e fiscalização de restauração de reboco, tratamento de trincas e pintura impermeabilizante em edifício residencial.",
        "normas_atendidas": "NBR 5674 / NBR 13755", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 17 ---
    {
        "id_doc": "CFT2504228054", "tipo": "TRT", "conselho": "CFT", "disciplina": "Civil / Arquitetura de Interiores",
        "titulo": "Projeto e Execução de Reforma com Integração de Ambientes (62.05 m²)",
        "cliente_empresa": "Pedro Ribeiro Adriani", "cidade": "Santos/SP", "ano": 2025,
        "descricao": "Detalhamento de paginação cerâmica, iluminação de realce em LED, painel ripado, bancada de mármore e ampliação de sala com sacada.",
        "normas_atendidas": "NBR 16280", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2504384630", "tipo": "TRT", "conselho": "CFT", "disciplina": "Civil / Regularização",
        "titulo": "Projeto Arquitetônico de Regularização de Unidade Mista (199.75 m²)",
        "cliente_empresa": "Wesley Cesar", "cidade": "Praia Grande/SP", "ano": 2025,
        "descricao": "Desenho arquitetônico para regularização de edificação de uso misto comercial e residencial.",
        "normas_atendidas": "Código de Obras Municipal / NBR 6492", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2504506852", "tipo": "TRT", "conselho": "CFT", "disciplina": "Multidisciplinar",
        "titulo": "Projetos As Built Elétrico, Hidráulico e Telecomunicações",
        "cliente_empresa": "Wesley Cesar", "cidade": "Praia Grande/SP", "ano": 2025,
        "descricao": "Levantamento cadastral As Built de instalações elétricas de baixa tensão, hidrossanitárias e infraestrutura de telecomunicações.",
        "normas_atendidas": "NBR 14645 / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 18 ---
    {
        "id_doc": "CFT2504574297", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / SPDA",
        "titulo": "Projeto Executivo de SPDA e Estudo de Coordenação e Proteção (233.36 m²)",
        "cliente_empresa": "Novoa Empreendimentos e Consultoria", "cidade": "Santos/SP", "ano": 2025,
        "descricao": "Análise de risco conforme NBR 5419:2015, dimensionamento de captores, condutores de descida, anel de aterramento e DPS.",
        "normas_atendidas": "NBR 5419:2015 / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2504608338", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / Luminotécnica",
        "titulo": "Projeto Luminotécnico e Fixação Estrutural de Forro de Gesso",
        "cliente_empresa": "Botelho e Kronemberg Eventos Ltda", "cidade": "Santos/SP", "ano": 2025,
        "descricao": "Cálculo de iluminância, especificação de tirantes e perfis para sustentação de forro e distribuição de circuitos elétricos.",
        "normas_atendidas": "NBR ISO/CIE 8995-1 / NBR 15758", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2504663082", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Segurança Contra Incêndio - Galpão de Serralheria (C-1)",
        "cliente_empresa": "Adeilson da Silva Lucena Serralheria", "cidade": "Guarujá/SP", "ano": 2025,
        "descricao": "Adequação técnica de extintores, sinalização e plano de emergência para oficina de montagem de estruturas de alumínio.",
        "normas_atendidas": "IT Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 19 ---
    {
        "id_doc": "CFT2504806972", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Medidas de Segurança Contra Incêndio - Clínica de Estética (142.41 m²)",
        "cliente_empresa": "Flavia Lima Ribeiro Estética Avançada", "cidade": "Araraquara/SP", "ano": 2025,
        "descricao": "Instalação de extintores de incêndio, blocos autônomos de LED e sinalização de rota de escape.",
        "normas_atendidas": "IT Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2504832452", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "PPCI para Estabelecimento de Prestação de Serviços (D-1)",
        "cliente_empresa": "Flavia Lima Ribeiro Estética Avançada", "cidade": "Araraquara/SP", "ano": 2025,
        "descricao": "Adequação de projeto de segurança contra incêndio para unidade de estética com rotas de fuga desobstruídas.",
        "normas_atendidas": "IT Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2504873707", "tipo": "TRT", "conselho": "CFT", "disciplina": "Multidisciplinar",
        "titulo": "Projeto As Built Multidisciplinar e Laudo de Regularização (125 m²)",
        "cliente_empresa": "Vandete Ramos Pereira", "cidade": "Praia Grande/SP", "ano": 2025,
        "descricao": "Desenho técnico de arquitetura, diagrama elétrico unifilar, rede de esgoto e ramal de telecomunicações.",
        "normas_atendidas": "NBR 5410 / NBR 5626", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 20 ---
    {
        "id_doc": "CFT2505081992", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "PPCI para Oficina de Manutenção e Reparação de Motocicletas (G-4)",
        "cliente_empresa": "Luis Marcelo Correia Guimarães", "cidade": "Praia Grande/SP", "ano": 2025,
        "descricao": "Instalação de sistema de combate a princípio de incêndio para carga de fogo de 300 MJ/m² e sinalização fotoluminescente.",
        "normas_atendidas": "IT-11 / IT-20 Bombeiros SP", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2505136478", "tipo": "TRT", "conselho": "CFT", "disciplina": "Elétrica / CPFL",
        "titulo": "Projeto Elétrico de Baixa Tensão e Padrão Coletivo C5 - GED 13 (53 kVA)",
        "cliente_empresa": "Menacker Engenharia Ltda", "cidade": "Guarujá/SP", "ano": 2025,
        "descricao": "Dimensionamento de condutores de alimentação, quadro de medição coletivo C5, circuitos de iluminação dirigida e eletroposto.",
        "normas_atendidas": "GED-13 CPFL / NBR 5410", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2605597484", "tipo": "TRT", "conselho": "CFT", "disciplina": "Civil / Arquitetura",
        "titulo": "Levantamento Cadastral e Laudo Técnico de Estabilidade Predial",
        "cliente_empresa": "Mario Nivaldo Rodrigues", "cidade": "Araraquara/SP", "ano": 2026,
        "descricao": "Levantamento topográfico/arquitetônico e elaboração de laudo de solidez de edificação comercial (70.99 m²).",
        "normas_atendidas": "NBR 13752 / NBR 6492", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "CFT2605818972", "tipo": "TRT", "conselho": "CFT", "disciplina": "Construção Civil",
        "titulo": "Reforma, Impermeabilização e Revestimentos em Unidade Sanitária",
        "cliente_empresa": "Denise Barbosa Brigido", "cidade": "São Paulo/SP", "ano": 2026,
        "descricao": "Substituição completa de pisos cerâmicos, impermeabilização de piso e paredes com argamassa polimérica e pintura.",
        "normas_atendidas": "NBR 16280 / NBR 9575", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PÁGINA 21 ---
    {
        "id_doc": "CFT2606038523", "tipo": "TRT", "conselho": "CFT", "disciplina": "Incêndio / PPCI",
        "titulo": "Medidas de Segurança Contra Incêndio - Academia de Musculação",
        "cliente_empresa": "Jessica Flavio dos Santos", "cidade": "Praia Grande/SP", "ano": 2026,
        "descricao": "Dimensionamento e regularização de extintores, blocos autônomos de iluminação e saídas de emergência desimpedidas.",
        "normas_atendidas": "IT Bombeiros SP / Decreto Estadual", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },

    # --- PROJETOS ESPECIAIS / PORTFÓLIO EXECUTIVO ---
    {
        "id_doc": "PROJ-2025-01", "tipo": "Projeto", "conselho": "CREA/CFT", "disciplina": "Elétrica / Geração",
        "titulo": "Consultoria e Projeto de Geração Híbrida e Paralelismo (1000 kVA + FV)",
        "cliente_empresa": "Caravelas Engenharia Ltda", "cidade": "Santos/SP", "ano": 2025,
        "descricao": "Estudo de Viabilidade Técnica e Econômica (VTE), paralelismo de dois geradores diesel de 500kVA com usina solar fotovoltaica, QTA e proteção anti-ilhamento.",
        "normas_atendidas": "NBR 5410 / Resoluções ANEEL", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "PROJ-2024-08", "tipo": "Projeto", "conselho": "CREA/CFT", "disciplina": "Estrutural / Mecânica",
        "titulo": "Cálculo e Detalhamento de Pipe Racks Industriais e Suportes Metálicos",
        "cliente_empresa": "Grupo Garcia", "cidade": "São Paulo/SP", "ano": 2024,
        "descricao": "Análise de esforços de torção e flambagem em suportes metálicos industriais com padronização em blocos dinâmicos CAD (-25% lead time).",
        "normas_atendidas": "NBR 8800 / NBR 6123", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "PROJ-2025-02", "tipo": "Projeto", "conselho": "N/A", "disciplina": "Dados / Otimização",
        "titulo": "Sistema de Gestão de Ativos em Tempo Real (Python + SQLite + Power BI)",
        "cliente_empresa": "Tracevia S/A", "cidade": "São Paulo/SP", "ano": 2025,
        "descricao": "Desenvolvimento de rotinas para rastreamento de ativos e logística de infraestrutura tecnológica (ITS), eliminando falhas de auditoria.",
        "normas_atendidas": "Práticas Lean Six Sigma / PMBOK", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    },
    {
        "id_doc": "PROJ-2026-01", "tipo": "Projeto", "conselho": "CREA/CFT", "disciplina": "Estrutural / Civil",
        "titulo": "Laudo Pericial e Projeto de Reforço com Estacas Mega Prensadas",
        "cliente_empresa": "Imóvel Mooca", "cidade": "São Paulo/SP", "ano": 2026,
        "descricao": "Inspeção patológica de recalque diferencial e dimensionamento de sistema de reforço de fundação por estacas mega de concreto prensadas hidraulicamente.",
        "normas_atendidas": "NBR 6122 / NBR 6118", "drive_id_ou_url": "PASTA_PROJETOS_DRIVE"
    }
]

df = pd.DataFrame(todos_os_registros)
df.to_csv("trts_projetos.csv", index=False, encoding="utf-8-sig")

print(f"Base de dados gerada com sucesso! Total de registros cadastrados: {len(df)}")