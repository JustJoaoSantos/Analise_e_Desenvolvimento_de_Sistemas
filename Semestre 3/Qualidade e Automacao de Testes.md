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