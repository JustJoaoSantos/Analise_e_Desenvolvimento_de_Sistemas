# U1A1 - Introducao aos Bancos de Dados
- Oque é
	- um banco de dados pode ser definido como um conjunto de dados devidamente relacionados.
	- Dados sao objetos conhecidos que podem ser armazenados e que possuem um significado implicito.
	- Um banco de dados apresenta as seguintes characteristicas:
		- É 
		
- Porque usar um banco de dados?

- Tipos de Bancos de Dados:
	- Relacional: Um banco de dados relacional se distingue por sua organização dos dados em relações, comumente chamadas de tabelas, as quais são compostas por linhas e colunas.
	- Orientado a Objetos: Basicamente, o modelo de dados orientado a objetos é caracterizado pela definição de bancos de dados por meio de objetos, com suas propriedades e operações. Isso significa que um registro é mais parecido com uma classe definida na linguagem C++, C# ou Java, por exemplo.
	

- A fim de modelar um banco de dados, três níveis de visão de dados devem ser considerados. São eles o conceitual, o lógico e o físico
	- O modelo conceitual, entendido como a primeira etapa, descreve a realidade do ambiente do problema, constituindo-se em uma perspectiva global dos principais dados e de seus relacionamentos (estruturas de informação), completamente independente dos aspectos de sua implementação tecnológica. 
	- Já o modelo lógico inicia-se somente após a criação do modelo conceitual, momento em que se considera uma das abordagens possíveis da tecnologia SGBD (relacional, hierárquica, rede ou orientada a objetos) para estruturação e estabelecimento da lógica dos relacionamentos existentes entre os dados definidos no modelo conceitual. 
	- Quanto ao modelo físico, ele será construído a partir do modelo lógico e descreve as estruturas físicas de armazenamento de dados conforme os requisitos de processamento e uso mais econômico dos recursos computacionais.
	
	- Um sistema gerenciador de banco de dados (SGBD) é um software cuja finalidade é gerenciar as informações de um banco de dados (também chamada de base de dados).
	
# U1A2 - Sistema Gerenciadores de Banco de Dados (SGBD ou DBMS)
- Oque e 
	- SGBD é um software que executa os processos de definicao, construcao, manipulacao e compartilhamento de banco de dados entre varios usuarios e aplicacoes, incluindo modulos para consulta, atualizacao e interfaces entre o sistema e o usuario.
	- O objetivo do SGBD é garantir a seguranca das informacoes inseridas no banco de dados e protege-las de acessos nao autorizados ou de problemas causados por erros de software ou hardware.
	- O SGBD escolhido deve possuir os fatores ACID para garantir que uma transacao no banco de dados seja realizada com sucesso.
	
- ACID (Atomicity, Consistency, Isolation, Durability)
	- Atomicidade: Garante que nenhuma ou a totalidade das operacoes da transacao sejam realizadas com sucesso.
	- Consistencia: Preserva as regras impostas no banco de dados. assim que a transacao for finalizada, todos os dados devem estar integros.
	- Isolamento: É a seguranca de que uma transacao nao interfira no trabalho de outra.
	- Durabilidade: É a certeza de que apos uma transacao ser realizada com sucesso, os resultados fiquem gravados no banco de dados, mesme que algum problema tenha ocorrido.
	
- Principais SGBDs do mercado
	- MySQL: gratuito de codigo aberto.
	- PostgreSQL: segue a mesma linha que o MySQL. 
	- MongoDB: focado em armazenamento NoSQL.
	- SQL Server: para uso comercial e proprietario.
	
# U1A3 - Dados como apoio a tomada de decisao
- Data Warehouse
	- Um deposito de dados (ou data warehouse) é um repositorio (ou arquivamento) de informacoes colhidas de varias origens, armazenadas sob um esquema unificado, em um unico local.
	- Uma vez reunidos, os dados sao reunidos por muito tempo, permitindo o acesso a dados historicos.
	- Os depositos de  dados oferecem ao usuario uma unica interface consolidada para os dados, facilitando a escrita de consultas de apoio a decisao.
	- Ele armazena dados, SGBDs, historicos.
	
- OLAP x OLTP
	- OLAP (On-Line Analytical Processing) informacoes sao processadas para uma analise complexa.
		- Exemplos: Data Warehouse.
	- OLTP (On-Line Transaction Processing) refere-se aos sistemas com os quais trabalhamos normalmente, ou seja, qualquer operacao (insercao, alteracao ou exclusao) é executada de imediato no banco de dados utilizando-se transacoes.  
		- Exemplos: Sistema de cadastro de clientes, sistema de gestao empresarial.
		
- Data Mining 
	- O termo mineracao de dados (data mining) refere-se em geral, ao processo de analisar grandes bancos de dados para encontrar pradoes uteis.
	- assim como a descoberta de conhecimento na IA (ou machine learnig) ou na analise estatistica, a mineracao de dados tenta descobrir regras e padroes a partir dos dados.
	- Busca a descoberta do conhecimento nos bancos de dados.
	
# U1A4 - Topicos relevantes sobre banco de dados 
- redundancia de dados 
	- É a criacao de copias adicionais  de informacoes, armazenando-as em bancos de dados diferentes ou usando mecanismos diferentes.
	- Com componentes duplicados, nao ha necessidade de se preocupar com imprevistos, nem mesmo quando ouver necessidade de atualizacoes ou manutencao de servidores.
	- Se uma fonte de dados ficar inacessivel ou falhar, copias redundantes podem ser usadas para manter as operacoes em dia.
	- O objetivo dessa pratica e garantir a preservacao e recuperacao de dados em caso dew falhas, erros ou incidentes como falhas de hardware, ataques ciberneticos ou desastres naturais.
	
- Seguranca em bancos de dados 
	- atualmente, todos os SGBDs relacionais possuem um subsistema de controle de acesso que é responsavel pelo:
		1. gerenciamento de usuarios;
		2. pela definicao de niveis de acesso e pela selecao das operacoes que podme ser executadas pelos usuarios;
		3. bem como pelas informacoes que podem ser acessadas.
		
- Niveis de privilegios dos usuarios gerenciados via SGBD:
	- Nivel de conta de usuario: cada conta ou usuario individual possui um tipo de privilegio especifico;
	- Nivel de relacao/tabela: define para cada tabela do banco de dados um privilegio especifico para acesso e manipulacao dos dados.
	
- Em sistemas padrão SQL, a segurança é baseada no conceito de direitos ou privilégios, por meio dos quais os usuários têm ou não permissão para executar determinadas operações. Atualmente, o padrão ANSI/ISO define quatro privilégios: SELECT (consulta/extração de dados), INSERT (inclusão de novos registros), UPDATE (atualização de registros) e DELETE (exclusão de registros). Se um usuário com privilégio somente de consulta (SELECT) tentar incluir um registro utilizando o comando “INSERT INTO”, o servidor SQL retornará uma mensagem de erro.
	- e.g GRANT INSERT, DELETE ON CLIENTES TO user001;
	- ou para revogar o privilegio de exclusao: REVOKE DELETE ON CLIENTES FROM user001;
	
# U2A1 - Modelagem de dados com o modelo Entidade-Relacionamento (ER)
- MER (Modelo Entidade-Relacionamento)
	- utilizado para descrever os objetos do mundo real atraves de entidades, com suas propriedades que sao os atributos e os seus relacionamentos.
	- As entidades representam um objeto do mundo real e que possuem uma existencia independente, como: pessoas, empresa, carro, entre outras coisas que podem ser representadas por uma entidade.
	- Os atributos descrevem as propriedades das entidades, ex.: entidade Pessoa possui atributos como nome, idade, data de nascimento, etc.
	
- Modelos de dados 
	- Modelo Conceitual 
		- Representa a realidade mediante uma visao global e generica dos dados. tem o objetivo de conter todas as informacoes sem que se retrate aspectos relativos ao banco de dados.
	- Modelo Logico
		- Compreende a descricao das estruturas que serao armazenadas no banco de dados e resulta em uma representacao grafica destes dados de maneira logica. inclusive ja nomeando-se os componentes e as acoes que exercem um sobre o outro.
	- Modelo Fisico 
		- Se encontram detalhados os componentes de estrutura fisica do banco de dados, como tabelas, campos, tipos de valores, indices, etc.
		
# U2A2 - Elementos do modelo Entidade-Relacionamento (ER) I
- Entidades 
	- Principal conceito desta modelagem, sao os objetos do "mundo real", da realidade a ser modelada, sobre os quais deseja-se conhecer as informacoes e os relacionamentos entre elas.
	- exemplo: hospital.
	
- Relacionamentos 
	- É a associacao entre entidades, sendo que cada uma dessas entidades é responsavel por desempenhar uma funcao dentro desse relacionamento.
	- Por exemplo: suponha-se que haja as entidades "medico", "paciente" e "Hospital", em um universo.
	- Um possivel relacionamento entre elas é o "Atendimento", de modo que um medico possa atender um paciente em determinado hospital.
	
- Atributos 
	- Sao as caracteristicas especificas de uma entidade, alem disso, ha tambem a possibilidade de haver atributos nos relacionamentos. 
	- Por Exemplo, na entidade "Pessoa" pode haver os atributos "Nome", "CPF", entre outros elementos que possam descrevegr as caracteristicas de um individuo.
	- Outro exemplo e no relacionamento "Casamento", o qual pode possuir os atributos "Data" e "Local"
	
- Cardinalidade
	- Especifica o numero minimo e o maximo de instancias que uma entidade pode participar.
	- segue o anexo: U2A2_Cardinalidade.png
	- no minimo 1 professor ministra 1 discilina
	- no maximo 1 professor ministra 1 disciplina
	- 0 disciplina pode ficar sem profesores
	- n disciplinas podem ter n profesores
	- Tipos:
		- 1:1 um pra um 
		- N:M muitos para muitos
		- 1:M um para muitos
		- N:1 Muitos para um
		
# U2A3 - Elementos do modelo Entidade-Relacionamento (ER) II
- Generalizacao e Especializacao
	- Sao conceitos usados para representar objetos do mundo real (entidades) que possuem os mesmos atributos, podem ser categorizados e podem ser representados em uma hierarquia que mostra as dependencias entre entidades de uma mesma categoria.
	- Atraves desses conceitos, e possivel atribuir propriedades particulares aa entidade generica (entidade pai) a um subconjunto das ocorrencias (entidade especializada).
	- segue anexo: Anexos/U2A3_generalizacao_de_dados.png
	- segue anexo: Anexos/U2A3_cardinalidade_de_dados.png
	
- Tipos de atributos 
	- Simples
		- sao atributos considerados atomicos ou indivisiveis.
		- e.g cpf, telefone
		
	- Composto 
		- Atributos compostos podem ser divididos em partes menores, com significados independentes.
		- e.g endereco (que pode ser segmentado em: rua, cep, complemento, etc.)
	
	- Monovalorado
		- Esse atributo possui apenas um valor para uma determinada entidade.
		- e.g cpf (para cada pessoa existe apenas um cpf), endereco (uma pessoa pode ter apenas um endereco)
		
	- Multivalorado
		- Permite que um atributo de uma mesma entidade possa ter mais de um valor
		- e.g celular (uma pessoa pode ter mais de um celular)
		
- Entidade Assosciativa
	- tabela intermediaria ou entidade que é introduzida para resolver um relacionamento muitos-para-muitos entre duas entidades em um modelo de banco de dados relacional.
	- quando duas entidades tem um relacionamento direto de muitos-para-muitos, ou seja, cada instancia de uma entidade pode se relacionar com varias instancias da outra entidade e vice-versa, é necessario criar uma terceira entidade para gerenciar esse relacionamento complexo.
	- segue anexo: Anexos/U2A3_entidade_associativa.png
	
# U2A4 - Elementos do modelo Entidade-Relacionamento (ER) III
- Entidades Fortes
	- É quando existe por ela só, independentemente da existencia de outras entidades.
	- Por exemplo, em um sistema academico, a entidade curso é independente de quaisquer outras para existir, portanto, e considerada "forte".
	
- Entidades Fracas
	- São aquelas que dependem de outras para existir. São identificadas por se relacionarem com entidades especificas.
	- Pensando em um sistema academico, a entidade ementa de uma disciplina só tem sentido se houver a entidade disciplina.
	
- Superchave
	- Uma superchave é uma restrição que impede a ocorrência de valores idênticos em atributos de duas ou mais entidades distintas. Em termos simples, isso possibilita a identificação única de uma linha dentro de uma relação. Em algumas situações, é possível que uma superchave contenha atributos que não sejam necessários para essa identificação única da linha. Por exemplo, em uma tabela de registros de clientes, a combinação do código e do número de CPF pode formar uma superchave. No entanto, dado que o código é exclusivo para cada cliente, o CPF não se faz necessário para identificá-lo de forma única.
	
- Chave Primaria
	- Atributo ou conjunto de atributos em uma tabela que serve para identificar exclusivamente seus registros. garante que nao haja registros duplicados nela, ou seja, nehum valor pode se repetir nos campos que a compoem
	
- Chave Estrangeira
	- Tem a funcao de estabelecer relacoes entre os registros de uma tabela com os registros de outra tabela por meio de uma chave primaria desta ultima.
	- Sao amplamente utilizadas para fornecer valores de outra tabela, a qual contem a chave primaria.