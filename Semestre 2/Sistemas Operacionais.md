# U1A1 - Introducao aos sistemas operacionais
- oque é
	- Um sistema operacional é um software que gerencia os recursos de hardware e software de um computador
	- um intermediario entre software e hardware 
	- fornece uma interface entre o usuario e o computador para que o usuario possa utilizar estes servicos de forma intuitiva
	
- S.O / O.S
	- conjunto de rotinas executado pelo processador de forma semelhante aos progamas dos usuarios
	- controla o funcionamento de um computador gerenciando a utilizacao e o compartilhamento dos seus diversos recursos, como processadores, memorias e dispositivos de entrada e saida.

- os sistemas operacionais possuem duas funcoes
	- facilitar o acesso a recursos do sistema;
	- organizar o compartilhamento de recursos de forma a garantir a sua protecao
	
- camadas para a realizacao de tarefas
	- Usuario interage com aplicacoes -> aplicacoes interagem com o O.S -> O.S comunica com os dispositivos de hardware
 
- Modelo em camada que o sistema funciona em
	- Aplicaoes
	- Utilitarios
	- Sistema operacional
	- Linguagem de Maquina
	- Microprogramacao
	- Circuitos eletronicos

- Modelo de comunicacao
	- Aplicacoes 
	- Kernel (chamadas de sistema)
	- Microkernel (servicos de microkernel)
	- Hardware
	
- Principais servicos dos SO 
	- Meios para que um programa seja carregado em memoria e executado;
	- Um sistema de arquivos, permitindo criar, ler, escrever e excluir arquivos;
	- Uma interface de acesso aos perifericos;
	- Mecanismos de monitoracao de recursos, capazes de identificar possiveis gargalos no sistema;
	- Meios para armazenar/manter o estado do sistema.
	
- Tipos de SOs
	- SO de computadores pessoais (e.g notebooks, desktop)
	- SO de servidores
	- SO embarcados / em hardware (e.g microwave) 
	- SO portateis (e.g cellphones)
	
# U1A2 - Evolucao dos sistemas operacionais
- OSs
	- 1 sistemas monotarefa/monoprogramaveis
		- UCP
		- Memoria principal
		- Dispositivos de E/S 
	- 2 sistemas multitarefa/multiprogramaveis
		- Sistemas Batch
		- Sistemas de tempo compartilhado
		- Sistemas de tempo real 
	- 3 Sistemas com multiprocessadores
		- Fracamente acoplados
			- SMP
			- NUVA
		- Fortemente acoplados
			- SOR (Sistemas Operacionais de Rede)
			- Sistemas Distribuidos
			
- monoprogramaveis
	- utiliza todo o recursos da maquina para realizar apenas uma tarefa 
	- fazio o processador ficar ocioso, por exemplo, se o usuario fizer apenas uma simples tarefa, mesmo que nao usase muito processador ele fazia apenas esta tarefa 
	
- Multiprogramaveis 
	- compartilhado de recursos e na possibilidade de trabalhar com mais de um aplicativo, ou o mesmo programa sendo processados ao mesmo tempo 
	- eles tambem sao clasificados em monousuario e multiusuario
	- Multiprogramavel monousuario 
		- utilizado por apenas um usuario, como computadores pessoais 
	- Multiprogramaveis Multiusuraio
		- compartilha os recursos como dispositidos de E/S entre varios usuarios
	
- Tipos de multiprogramaveis
	- Batch: armazenado em fita ou disco, nao exige interacao com usuario 
	- Tempo compartilhado: divide o tempo do processador em intervalos, cada usuario possui seu ambiente de trabalho proprio
	- Tempo Real: Precisam dedicar toda a sua capacidade de processamento para executar uma determinada tarefa.
	
- Multiplos processadores 
	- utiliza duas ou mais CPUs que trabalham em conjunto e isso significa que uma maquina pode realizar varias tarefas ao mesmo tempo 
	- Vantagem
		- Escabilidade: pode ampliar o potencial de processamento ao adicionar mais processadores
		- Disponibilidade: possibilidade de manter o processo em execucao mesmo no caso de falhas
		- Balanciemanete de carga: capasidade de distribuir o processamento de acordo com os processadores disponiveis aumentando a performance da maquina.
		
	- Fortemente Acoplado
		- ha varios processadores compartilhando uma unica memoria fisica e dispositivos E/S 
		- Simétricos: nos sistemas simétricos os processadores compartilham uma única memória e utilizam o mesmo sistema operacional.
		- Assimétricos: nos sistemas assimétricos existe um processador principal (mestre) que controla o sistema e delega atividades para os demais processadores.
	
	- Fracamente Acoplado	
		- Eles funcionam de forma independente, possuindo seu sistema operacional e gerenciando seus próprios recursos como memória, CPU e dispositivos de entrada e saída. O sistema é fracamente acoplado por depender de uma rede para distribuir as atividades do processamento
		- Operacionais de rede: os sistemas operacionais de rede são independentes e estão conectados por meio de uma rede. Nela, cada estação de trabalho ou nó possui um sistema operacional próprio e tem a capacidade de processamento das suas aplicações 
		- Operacionais distribuídos: os sistemas operacionais distribuídos permitem que um programa seja dividido em partes e que cada parte seja executada em nós diferentes da rede.
		
# U1A3 - Caracteristicas dos Sistemas Operacionais
- Gerenciamento de Hardware: os SO gerenciam todos os recursos de hardware do computador.
- Interface de Usuario: o SO fornece interface para que os usuarios interajam com o sistema de forma grafica (GUI) ou por linha de comando (CLI)
- Multitarefa: capacidade de executar varias tarefas simultaniamente.
- Multithreading: suporte a multithreading, permitindo qu programas tsejam divididos em varias threads para executar tarefas simultanias, aproveitando melhor os multiplos nucleos do processador.
- Gerenciamento de memoria: alocacao dinamica de memoria para garantir que os programas tenha acesso a quantidade nescessaria de memoria 
- Sistemas de arquivo: gerencia o armazenamento de dados em discos rigidos, unidades de estado solido e outros dispositivos de armazenamento.

- MS Windows
	- mais de 40 milhoes de linhas de codigo
	- escrita em maior parte c, c++ e assembly
	- criado combinando os modelos em camada e cliente-servidor 
	- O que tornou o Windows um padrão de uso foi o acordo feito entre a Microsoft e os fabricantes de computadores. Eles já saíam de fábrica juntamente com o sistema operacional da Microsoft e, devido à popularidade dos computadores, a Microsoft conseguiu atingir um grande número de usuários.
	
- Unix
	- inicialmente desenvolvido em assembly para microcomputador PDP-7
	- estrutura do processo contem o seu contexto de software
	- Escrito em linguagem de alto nível, o que facilita a compreensão e a portabilidade para outras plataformas.
	- Flexibilidade, sendo usado em diversas aplicações.
	- Suporte a protocolos de rede.
	- Possui um sistema de arquivos com uma estrutura simples.
	- Possui uma interface simples e uniforme com os dispositivos de entrada/saída.
	
- Linux
	- Inplementacao mais popular do kernel unix-like 
	- É licenciado pela GNU Public License (GPL) e o usuário pode baixar e usar em quantas máquinas quiser.
	- O seu código-fonte é aberto e todos os usuários têm acesso e podem modificá-lo.
	- Um dos pontos fortes do Linux é a linha de comando que permite uma administração efetiva do sistema operacional.
	- Ele permite que o usuário adeque o sistema operacional do jeito que ele desejar em relação ao ambiente gráfico.
	- Ele é gratuito e possui suporte em diversos fóruns e sites de ajuda, além de o usuário ter a opção de contratar o suporte de grandes empresas.
	- A cada dia cresce a popularidade do Linux e mais pessoas conhecem e aprendem sobre as vantagens de seu uso.
	
# U1A4 - Composicao dos Sistemas Operacionais 
- Os SOs sao compostos por varias camadas e componentes que trablham juntos para gerenciar o hardware.

- Kernel
	- Parte central do SO 
	- gerencia recursos de hardware, como CPU, memoria e dispositivos E/S
	- controla a execucao de processos e a comunicacao entre eles 
	- responsavel por manter a estabilidade do sistema.

- Shell
	- interface entre o usuario e o sistema operacional 
	- permite que o usuario interaja com o sistema, execute comandos e forneca entrada de texto.

- Sistemas de Arquivos 
	- responsavel pelo Gerenciamento e organizacao dos dados em dispositivos de armazenamento.
	- fornece estrutura hierarquica de diretorios e arquivos, permitindo o armazenamento, acesso e organizacao eficaz dos dados.

- Drivers de Dispositivos 
	- programas que permitem que o SO se comunique com hardware especifico, como placas de video, impressoras, discos rigidos, etc.

- Processos
	-

- Gestao de Memoria	
	-

- Gestao de Dispositivos E/S 
	- 

- Servicos de Sistemas 
	- oferecem uma variedade de servicos e utilitarios que auxiliam no gerenciamente do sistema, como agendadores de tarefas, servicos de rede, sistemas de gerenciamento de energia, gerenciadores de dispositivos e muito mais.

- Registro
	-

- Bibliotecas de software
	- contem funcoes e recursos compartilhados que os aplicativos podem usar

- Camadas de Seguranca
	- incluem mecanismos de seguranca, como controle de acesso, autenticacao, criptografia e firewalls para protejer o sistema e os dados contra ameacas.

- Aplicativos do sistema 
	- Geralmente incluem aplicativos essenciais, como gerenciadores de arquivos, editores de testos, utilitarios de rede e ferramentas de configuracao

- Servicos de rede 
	- fornecem suporte para comunicacao de rede, permitindo que dispositivos se conectem a redes locais ou a internet

- Aplicativos
	- os aplicativos são programas que os usuários executam para realizar tarefas específicas. Isso inclui aplicativos de produtividade, jogos, navegadores da web e qualquer software que não seja parte essencial do sistema operacional. 
- Recursos de gerenciamento
- Configuracao e personalizacao

# U2A1 - Processos, Conceito e Gerenciamento 
- Introducao
	- a estrutura de um SO é carregado todas as vezes em que o pc for ligado ou reiniciado
	- esse processo de chama ativacao ou boot
	- o SO é composto basicamente por um conjunto de rotinas como nucleo do sistema, chamado kernel, que tem por funcao realizar o controle e tratamente de interrupcoes e excecoes, criar e eliminar processos e threads, sincronizar a comunicacao entre eles e escalonar e controla-los

- Processos
	- instancia de um programa de computador que esta sendo executada.
	- é de responsibilidade desse conjunto de rotinas gerenciar memoria, sistemas de arquivos, dispositivos E/S, permitir suporte a redes locais, realizar contabilizacao das acoes do sistema e tambem sua auditoria e seguranca.
	- para cada uma das rotinas que o sistema executa há um mecanismo de controle chamado de system call, que pode ser explicito ou implicito

- System call Explicito 
	- ha uma instrucao de qual chamada devera ser executada no proprio programa, atraves da implementacao de uma funcao  que carrega os seus respecitivos paramentros
- System call Implicito 
	- há a inserçao de um comando da linguagem de programacao 
	
- System call 
	- responsavel por verificar os parametros da solicitacao e enviar a sua respectiva resposta com o estado do processo, concluido ou se houve algum erro e precisa retornar a pilha de processos.
	
- Hierarquia de Processos 
	- Quando um processo cria outro, o processo pai e o processo filho ficam associados.
	- o filho pode gerar outros processos criando assim uma hieraquia de processos.
	- no Unix um processo-pai, seus filhos e descendentes formam um grupo de processos 

	- O windows nao possui uma hieraquia de processos,
	- cada processo possui um identificador proprio e quando um processo criar outro existe uma ligacao entre eles, mas ela é quebrada quando o processo-pai passa seu identificador para outro processo.
	
- Estados dos processos
	- 1 Em execucao -> Bloqueado
	- 2 Em execucao -> Pronto
	- 3 Pronto -> Em Execucao 
	- 4 Bloqueado -> Pronto 

	- Execucao: esta sendo processado pela CPU.
	- Bloqueado: esta no estado de espera quando aguardo um evento externo (e.g input do usuario) ou pro um recurso.
	- Pronto: possui todas as condicoes necessarias para executar e esta aguardando.
	
- Implementacao de processos 
	- para implementar o modelo de processo o SO mantem um quadro de processos contendo informacoes sobre o estado do processo, seu contador de programa, o ponteiro da pilha, a alocacao de memoria, o status dos arquivos abertos, entre outros, que permite que o processo reinicie do ponto em que parou.

- Processo Thread 
	- foi desenvolvido com o intuito de reduzir o tempo que se leva para criar um novo processo em aplicacaoes concorrentes, bem como o uso de recursos 
	- quando se fala thread quer dizer que um processo ou os seus subprocessos estao ocupando um mesmo espaco em memoria.

	- Um bloco de controle de thread é conhencido como TCB (Thread Control Block)
	- O TCB é responsavel por controlar a prioridade e o estado de execucao, alem de conter os bits de estado do thread.

- Tipos de thread 
	- Thread de usuário: são implementados pela aplicação do usuário e o sistema operacional não sabe de sua existência. A vantagem é que não é necessária nenhuma mudança entre os modos de usuário e núcleo, tornando-se rápido e eficiente.
	- Thread do núcleo: são implementados e gerenciados pelo núcleo do sistema operacional. A desvantagem desta implementação é que todo o gerenciamento dos threads é feito por chamadas ao sistema, o que compromete a performance do sistema.
	- Threads híbridos: são implementados tanto no espaço do usuário, quanto no núcleo do sistema operacional. O sistema operacional sabe dos threads do usuário e faz o seu gerenciamento. A vantagem desta implementação é a flexibilidade em função das duas implementações.
	
# U2A2 - Comunicacao entre processos, Mecanismos e Sincronizacao 
- O SO se comunica com o usuario de tres formas:
	- Atraves de procedimentos proprios do sistema,
	- Atraves da interacao com os aplicativos,
	- Atraves das linguagems de comando.
	
- Para identificar qual deles devera ser acionado, o SO recebe o status daquela situacao, que é definido por uma sequencia de bits de identificacao (ID) no registrador responsavel por essa operacao.
- Modo Usuario: isso quer dizer que apenas instrucoes chamadas nao privilegiadas poderam ser executadas e por isso uma quantidade menor de instrucoes a executar.
- Modo Kernel: o sistema tem acesso irrestrito as intrucoes do processador.

- Tratamento de Erros 
	- Alguns algoritmos sao utilizados para reduzir a probabilidade de erros 
	- Exclusao mutua: impede que dois ou mais processos sejam executados compartilhando o mesmo recurso simultaniamente.
	- Sincronizacao condicional: implementa a sincronizacao de execucao dos processos associada a uma verificacao condicional de acesso a regiao critica.
	- Semaforos: permite a pratica da exclusao mutua com a insercao de condicao para acesso a regiao critica e execucao dos processos. utiliza as instrucoes DOWN e UP.
	- Monitores: implementados pelo compilador e por esse motivo sao considerados estruturados
	- Troca de Mensagem: nao necessita de variaveis compartilhadas, mas estabelece um canal de comunicacao em que seja possivel enviar (SEND) e receber (RECEIVE) mensagens para a sincronizacao de execucao dos processos.
	- Deadlock: ocorre essa situacao quando um processo esta aguardando por tempo indeterminado a alocacao de um recurso ou um evento que nao ocorrera em funcao da alocacao dinamica de recursos que trabalham com concorrencia.
	

- Regiões críticas
	- Para impedir as condições de disputa, é necessário definir maneiras que impeçam que mais de um processo leia e escreva ao mesmo tempo na memória compartilhada. Esses métodos são chamados de exclusão mútua, ou seja, quando um processo estiver lendo ou gravando dados, sua região crítica ou processo deve esperar.
	- A parte do programa em que o processo acessa a memória compartilhada é chamada de região crítica ou seção crítica.
	- Segundo Tanenbaum (2003), para termos uma boa solução, é necessário satisfazer quatro itens:
		- Dois ou mais processos jamais estarão ao mesmo tempo em suas regiões críticas.
		- Não se pode afirmar nada sobre o número e a velocidade de CPUs.
		- Nenhum processo que esteja executando fora de sua região crítica pode bloquear outros processos.
		- Nenhum processo deve esperar sem ter uma previsão para entrar em sua região crítica.
		
# U2A3 - Escalonamento de Processos e Threads: ALgoritmos e Politicas
- Escalonador de Processos
	- subsistema do SO responsavel por decidir o momento em que cada processo obtera a CPU.
	- os processos que necessitam de processamento ocuparao a CPU por um tempo maior e nao precisaram da intervencao do usuario.
	
- Criterios de Escalonamento 
	- alguns sao necesarios e determinados de acordo com as Caracteristicas do SO.
	- dentre os criterios, podemos elencar a analise de eficiencia e utilizacao do processador.
	- o recomendade é que o nivel de capacidade esteja ocupando, em media, 90% para ser considerado alto, ou seja, com bom potencial de aproveitamento do recurso.
	- Outro criterio para a definicao do escalonamento é o throughput, esse é um indicador que mostra quantos processos foram executados dentro de um intervalo de tempo.
	- TEMPOS:
		- o tempo de processador ou tempo de UCP: é outro criterio relevante para a escolha ou determinacao do tipo de escalonamento aplicado. é o tempo que um processo leva para ser executado e finalizado
		- o tempo de espera: define o tempo em que um processo fica na fila dos processos em estado de pronto.
		- tempo de turnaround: tem a funcao de apresentar o tempo total que um processo ocupa deste sua criacao ate seu encerramento.
		- o tempo de resposta: tempo que leva a partir da criacao do processo para que esse seja atendido pelo sistema.
		
- Escalonador de Processos 
	- Dar privilegios para aplicacoes criticas.
	- Balancear o uso da CPU entre processos.
	- Ser justo com todos os processos, pois todos devem poder usar o processador.
	- Maximizar a produtividade (Throughput)
	- Proporcionar menores tempos de resposta para usuarios interativos.
	
- Escalonamento de processos 
	- foram criados para controlar quais os processos tem prioridade e quais processso estao na file para processamento.
	- Tipos:
		- Nao preemptivos e preemptivos;
		- First In First Out (FIFO)
		- Shortest job first (SJF) 
		- Cooperativo;
		- Circular
		- Por prioridades 
		- Circular por prioridades
		- Por multiplas filas 
		- Por multiplas filas com realimentacao 
		- Escalonamento em Sistemas de tempo real
		
- Preemptivo 
	- compartilhamento de tempo e recursos 
	- intercala os processos em execucao 
	
- Nao Preemptivo 
	- recursos dedicados
	- so ha liberacao quando o processo é finalizado ou por erro de execuçao
	
- FIFO 
	- primeiro processo a entrar na file sera o primeiro a ser alocado para processamento 
	- ele agrupa o processo por ordem de chegada em estado pronto e faz o escalonamento assim que chamados a execucao.
	
- SJF 
	- considera o tempo de execucao de um processo e nao a ordem de chegada na fila 
	- este algoritmo seleciona o processo com menor tempo de execucao e este tem a prioridade saindo do estado de pronto.
	
- Circular 
	- trabalha com fila (FIFO) e o primeiro processo em estado de pronto sera o primeiro a ser enviado para ser executado.
	- um processo pode passar do estado de execucao para o estado de espera quando excede o tempo de entrada em processamento.
	
- Por prioridades 
	- cada processo é atribuido a uma prioridade, e aquele que tem a maior prioridade sera aquele que sera executado no estado de pronto 
	- se tiver dois processso com a mesma prioridade ambos sera ordenados por FIFO 
	- esse tipo de processo nao pode ser preemptivo, ocorrendo por uma interrupcao de tempo, ou de clock, de forma que o sistema identifique novamente os estados dos processos e quais estao em pronto.

- Circular por prioridade 
	- O algoritmo associa cada processo uma fatia de tempo e a sua ordem de prioridade com relacao aos demais.
	- o processo sera iniciado e encerrado sem interrupcoes ou passara voluntariamente para o estado de espera.
	
- Por Multiplas Filas 
	- Trabalha com a formacao de varias filas que sao tratadas de acordo com a importancia da aplicacao para o SO ou mesmo a quantidade e a area da memoria que sera alocada.

- Scheduling
	- o agendador de tarefas (scheduling) é uma atividade organizacional feita pelo escalonador (scheduler) da CPU ou de um sistema distribuido, possibilitando executar os processos mais viaveis e concorrentes, priorizando determindados tipos de processos, como os de I/O Bound e os CPU bound.
	
# U2A4 - Threads
- Oque sao:
	- Unidade basica de execucao de um programa 
	- processo leve que pode ser considerado como um 'subprocesso' dentro de um processo maior.
	- elas permitem que um programa execute varias tarefas de forma concorrente tornando-o mais eficiente e responsivo
	
- Principais aspectos
	- Execucao concorrente
		- permitem que partes diferentes de um programa sejam executadaas concorrentemente, o que pode melhorar o desempenho e a capacidade de resposta do programa.
	- Compartihamento de recursos 
		- Threads em um mesmo processo copartilham o mesmo espaco de memoria o que facilita o compartlhamento de dados e recursos entre elas.
		
- Criacao de Threads 
	- os SOs e as linguagens de programacao geralmente fornecem mecanismos para criar e gerenciar threads. elas podem ser criadas em um processo para realizar tarefas especificas.

- Threads e programacao paralela 
	- A programacao com thread é uma forma de programacao paralela que envolve a execucao de varias tarefas simultaniamente para aproveitar melhor o poder de processamento de sistemas com multiplos nucleos de CPU.
	
- Tipos de threads 
	- Threads de usuario: criadas e gerenciadas pela bibliotecade threads da linguagem de programacao ou pela aplicacao em si.
	- Thread do kernel: gerenciadas pelo proprio kernel do sistema operacional.

- Concorrencia e sicronizacao: ao usar threadss é importante lidar com questoes de concorrencia como a sincronizacao de acesso a recursos compartilhados.
- Escalonamento de Threads: o SO é responsavel pelo escalonamento das threads, decidindo quais threads devem ser executadas e em qual ordem.

- Modelos de threads 
	- referem-se as diferentes abordagens usadas para criar, gerenciar e coordenar threads dentro de um processo maior.
	- cada modelo tem suas caracteristicas e trade-offs e a escoha de modelo depende dos requisitos especificos do sistema e do aplicativo.

- Modelo Many-to-One
	- varias threads de nivel de usuario sao mapeadas para uma unica thread de nivel kernel.
	- a implementacao das threads de nivel usuario é feita inteiramente no espaco do processo do usuario e o SO nao tem conhecimento das threads.
	
- Modelo One-to-One 
	- cada thread de nivel de usuario é mapeada para uma unica thread de nivel de kernel.
	- cada thread de nivel de usuario é tratada como um processo separado pelo SO.

- Modelo Many-to-Many 
	- varias threads de nivel de usuario sao mapeadas para um numero menor de threads de nivel kernel.
	- a correspondencia entre threads de nivel usuario e threads de nivel de kernel é flexivel.

- Modelo Two-Level
	- combina aspectos dos modelos many-to-One e One-to-One 
	- as threads de nivel usuario sao mapeadas para threads de nivel kernel mas de forma mais flexivel do que a correspondencia one-to-one
	
- Modelo Hybrid (Híbrido)
	- são uma mistura de várias abordagens, muitas vezes personalizadas para atender às necessidades específicas do sistema e do aplicativo. 
	- Eles podem ser projetados para combinar as vantagens de diferentes modelos, adaptando-se a diferentes situações.
	
- Relacao entre threads e processos 
	- um thread é uma unidade basica de processamento que pode ser executada simultaniamente com outros threads dentro do mesmo processo.
	- threads compartilham o mesmo espaco de endereco de memoria e recursos do sistema, o que os torna mais eficientes em termos de uso de recursos do que processos independentes.
	- um processo é um programa em execucao.
	- ele contem o codigo executavel, dados e recursos do sistema, como arquivos abertos e conexoes de rede

- Processos contem Threads 
	- Um processo é uma unidade independente de execução em um sistema operacional que contém seu próprio espaço de endereço de memória, registradores e contexto de execução. Um processo pode ser visto como um programa em execução.
	- Dentro de um processo, pode haver um ou mais threads. Os threads são unidades de execução menores que compartilham o mesmo espaço de endereço de memória do processo pai.
	
- Isolamento vs. compartilhamento:
    - Os processos são isolados uns dos outros, o que significa que eles não compartilham memória ou recursos diretamente. Cada processo tem seu próprio espaço de endereço de memória.
    - Os threads em um processo compartilham o mesmo espaço de memória e recursos, o que as torna mais leves em termos de recursos e permite uma comunicação direta entre elas.

- Criação e terminação:
    - Os processos são criados e terminados de forma independente. O processo pai pode criar processos filhos que executam programas separados.
    - Os threads são criados e terminados dentro de um processo existente. Um thread é geralmente uma subdivisão de um processo maior.

- Sincronização e comunicação:
    - A comunicação e a sincronização entre processos geralmente são mais complexas, envolvendo mecanismos como pipes, sockets ou memória compartilhada. Os processos são menos propensos a problemas de concorrência, mas a comunicação requer mais esforço.
    - Os threads podem se comunicar e sincronizar mais facilmente, pois compartilham memória. Isso pode levar a problemas de concorrência, como condições de corrida, que precisam ser gerenciadas com cuidado.

- Overhead:
    - Criar e gerenciar processos geralmente tem um overhead mais alto em termos de consumo de recursos (CPU e memória) em comparação com threads.
    - Os threads são mais leves em termos de recursos, pois compartilham recursos comuns dentro de um processo.

- Escalonamento:
    - Processos são escalonados pelo sistema operacional, o que pode ser mais pesado e lento, pois envolve a troca de contexto completa.
    - Threads dentro de um processo podem ser escalonadas com mais eficiência, já que compartilham o mesmo espaço de memória.
	
# U3A1 - Arquivos e Sistemas de Arquivos 
- Arquivos sao estruturas de dados ou instrucoes que estao relacionadas logicamente e se associam a um determinado contexto.
- A fim de organizar esses arquivos o SO conta com uma estrutura chamada Sistema de arquivos.
- Case sensitive:
	- os sistemas baseados em Unix fazem distincao entre maiusculas e minusculas
	- o windows nao faz essa distincao 

- Estrutura de Arquivos 
	- Sequência estruturada de bytes: o sistema operacional não sabe qual é o conteúdo do arquivo, e tudo o que ele vê são bytes. A sequência estruturada de bytes oferece flexibilidade, uma vez que os programas de usuário podem dar o nome que quiserem aos seus arquivos e inserir o conteúdo que desejarem.
	- Sequência de registro de comprimento fixo: um arquivo é uma sequência de registros de tamanho fixo, cada um com uma estrutura interna. O objetivo é que a operação de leitura retorne um registro e a operação de escrita sobreponha ou anexe um registro.
	- Árvore de registros: um arquivo é formado por uma árvore de registros, não necessariamente do mesmo tamanho, cada um contendo um campo-chave em uma posição fixa do registro. A árvore é ordenada pelo campo-chave, para que se busque mais rapidamente por uma chave específica. Novos registros podem ser inseridos no arquivo, e é o sistema operacional que decide onde colocá-los. Esse tipo de arquivo é amplamente aplicado em computadores de grande porte, usados ainda para alguns processamentos de dados comerciais.
	
- Tipos de Arquivos 
	- Diferentes tipos de arquivos são suportados pelos sistemas operacionais, tais como arquivos regulares, diretórios, arquivos especiais de caracteres e especiais de blocos.
	- Arquivos regulares podem ser subdivididos em:
		- Arquivos ASCII: são formados por linhas de texto. A grande vantagem dos arquivos ASCII é que eles podem ser mostrados e impressos como são e podem ser editados com qualquer editor de textos, além de facilitar a conexão entre a saída de um programa e a entrada de um outro.
		- Arquivos binários: possuem alguma estrutura interna, conhecida pelos programas que os usam. Os sistemas operacionais devem reconhecer pelo menos um tipo de arquivo: seu próprio arquivo executável.
	- Arquivos de diretórios mantêm a estrutura dos sistemas de arquivos. 
	- Arquivos especiais de caracteres são relacionados à entrada/saída e usados para modelar dispositivos de E/S, como terminais, impressoras e rede. 
	- Arquivos especiais de blocos são usados para modelar discos.
	
- Quando o SO precisar realizar uma funcao, a operacao em andamento é compreendida pelo computador como um processo que devera ser executado e direcionado ao driver correto para que essa acao ocorra.
- O Driver é o conjunto de rotinas que devem ser executadas de acordo com o formato do arquivo.

- Funcionalidades dos sistemas de arquivos 
	- Manipulacao de Arquivos:
		- Abrir
		- Fechar
		- Criar
		- Destruir
		- Copiar
		- Renomear
		- Listar
	- Manipulacao de dados dos arquivos:
		- Ler 
		- Escrever 
		- Atualizar 
		- Inserir 
		- Apagar 
	- Atributos de arquivos 
		- Tamanho 
		- Localizacao 
		- Acessibilidade 
		- Tipo 
		- Volatilidade 
		- Atividade 
		- Backup 
	- Rotinas de E/S de arquivos 
		- CREATE (criar)
		- OPEN (abrir)
		- READ (ler)
		- WRITE (ler)
		- CLOSE (fechar)
		- DELETE (eliminar)
		
- Registros 
	- podem ser definidos como logico ou fisico 
	- Registros logicos: campos que contem atributos como nome, tipo e comprimento. podem representar valores constantes ou variaveis.
	- Registros fisicos: referem-se a acoes que seram desempenhadas pelo sistema de arquivos.
	
- Atributos 
	- sao informacoes de controle de cada arquivo que variam de acordo com o sistema de arquivos, como tamanho, protecao, identificacao do criador e data de criacao.
	
- Organizacao de Arquivos 
	- refere-se a forma como os dados sao armazenados em arquivos e essa organizacao é crucial para a eficiencia do acesso e manipulacao dos dados.
	- classificao para a organizacao de arquivos:
		- Sequencial (ou nao estruturada)
		- Indexada
		- Relativa
		- Estrutura em Arvore

- A Sequencial (ou nao estruturada)
	- Nessa forma de organizacao, nao ha necessariamente uma estrutura logica definida, preestabelecida.
	- por esse motivo, o acesso ao registro é precario, pois é necessária a leitura de todos os registros, até que seja encontrado o que está de fato sendo procurado.
	
- A Indexada 
	- Os dados se interligam atraves de um indice, que a partir de sua definicao, organizara os dados de um registro de acordo com uma determinada regra.
	- Essa ligacao pode ser atraves de uma deficao de idade, altura, sexo e classe social que sejam compativeis.

- A Relativa 
	- Refere-se a alocacao dinamica e aleatoria do arquivo, por esse motivo, ele podera ser localizado a partir de uma chave de acesso e do local em que esta armazenado.
	- O sistema de arquivos tera a responsabilidade de gerenciar o caminho do dispositivo ou local de armazenamento do arquivo.

- Estrutura em Arvore 
	- A descricao dos elementos:
		- bin: encontram-se arquivos executaveis que sao necessários para a recuperacao de dados e reparacao de arquivos.
		- etc: armazena arquivos que servem para realizar a configuracao de arquivos locais e software.
		- home: associado ao usuario direta ou indiretamente, necessitando da administracao local.
		- usr: indica uma particao e os respectivos arquivos que podem ser compartilhados no modo somente leitura.
		
# U3A2 - Sistema de Diretorios
- Estrutura de Diretorios 
	- é como o sistema organiza logicametne os diversos arquivos contidos em um disco.
	- o diretorio é uma estrutura de dados que contem entradas associadas aos arquivos em que cada entrada armazena informacoes como localizacao fisica, nome, organizacao e demais atributos.
	
- Estrutura de Diretorios em sistemas de arquivos hieraquico
	- arquivos e subdiretorios sao organizados em uma arvore, facilitando a organizacao e navegacao eficiente.
	- exemplo:
		- /home/arquivo1.txt 
		- '/' reprezentando o diretorio raiz.
		- 'home' contendo arquivos do usuario
		- 'arquivo1.txt' representado um arquivo de texto 
	
- Atributos dos arquivos 
	- Tamanho: especifica o tamanho, quantidade de caracteres ou bytes do arquivo.
	- Protecao: especifica padroes de seguranca de acesso do arquivo.
	- Dono/Proprietario/Usuarios: estabelece que criou, ou seja, associa ao usuario ou conta.
	- Criacao: delimita data e hora de criacao do arquivo.
	- Backup: disponibiliza data e hora de ultima atualizacao.
	- Organizacao: indica qual é a logica e a hierarquia utilizada para armazenar os arquivos nos respecitivos diretorios.
	
- Organizacao de Diretorios 
	- refere-se aos diferentes niveis de complexidade, nivel unico, dois niveis ou arvore.
	- Nivel Unico
		- tambem chamada de single level directory, tem muitas limitacoes.
		- por exemplo, os usuarios nao podem criar arquivos com o mesmo nome para evitar conflitos de acesso, pois os arquivos recebem todas as caracteristicas destacadas e sao alocados para armazenamento.
		- mas, para evitar esse tipo de conflito, foi desenvolvida a estrutura de diretorios de dois niveis.
		- o primeiro nivel destina-se a divisao de contas de usuarios e o outro a alocacao dos arquivos criados.
	- Dois Niveis
		- Essa estrutura fez com que arquivos criados por contas de usuarios distintos pudessem ter os mesmos nomes, pois nao estao alocados no mesmo diretorio e nao causam danos de integridade ou conflitos na localizacao e acesso aos arquivos.
		- nessa estrutura, o diretorio do usuario aponta para a sua respectiva area de alocacao de arquivos, que foi destinada pelo proprio sistema de arquivos.
	- Arvore
		- Na estrutura em arvore, a raiz é a propria area do usuario que esta apontando para os diretorios e esses apontam para os seus respectivos arquivos.
		- A analise se dá como em uma arvore em que a raiz é o proprio usuario, os galhos sao os diretorios e as folhas sao os arquivos.
		- a essa seguencia de caminhos da-se o nome de path.
		
- Alocacao de Arquivos
	- refere-se a maneira como o espaco de armazenamento em um dispositivo de armazenamento é alocado para armazenar arquivos.
	- Alocacao de Tabelas:
		- para que o SO possa alocar arquivos é preciso que realize a gerencia dos espacos disponiveis em disco, quanto e quais partes do HD estao disponiveis 
		- as estruturas de dados que podem ser usadas para essa alocacao sao basicamente lista e tabela.
		- cada linha da tabela representa um bloco do HD 
		- os zeros representam os espacos livres em memoria e os ums os espacos ocupados.
		- a desvantagem desse tipo de estrutura é que ocupa muito espaco em memoria, uma vez que para cada bloco do HD deve existir uma entrada de dados na tabela.
	- Alocacao Encadeadas:
		- Na alocacao encadeadas o controle ocorre atraves dos blocos do discos que estao sem arquivos, ou seja, livre.
		- cada bloco contem uma area que determina o endereco que devera ser utilizado pelo proximo bloco.
		- a partir do primeiro bloco disponivel que for encontrado, esse apontara para o endereco do proximo bloco disponivel, para realizar a alocacao de dados e cria-se o conceito da lista encadeada.
		
# U3A3 - Implementacao de Sistema de Arquivos 
- Gerenciamento de espaco de disco:
	- As principais considerações envolvidas no gerenciamento de espaço em disco:
		- Monitoramento de uso de espaço: monitorar regularmente a quantidade de espaço em disco disponível e o espaço ocupado por arquivos e aplicativos. Isso pode ser feito por meio de utilitários de sistema ou software de terceiros.
		- Limpeza de arquivos desnecessários: regularmente, identificar e excluir arquivos desnecessários, como arquivos temporários, logs antigos, cache de aplicativos e outros dados não essenciais.
		- Gerenciamento de logs: controlar e configurar a retenção de logs de sistema e aplicativos para evitar que eles ocupem muito espaço em disco. Defina políticas de rotação de logs para manter um histórico gerenciável.
		- Compactação e desfragmentação: em sistemas de arquivos que usam estratégias de alocação não contígua, como o sistema de arquivos NTFS do Windows, a desfragmentação pode ser útil para otimizar o espaço em disco e melhorar o desempenho do sistema. Além disso, a compactação de arquivos pode reduzir o espaço ocupado por arquivos de dados.
		- Redimensionamento de partições: à medida que as necessidades de armazenamento mudam, pode ser necessário redimensionar as partições no disco. Isso pode ser feito para expandir ou reduzir o espaço alocado para determinados sistemas de arquivos.
		- Políticas de retenção de dados: definir políticas de retenção de dados para garantir que os dados sejam mantidos o tempo necessário e, em seguida, sejam excluídos de forma segura. Isso é especialmente importante para dados sensíveis ou regulamentados.
		- Backup e recuperação de dados: implementar práticas de backup regulares para proteger contra perda de dados devido a falhas de hardware, erros humanos ou outros eventos imprevistos. Certificar-se de que os dados possam ser recuperados de maneira eficaz.
		- Armazenamento de dados em nuvem: considerar a integração de serviços de armazenamento em nuvem para expandir a capacidade de armazenamento e fazer backup de dados críticos.
	
- Envolve basicamente criar para cada arquivo o seu respectivo descritor
- Descritor de arquivos é um registro no qual sao mantidas as informacoes a respeito do arquivo.
- Essas informacoes incluem os seus atributos, alem de outros dados que nao sao visiveis para o usuario mas sao importantes para o SO.
- o Descritor é acessado em todas as operacoes de leitura e escrita do arquivo.

- Para tornar mais rapido o acesso aos arquivos o sistema de arquivos mantem na memoria uma tabela contendo todos os descritores em uso.
- quando um arquivo entra em uso o seu descritor é copiado do disco para a memoria.

- Alocacao de Sistemas de arquivos 
	- existem varias tecnicas de alocacao, cada uma com sua proprias caracteristicas:
		- Alocacao contigua: um arquivo é armazenado em um unico bloco contiguo de espaço no disco, isso facilita o acesso sequencia aos dados.
		- Alocacao por lista encadeada: consiste em organizar os mesmos como um conjunto de blocos ligados logicamente no disco, independentemente de sua localizacao fisica.
		- Alocacao por lista encadeada usando uma tabela na memoria: nesse metodo cada palavra de ponteiro de cada bloco de disco é inserida em uma tabela na memoria principal chamada de FAT (file allocation Table).
		- I-nodes: nesse metodo cada arquivo é associado a uma estrutura chamada i-node (index node), relacionando os atributos e os enderecos em disco dos blocos de arquivos.
		
- Tabela de Descritores 
	- Tambem chamada de TDAA ela é responsavel por manter atualizadas as informacoes dos arquivos abertos.
	- com o intuito de reparar possiveis conflitos de acessos o sistema de arquivos se encarrega de criar uma tabela descritiva de arquivos abertos por processo chamada de TAAP.
	- para cada arquivo aberto é criada uma entrada na TAAP que contem a posicao corrente do arquivo.
	- Em relacao ao tipo de permissao associado e ainda um ponteiro que indica a sua correspondencia na tabela dos descritivos de arquivos abertos.
	
# U3A4 - Seguranca de Sistemas de Arquivos 
- É necessario que o SO ofereca protecao dos arquivos para que usuarios e processos que nao tenham permissao nao consiga acessar arquivos sigilosos ou sensiveis.
- um sistema de arquivos possui diferentes mecanismos de proteção, como:
    - Senha de acesso: para ter acesso ao arquivo, é necessário que o usuário a conheça e que o sistema conceda o acesso ao arquivo. Nesse caso, como um arquivo possui apenas uma senha, não é possível definir quais tipos de operações serão realizadas.
    - Grupo de usuários: essa proteção consiste em associar cada usuário a um grupo para compartilhar arquivos. Durante a criação do arquivo, o usuário define quais usuários terão acesso a ele.
    - Lista de controle de acesso (Access Control List - ACL): é uma lista associada a cada arquivo, com as permissões de cada usuário. Quando um usuário tenta acessar um arquivo, o sistema operacional verifica sua permissão para autorizar ou não a operação realizada.

- Elementos basicos para um plano de seguranca de informacao:
	- Autenticacao de usuarios: os processos estao associados aos usuarios que os criam no sistema. por esse motivo é necessario realizar esse procediemnto de conferencia que analisa o que ele pode e nao fazer.
	- Protecao de recursos basicos: Identificar se o usuario pode acessar um determindado recurso ou suas configuracoes.
	- Tipos de ameaça: possiveis virus, aplicativos e softwares maliciosos, bem como tecnicas aplicadas que possam representar um risco a softwares.
	- Avaliacao de seguranca do SO: a agencia de seguranca nacional dos estados unidos, em 1983, lancou um documento que contem os criterios confiaveis de avaliacao de sistemas computacionais do departamento de defesa.
	- Criptografia: algoritmos aplicados a codificacao e decodificacao de informacoes em sistemas computacionais.
	
- Seguranca e mecanismos de protecao 
	- quando se trata da autenticacao dos usuarios é importante estabelecer suas respectivas senhas e logins de acesso, ou nomes que os identifiquem e os diferenciem
	- outro fator importante a ser definido quanto as senhas de acesso dos usuarios é o grau ou nivel de seguranca que oferecem.
	- essas senhas devem estar protegidas do acesso indevido no sistema.
	- para minimizar a possibilidade do algoritmo de criptografia ser discoberto (e por conseguinte a senha) utiliza-se o que se chama criptografia de sentido unico em que a senha utilizada pelo usuario no momento do login é comparada aquela que esta armazenada.
	- uma das tecnicas mais utilizadas para criptografia de dados é a funcao hash.
	- A tecnica biometrica tambem tem ganhado espaco no mercado, apesar de requerer mecanismos tecnologicos mais aprimorados do que os algoritmos e tecnicas mencionadas.
	- a empresa que nao cumprir com os pilares da seguranca da informcao (confidencialidade, integridade e disponibilidade) pode sofrer uma serie de penalidades.
	
- Seguranca e Mecanismos de Protecao 
	- existem verificacoes que visam proteger o acesso indevido dos recursos basicos do computador.
	- CPU: o acesso é controldado basicamente pelo codigo do escalonador e do contexto (hardware e software). por esse motivo, o acesso deve ser restrito apenas a alguns tipos de recursos, como as instrucoes de software e a acao dos registradores.
	- Memoria: pode ocorrer de forma irrestrita atraves da CPU pelos registradores de base e de limite.
	- Lista de controle de acesso: outra forma de realizar a protecao dos recursos basicos, em que sao combinadas as permissoes, de acordo com cada um dos membros da lista, criando o conceito de identidade permissao, que se associam a cada usuario e tipo de recurso.
	- Aptidoes: Relacionamento entre pares de recursos-permissao ao inves de permissao por usuario.
	
- Objetivo de protecao e seguranca 
	- principais objetivos de proteção e segurança:
		- Confidencialidade: garantir que as informações só sejam acessíveis por pessoas autorizadas. Isso envolve prevenir o acesso não autorizado a dados sensíveis.
		- Integridade: certificar-se de que os dados e os recursos não tenham sido alterados indevidamente, quer intencionalmente ou não. Isso implica manter a precisão e a confiabilidade das informações.
		- Disponibilidade: assegurar que os recursos e informações estejam disponíveis quando necessário. Isso inclui proteção contra interrupções, falhas e ataques que possam tornar os recursos inacessíveis.
		- Autenticidade: garantir que a identidade dos usuários, sistemas e recursos possa ser verificada. Isso envolve autenticação para confirmar que alguém é realmente quem afirma ser.
		- Não repúdio: impedir que uma pessoa negue ter realizado uma ação específica, como negar o envio de um e-mail ou a conclusão de uma transação.
		- Rastreabilidade: manter registros e logs de atividades para que seja possível rastrear quem fez o quê, o quando e o porquê. É importante para auditorias e investigações.
		- Controle de acesso: garantir que os recursos sejam acessados apenas por pessoas autorizadas e que os privilégios de acesso sejam concedidos de acordo com a necessidade.
		- Resistência a ataques: implementar medidas de segurança para resistir a ataques cibernéticos, invasões, vírus, malware e outras ameaças.
		- Recuperação e continuidade de negócios: planejar para a recuperação de desastres e a continuidade dos negócios, para garantir que, em caso de falha ou desastre, as operações possam ser restauradas de maneira eficaz.
		- Proteção de dados pessoais: proteger a privacidade e os dados pessoais dos indivíduos, garantindo conformidade com regulamentações de proteção de dados, como o Regulamento Geral de Proteção de Dados (RGPD).
		- Proteção física: garantir que os recursos físicos, como servidores, instalações e dispositivos, estejam protegidos contra acesso não autorizado, roubo e danos.
		- Conscientização e treinamento: educar funcionários e usuários sobre boas práticas de segurança, sensibilizando-os para as ameaças e os procedimentos de segurança.
		
- Ameacas a seguranca do sistema 
	- Malware: Inclui vírus, worms, cavalos de Troia, spyware, adware e outros tipos de software malicioso que podem infectar sistemas e dispositivos, comprometendo sua integridade e confidencialidade.
	- Ataques de Phishing: e-mails e mensagens falsas são usados para enganar os usuários e obter informações confidenciais, como senhas e números de cartão de crédito.
	- Engenharia social: atacantes utilizam táticas psicológicas para manipular pessoas e obter informações confidenciais ou acesso a sistemas.
	- Ataques de força bruta: tentativas repetidas de adivinhar senhas ou chaves de criptografia para obter acesso não autorizado a contas e sistemas.
	- Injeção de SQL: ataques que exploram vulnerabilidades em aplicativos da web para inserir comandos SQL maliciosos em bancos de dados, comprometendo a integridade dos dados.
	- Cross-Site Scripting (XSS): Vulnerabilidades em sites que permitem que atacantes injetem scripts maliciosos em páginas da web visitadas por outros usuários, comprometendo sua segurança.
	- Ataques de negociação de sessão: atacantes tentam roubar ou assumir sessões de usuários autenticados para ganhar acesso não autorizado a contas.
	- Vulnerabilidades de software: falhas no software e sistemas que podem ser exploradas por atacantes para ganhar acesso não autorizado ou causar danos.
	- Ataques de negação de serviço (DoS/DDoS): sobrecarregar sistemas, redes ou serviços com tráfego malicioso para torná-los inacessíveis.
	- Ataques de ransomware: software malicioso que criptografa dados e exige resgate em troca da chave de descriptografia.
	- Ataques de invasão: atacantes tentam ganhar acesso não autorizado a sistemas e redes explorando vulnerabilidades.
	- Ameaças internas: funcionários desonestos ou ex-funcionários podem representar uma ameaça, roubando dados ou realizando atividades maliciosas.
	- Roubo ou perda de dispositivos: dispositivos móveis ou computadores contendo informações sensíveis podem ser roubados ou perdidos.
	- Vazamento de informações: informações confidenciais podem ser divulgadas de maneira não intencional, seja por erro humano ou falha de segurança.
	- Problemas de gerenciamento de senhas: senhas fracas ou comprometidas podem permitir acesso não autorizado a contas.
	- Ataques de redes wi-fi não seguras: redes wi-fi não seguras podem ser alvos de ataques de interceptação e acesso não autorizado.
	- Ataques a firmware: ataques que visam o firmware de dispositivos, como BIOS, para ganhar controle total sobre o hardware.
	
- Mecanismos de seguraca
	- Criptografia: envolve a codificação de dados de forma que só possam ser lidos por pessoas ou sistemas autorizados. Protege a confidencialidade dos dados, garantindo que apenas as partes autorizadas possam acessá-los.
	- Controle de acesso: determina quem tem permissão para acessar recursos, sistemas ou informações. Ele envolve a autenticação (verificar a identidade do usuário) e a autorização (conceder ou negar permissões de acesso).
	- Firewalls: são projetados para monitorar e controlar o tráfego de rede, permitindo que apenas o tráfego autorizado passe e bloqueando tráfego não autorizado. Eles ajudam a proteger sistemas contra-ataques de rede.
	- Sistemas de Detecção de Intrusões (IDS) e Sistemas de Prevenção de Intrusões (IPS): IDS monitoram a rede em busca de atividades suspeitas, enquanto os IPS têm a capacidade de tomar medidas ativas para impedir ou responder a ataques em tempo real.
	- Autenticação de Dois Fatores (2FA): além de senhas, a autenticação de dois fatores exige um segundo método de autenticação, como um código gerado em um aplicativo móvel ou enviado por SMS. Isso aumenta a segurança das contas.
	- Assinaturas digitais: as assinaturas digitais são usadas para verificar a autenticidade de documentos e mensagens eletrônicas, garantindo que não tenham sido alterados e que foram assinados por um remetente específico.
	- Políticas de segurança: ter políticas de segurança documentadas e implementadas ajuda a estabelecer diretrizes claras para a segurança da informação e o comportamento dos usuários.
	- Auditoria e registros de segurança: manter registros detalhados de atividades do sistema e logs de auditoria ajuda a rastrear e investigar incidentes de segurança.
	- Segurança física: controles físicos, como câmeras de segurança, sistemas de controle de acesso e alarmes, protegem instalações e equipamentos contra acesso não autorizado.
	- Segurança de rede: implementar medidas de segurança de rede, como segmentação de rede, VLANs, VPNs e proteção contra-ataques DDoS, para proteger a infraestrutura de rede.
	- Antivírus e antimalware: utilizar software antivírus e antimalware ajuda a detectar e remover ameaças de software malicioso em sistemas e dispositivos.
	- Segurança de e-mail: filtragem de e-mail, autenticação de remetentes e treinamento de conscientização dos usuários podem ajudar a proteger contra-ataques de phishing e spam.
	- Segurança de aplicativos: realizar testes de segurança de aplicativos, como verificação de vulnerabilidades e testes de penetração, para identificar e corrigir vulnerabilidades.
	- Recuperação de desastres e continuidade de negócios: planejar e testar estratégias para a recuperação de desastres, para garantir a continuidade das operações após eventos catastróficos.
	
# U4A1 - Gerenciamento de Entrada e Saida 
- Principios de E/S 
	- referem-se às diretrizes e técnicas gerais que governam a comunicação entre o software e os dispositivos de E/S 
	- elas tem o objetivo de tornar essa comunicacao eficiente, confiavel e facil de usar.
	- Alguns dos mais comuns incluem:
		- Transparência: os detalhes específicos do dispositivo de E/S não devem ser visíveis para o software de aplicação, que deve ser capaz de interagir com dispositivos de forma abstrata.
		- Eficiência: as operações de E/S devem ser concluídas de forma eficiente para evitar atrasos no funcionamento do sistema.
		- Consistência: as operações de E/S devem ser consistentes e previsíveis para que os desenvolvedores de software possam confiar em seu comportamento.
		
		
- Gerenciamento de E/S 
	- muitas vezes referido como I/O (Input/Output) é uma parte essencial dos SOs.
	- Ele envolve a comunicacao eficiente entre o sistema computacional (CPU, Memoria) e dispositivos externos, como teclado, mouse, discos, redes e outros perifericos 
	- Comsiderada uma das mais complexas tarefas que o SO realiza, ela é responsavel por facilitar a comunicacao entre as solicitacoes dos usuarios e as aplicacoes.
	- Principais conceitos relacionados a operacao:
		- Subsistemas de E/S 
		- Device Driver 
		- Controladores
		- Dispositivos de E/S 
		- Discos Magneticos ou SGBD
		- Seguranca 
	
- Arquitetura de Gerencia de Dispositivos 
	- dividida em camadas que se distribuem da seguinte forma:
	1. Dispositivos ou Perifericos E/S: mecanismos que permitem a interacao entre usuario e maquina de forma amigavel e segura junto as aplicacoes 
	2. Controlador: faz a interface entre a solicitacao do usuario e o driver. composto por memoria e registradores progamados para enviar as instrucoes ao respectivo driver.
	3. Device driver: possui instrucoes que realizarao a comunicacao das solicitacoes enviadas pelo controlador, ao subsistema de E/S. sua funcao principal é interpretar as instrucoes recebidas para os controladores e os subsistemas E/S 
	4. Subsistema E/S: tem a funcao de distinguir de acordo com cada dispositivo as solicitacoes e executar as rotinas de comunicacao que realiza entre as aplicacoes dos sistemas de arquivos e dos sistemas de gerenciamento de dados.
	5. Sistema de arquivos, SGBDs e as aplicacoes se relacionam de forma a gerar as demandas de processo.
		
- Sincronismo das operacoes E/S 
	- sincrona: o processo que realizou a operacao fica aguardando no estado de espera pelo seu termino, a maioria dos comandos das linguagem de alto nivel funciona desta forma.
	- assincrona: o processo que realizou a operacao nao aguarda pelo seu termino e continua pronto para ser executado e o sistema deve oferecer algum mecanismo de sinalizacao que avise ao processo que a operacao foi terminada.
	
- Camadas de Software de E/S 
	- As camadas de software de E/S referem-se à organização do software que gerencia as operações de entrada e saída.
	- Incluem:
		- Camada de driver de dispositivo: essa camada lida diretamente com os dispositivos de hardware e fornece uma interface de programação de dispositivos (API) para o sistema operacional e os aplicativos.
		- Camada de gerenciamento de E/S (I/O manager): essa camada gerencia as solicitações de E/S dos aplicativos, escalona as operações e garante que elas sejam executadas de maneira eficiente e confiável.
		
- Subsistemas de E/S 
	- Subsistemas de E/S são componentes especializados que oferecem funcionalidades adicionais para melhorar a capacidade de gerenciamento de E/S do sistema.
	- Incluem:
		- Sistema de arquivos: gerencia a leitura e gravação de dados em dispositivos de armazenamento de massa, como discos rígidos e unidades de armazenamento flash.
		- Sistema de impressão: controla as operações de impressão, permitindo que os aplicativos enviem documentos para impressoras.
		- Subsistema de rede: gerencia a comunicação de rede, permitindo que os aplicativos se comuniquem com outros dispositivos na rede.
		
# U4A2 - Swapping: troca de processos
- O swapping (troca de processos) é realizado quando nao existe memoria principal o suficiente para executar todos os programas do computador ao mesmo tempo.
- No swapping um programa é totalmente carregado em memoria e executado por um tempo definido, enquanto os demais programas aguardam, em disco, sua vez de executar.
- O Swapping traz totalmente cada processo para a memoria, o executa por um tempo e o retorna para o disco.
- O Sistema escolhe um processo residente que é transferido da memoria principal para a memoria secundaria (swap out) geralmente o disco.
- O processo é carregado de volta da memoria secundaria para a memoria primaria (swap in) e pode continuar sua execucao como se nada tivesse ocorrido.
- quando o processo escolhido para ser retirado da memoria principal esta em estado de espera ou de pronto, podendo ser considerado nao residente, recebem o nome de outswapped.
- quando o processo nao residente alocado encerra a sua execucao ele é retirado da memoria principal e retorna ao local de origem.

- A tecnica de swapping somente podera ser implementada a partir do uso de um registrador de alocacao.

- Vantagems 
	- ao se realizar swapping é possivel compartilhar mais recursos ou enderecos na memoria principal.
	- com melhor aproveitamento da memoria principal conseguimos tambem otimizar o processamento e maximizar a utilizacao dos recursos da maquina de forma geral.
	
- Tipos de Swapping 
	- Swapping por paginaçao ou paginacao de swapping 
	- Strings de referencia: lista de referencia a sequencia ordenada de acessos a pagina para leitura ou gravacao.
	- Politicas de substituicao global
	- Minimo de Belady: uma pagina que ainda nao tenha sido utilizada sera a mais viavel escolha para se realizar swap para memoria secundaria
	- Segunda chance: exetensao de FIFO com uma verificacao. se o bit de acesso for 0, a pagina sera enviada por swap para a memoria secundaria, se o bit de acesso for 1, entao o bit de acesso é deletado e a pagina reinserida ao final da fila.
	- Algoritmo do relogio: infere em mais uma analise sob a politica da segunda chance pois organiza a partir da ideia de ponteiros do relogio, as paginas ao redor e se for preciso realizar swap em memoria secundaria, teremos aquela pagina que esta sendo apontada para verificacao do bit de acesso.
	- Conjunto de trabalho: define-se como o conjunto de paginas que o processo utiliza em um determinad intervalo de tempo.
	- Desempenho: faz referencia direta a eficiencia e aos cuidados na escolha da politica de substituicao local e global. sao considerados os fatores: tempos de acesso e o Thrashing: onde uma grande quantidade de recursos computacionais é utilizada para fazer uma quantidade minima de trabalho.
	- Frequencia de falha: a partir das falhas de paginação entre os processos, a tendência nessa política é verificar se há páginas sem uso ou com pouco uso. Se houver, será feito swap para memória secundária das páginas sem tanta utilidade, pertencentes ao processo que apresentou mais páginas residentes em memoria principal do que em seu conjunto de trabalho.
	- Segmentos Paginados: representam os segmentos dos espaços de endereçamento e se esses forem relativamente grandes, há a sua paginação, a fim de torná-lo menor.
	- Arquivos mapeados na memoria: uma vez um arquivo mapeado, este será armazenado. A alocação de páginas para um determinado processo ocorre toda vez em que há uma solicitação de mapeamento de um arquivo em memoria.
	- Copia-na-escrita: por exemplo a fork (UNIX), em que cria um processo-filho que é a cópia do processo-pai, porém o que há em termos de swap é a cópia no mesmo segmento de memória, tanto do processo-filho quanto do processo-pai de seu mapeamento de endereço em memória virtual, sendo apenas liberados para leitura. Caso aconteça a tentativa de gravação, há uma interrupção e será registrada pela MMU.
	
- Algoritmos de Swapping 
	- Os algoritmos de troca de processos são projetados para gerenciar a alocação de memória para processos quando a memória principal se esgota. Esses algoritmos determinam quais processos devem ser movidos da memória principal (RAM) para a memória secundária (geralmente disco rígido) para liberar espaço para outros processos.
	- Incluem:
		- FIFO (First-In, First-Out): esse algoritmo remove o processo que está na memória há mais tempo. Ele é simples de implementar, mas não considera a importância ou prioridade dos processos.
		- LRU (Least Recently Used - Menos Recente Usado): o algoritmo LRU remove o processo que não foi usado por mais tempo. Ele leva em consideração a frequência de acesso dos processos e tende a manter na memória os processos mais ativos. No entanto, pode ser caro de implementar em termos de rastreamento da ordem de acesso.
		- MFU (Most Frequently Used - Mais Frequente Usado): esse algoritmo remove o processo que foi usado com menos frequência. Ele é baseado na premissa de que os processos menos frequentemente usados são os menos importantes.
		- LRU aproximado (Approximate LRU): é uma versão simplificada do LRU que utiliza contadores para acompanhar o uso dos processos. Os processos com os menores contadores são escolhidos para serem movidos para a memória secundária.
		- NUR (Not Used Recently - Não Usado Recentemente): o algoritmo NUR classifica as páginas de memória com base em critérios como uso recente e modificações. Ele remove as páginas de acordo com sua classificação.
		- Segunda Chance (Second Chance): este algoritmo é uma variação do FIFO, mas com uma “segunda chance”. Se uma página tiver sido usada recentemente, ela é mantida na memória. Caso contrário, é removida.
		- Contagem de Bit de Referência (Reference Bit Counting): nesse caso, cada página é associada a um contador de bits. Periodicamente, os bits são movidos para a direita e o bit menos significativo é observado. As páginas com bits menos significativos iguais a zero são removidas.
		- WSClock (Working Set Clock): o algoritmo combina aspectos do relógio e do working set. Ele considera a idade das páginas e o working set de um processo para decidir quais páginas devem ser removidas.
		- Algoritmo de Substituição de Contador: neste algoritmo, cada página possui um contador. Periodicamente, o contador é incrementado. As páginas com contadores mais baixos são selecionadas para remoção.
		
- Localizacao de swap 
	- Windows: arquivo PAGEFILE.SYS em C:/
	- Linux: diretorio /swap na raiz 
	
- Alocaçao de Tabelas 
	- Para que o SO possa alocar os arquivos é preciso que realize a gerencia dos espaços disponiveis em disco, quanto e quais partes do HD estao disponiveis.
	- As estruturas de dados que podem ser usadas para essa alocacao sao basicamente lista e tabela.
	
# U4A3 - Gerenciamento de Memoria 
- O SO de ve proteger as areas de memorias utilizadas pelos processos de forma que se um programa tente acessa-la indevidamente o sistema seja impedido
- Registradores fazem parte da unidade central de processamento (CPU) e são rápidos pois armazenam a informação ou instrução de processo que deverá ser executada imediatamente.
- A memória cache é considerada mais lenta que os registradores porém mais rápida que a memória principal
- Ela existe pois são necessários alguns mecanismos de armazenamento para permitir que a CPU acesse e realize o processamento da instrução de processo mais rapidamente do que se tivesse que acessar determinado dado ou instrução diretamente em uma das outras memórias: principal, secundária ou permanente.

- Memoria Principal: conhecida também como armazenamento primário é nela que se concentra o gerenciamento de memória realizado pelo sistema operacional nela se concentram as aplicações que serão diretamente solicitadas pelo processador através do mecanismo de endereçamento. Não é considerada muito rápida, porém pode ser de capacidade de armazenamento relevante na ordem de alguns gigabytes. Como exemplo, podemos citar a memória RAM.
- Memoria ROM: icam gravadas as especificações do sistema e não devem ser alteradas. Por esse motivo, a memória ROM fica disponível apenas para leitura. A memória secundária é responsável pelo armazenamento permanente de dados e não permite endereçamento, por exemplo, os pen drives, os CDs e DVDs. É considerada mais lenta em função de não permitir endereçamento e ter de ser localizada por um sistema de arquivos, que é tratado de forma diferenciada e separado do sistema operacional.

- Gerencimento de Memoria e de Processador 
	- O gerenciamento de memória também conhecida como MMU (Memory Management Unit) cuja função é a de mapear os endereços lógicos em que estão as instruções nas memórias físicas
	
- O Gerenciamento de memoria pode ser dividido em duas classes:
	- Sistemas que durante o processamento levam e trazem a informação da memória para o disco (troca de processos e paginação).
	- Sistemas que não o fazem. A troca de processos (swapping) carrega todo o programa para a memória principal, o executa por um determinado tempo e depois o mesmo retorna para o disco
	
- Monoprogramacao sem troca de processo ou paginacao 
	- Este método de gerenciamento de memória é o mais simples, pois somente um programa é executado por vez e a memória é compartilhada entre o sistema operacional e o programa
	- O sistema operacional está utilizando o espaço de endereçamento em RAM ((a)), modelo aplicado aos mainframes e minicomputadores
	- O sistema operacional está utilizando o espaço de endereçamento em ROM somente para a leitura ((b)), usado em alguns computadores de mão e em sistemas embarcados.
	- Os drives de dispositivos estão em ROM e os programas do usuário e o sistema operacional está em RAM ((c)) – modelo utilizado nos primeiros computadores pessoais (MS-DOS).
	
- Multiprogramaçao com particoes fixas 
	- A maioria dos sistemas operacionais modernos permite que vários processos executem ao mesmo tempo (multiprogramação) e quando um processo é bloqueado aguardando uma informação de entrada/ saída, outro processo poderá utilizar a CPU, aumentando a sua utilização.
	
- Problemas da Multiprogramaca
	- A multiprogramação apresenta dois problemas essenciais: relocação e proteção.
	- A relocação é a transferência de um código de um local para outro de forma que um programa não escreva na área de outro programa.
	- A relocação é necessária uma vez que processos executam em diferentes endereços na memória física.
	- Tanto os problemas de relocação quanto de proteção podem ser resolvidos fornecendo o processador com dois registradores(memória localizada no processador): base e limite

# U4A4 - Memoria Virtual 
- Um computador que utiliza memória virtual permite que o volume de informações de um programa como código dado e pilha ultrapasse a quantidade total de memória física disponível para ele, mantendo as partes ativas na memória e as demais no disco rígido.
- A memória virtual é um arquivo dinâmico e de tamanho variável na maioria dos sistemas operacionais.
- A memória virtual permite que vários processos compartilhem a memória principal, uma vez que, somente algumas partes dos processos estarão ativas na mesma, possibilitando uma utilização eficiente do processador e reduzindo a fragmentação da memória principal
- É comum associar o conceito de memória virtual com vetores em função de os dados serem alocados em posições distintas, não haver a necessidade de saber a exata posição de um determinado dado.
- Instruções de código sejam desenvolvidas para que no contexto de software possam trazer a instrução de acordo com a sua respectiva identificação.
- A diferença é que um aplicativo ou software não fará a referência direta aos endereços de memória física do processo, e sim ao seu respectivo endereço de memória virtual.
- Em termos de processamento, por esse necessitar apenas do endereço físico, temos a conversão do endereço virtual ao seu em memória principal
- A memória virtual se mostra como uma solução em função de trabalhar com uma quantidade maior de processos que compartilham a memória principal, uma vez que destes processos já estão alocadas apenas as partes residentes.
- Isso faz com que menos recursos de processamento sejam utilizados.
	- Existem três técnicas para implementar memória virtual:
		- Paginação;
		- Segmentação;
		- Segmentação com paginação
		
- Paginaçao 
	- A paginação é a técnica de gerência de memória em que o endereçamento virtual e o espaço de endereçamento real são divididos em blocos do mesmo tamanho chamado páginas.
	- Foi criada para fornecer um espaço de endereçamento linear sem a necessidade de adquirir mais memória física.
	
- Gerenciamento da demanda de processos no contexto de alocacao de recursos em memoria virtual 
	- para permitir o controle de demanda, foi criada a política de busca de páginas.
	
		- Essa pode ser classificada em: paginação por demanda, ou seja, há a transferência da memória secundária para a principal apenas quando há a referência e ainda há a paginação antecipada, voltada também para o controle de demanda, no entanto com o acréscimo de páginas, caso o processo venha precisar já tem algumas alocadas e a disposição
	- Alem da politica de buscas, temos tambem as seguintes politicas:
		- Alocacao de paginas 
		- Substituicao de paginas 
		- Working set 
		- Algoritimos de substituicao de paginas 
			- Ótimo.
			- Aleatória.
			- FIFO (First in First out).
			- LFU (Least – Frequently - Used).
			- LRU (Least – Recently - Used).
			- NRU (Not – Recently - Used).
			- FIFO com buffer de páginas.
			- FIFO circular
		- Politica para estabelecer o tamanho da pagina 
		- Paginacao com multiplos niveis 
		- traducao de enderecos virtuais em enderecos reais
		- protecao de memoria 
		- compartilhamento de memoria.