# Unidade 1
***
## U1A1 - Introdução
***
### A Linguagem SQL
● Linguagem padrão dos SGBD.
● SQL, do inglês Structured Query Language
● É a forma de tratarmos os vários aspectos de um banco de
dados:
	○ Definir esquemas de relacionamento;
	○ Criar restrições em relacionamentos;
	○ Realizar consultas interativas;
	○ Segurança e controle de atualizações.
● Nos seus estudos, você utilizará o SGBD MySQL.
● Trabalha com várias plataformas, tendo sido escrito em C e C++
● Definir instruções SQL incorporadas de maneira embutida ou
	dinâmica em linguagens, como por exemplo, Node.js, PHP, C#,
	C++, Java, Android, Swift, etc.
● Na linguagem SQL, destacam-se cinco subconjuntos de
	instruções:
● Linguagem de Definição de Dados (DDL)
	○ CREATE, DROP, ALTER, TRUNCATE
● Linguagem de Manipulação dos Dados (DML)
	○ INSERT, UPDATE, DELETE
● Linguagem de Consulta a Dados (DQL)
	○ SELECT, SHOW, HELP
● Linguagem de Controle de Dados (DCL)
	○ GRANT, REVOKE
● Linguagem de Transação de Dados (DTL)
	○ START TRANSACTION, COMMIT, SAVEPOINT, ROLLBACK
	
### Subconjuntos de Instruções
- DDL (Data Definition Language): 
	+ Linguagem de definição de dados
	+ é um conjunto de instruções SQL voltado para a definição dos 
		dados e sua estrutura.
	
- DML (Data Manipulation Language): 
	+ Linguagem de manipulação dos dados
	+ é um conjunto de instruções SQL direcionado para a inserção e 
		manutenção dos dados. 
		
DQL (Data Query Language):
	+ Linguagem de consulta a dados  
	+ um conjunto de instruções SQL voltado para a consulta de todos 
		os dados armazenados e suas relações, além de fornecer 
		assistência com comandos de sintaxe.

DCL (Data Control Language): 
	+ Linguagem de controle de dados
	+ é um conjunto de instruções SQL destinado ao controle de 
		autorizações de acesso e níveis de segurança

DTL (Data Transaction Language):
	+ Linguagem de transação de dados
	+ é um conjunto de instruções para o controle de transações 
		lógicas agrupadas e executadas por comandos DML.
		
### Transação em Banco de Dados 
- Atomicidade: 
	+ todas as operações em uma transação são tratadas como uma 
		unidade indivisível: ou todas as operações são concluídas com
		sucesso, ou nenhuma delas é aplicada. Se uma operação falhar, 
		a transação é revertida para o estado anterior.
- Consistência: 
	+ a transação leva o banco de dados de um estado consistente 
		para outro estado consistente. Isso significa que as 
		restrições de integridade do banco de dados devem ser 
		mantidas antes e após a execução da transação.
- Isolamento: 
	+ cada transação é executada de forma isolada das outras. As 
		modificações feitas por uma transação são invisíveis para 
		outras transações até que a primeira seja concluída. Isso 
		ajuda a evitar interferências e inconsistências causadas por 
		operações concorrentes.
- Durabilidade: 
	+ uma vez que uma transação é concluída com sucesso, suas 
		alterações tornam-se permanentes no banco de dados, mesmo em 
		caso de falha do sistema. Isso garante que as modificações 
		sobrevivam a eventos como quedas de energia ou falhas no 
		hardware.
		
## U1A2 - Linguagem de consulta de dados
***
### As Cláusulas SELECT e FROM
● SELECT – identificação dos campos desejados.
● FROM – lista as tabelas que deverão ser lidas.

> SELECT Nome FROM cidade;
> SELECT * FROM cidade;
> SELECT Nome, Populacao / 2 FROM cidade;
> SELECT DISTINCT Nome FROM cidade;

### A Cláusula WHERE
● WHERE - Consiste em expressões lógicas envolvendo os
	campos das tabelas da cláusula FROM.

> SELECT Nome, Populacao FROM cidade WHERE Populacao < 100000;
> SELECT Nome, Populacao
	FROM cidade
	WHERE Populacao BETWEEN 90000 AND 100000;
	
### Operação de renomeação e variáveis do registro
● Os campos podem ser renomeados com a cláusula AS
	○ nome-antigo AS nome-novo
- Nao é permanentes.
> SELECT Nome, Populacao AS PopulacaoDaCidade FROM cidade;
> SELECT C.Nome, C.Populacao, P.população FROM cidade as C, pais as P

### Operações de String e ordenação
● O operador LIKE determina a correspondência de padrões
	usando caracteres especiais: % ou _
> SELECT Nome FROM cidade WHERE Nome LIKE ‘Sor%’;

● Operador ORDER BY para ordenação (ASC ou DESC)
> SELECT Nome FROM cidade ORDER BY Nome;
> SELECT Nome FROM cidade ORDER BY Nome DESC;

## U1A3 - Criação de banco de dados 
***
### Planejamento de um banco de dados
● Para planejar um banco de dados, entendemos que há cinco
	passos principais:
	1. Coletar informações.
	2. Identificar suas principais estruturas.
	3. Modelar a estrutura.
	4. Identificar nas estruturas os tipos de dados (brutos, de
		categorização, de identificação, de referência).
	5. Identificar quais são seus relacionamentos.
	
### Internacionalização de um banco de dados
● Devemos prestar atenção na abrangência de utilização do banco
	+ Respeitar as regras de escrita e gramática ou representação
		de cada país
● MySQL possui as cláusulas CHARSET e COLLATION.
● CHARSET: designa um conjunto de símbolos e codificações e
	como eles são representados binariamente.
● COLLATION: conjunto de regras para comparação de caracteres
	em um CHARSET.
	+ 0: A, 1: B, 2: a, 3: b
● Como verificar CHARSET/COLLATION instalados no seu MySQL:
	+ SHOW CHARACTER SET;
	+ SHOW COLLATION;
●Exemplos:
	+ CHARSET: latin1 , COLLATION: latin1_swedish_ci
	+ CHARSET: utf8 , COLLATION: utf8_general_ci
	
### Criar um banco de dados
● Deveremos utilizar as instruções da classe da linguagem de
	definição de dados (DDL).
● os sufixos _ci e _cc representam case insensitive e case 
	sensitive respectivamente.
● CHARSET utf8 vs utf8mb4 
	+ utf8: alias para utf8mb3, armazenar apenas BPM de 3 bits
	+ utf8mb4: armazena character BPM de até 4 bits, padrão.
```SQL 
CREATE DATABASE IF NOT EXISTS mundo
	DEFAULT CHARSET = utf8mb4
	DEFAULT COLLATE = utf8_general_ci;

SHOW DATABASES;
ALTER DATABASE mundo CHARSET = latin1;
DROP DATABASE IF EXISTS mundo;
```

## U1A4 - Criação de Tabelas 
***
### Modelo de dados
• Diagrama Entidade-Relacionamento (DER)
• Certeza de que todos os dados existentes em um determinado 
	contexto estão completamente representados.
• Administrador de banco de dados (DBA) utiliza o modelo para
	gerar o BD físico

### Criação de tabelas
● Sintaxe da estrutura CREATE TABLE:
```SQL
CREATE TABLE [IF NOT EXISTS] nome_tabela (
	nome_campo tipo_campo[tamanho] [NOT NULL|NULL]
	[DEFAULT valor] [AUTO_INCREMENT] [PRIMARY KEY]
);
```
### Tipos de Dados: nomenclatura
● M: tamanho do dado
	+ Seu valor máximo está relacionado ao tipo de dado
● D: quantidade de dígitos “depois da vírgula”.
	+ Valor máximo é 30 (ou M-2)
● [ ]: partes opcionais na definição dos tipos.
● UNSIGNED: não aceita números negativos
● ZEROFILL: preencher com zeros à esquerda. E recebe o UNSIGNED

### Tipos Numéricos
● SMALLINT [(M)] [UNSIGNED] [ZEROFILL]
	+ inteiro no intervalo de -32768 a 32767. O intervalo sem sinal
		é de 0 a 65535.
● INT [(M)] [UNSIGNED] [ZEROFILL]
	+ Inteiro no intervalo de -2147483648 a 2147483647. O
		intervalo sem sinal é de 0 a 4294967295.
● BIGINT [(M)] [UNSIGNED] [ZEROFILL]
	+ intervalo de -9223372036854775808 a
		9223372036854775807.
● FLOAT [(M, D)] [UNSIGNED] [ZEROFILL]
	+ ponto flutuante, de precisão simples. Os valores admissíveis
		são -3,402823466E+38 a -1,175494351E-38, 0 e
		1,175494351E-38 a 3,402823466E+38.
● DOUBLE [(M, D)] [UNSIGNED] [ZEROFILL]
	+ ponto flutuante de precisão dupla.
	+ -1,7976931348623157E+308 a -2,2250738585072014E-308,0
	+ Sinônimo: DOUBLE PRECISION.

### Tipo Data e hora
● DATE
	+ MySQL exibe no formato 'YYYY-MM-DD’ e permite números
		ou strings
● DATETIME [(fsp)]
	+ Combinação de data e hora, no formato 'AAAA-MM-DD HH:
		MM: SS [fracao]’
● TIME [(fsp)] -> 'HH: MM: SS [fração]’
● YEAR [4] -> 'YYYY'

### Tipo Texto
● VARCHAR (M) [CHARACTER SET charset_name] [COLLATE collation_name]
	+ cadeia de comprimento variável.
● ENUM ('valor1', 'valor2', ...) [CHARACTER SET charset_name]
	[COLLATE collation_name]
	+ objeto de string que pode ter apenas um valor, escolhido na
		lista de valores 'valor1', 'valor2', [...], NULO, ou vazio.
	+ Armazenado como inteiro pelo banco
	
## U1A5 - Exemplo 
```SQL 
CREATE DATABASE IF NOT EXISTS Biblioteca;
USE Biblioteca;

CREATE TABLE IF NOT EXISTS Livros (
	ISBN INT PRIMARY KEY,
	Titulo VARCHAR(100) NOT NULL,
	Ano_Publicacao INT,
	ID_Autor INT
);

CREATE TABLE IF NOT EXISTS Autores (
	ID_Autor INT PRIMARY KEY,
	Nome VARCHAR(50) NOT NULL,
	Pais_Origem VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Editoras (
	ID_Editora INT PRIMARY KEY,
	Nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Usuarios (
	ID_Usuario INT PRIMARY KEY,
	Nome VARCHAR(50) NOT NULL,
	Data_Nascimento DATE
);
```