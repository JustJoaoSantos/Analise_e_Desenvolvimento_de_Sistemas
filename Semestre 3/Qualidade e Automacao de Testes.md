# Unidade 1 - Formas e Qualidade de Testes
***
## U1A1 - A História e os Fundamentos da Testagem em Softwares
• O que é monitoramento contínuo?
• Importância para a estabilidade e desempenho das aplicações.
• Principais desafios no monitoramento de software.
• Monitoramento reativo versus proativo.
• Benefícios do uso de ferramentas especializadas.
• Objetivos do curso sobre monitoramento contínuo.

### Ferramentas de monitoramento – Prometheus
• Criado pela SoundCloud, o Prometheus é uma solução 
	open-source voltada para monitoramento, permitindo a coleta 
	e análise de métricas em tempo real.
• Coleta de métricas baseada em "pull“.
• Uso de "exporters" para diversas aplicações.
• Consultas e alertas com PromQL.
• Integração com Kubernetes e outras plataformas.
• Casos de uso do Prometheus na indústria.

### Ferramentas de Monitoramento - New Relic
• O New Relic é uma plataforma de Monitoramento de Desempenho
	de Aplicações (APM) que coleta, analisa e visualiza dados em
	tempo real para identificar problemas e otimizar sistemas.
• Monitoramento de Desempenho de Aplicações (APM).
• Coleta e análise de logs e eventos.
• Rastreamento distribuído para sistemas complexos.
• Detecção de anomalias com Inteligência Artificial (IA).
• Comparação entre New Relic, Prometheus e Grafana.

### Aplicação prática e boas práticas
- Escolha: Como selecionar a ferramenta ideal para cada 
	necessidade
- Configuração: Passos iniciais para integração com aplicações.
- Métricas: Definição dos principais indicadores de 
	monitoramento.
- Automação: Criação de alertas para resposta rápida a 
	incidentes.
- Otimização: Uso de dados coletados para melhorias contínuas.
- Conclusão: Importância do monitoramento contínuo para 
	ambientes seguros.
	
### Qualidade: Mais do que encontrar defeitos
- Verificação
	- Estamos construindo o produto correntamente?
	- Ex.: regra de cálculo, API, Integração, banco de dados 
	
- Validação
	- Estamos construindo o produto certo?
	- Ex.: fluxo de compra compreensível, transferência segura,
		necessidade do usuário atendida.

- Prevenção
	- Como evitar que a falha volte?
	- Ex.: regressão automatizada, code review, pipeline,
		monitoramento.
		
### Evolução dos Testes de Software 
- 1950 ~ 1970
	- Cascata
	- Foco em depuração e, posteriormente, testes documentados no 
		fim do ciclo
		
- 2001 
	- Manifesto Ágil
	- Revolução nos testes: ciclos curtos, feedback rápido e QAs
		integrados aos testes.
		
- 2009
	- DevOps
	- Surgimento do termo e foco em aproximar Dev, Ops e Qualidade 
	
- 2010
	- Automação e CI 
	- Pipelines contínuas (CI/CD) e testes rodando a cada commit.
	
- Atualidade
	- IA & Obs
	- Testes generativos, análise preditiva e foco em
		monitoramento contínuo.
		
## U1A2 - Sistemas da qualidade: definição e importância na testagem
***
### O que é o TMMI?
• TMMI: Test Maturity Model Integration
• Definição: modelo para avaliar e melhorar a maturidade
	dos testes de software.
• Objetivo: aumentar a eficiência e a qualidade nos processos 
	de testagem.
• Origem: inspirado no CMMI, focado exclusivamente em testes.
• Importância: ajuda empresas a identificarem pontos fracos
	e fortalecerem seus testes.
• Aplicação: utilizado em projetos ágeis e tradicionais

### Níveis de maturidade do TMMI
• Nível 1 - Inicial: testes não estruturados, sem processos 
	definidos.
• Nível 2 - Gerenciado: testes básicos, ligados ao controle 
	de qualidade.
• Nível 3 - Definido: processo de testes documentado e 
	padronizado.
• Nível 4 - Medido: uso de métricas para monitorar e melhorar 
	testes.
• Nível 5 - Otimizado: testes contínuos, com foco em inovação 
	e prevenção de falhas.

### Testagem e Qualidade
- Testagem estruturada: Reduz erros ao seguir processos claros.
- Qualidade: A maturidade dos testes reflete diretamente no 
	produto final.
- Cobertura: Quanto mais testagens, menores os riscos de 
	falhas críticas.
- Confiabilidade: Produtos testados de forma madura são mais 
	estáveis.
- Eficiência: Testes bem definidos diminuem retrabalho e 
	custos extras.

### Benefícios da implementação do TMMI
• Redução de custos: menos falhas, menos gastos com correções.
• Aumento da produtividade: testes claros aceleram o 
	desenvolvimento.
• Tomada de decisões: métricas ajudam a guiar melhorias 
	contínuas.
• Satisfação do cliente: produtos mais estáveis geram confiança.
• Competitividade: empresas maduras em testes destacam-se 
	no mercado

### Custos e Estratégias
- Investimento:
	- Custos iniciais, mas retorno garantido a longo prazo.

- Treinamento:
	- Equipes capacitadas aplicam testes de forma eficaz.

- Ferramentas:
	- Softwares de automação auxiliam nos processos.

- Monitoramento:
	- Métricas avaliam a evolução dos testes.

- Ajustes:
	- Revisão contínua para manter o alto nível de maturidade.
	
### Ferramentas 
- Web: Selenium / Katalon 
- Java: JUnit / TEstNG
- Desempenho e stress: JMeter / LoadRunner
- organizacao: QTeste e similares

### Testes Manuais
- São realizados por uma pessoa, que interage diretamente com
	o sistema.
- O testador verifica se as funcionalidades funcionam conforme
	o esperado.
- Permitem observar aspectos visuais, mensagens, navegação e
	experiência do usuário.
- São úteis para encontrar problemas que podem não ser previstos
	em scripts automatizados.
- Costumam ser mais flexiveis, pois o testador pode explorar
	diferentes caminhos durante o uso.
	
### Testes Automatizados 
- São executados por scripts ou ferramentas de teste.
- Simulam ações do usuário ou verificam partes internas do 
	sistema.
- São indicados para testes repetitivos e validações frequentes.
- Ajudam a identificar rapidamente se uma alteração no código
	causou algum erro.
- Exigem planejamento, escrita dos testes e manutenção dos 
	scripts.
	
## U1A3 - Diferentes Tipos de Testes 
***
### Selenium e JUnit 
• O que é o Selenium:
	• Ferramenta de código aberto para automação de navegadores web.
	• Oferece uma interface única para escrever scripts de teste.
	• Suporta diversas linguagens de programação como Ruby, Java, NodeJS, PHP,
		Perl, Python e C#.
• O que é o JUnit:
	• Framework de código aberto para testes unitários na linguagem Java.
	• Usado por desenvolvedores Java para criar e executar testes automatizados.
	• Permite a reexecução de casos de teste sempre que um novo código é
		adicionado.
	• Garante que alterações no código não quebrem funcionalidades existentes.

### Selenium 
• Ferramenta de código aberto para automação de testes web.
• Compatível com C#, Java, Python e outras linguagens.
• Suporte a Windows, Linux e macOS.
• Executa testes em diversos navegadores.
• Compara resultados obtidos com os esperados.
• Verifica a conformidade da aplicação.

### JUnit 
• Framework open-source para testes automatizados em Java.
• Hospedado no GitHub.
• Verifica funcionalidades de classes e métodos.
• Permite execução automática de todos os testes.
• Garante integridade e estabilidade em novas versões do sistema.
• Utiliza anotações (Annotations) para identificação de métodos de teste.
• Indica execução antes ou depois de classes.
• Permite ignorar testes quando necessário.
• Suporta criação de suítes de teste para execução conjunta.

- Escrevendo Testes para JUnit 
	- Precisa usar os métodos da classe junit.framework.assert
	- Cada método de teste verfica uma condição (asserção) e 
		relata ao executor de teste se o teste falhou ou foi 
		bem-sucedido.
	- O executor de teste usa o resultado para reportar ao 
		usuário (no modo CLI) ou atualizar a exibição (em um IDE).
	- Todos os métodos retornam void
	- Alguns métodos representativos de junit.framework.assert:
		``` Java 
		assertTrue (boolean)
		assertTrue (String, boolean)
		fail (String)
		```
		
- Principais Anotações do JUnit 
	- @Test: marca um método como um caso de teste.
	- @BeforeEach: Executado antes de cada método de teste.
	- @AfterEach: Executado após cada método de teste.
	- @BeforeAll: Executado uma vez antes de todos os testes (método static).
	- @AfterAll: Executado uma vez após de todos os testes (método static).
	- @Disabled: Ignora um teste temporariamente.
	
### Misturando Selenium e JUnit 
• Integração do JUnit com Selenium WebDriver para testes automatizados
	em aplicações web.
• Facilita a criação de casos de teste estruturados e organizados.
• Uso combinado com Selenium melhora a sistematização dos testes.
• Passos para automação com JUnit e Selenium em uma grade online:
• Baixar os arquivos JAR do JUnit.
• Adicionar os JARs ao projeto Selenium.
• Utilizar anotações e métodos do JUnit nos primeiros scripts Selenium.
• Executar testes em nuvem com JUnit e Selenium via LambdaTest.

### Criando um Teste com JUnit e Selenium 
• Crie um projeto Java em sua IDE favorita.
• Adicione as dependências do JUnit e Selenium ao projeto.
• Configure o WebDriver correspondente ao seu navegador.
• Implemente um método de teste que abra o navegador e acesse uma
	página.
• Localize e interaja com elementos da página (ex.: clique ou digite).
• Verifique o resultado esperado usando asserções do JUnit.
• Execute o teste e observe os resultados na IDE.
• Finalize fechando o navegador após o teste.

### Teste de Unidade 
- Um teste unitário verifica se uma unidade de código produz o 
	resultado esperado em condições controladas. Ele deve falhar
	por causa da unidade testada, não por banco de dados, rede ou 
	serviços externos.
	
- As unidades podem ser:
	- Funções individuais ou métodos dentro de um objeto.
	- Classes de objetos com vários atributos e métodos.
	- Componentes compostos com interfaces definidas usados 
		para acessar suas funções.
		
### Ferramentas 
- IntelliJ IDEA 
	- Utilizada amplamente para desenvolvimento em Java, oferecendo
		recursos como autocompletar código, depuração, Integração
		com sistemas de versionamento e suporte nativo a ferramentas 
		como Maven e JUnit.
	
- JUnit 
	- É uma biblioteca de testes para Java que permite escrever 
		e executar testes automatizados, facilitando a verficação
		de que métodos e classes funcionam corretamente. É uma 
		ferramenta essencial no desenvolvimento orientado a 
		testes (TDD).
	
- Maven 
	- É uma ferramenta de automação de build e gerenciamento de
		dependências que simplifica o processo de compilação, 
		empacotamento, execução de testes e controle de versões 
		em projetos java.

## U1A4 - Qualidade no Processo de Desenvolvimento de Software 
***
### Qualidade e teste de Software 
• Importância da qualidade no desenvolvimento de software.
• Papel dos testes na garantia de conformidade e
	confiabilidade.
• Relevância das normas internacionais no processo de
	desenvolvimento.
• Impactos positivos da padronização nos projetos de
	software.

### ISO 12207 - Processos do ciclo de vida do software 
• Estruturação dos processos de ciclo de vida de software.
• Principais processos: aquisição, desenvolvimento e manutenção.
• Benefícios da ISO 12207 para a gestão de projetos.
• Importância da norma na organização das atividades de 
	software.
	
### ISO/IEC 25000 - Qualidade de Software 
- Conjunto de normas conhecido como SQuaRE: Software Product
	Quality Requeriments and Evaluation.
- Define critérios para especificar, medir e avaliar a
	qualidade de produtos de software.
- Ajuda a transformar "qualidade" em aspectos observáveis, 
	como desempenho, segurança, usabilidade e manutenibilidade.
- Apoia a definição de requisitos de qualidade, além dos 
	requisitos funcionais.
- É útil em atividades de testes, auditorias, aquisição de 
	software e melhoria de produtos.

### IEEE 1012 - Verificação e validação 
• Conceitos de verificação e validação no software.
• Estrutura dos processos definidos pela IEEE 1012.
• Importância da verificação e validação para a qualidade final
	do produto.
• Compatibilidade com diferentes modelos de ciclo de vida

### IEEE 829 - Documentação de testes 
• Finalidade da documentação de testes no ciclo de vida do
	software.
• Estrutura básica dos documentos conforme a IEEE 829.
• Benefícios da padronização na comunicação da equipe.
• Responsabilidades do gerente de teste e da equipe.

### Normas e Modelos de Qualidade 
- ISO/IEC 12207: Processos do ciclo de vida de software 
- IEEE 1012: Verificação e Validção
- IEEE 829: Documentação de testes.
- ISO/IEC 25000: Qualidade do produto e em uso.
- CMMI / MPS.BR: Maturidade de processos.

# Unidade 2 - Automação de Testes 
***
## U1A1 - Etapas de Testagem no Desenvolvimento de Software
***
### Identificação de pontos críticos no desenvolvimento
• A qualidade do software depende da detecção antecipada de
	falhas e riscos.
• Pontos críticos são áreas do sistema mais propensas a erros e
	instabilidades.
• Identificá-los permite direcionar os testes de forma mais
	eficiente e estratégica.
• Reduzir falhas melhora a confiabilidade do software e a
	experiência do usuário final.
	
### Áreas de risco no código
• Códigos frequentemente modificados apresentam maior probabilidade
	de falhas.
• Monitorar essas alterações ajuda a priorizar testes e prevenir
	regressões.
• Ferramentas de versionamento indicam padrões de mudanças em
	componentes críticos.
• Testes de regressão são essenciais para garantir a estabilidade das
	funcionalidades existentes.

### Como Encontrar Pontos Críticos?
- Muitas alterações: Módulos modificados com frequência tendem
	a quebrar mais.
	
- Regras complexas: Cálculos, permissões, impostos, descontos
	e transações exigem mais atenção.
	
- Histórico de falhas: Áreas com bugs recorrentes merecem mais 
	validação.
	
- Segurança e estabilidade: Funcionalidades ligadas a 
	autenticação, dados sensíveis e disponibilidade devem 
	ser priorizadas.
	
- Integrações: APIs, banco de dados, pagamentos e serviços externos 
	precisam de testes cuidadosos.
	
- Código legado: Sistemas com arquitetura frágil ou pouco
	documentada apresentam maior risco.
	
### Requisitos mínimos para testes eficazes
1. Cenários de Testes 
2. Cobertura de Código 
3. Integrações 
4. Condições Extremas 

### Métricas de Cobertura: O Que Observar?
- Funções: Verfica se as funções foram chamadas durante os testes.
- Declarações: Analisa se os comandos do código foram executados.
- Ramificações: Avalia os diferentes caminhos de decisão do 
	programa.
- Condições: Verifica se as condições foram testadas como 
	verdadeiro e falso.
- Linhas: Mede quais linhas do código foram percorridas durante 
	a execução dos testes.
	
### CI/CD 
1. Commit no repo : dispara o pipeline 
2. Build automatico : compila e empacota 
3. Testes automáticos : unit + integração
4. Deploy em staging : ambiente de testes 
5. Testes de aceite : QA e smoke tests
6. Deploy em produção : release final

## U1A2 - Testes de Campo e Testes de Ponto a Ponto 
***
### Alpha, Beta e Gamma
- Ideia central: cada fase aumenta a exposição do produto 
	ao mundo real 

- Alpha: Empresa 
	- ambiente controlado
	- QA + devs 
	- falhas críticas 
	
- Beta: Usuários reais
	- pré-lançamento
	- feedback de uso 
	- beta fechado ou aberto 
	
- Gamma: lançamento controlado 
	- Última verificação 
	- monitoramento real 
	- correções rápidas 
	
### Alpha x Beta 
- Testadores
	- Alpha: Funcionarios internos 
	- Beta: Usuários finais / clientes 
	
- Ambiente 
	- Alpha: Controlado e preparado
	- Beta: Condições reais de uso
	
- Técnica
	- Alpha: Caixa branca + caixa preta
	- Beta: principalmente caixa preta 
	
- Objetivo
	- Alpha: Encontrar falhas críticas 
	- Beta: Avaliar interação e satisfação 
	
- Correção
	- Alpha: Problemas corrigidos imediatamente
	- Beta: Feedback vira melhoria para versões futuras
	
### Estabilidade e Aceitação
- O sistema precisa operar por longos períodos sem falhas 
	e se recuperar rápidamente quando algo dá errado.
- ex.: teste de recuperação e caos controlado.

- Valida se o produto atende às expectativas, entrega valor e é
	compreensível para o público-alvo.
- ex.: testes guiados, exploratórios, A/B e card sorting.
	
### Testes de Campo 
- Rede Instável
- Dispositivos Variados
- GPS e Sensores
- Pagamentos Reais 
- Comportamento do Usuário

### Teste Ponto a Ponto
- Geralmente executado no Estágio Gamma

- Cliente -> Pedido -> Pagamento -> Estoque -> Logística

- O que verificar
	- Chamadas entre APIs 
	- Integridade dos dados tranmitidos
	- Tempos de resposta 
	- Falhas em serviços externos 
	
- Ferramentas e exemplos
	- Postman, WireMock, AWS X-Ray,
	- Azure Application Insight,
	- Wireshark, Tsung, Splunk e Elk Stack.
	
### Testes Modernos 
- Código (commit) -> 
- CI/CD (pipeline) -> 
- Testes (automação) ->
- Monitoramento (produção) -> 
- Aprendizado (melhorias).

## U2A3 - Métodos Combinados de Testagem
***
### Testes de software e qualidade
• Os testes de software garantem qualidade, confiabilidade e
	segurança nas aplicações.
• Diferentes abordagens ajudam a identificar falhas em várias 
	fases do desenvolvimento.
• Métodos eficazes evitam erros em produção, reduzindo custos 
	com correções.
• Testes bem aplicados melhoram a experiência do usuário e a
	estabilidade do sistema.

### Testes de Caixa Preta ou Teste Funcional 
1. Avalia o comportamento do software sem analisar seu código-
	fonte.
2. Compara as entradas e saídas esperadas para garantir que o
	sistema funcione corretamente.
3. Útil para validar requisitos funcionais e regras de negócio 
	sem conhecimento técnico.
4. Testado por usuários, analistas e desenvolvedores para 
	garantir eficiência.
	
- O programa é uma caixa preta cujo comportamento é determinado
	destudando-se as suas entradas e saídas.
	
- Os casos de testes são derivados da especificação funcional.

- Os casos de teste são definidos com base na especificação 
	do software (descrições, casos de uso, requisitos, diagramas,
	etc.)

- Envolve dois passos:
	1. identificar as funções que o software deve realizar
		(especificação dos requisitos)
	2. Criar casos de teste capazes de checar se essas funcoes
		estão sendo executadas corretamente.
		
### Exemplo de teste de caixa preta 
- Um site de compras deve calcular descontos corretamente no
	carrinho.
- O testador insere cupons e verifica se os valores são ajustados
	corretamente.
- O sistema deve seguir as regras definidas, sem necessidade de
	revisar o código.
- Se um erro for encontrado, os desenvolvedores corrigem a
	lógica do cálculo.
	
### Testes de Caixa Branca 
- Tem o foco em determinar se o software sob teste exercita 
	todas as estruturas de programação.
	
- Seu principal objetivo é encontrar falhas no software por meio 
	da análise de sua estrutura interna.
	
- O que observar:
	- Condicionais e decisões,
	- Laços de repetição,
	- Caminhos executados,
	- Tratamento de exceções,
	- Vulnerabilidades no código.

- Analisa a estrutura interna do código para validar seu
	funcionamento correto.
- Examina fluxos de controle, loops e condições para garantir
	eficiência.
- Requer conhecimento técnico para identificar falhas e otimizar o
	desempenho.
- Muito utilizado para aumentar a segurança e a robustez do
	software.
	
### Exemplo de teste de caixa branca 
- No login de um sistema, é necessário bloquear acessos após
	tentativas falhas.
- O testador verifica se a lógica do código realmente impede
	múltiplas tentativas.
- Testes analisam se todas as condições e os caminhos do código
	foram cobertos.
- O objetivo é evitar brechas de segurança e garantir a lógica
	correta do software.
	
### Testes de caixa cinza
- Combina aspectos dos testes de caixa preta e caixa branca para
	maior precisão.
- O testador tem conhecimento parcial da estrutura interna do
	sistema.
- Ajuda a criar testes mais eficazes, equilibrando desempenho e
	segurança.
- Permite descobrir falhas que não seriam detectadas apenas com
	uma abordagem.

### Exemplo de teste de caixa cinza
- Um sistema criptografa senhas antes de armazená-las no
	banco de dados.
- O testador insere senhas com caracteres especiais e avalia
	como o sistema responde.
- Conhecendo parcialmente a lógica interna, verifica se a
	criptografia é aplicada corretamente.
- Isso ajuda a garantir a segurança dos dados e evitar
	vulnerabilidades
	
### Teste de regressão 
- Garante que atualizações ou correções não causem falhas em partes já
	testadas.
- Reexecuta testes anteriores para validar a estabilidade após mudanças
	no software.
- Previne o retorno de bugs antigos que poderiam afetar o funcionamento
	do sistema.
- Essencial para garantir qualidade em projetos de software contínuos e
	iterativos

### Exemplo de teste de regressão 
- Um aplicativo de banco adiciona um novo método de
	pagamento digital.
- Os testadores verificam se as funções antigas de pagamento
	ainda funcionam corretamente.
- Qualquer erro pode comprometer transações financeiras e gerar
	prejuízos.
- O teste de regressão reduz esses riscos, garantindo a
	estabilidade do sistema.
	
### Testes não Funcionais 
• Avaliam características como desempenho, segurança,
	usabilidade e compatibilidade.
• Diferente dos testes funcionais, analisam a experiência do
	usuário e a resposta do sistema.
• São fundamentais para garantir que o software seja rápido,
	seguro e eficiente.
• Ajudam a medir a escalabilidade do sistema para suportar
	diferentes cargas de uso.
	
### Exemplos de testes não funcionais 
1. Teste de desempenho: avalia o tempo de resposta do sistema
	sob diferentes condições.
2. Teste de segurança: detecta vulnerabilidades e protege dados
	sensíveis dos usuários.
3. Teste de compatibilidade: verifica se o software funciona
	corretamente em diferentes dispositivos.
4. Teste de usabilidade: mede a facilidade de uso da interface
	para melhorar a experiência do usuário.
	
### Quando utilizar cada teste?
- O teste de caixa preta é ideal para validar requisitos sem
	analisar o código-fonte.

- O teste de caixa branca é essencial para verificar fluxos
	internos e melhorar a segurança.
- O teste de caixa cinza combina ambos para garantir cobertura
	ampla e eficaz.
- Testes de regressão evitam que atualizações quebrem funções
	já testadas.
	
## U2A4 - Ciclo de Vida de Programas e atualizações 
***
### Planejamento do Ciclo de Vida do Software
• Softwares possuem um ciclo de vida com início, evolução
e fim, exigindo planejamento estratégico.
• A falta de gestão adequada pode levar a custos
elevados, falhas de segurança e insatisfação dos
usuários.
• Empresas líderes estabelecem cronogramas claros para
atualizações, suporte e substituição.
• Esta apresentação explora como estruturar um ciclo de
vida eficiente para maximizar desempenho e longevidade.

- Ciclo de vida de um software 
	1. Planejamento,
	2. Análise de requisitos,
	3. Design
	4. Codificação e Testagem,
	5. Implantação,
	6. Manutenção.

### Manutenção Contínua 
- Detectar falhas em produção com monitoramento em tempo real.
- Corrigir defeitos antes que comprometam a estabilidade da 
	aplicação.
- Otimizar desemplenho a partir de métricas, logs e feedbacks
	dos usuários.
- Automatizar entregas para reduzir erro humano e aumentar 
	previsibilidade.
- Ferramentas:
	- Sentry e New Relic: rastreamento de erros.
	- Datadog e AppDynamics: observabilidade.
	- Jenkins e GitHub Actions: CI/CD.
	
### Automação de Testes como Rede de Proteção
- Sem automação:
	- Validação manual demorada,
	- Baixa previsibilidade,
	- Medo de alterar código legado,
	- Maior chance de regressão.
	
- Com automação:
	- Feedback contínuo,
	- Cobertura do comportamento esperado,
	- Refatorações mais seguras,
	- Evolução com menor risco.
	
### Substituição segura de sistemas legados
1. Mapear dependências
2. Separar essencial 
3. Escolher estratégia 
4. Testar e migrar
5. Preparar rollback

### Obsolescência: quando o sistema vira obstáculo
- Bibliotecas, frameworks ou banco de dados desatualizados,
- Dificuldade de integrar novos serviços ou APIs,
- Aumento de bugs, falhas de segurança e lentidão,
- Conhecimento concentrado em poucos profissionais,
- Novas demandas de negócio inviáveis na arquitetura atual.

- Como decidir
	- Manter: baixo risco e boa aderência ao negócio.
	- Refatorar: valor alto, mas estrutura degradada.
	- Modernizar: trocar partes críticas progressivamente.
	- Substituir: custo e risco superam o valor de manter.
	
# Unidade 3 - Metodologias Ágeis
***
## U3A1 - Metodologias Ágeis e a Automação de Testes 
***
### Por Que Falar em Agilidade?
- Modelos tradicionais funcionam bem quando o escopo é estavel.
	Porém, em muitos projetos de software, requisitos mudam, riscos
	aparecem e o cliente aprende durante o processo.
	
- Do plano rígido para a adaptação orientada por feedback
	1. Mudança frequente: Requisito evoluem com o mercado e com 
		o uso real 
	2. Ciclos Curtos: Entregas menores permitem validação mais 
		rapida.
	3. Colaboração: Equipe e cliente reduzem dúvidas ao conversar
		contínuamnete.
	4. Valor Contínuo: O foco passa a ser entregar algo útil a
		cada incremento.
		
### Manifesto Ágil 
- Indivíduos e interações -> mais que processos e ferramentas
- Software em funcionamento -> mais que documentação extensa
- Colaboração com o cliente -> mais que negociação contratual
- Resposta a mudança -> mais que seguir um plano fixo

### Transformação digital e agilidade
• As metodologias ágeis surgem como resposta à
	necessidade de adaptação rápida a mudanças constantes.
• Na prática, elas priorizam ciclos curtos de entrega e
	feedback contínuo com o cliente.
• A implementação começa com mudanças culturais
	dentro das equipes de TI.
• O foco é garantir entregas constantes de valor,
	adaptando-se ao longo do projeto.

### Fundamentos das metodologias ágeis
• O Manifesto Ágil define princípios como colaboração e
	resposta a mudanças.
• Na aplicação, isso exige eliminar estruturas rígidas e adotar
	práticas iterativas.
• As equipes se organizam em torno de metas de curto prazo,
	com planejamento adaptável.
• Cada ciclo inclui planejamento, execução, revisão e
	retrospectiva para ajustes constantes.

### O papel das equipes ágeis
• Equipes ágeis são multidisciplinares e auto-organizadas.
• Elas decidem juntas como dividir tarefas e solucionar
	problemas.
• O processo é guiado por reuniões diárias de alinhamento e
	ciclos curtos de entrega.
• A transparência e a comunicação contínua são essenciais para
	o funcionamento eficiente.

### Introdução ao Scrum
• Scrum divide o trabalho em sprints, que duram de 1 a
	4 semanas.
• Durante cada sprint, há planejamento, execução e
	entrega de um incremento de produto.
• O Product Owner prioriza as tarefas, o Scrum Master
	garante o processo e o time executa.
• Reuniões diárias chamadas Daily Scrum mantêm todos
	alinhados sobre progresso e obstáculos

### Como funciona o Kanban
• O Kanban utiliza quadros visuais para mapear o fluxo de
	trabalho.
• Cada tarefa passa por colunas como “A Fazer”, “Em
	Progresso” e “Concluído”.
• A equipe limita a quantidade de tarefas em andamento
	para evitar sobrecarga.
• As melhorias ocorrem com base na observação contínua
	do fluxo e dos gargalos

### Testes no ágil: uma nova postura
• Os testes deixam de ser uma etapa final e passam a ser
	contínuos.
• O testador participa do planejamento desde o início do
	sprint.
• Os testes são realizados em paralelo ao desenvolvimento,
	com automação sempre que possível.
• A meta é identificar falhas rapidamente e evitar retrabalho
	futuro.

### Testes automatizados e entrega contínua
• A automação permite testes rápidos e repetíveis em
	cada integração de código.
• Ferramentas como Jenkins e Selenium são integradas ao
	fluxo de desenvolvimento.
• Cada modificação no sistema aciona automaticamente
	uma bateria de testes.
• A entrega contínua só é possível com uma base sólida
	de testes automatizados.

- Planejar -> Codificar -> Testar -> Corrigir -> Entregar

### Novo Papel do Testador em Equipes Ágeis 
- Antes da sprint 
	- ajuda a tornar requísitos testáveis
	- ex. revisar críterios de aceitação
	
- Durante a aprint
	- colaborar com devs e automatiza verificações
	- ex. criar testes de regressão 
	
- Depois da entrega 
	- analisa resultados e apoia melhoria contínua 
	- ex. propor ajustes na retrospectiva.

### Comunicação e feedback nos testes ágeis
• Os testes se baseiam em comunicação direta entre
	desenvolvedores e testadores.
• As falhas são discutidas em tempo real, promovendo
	correções mais ágeis.
• O feedback é incorporado imediatamente ao ciclo de
	desenvolvimento.
• Isso reduz retrabalho e aumenta a qualidade do produto
	final

### Agilidade e qualidade
• Agilidade não significa pressa, mas entrega inteligente e
	incremental.
• A qualidade é construída desde o início, com testes unitários e
	validações contínuas.
• Cada sprint busca um produto utilizável e testado.
• Esse modelo previne acúmulo de erros e acelera a entrega de
	valor.

### Gestão ágil com Scrum
• O Scrum estrutura o gerenciamento em ciclos bem
	definidos.
• Cada sprint começa com uma reunião de planejamento
	detalhada.
• As metas são revisadas e refinadas constantemente junto
	ao Product Owner.
• O progresso é medido por entregas incrementais e
	reuniões de retrospectiva.

### Vantagens reais das metodologias ágeis
• Com ágil, equipes reagem melhor a mudanças de escopo e
	exigências.
• A colaboração entre áreas é reforçada por reuniões frequentes
	e objetivos comuns.
• A transparência e visibilidade reduzem erros de comunicação e
	falhas de entrega.
• Os projetos se tornam mais previsíveis e com maior qualidade
	percebida.

### Limitações e desvios comuns
• Nem toda adoção de ágil gera bons resultados de forma
	automática.
• A falta de compreensão dos princípios pode levar a uma
	“agilidade de fachada”.
• Processos são seguidos, mas a colaboração e adaptação
	real são ignoradas.
• É preciso revisar constantemente práticas e valores para
	garantir a efetividade.
	
## U3A2 - Ferramentas Case para automação de Testes 
***
### Ferramentas Case 
- Definição Prática 
	- Ferramentas que apoiam atividades de desenvolvimento, 
		manutenção, documentação e testes, reduzindo esforço manual 
		e aumentando padronização.
		
- O que elas ajudam a fazer?
	+ modelar requisitos e arquitetura;
	+ rastrear mudanças e artefatos;
	+ gerar ou validar casos de teste;
	+ executar testes automatizados;
	+ registrar métricas e relatórios.
	
### Upper CASE x Lower CASE 
- Upper CASE 
	+ atua nas fases iniciais;
	+ apoia requisitos, análise e projeto;
	+ favorece modelos, diagramas e arquítetura;
	+ antecipa problemas estruturais.
	
- Lower CASE 
	+ atua nas fases técnicas;
	+ apoia codificação, testes e manutenção;
	+ integra depuração, controle de versões e execução 
		automatizada;
	+ reduz retrabalho na implementação.

- Concepção -> Realização Técnica 
	1. Requísitos 
	2. Análise 
	3. Projeto 
	4. Código 
	5. Testes 
	6. Manutenção
	
### O que é orientação a objetos no software
• A orientação a objetos é um paradigma de programação
	baseado em objetos.
• Cada objeto representa uma entidade com atributos
	(dados) e métodos (comportamentos).
• Esse modelo busca refletir estruturas do mundo real no
	software.
• Facilita a organização, manutenção e reutilização de
	código em sistemas complexos.

### Por que OO ajuda na automação?
+ Classes e métodos menores facilitam testes unitários;
+ Encapsulamento ajuda a validar comportamentos por interfaces 
	públicas.
+ Herança e polimorfismo permitem reaproveitar testes em 
	subclasses.
+ Baixo acoplamento reduz efeitos colaterais entre módulos.

### Exemplos de ferramentas OO 
• Ferramentas como Enterprise Architect, Visual Paradigm e
	StarUML são amplamente utilizadas.
• Elas possibilitam modelagem visual e documentação
	automatizada de sistemas.
• Oferecem integração com IDEs e linguagens como Java, Python
	e C++.
• São valiosas para grandes equipes que atuam em ambientes
	colaborativos.

### Realidade Virtual nos Testes 
- Aplicações possiveis:
	+ jogos digitais e aplicativos interativos;
	+ treinamento em ambientes críticos;
	+ sistemas de saúde, segurança e aviação;
	+ validação de interfaces tridimensionais;
	+ simulações perigosas, caras ou impraticáveis no mundo real.
	
## U3A3 - Etapas de Elaboração e Testagem de Programas 
***
### Escopo: O que entra e o que fica de fora 
- O que entra:
	+ Funcionalidades combinadas
	+ Requisitos principais 
	+ critérios de Aceitação
	+ Integrações necessárias
	
- O que fica de fora:
	+ Funcionalidades futuras 
	+ Demandas não priorizadas 
	+ Restrições técnicas 
	+ Mudanças fora do acordo
	
### Perguntas para definir um bom escopo 
+ Qual problema o sistema deve resolver?
+ Quem usará o sistema e em quais situações?
+ Quais funcionalidades são obrigatórias nesta entrega?
+ Quais restrições de prazo, custo e tecnologia existem?
+ Como saberemos que a funcionalidade está correta?
+ O que será adiado para versões futuras?

### Do Escopo ao Teste
+ Cada funcionalidade combinada deve gerar um ou mais testes.
+ Requisitos críticos merecem testes mais detalhados e repetiveis.
+ Mudanças no escopo devem atualizar plano, casos e dados de teste.
+ Testar "o que foi combinado" evita tanto lacunas quanto 
	excesso de trabalho.
	
### Tipos de Testes no Ciclo do Programa 
- Unitário: Verifica pequenas partes do código: funções, métodos
	ou classes.
- Integração: Avalia se módulos, APIs e banco de dados funcionam
	em conjunto.
- Sistema: Testa o comportamento do em cenário próximo ao real.
- Aceitação: Confirma se a entrega atende às necessidades do 
	cliente e ao escopo.
	
### Escolha da Linguagem de Programação 
+ Tipo de aplicação: web, embarcada, corporativa, científica,
	tempo real, etc.
+ Desempenho esperado: tempo de resposta, uso de memória, volume
	de dados.
+ Manutenção: legibilidade, organização, facilidade para 
	evoluir o código.
+ Integração: banco de dados, APIs, serviços em nuvem e Sistemas
	legados.
+ Equipe: experiência, curva de aprendizado e disponibilidade
	de suporte.
	
### Comparando Decisões Técnicas 
- C/C++:
	+ Alto desempenho e controle de memória.
	- Mais cuidado com ponteiros, memória e testes.
	
- Java:
	+ Robustez, portabilidade e uso corporativo.
	- Depende da JVM e de configuração do ambiente.
	
- Python:
	+ Legibilidade, produtividade e bibliotecas.
	- Pode exigir otimização para tarefas intensivas.
	
- JavaScript:
	+ Aplicações web e integração com APIs.
	- Ecossistema amplo e mudanças frequentes 
	
### Linguagem, Desempenho e Manutenção 
- Baixo nível
	+ Mais controle sobre a memória e recursos,
	+ Útil para alto desempenho,
	+ Exige mais atenção a detalhes técnicos.
	
- Alto nível 
	+ Código mais legivel e produtivo,
	+ Boa manutenção e bibliotecas prontas,
	+ Pode precisar de otimização em dados intensivos.
	
- Exemplo prático:
	+ Python pode usar NumPy ou pandas para acelerar o 
		processamento de dados, combinando código de alto nivel com 
		bibliotecas otimizadas.
		
## U3A4 - Hackers Éticos e Detecção de Falhas 
***
### Quem é o hacker éticos?
> Profissional autorizado a usar técnicas de hacking para 
	encontrar vulnerabilidades antes que elas sejam exploradas
	por criminosos.
	
+ Atua dentro de escopo definido e documentado.
+ Simula ataques reais sem finalidade destrutíva.
+ Produz evidências, recomendações e prioridades de correção.
+ Ajuda a aumentar a maturidade de segurança da organização.
	
### Pentest: Simulação controlada de ataque
> O teste de penetração avalia a robustez do sistema simulando
	ataques reais, externos ou internos, sempre com autorização
	e objetivo defensivo.
	
1. Reconhecimento: Coleta de informações sobre ambiente e 
	superficie de ataque.

2. Mapeamento: Identificação de serviços, portas, versões e 
	expostos.

3. Exploração controlada: Teste de falhas com limite de escopo
	e sem dano operacional.
	
4. Relatório: Evidências, criticidade e ações corretivas.

### Análise de Vulnerabilidades 
> É a identificação sistemática de falhas, normalmente 
	combinando ferramentas automatizadas e investigação manual.
	
- Ferramentas automatizadas
	+ Varredura de falhas conhecidas;
	+ Rapidez e ampla cobertura;
	+ Ajuda a priorizar correções.
	
- Investigação manual 
	+ Valida resultados;
	+ Encontra falhas mais sofisticadas;
	+ Analísa contexto e impacto real.
	
- Resultado 
	-	Mapa de Vulnerabilidades por risco, criticidade e 
		prioridade de correção.
		
### Pentest X Análise de Vulnerabilidades 
- Pentest 
	+ Simula ataques reais e controlados;
	+ Busca medir o impacto prático de uma falha;
	+ Produz evidências de exploração e recomendações;
	+ É indicado para ambientes críticos e validação de controle.
	
- Análise de Vulnerabilidades
	+ Identifica e classifica falhas de segurança;
	+ Combina varreduras automatizadas e validação manual;
	+ Ajuda a montar uma lista priorizada de correções;
	+ É útil como rotina periódica e monitoramento contínuo.
	
> Métodos complementares: um mostra onde estão as falhas; o 
	outro testa até onde elas podem ir.
	
### Falhas Comuns Encontradas
1. Configuração Incorreta: Permissões abertas, serviços 
	expostos ou politicas frágeis.
	
2. Sistemas Desatualizados: Versões antigas acumulam 
	vulnerabilidades conhecidas.
	
3. Autenticação Fraca: Senhas simples, ausência de MFA ou
	sessões mal protegidas.
	
4. Controle de Acesso Insuficiente: Usuários acessam dados ou 
	funções alêm do necessário.
	
5. Falhas Humanas: Phishing, Compartilhamento indevido e baixa 
	conscientização.
	
# Unidade 4 - TDD(Test Driven Development) e BDD (Behavior Driven Development)
***
## U4A1 - Métodos Ágeis 
***
### Por que testes combinam com métodos ágeis?
> Requisito refinado -> Teste antecipado -> 
	Código com feedback  -> Entrega mais confiável.

+ Em sprints curtas, falhas descobertas tarde custam caro.
+ Testes automatizados criam uma rede de segurança para 
	mudanças frequentes.
+ Critérios claros aproximam equipe técnica, negócio e usuários.

### TDD: Desenvolvimento Orientado por Testes 
+ Foco princípal: unidade de código, lógica interna e design 
	incremental.
+ Beneficio: maior segurança para alterar e evoluir o sistema.
+ Exemplos de ferramentes: Junit, NUnit, PyTest, Jest

### Exemplo de TDD 
```Teste antes do código
@Test 
void 
deveCalcularValorTotalDaCOnsulta() {
	Agendamento a = new Agendamento(120.00, 2);
	assertEquals(240.00, a.valorTotal());
}
```

``` Implementação minima
class Agendamento {
	double valor;
	int qtd;
	
	double valorTotal() {
		return valor * qtd;
	}
}
```

+ O teste expressa uma expectativa objetiva.
+ O código é escrito para passar no teste.
+ A refatoração melhora a estrutura sem quebrar o comportamento.

### BDD: Desenvolvimento Orientado por Comportamento 
> História de usuário -> critérios de aceitação -> cenários 
	Gherkin -> Testes automatizados 
	
+ Foco principal: comportamento visivel ao usuário e valor de 
	negócio.
+ Cenários podem ser lidos por desenvolvedores, testadores e 
	stakeholders.
+ Exemplos de ferramentas: Cucumber, SpecFlow, Behave.

### Exemplo de BDD com Gherkin 
> Funcionalidade: agendamento de consulta 
> Cenário: Horário disponivel
+ Dado que existe horário livre às 14h
+ Quando o paciente confirma a consulta 
+ Então o sistema confirma a consulta 
+ E envia uma notificação ao paciente 

- Dado: contexto inicial 
- Quando: ação do usuário 
- Então: resultado esperado 

+ Serve como especificação, teste e documentação viva.
+ Reduz interpretações diferentes sobre uma mesma história.

### TDD e BDD: diferenças principais 
- Foco:
	+ TDD: Código e unidades técnicas 
	+ BDD: Comportamento e valor de negócio 
	
- Linguagem:
	+ TDD: Técnica, voltada ao programador
	+ BDD: Natural, próxima ao domínio
	
- Momento:
	+ TDD: Antes da implementação da unidade 
	+ BDD: No refinamento dos requísitos 
	
- Resultado:
	+ TDD: Código mais testável e seguro 
	+ BDD: Critérios claros e documentação viva.
	
> Resumo: TDD pergunta "o código está correto?", o BDD pergunta 
	" o sistema faz o que o usuário espera?"
	
### Como integrar BDD e TDD na sprint 
> Refinar História com negócio -> Escrever cenários BDD 
	-> Criar testes unitarios TDD -> Implementar e refatorar 
	-> Executar no pipeline.
	
+ Critérios de aceitação viram cenários automatizados.
+ Desenvolvedores implementam as unidades que sustentam esses 
	comportamentos.
+ A integração continua executa os testes a cada alteração.

## U4A2 - Práticas de Desenvolvimento Guiado por Comportamento (BDD)
***
### Introdução aos Cenários BDD Práticos
+ O BDD foca em descrever comportamentos do usuário.
+ Cenários são exemplos claros que explicam esses 
	comportamentos.
+ Eles ajudam a evitar mal-entendidos entre equipes.

### Estrutura Básica de um Cenário BDD 
1. Um cenário segue o formato Given-When-Then.
2. Given define o contexto inicial da situação.
3. When descreve a ação executada pelo usuário.
4. Then mostra o resultado esperado dessa ação.

### Given 
+ O Given define o contexto inicial em que o cenário acontece.
+ Ele descreve o estado do sistema ou as confições prévias 
	necessárias.
+ É o ponto de partida que garante que o ambiente está pronto
	para o teste.
+ Por exemplo, "Dado que o usuário está logado", significa que 
	o usuário já acessou o sistema antes da ação.
	
### When 
+ O When representa a ação ou evento realizado pelo usuário ou 
	pelo sistema.
+ É o gatilho que inicia o comportamento que queremos validar.
+ Essa etapa foca em descrever exatamente o que acontece no 
	teste.
+ Por exemplo, "Quando o usuário clicar no botão de salvar"
	indica a ação que deve ser executada.
	
### Then 
+ O Then descreve o resultado esperado após a ação executada.
+ Ele valida se o sistema respondeu corretamente ao 
	comportamento solicitado.
+ Essa etapa define o critério de sucesso do cenário.
+ Por exemplo, "Então o sistema deve mostrar uma mensagem de 
	confirmação" demonstra o resultado esperado.
	
### Exemplo Simples de Cenário em Gherkin 
+ Given que o usuário está logado no sistem.
+ When ele solicita a retirada de um produto do carrinho.
+ Then o produto é removido da lista de compras.
+ Este exemplo demonstra um fluxo comum de usuário.

### Benefícios de Escrever Cenários Claros 
+ Facilitam o entendimento entre times técnicos e de negócios.
+ Servem como documentação viva do sistema.
+ São base para criação de testes automatizados.
+ Reduzem erros causados por requisitos mal definidos.

### Introdução ao Cucumber 
+ Cucumber é uma das ferramentas mais utilizadas para 
	implementar BDD em projetos de software.
+ ela permite que cenários escritos em linguagem natural,
	como Gherkin, sejam traduzidos em testes automatizados.
+ Essa integração facilita o entendimento entre 
	desenvolvedores, testadores e clientes, promovendo 
	colaboração.
+ Além de Ruby, o Cucumber suporta várias linguagens,
	tornando-o flexível para diferentes equipes e projetos.
	
### Como o Cucumber Funciona 
+ O Cucumber interpreta arquivos com exetensão .feature que 
	contêm cenários escritos em Gherkin.
	
+ Cada passo do cenário precisa estar mapeado para um código 
	chamada "step definition".
+ Quando executado, o Cucumber percorre esses passos para 
	validar se o sistema está funcionando conforme o esperado.
	
+ Testes bem sucedidos indicam conformidade, enquanto falhas 
	revelam discrepâncias que precisam ser corrigidas.
	
### Exemplo de Step Definition no Cucumber 
+ No Cucumber, cada linha do cenário corresponde a uma função
	no código fonte.
	
+ Por exemplo, "Given que o usuário está logado" pode chamar 
	um script que simula o login.
	
+ Essas funções interagem com o sistema, realizando ações ou 
	verificações automáticas.
	
+ Essa abordagem une a documentação clara dos cenários com 
	a execução prática dos testes.
	
### Introdução ao Behave 
+ Behave é a ferramenta BDD mais popular para projetos escritos 
	em Python.
	
+ Ela segue o mesmo padrão do Cucumber, utilizando arquivos 
	.feature com cenários em Gherkin.
	
+ O Behave é ideal para equipes que preferem desenvolver em 
	Python, mantendo a consistência do código.
	
+ Além disso, o Behave facilita a integração com outras 
	bibliotecas e frameworks Python de teste.
	
### Estrutura do  Behave 
1. Os cenários ficam em arquivos .feature, escritos com a 
	linguagem Gherkin.
	
2. As ações e verificações são implementadas em arquivos 
	Python chamados "steps".
	
3. Cada passo do cenário tem uma função correspondente, que 
	manipula o ambiente ou valida resultados.
	
4. O Behave executa os cenários em sequência, fornecendo 
	relatórios detalhados sobre o sucesso ou falha dos testes.
	
### Criando um Cenário Prático no Behave 
+ Imagine um cenário onde um cliente faz uma tranferência
	bancária com saldo suficiente.
	
+ O Given configura a conta do cliente com o saldo inicial 
	necessário.
	
+ O When executa a ação de transferir o valor para outra pessoa.

+ O Then verifica se o saldo foi atualizado corretamente após 
	a operação.
	
### Escrevendo Cenários Completos e Detalhados 
+ Um bom cenário deve contemplar situações reais e também
	possíveis erros ou exceções.
	
+ Cada passo deve ser claro, evitando termos técnicos que 
	confundam os envolvidos.
	
+ Cenários muito genéricos dificultam a automação e a 
	validação do comportamento esperado.
	
+ A linguagem usada deve ser acessível para desenvolvedores 
	e partes interessadas.
	
### Ligando Cenários ao Código Automatizado 
+ A Ponte entre cenários e código são as chamadas "step 
	definitions".
	
+ essas funções traduzem os passos em comandos que interagem 
	com o sistema.

+ Elas podem manipular os dados, executar ações e validar 
	respostas automaticamente.
	
+ Assim, os cenários escritos em linguagem natural tornam-se
	testes funcionais executáveis.
	
### Executando e Validadndo Cenários BDD 
+ Ao executar, o Cucumber ou Behave interpreta cada passo do 
	cenário.
	
+ Se o comportamento do sistema corresponde ao esperado, o 
	teste é aprovado.
	
+ Se houver divergência, o teste falha e gera relatórios para 
	análise rápida.
	
+ Essa validação contínua ajuda a detectar problemas logo no 
	desenvolvimento.
	
### Integração com Pipelines de CI/CD 
+ Os cenários BDD podem ser automatizados dentro de pipelines 
	de integração contínua.
	
+ Isso permite que testes rodem automaticamente a cada 
	alteração no código.
	
+ Falhas nos testes impedem a propagação de erros para 
	ambientes de produção.
	
+ Essa prática promove maior qualidade e confiança nas 
	entregas de software.
	
### Dicas para Criar Cenários Eficientes
+ Cenários devem focar em comportamentos essenciais do usuário 
	e do sistema.
	
+ Evite incluir muitos detalhes técnicos que não são relevantes 
	para o comportamento.
	
+ Reutilize passos comuns para facilitar a manutenção dos 
	testes automatizados.
	
+ Mantenha a documentação atualizada para refletir mudanças 
	no sistema.
	
## U4A3 - Desenvolvimento Orientado a Testes (TDD)
***
### Test-Driven Development (TDD)
• Prática essencial para desenvolvimento ágil.
• Apesar de seus benefícios, muitos caem em armadilhas que 
	prejudicam a eficiência.
• Neste vídeo, vamos mostrar como evitar os erros mais comuns 
	ao usar TDD.
• Nosso objetivo é tornar sua aplicação de TDD mais segura e 
	produtiva.

### O que é TDD?
• TDD é uma metodologia em que primeiro se escreve o teste, 
	depois o código.
• O ciclo clássico é: 
	Escrever o teste >> Implementar o código >> Refatorar.
• Esse processo ajuda a criar software mais confiável e bem 
	estruturado.
• Além disso, TDD facilita mudanças e garante que o código 
	atenda aos requisitos.
	
### Vantagens do TDD 
• TDD ajuda a encontrar falhas logo no início do 
	desenvolvimento.
• Melhora a qualidade do código, reduz retrabalho e facilita 
	manutenção.
• Estimula um design orientado ao comportamento, com foco em 
	funcionalidades.
• Mas, quando mal utilizado, pode gerar excesso de burocracia 
	e frustração.
	
### Por que falar sobre armadilhas?
• Muitos desenvolvedores iniciam com TDD, mas cometem erros 
	críticos.
• Esses erros comprometem a eficiência e desmotivam o uso da 
	prática.
• Evitar essas armadilhas permite extrair o máximo dos 
	benefícios do TDD.
• Nos próximos slides, vamos analisar as principais armadilhas 
	e como superá-las.
	
### Armadilha 1: testes superficiais
• Testes rasos não capturam comportamentos importantes do 
	sistema.
• Quando o teste não representa a realidade, o código fica 
	vulnerável.
• O risco é criar uma falsa sensação de segurança no software.
• É essencial que os testes sejam relevantes e desafiadores 
	para o código.
	
### Como evitar testes superficiais?
• Estude e compreenda profundamente os requisitos do sistema.
• Pense em diferentes cenários, inclusive os casos extremos 
	e falhas.
• Escreva testes que realmente validem comportamentos 
	essenciais e não triviais.
• Garanta que, se algo quebrar, o teste falhe, cumprindo sua 
	função.
	
### Armadilha 2: excesso de testes
• Alguns desenvolvedores tentam testar absolutamente tudo, 
	sem critério.
• Esse excesso torna a suíte de testes lenta e difícil de 
	manter.
• Além disso, muitos testes podem se tornar redundantes e 
	inúteis.
• O foco deve ser testar o que realmente importa para o 
	funcionamento.
	
### Como evitar excesso de testes?
• Priorize o teste de unidades críticas e pontos frágeis
	do sistema.
• Evite testar implementações internas que podem mudar 
	facilmente.
• Mantenha uma suíte de testes enxuta, eficiente e com 
	propósito claro.
• Revise periodicamente os testes e elimine os que não agregam 
	valor.
	
### Armadilha 3: paralisia de análise
• TDD pode gerar uma obsessão por prever todos os casos de 
	teste.
• Isso leva à paralisia, em que o desenvolvedor teme começar 
	sem “o teste perfeito”.
• A tentativa de prever tudo trava o desenvolvimento e 
	prejudica a produtividade.
• TDD deve ser uma prática iterativa, não um bloqueio criativo.

### Como evitar a paralisia de análise?
• Comece com testes simples e evolua conforme o entendimento 
	aumenta.
• Aceite que os testes podem e devem ser ajustados ao longo 
	do tempo.
• Evite buscar perfeição absoluta desde o início, foque no 
	progresso.
• Confie no ciclo iterativo de TDD para melhorar gradualmente.

### Armadilha 4: ignorar a refatoração
• Após passar no teste, muitos pulam a etapa de refatoração 
	por pressa.
• Isso acumula “dívidas técnicas” e prejudica a qualidade do
	código.
• Refatorar é essencial para manter o código limpo e 
	sustentável.
• Sem refatoração, o código pode se tornar confuso e difícil
	de manter.

### Como evitar ignorar a refatoração?
• Incorpore a refatoração como parte obrigatória do ciclo TDD.
• Após passar no teste, sempre revise o código para melhorar 
	clareza e estrutura.
• Busque eliminar duplicações, melhorar nomes e simplificar 
	lógicas.
• Valorize a manutenção contínua como parte do processo de 
	desenvolvimento.

### Armadilha 5: esquecer o design do sistema 
• TDD ajuda no design, mas não substitui boas práticas 
	arquiteturais.
• Alguns focam demais nos testes e esquecem de pensar na 
	estrutura geral.
• O resultado é um sistema com testes, mas difícil de evoluir 
	ou manter.
• TDD deve ser aliado de um bom design, não um substituto.

### Como evitar esquecer o design?
• Antes de escrever testes, reflita sobre a arquitetura e 
	responsabilidades do sistema.
• Use princípios de design como SOLID para guiar a estrutura 
	do código.
• Deixe que os testes orientem a implementação, mas não 
	dominem o design.
• Lembre: bons testes surgem de um bom design, e vice-versa.

### Dicas finais para evitar armadilhas
• Comece a aplicar TDD em projetos pequenos e evolua 
	gradualmente.
• Revise continuamente sua prática para identificar melhorias 
	e eliminar vícios.
• Não tenha medo de ajustar sua abordagem conforme ganha 
	experiência.
• Lembre-se: TDD é uma ferramenta poderosa, mas depende de 
	bom senso.
	
## U4A4 - Futuro da Qualidade e da Testagem em Software 
***
### Por que falar em futuro da testagem?
+ Sistemas atuais combinam software, sensores, redes, nuvem 
	e múltiplos dispositivos.

+ O número de cenários possíveis cresce rapidamente e 
	inviabiliza testes totalmente manuais.

+ Qualidade passa a envolver funcionalidade, desempenho, 
	segurança, escalabilidade e experiência do usuário. 
	
> Quanto mais conectado e dinâmico o sistema, mais o teste 
	precisa ser contínuo, observável e inteligente.
	
### IoT: quando o teste encontra o mundo físico
+ Dispositivos diferentes: sensores, wearables, celulares, 
	controladores e plataformas embarcadas.
	
+ Redes heterogênias: Wi-Fi, 4G/5G, Bluetooth, protocolos 
	próprios e instabilidade de sinal.
	
+ Dados contínuos: eventos em tempo real exigem monitoramento,
	simulação e validação constante.
	
### 5G e sistemas distribuídos 
+ Aplicações críticas em tempo real exigem resposta imediata e 
	alta disponibilidade.
	
+ A carga fica distribuida entre nós, serviços, borda, nuvem 
	e dispositivos finais.
	
+ Os testes precisam simular variações de rede, falhas de 
	sicronização e aumento de usuários.
	
### Exemplo prático: jogo digital com IoT e 5G
+ Um jogo em realidade aumentada usa câmera, sensores, 
	localização, nuvem e conexão móvel.
	
+ Uma falha de sicronização pode gerar atraso, travamento, 
	perda de estado ou vantagem injusta.
	
+ Testar envolve desempenho, segurança, interoperabilidade e 
	comportamento do jogador.
	
- Jogador: ação 
- Dispositivo: sensores 
- Rede 5G: latência
- Nuvem: processamento 
- Jogo: resposta 

### Limites dos Testes Tradicionais 
+ O testador não consegue prever todas as combinações de 
	dispositivos, redes e ações possíveis.
	
+ A manutenção dos scripts cresce quando a interface, as regras 
	e os serviços mudam com frequência.
	
+ A automação precisa ser mais adaptativa, priorizada por 
	risco e integrada ao fluxo CI/CD.
	
### IA e ML na Automação de Testes 
+ Geração automática de casos com base em requisitos, logs 
	e comportamento histórico.
	
+ Priorização de testes com maior chance de encontrar falhas 
	após uma alteração do código.
	
+ Detecção de anomalias em métricas como latência, uso de 
	memória, travamentos e erros de rede.
	
- Dados -> Modelo -> Testes -> Falhas -> Dados ->

### Como um Teste Inteligente pode Funcionar 
1. Coletar dados: logs, bugs, uso real 
2. Aprender padrões: riscos e anomalias 
3. Gerar/priorizar: casos de teste 
4. Executar e analisar: feedback contínuo.

> Exemplo: após muitas falhas em login sob rede instável, o 
	modelo passa a priorizar cenários de autenticação com perda 
	de pacote e alta latência.
	
### Competência do profissional de QA (Quality Assurance)
+ Automação e programação de testes.
+ Conhecimentos de redes, nuvem, IoT, segurança e desempenho.
+ Noções de dados, Machine Learning e interpretação de métricas.
+ Capacidade de questionar resultados e transformar evidências 
	em decisões.
	
> O QA do futuro interpreta evidências e orienta decisões, 
	não apenas executa casos de teste.