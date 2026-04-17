# Gestao de Projetos
## Interface vs Classe Abstrata
- Interface 
	- Definicao: contrato que define apenasos comportamentos que uma classe deve implementar, sem fornecer implementacao concreta.
	- Conceito: Estrutura que abstrai totalmente a implementação, estabelecendo apenas a assinatura dos métodos que devem ser fornecidos. 
	- Intanciacao: Não pode ser instanciada; deve ser implementada por uma classe concreta que forneça a lógica dos métodos. 
	- Conteudo de metodos: Tradicionalmente apenas assinaturas. 
	- Estado (Atributos): Não mantém estado de instância; admite apenas constantes. 
	- Construtores: Não possui construtor. 
	- Herança/Implementação: Suporta múltiplas implementações: uma classe pode implementar várias interfaces. 
	- Flexibilidade/Extensibilidade:  Estrutura altamente flexível, permitindo combinar múltiplas interfaces em uma única classe, facilitando extensibilidade de comportamentos. 
	- Relação semântica: Representa uma relação de capacidade/comportamento (“sabe-fazer”). 
	- Reuso de código:  Não permite reuso de código, apenas contratos. 
	- Acoplamento: Promove baixo acoplamento, pois só exige o contrato. 
	- Polimorfismo: Suporta polimorfismo por contrato, permitindo que diferentes classes sejam tratadas de forma uniforme. 
	- Quando usar: Ideal quando classes distintas necessitam compartilhar apenas comportamentos, sem herança comum
	
- Classe Abstrata
	- Definicao: É uma classe que não pode ser instanciada diretamente e serve como base para outras classes por meio da herança, podendo conter métodos implementados e métodos abstratos (sem corpo). 
	- Conceito: Estrutura que possibilita a criação de um modelo parcial, unindo código já implementado com pontos obrigatórios de especialização. 
	- Instanciacao: Não pode ser instanciada diretamente; deve ser estendida por uma classe concreta que complete sua implementação. 
	- Conteudo de metodos: Permite métodos concretos e abstratos. 
	- Estado (Atributos): Pode armazenar estado (atributos/variáveis de instância) representando dados persistentes do objeto. 
	- Construtores: Pode possuir construtor, chamado indiretamente pelas subclasses. 
	- Herança/Implementação: Suporta herança simples: uma classe só pode estender uma classe abstrata. 
	- Flexibilidade/Extensibilidade:   Estrutura menos flexível, pois a herança simples limita a combinação de comportamentos; adequada quando há hierarquia clara
	- Relação semântica: Representa uma relação de generalização/especialização (“é-um tipo de”). 
	- Reuso de Codigo: Permite reuso de implementações comuns e atributos. 
	- Acoplamento:  Gera acoplamento mais forte entre superclasse e subclasses. 
	- Polimorfismo: Suporta polimorfismo por herança, permitindo chamadas genéricas a métodos das subclasses. 
	- Quando usar: Ideal quando várias classes compartilham lógica comum e precisam de uma base com implementação parcial. 
	
## PMBOK (Project Management Body of Knowledge)
- Um guia abrangente que nos oferece um conjunto de boas praticas em gestao de projetos, como um mapa detalhado, que integra 10 areas de conhencimento.
- Areas 
	- Gerenciamento de Escopo
		- Define os limites e entregas do projeto
	- Gerenciamento de Aquisicoes
		- Lida com compras e contratos externos
	- Gerenciamento das partes interessadas
		- Gerencia as expectativas das partes interessadas (Stakeholders)
	- Gerenciamento do cronograma
		- Planeja e controla o cronograma do projeto
	- Gerenciamento de riscos
		- Identifica e planeja para riscos potenciais
	- Gerenciamento de custos
		- Acompanha e controla o orçamento do projeto
	- Gerenciamento de recursos 
		- gerencia equipe, equipamentos e materiais
	- Gerenciamento de qualidade 
		- Garante que os padroes do projeto sejam atendidos.
	- Gerenciamento de comunicacoes
		- Facilita o fluxo de informacoes eficiente
	- Gerenciamento da integracao
		- coordena e unifica todas as areas do projeto
			
- Tipos de gerenciamento de projetos 
	- PMBOK: guia pratico e abrangente para gerenciamento de projetos 
	- Agile Practices: Encorajar em flexibilidade adaptabilidade e valores continuos
	- Scrum: Adequado para desenvolvimento iterativo e adaptabilidade
	- Waterfall: Ideal para projetos com etapas claras e sequenciais
	- Kanban: Melhorar o fluxo de trabalho, com flexibilidade e comunicacao
	- XP: O eXtreme Programming (XP) é uma metodologia ágil que foca na adaptação contínua e na alta qualidade do software.
	
## Planejamento Estrategico
- O que é?
	- É um processo sistematico que responde a tres perguntas fundamentais:
		- Onde estamos agora? que envolve a analise do cenario atual.
		- para onde queremos ir? definindo metas e objetivos
		- como vamos chegar la? criar estrategias e planos de acao

- O planejamento estrategico sera eficas se refletir nos seguintes beneficios:
	- Clareza e direção: garante que todos saibam o que deve ser feito e por quê.
	- Decisões mais assertivas: reduz riscos de escolhas precipitadas.
	- Uso eficiente de recursos: tempo, dinheiro e energia são aplicados no que realmente importa.
	- Antecipação de problemas: ao analisar cenários, a empresa/profissional se prepara para lidar com imprevistos.
	- Engajamento da equipe: quando os objetivos estão claros, todos trabalham mais alinhados. 	
	
- Exemplo Pratico, Como fazer?
	- o processo de planejamento estrategico geralmente passa por cinco etapas:
		1. Analise de ambiente (interno e externo)
		2. Definir missao, valores e visao
		3. Estabelecer objetivos e metas 
		4. Criar planos de acao
		5. Monitorar e ajustar
		
## Gestao de Pessoas
- O que é?
	- É o conjunto de praticas e politicas voltadas para atrair, desenvolver, motivar e reter talentos dentro da organizacao,
	- Nao se limita ao setor de RH, mas se estende a todos os lideres e gestores, que atuam diretamente na valorizacao do capital humano.
	
- Qual a importancia?
	- Vital para:
		- Elevar a motivacao e engajamento da equipe
		- Desenvolver habilidades tecnicas e comportamentais
		- Reduzir conflitos e aumentar a cooperacao
		- Favorecer a inovacao e a criatividade
		
- Como Fazer? 
	- A gestao de pessoas se apoia em cinco processos principais:
		1. Recrutamento e Seleção: atrair profissionais alinhados à cultura e às necessidades técnicas.
		2. Treinamento e Desenvolvimento: capacitar continuamente os colaboradores.
		3. Avaliação de Desempenho: medir resultados
		e fornecer feedback.
		4. Remuneração e Reconhecimento: valorizar e reter talentos.
		5. Clima Organizacional: manter relações saudáveis
		e um ambiente motivador.