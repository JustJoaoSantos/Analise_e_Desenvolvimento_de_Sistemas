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
	
# U1A2 - Sistema Gerenciadores de Banco de Dados (SGDB)
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