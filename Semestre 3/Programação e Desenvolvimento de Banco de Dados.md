# Unidade 1
***
## U1A1 - Introdução
***
### A Linguagem SQL
- Linguagem padrão dos SGBD.
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
- M: tamanho do dado
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
***
### CREATE
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

### INSERT
```SQL
INSERT INTO Usuarios (ID_Usuario, Nome, Data_Nascimento)
VALUES (101, 'Joao Santos', '2002-10-26');
```

### SELECT
```SQL
SELECT * FROM Funcionarios;
SELECT * FROM Funcionarios WHERE departamento = 'TI';
SELECT UPPER(nome) AS 'Nome do Funcionário', UPPER(departamento) AS 'Área de Atuação' FROM Funcionarios;

SELECT departamento, SUM(salario) as 'Soma dos Salarios' 
FROM Funcionarios 
GROUP BY departamento
ORDER BY SUM(salario) DESC;
```

# Unidade 2
***
## U2A1 - Comandos DML para manipulação de bancos de dados
***
### ● Linguagem de manipulação de dados (DML)
○ inserir, atualizar, excluir ou modificar dados
○ Principais instruções
○ Cláusulas condicionais

### Instrução de Inserção (INSERT)
● Permite adicionar novas linhas ou registro numa tabela
	existente.
	INSERT INTO nome_tabela (col1, col2) VALUES(15, 2);
	INSERT INTO nome_tabela (col1, col2) VALUES(15, 2), (1,3);
	
● Inserir múltiplas linhas
	INSERT INTO nome_tabela (a,b,c)
	VALUES(1,2,3), (4,5,6), (7,8,9);
	
● Exemplo: considere a tabela a seguir
```SQL 
CREATE TABLE IF NOT EXISTS convidado (
	id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(50) NOT NULL DEFAULT ’’,
	nascimento DATE,
	estudante ENUM('Não', 'Sim') NOT NULL DEFAULT 'Não'
);
```

```SQL 
INSERT INTO CONVIDADO (nome, nascimento, estudante)
VALUES ('Dani Moura', '1979-03-28', 'Sim');
```

- Resultado:
	+ id: 1
	+ nome: dani Moura
	+ nascimento: '1979-03-28'
	+ estudante: Sim
	
```SQL 
INSERT INTO CONVIDADO (nome, nascimento, estudante)
VALUES ('Rui Albuquerque', null , 'Sim');
```

- Resultado:

| id  | nome            | nascimento | estudante |
| --- | --------------- | ---------- | --------- |
| 2   | Rui Albuquerque | null       | sim       |

### Instrução de Atualização (UPDATE)
● UPDATE: atualiza colunas de linhas existentes na tabela
	nomeada com novos valores.
● SET: indica quais colunas modificar e os valores que devem ser
	fornecidos.
```SQL 
UPDATE convidado
SET estudante = 'Sim'
WHERE nome = 'Lebrencio Grulher'
AND nascimento = '08-Jul-1990';
```

● WHERE: condições que identificam quais linhas devem ser
	atualizadas
● ORDER BY e LIMIT:
```SQL 
UPDATE convidado SET estudante = 'Não';
UPDATE convidado
SET estudante = 'Sim'
WHERE nascimento < '08-Jul-1990’
LIMIT 10
ORDER BY nome;
```

● UPDATE pode ser usado para várias tabelas ao mesmo tempo
	○ Não pode utilizar ORDER BY e LIMIT, neste caso
```SQL 
UPDATE lista, produto SET lista.preco = produto.preco
WHERE lista.id = produto.id;
```

Instrução de Exclusão (DELETE)
● Instrução DML que exclui linhas de uma tabela.
● Uso semelhante à UPDATE.
● Sua sintaxe geral é dada por:
```SQL 
DELETE FROM
nome_tabela
[WHERE condição]
[ORDER BY ...]
[LIMIT quantidade_linhas]
```
● Exemplos: DELETE FROM convidados
```SQL 
WHERE estudante = 'Sim'
ORDER BY nome
LIMIT 10;
DELETE FROM log_usuario
WHERE usuario = ‘rm’
ORDER BY datahora_acao LIMIT 1;
```

## U2A2 - Alteração de tabelas
***
### Alteração de tabelas (ALTER TABLE)
● Comando que altera a estrutura de uma tabela
	○ Adicionar ou excluir colunas
	○ Criar ou destruir índices
	○ Renomear colunas, ou a própria tabela
	○ Alterar o mecanismo de armazenamento
	> ALTER TABLE nome_tabela
		[especificação_alteração
		[,especificação_alteração] ...]


● A sintaxe para as alterações é semelhante às cláusulas da
	instrução CREATE TABLE.
● Alguns comandos de especificação_alteração:
	> ADD [COLUMN] (nome_coluna definição_coluna,...)
		CHANGE [COLUMN] nome_antigo nome_novo
		definição_coluna
		DROP [COLUMN] nome_coluna
		RENAME COLUMN antigo_nome_coluna TO
		novo_nome_coluna

● Múltiplas cláusulas ADD, ALTER, DROP e CHANGE são permitidas
	em uma única instrução ALTER TABLE, separadas por vírgulas
● Outros exemplos:
```SQL 
ALTER TABLE cliente 
DROP COLUMN parentesco, DROP COLUMN telefones;
```

```SQL 
ALTER TABLE cliente AUTO_INCREMENT = 13;
```

```SQL
ALTER TABLE pessoas CHARACTER SET = latin1;
```	

- Alteração de coluna:
```SQL 
ALTER TABLE Customers
ADD Email varchar(255);
```
	
### Adicionando e excluindo colunas(ADD e DROP)
● ADD: adicionar novas colunas a uma tabela
● DROP: remover colunas existentes
● FIRST ou AFTER nome_coluna: adicionar uma coluna a uma
	posição específica dentro de uma linha da tabela. O padrão é na
	última linha.

### Renomeando, redefinindo e reordenando colunas
● As cláusulas CHANGE, MODIFY, RENAME COLUMN e ALTER
	permitem que os nomes e definições de colunas existentes
	sejam alterados. Exemplos:
> ALTER TABLE pessoas CHANGE antigo novo BIGINT NOT NULL;
> ALTER TABLE pessoas MODIFY nome INT NOT NULL;
> ALTER TABLE pessoas RENAME COLUMN novo TO antigo;
```SQL 
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
```

## U2A3 - Uso de Restrições (Constraints)
***
### Usando restrições (constraints)
```SQL 
CREATE TABLE pessoa (
	id int NOT NULL PRIMARY KEY,
	nome varchar(255) NOT NULL,
	sobrenome varchar(255),
	idade int 
);

ALTER TABLE pessoa 
DROP PRIMARY KEY;

ALTER TABLE pessoa
ADD CONSTRAINT PK_pessoa PRIMARY KEY (id, sobrenome);
```

● Sintaxe para definição de restrição de chave estrangeira com
	CREATE TABLE ou ALTER TABLE
```SQL 
ALTER TABLE nome_tabela
ADD [CONSTRAINT [símbolo]] FOREIGN KEY
[index_nome] (index_col_nome, ...)
REFERENCES nome_tabela (index_col_nome,...)
[ON DELETE referências]
[ON UPDATE referências]
```
+ referências: RESTRICT | CASCADE | SET NULL | NO ACTION

● Regras para nomear um índice de chave estrangeira:
	○ Se definido, o valor do símbolo CONSTRAINT é usado. Caso
		contrário, o valor do index_nome FOREIGN KEY é usado.
	○ Se nenhum símbolo CONSTRAINT ou FOREIGN KEY
		index_nome estiverem definidos, o nome do índice de chave
		estrangeira será gerado usando o nome da coluna de chave
		estrangeira de referência
		
● Integridade referencial:
```SQL 
CREATE TABLE pai (
	id INT NOT NULL,
	nome VARCHAR(50),
	PRIMARY KEY (id)
);

CREATE TABLE filha (
	id INT PRIMARY KEY,
	parente_id INT,
	nome VARCHAR(50)
);

ALTER TABLE filha
ADD CONSTRAINT FK_parente
FOREIGN KEY (parente_id) REFERENCES pai(id);
```

### Qualificadores
● São utilizados com as cláusulas ON UPDATE e ON DELETE
	○ CASCADE: qualificador que exclui ou atualiza a linha da
		tabela pai e exclui ou atualiza automaticamente as linhas
		correspondentes na tabela filha.
	○ SET NULL: exclui ou atualiza a linha da tabela pai e define
		como NULL a coluna ou colunas de chave estrangeira na
		tabela filha.
	○ RESTRICT: rejeita a operação de exclusão ou atualização da
		tabela pai.

● Para excluir uma restrição, podemos executar a instrução
	abaixo, em que a chave criada é mantida após esta execução,
	assim somente a restrição será excluída.
	> ALTER TABLE filha DROP FOREIGN KEY FK_parente;
	
	
## U2A4 - Exclusão de tabelas em banco de dados
***
### Restrição FOREIGN KEY
● A restrição FOREIGN KEY é usada para impedir ações que
destruam links entre tabelas
```SQL
CREATE TABLE aluno (
	id INT NOT NULL
	AUTO_INCREMENT PRIMARY
	KEY,
	nome CHAR(50) NOT NULL
);

CREATE TABLE curso (
	id INT NOT NULL
	AUTO_INCREMENT PRIMARY
	KEY,
	nome CHAR(50) NOT NULL
);

CREATE TABLE nota (
	aluno_id INT NOT NULL,
	curso_id INT NOT NULL,
	dataavaliacao DATE NOT NULL,
	nota DOUBLE NOT NULL,
	PRIMARY KEY(aluno_id, curso_id, dataavaliacao
),
INDEX i2 (curso_id),
FOREIGN KEY (aluno_id) REFERENCES aluno(id) ON DELETE
CASCADE,
FOREIGN KEY (curso_id) REFERENCES curso(id) ON DELETE
[ACTION]
```

### SHOW CREATE TABLE
● mostra dados referentes a tabela criada 
> SHOW CREATE TABLE nota;

```SQL 
CREATE TABLE `nota` (
	`aluno_id` int NOT NULL,
	`curso_id` int NOT NULL,
	`dataavaliacao` date NOT NULL,
	`nota` double NOT NULL,
	PRIMARY KEY (`aluno_id`,`curso_id`,`dataavaliacao`),
	KEY `i2` (`curso_id`),
	CONSTRAINT `nota_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES
	`aluno` (`id`) ON DELETE CASCADE,
	CONSTRAINT `nota_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES
	`curso` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci
```

### Outras operações
- DROP TABLE: remover uma ou mais tabelas
 > DROP TABLE [IF EXISTS] nome_tabela [, nome_tabela] ...
- Exclusão com restrição de chave estrangeira:
	> ALTER TABLE nota DROP FOREIGN KEY nota_ibfk_1;
		DROP TABLE IF EXISTS aluno;
		
- TRUNCATE TABLE: instrução para esvaziar uma tabela completamente
	+ Zera o contador AUTO_INCREMENT, mais rapido que o DELETE FROM 
	> TRUNCATE [TABLE] nome_tabela;
	
- Instruir o MySQL a “respeitar” as restrições
	> SET FOREIGN_KEY_CHECKS = 1;
	
- Instruir o MySQL a “ignorar” as restrições
	> SET FOREIGN_KEY_CHECKS = 0;
	
# Unidade 3
***
## U3A1 - Junções em bancos de dados 
```SQL Bando de Exemplo
CREATE TABLE categoria (
	id INT(3) PRIMARY KEY AUTO_INCREMENT,
	Nome VARCHAR(50) NOT NULL
);

CREATE TABLE produto (
	Codigo INT(3) PRIMARY KEY AUTO_INCREMENT,
	Nome VARCHAR(50) NOT NULL,
	Valor DECIMAL(6, 2),
	Id_Categoria INT(3) NOT NULL FOREIGN KEY (Id_Categoria) REFERENCES categoria(id)
);

INSERT Categoria VALUES (0, 'DVD'), (0, 'Livro'), (0, 'Informatica');

INSERT Produto VALUES (0, 'Código da Vinci', 39,99, 2), (0, 'vancock', 89.99, 1);
```
### Parâmetro JOIN
- Unir duas ou mais tabelas, ao se apontar os campos correspondentes entre elas.
	> SELECT[campo] FROM [tabela_1>JOIN<tabela_2] ON
		[tabela_1].[chave_primária] =
		[tabela_2].[chave_estrangeira]
		WHERE [condição];
		
- Tipos de JOIN: INNER, LEFT e RIGHT JOIN.

### Junção interna (JOIN / INNER JOIN)
- Consulta que retorne o nome da categoria e seus respectivos
	nomes dos produtos
```SQL
SELECT categoria.nome, produto.nome FROM
Categoria INNER JOIN Produto
ON Categoria.Id = Produto.Id_Categoria;
```

- Saida:

| nome  | nome            |
| ----- | --------------- |
| Livro | Código da Vinci |
| DVD   | Hancock         |

### INNER JOIN
- Utilizar condições nas consultas, quando for necessário fazer as junções entre as tabelas
```SQL
SELECT categoria.nome as "Tipo", produto.nome as "Produto", produto.valor
FROM Categoria INNER JOIN Produto
ON Categoria.Id = Produto.Id_Categoria
WHERE produto.valor < 50.00;
```
| Tipo  | Produto        | Valor |
| Livro | Código da vinci| 39.99 |

Junção Externa
● Considere as tabelas de exemplo:
	> SELECT * FROM categoria SELECT * FROM produto
|	id | Nome        |   | Codigo | Nome           | Valor | Id_Categoria|
| 1  | DVD         |   |   1    | Código da vinci| 39.99 | 2           |
| 2  | Livro       |   |   2    | Hancock        | 89.99 | 1           |
| 3  | Informatica |   

● Quando o operador de junção externa for utilizado no SQL, é
	gerado o resultado da junção mais as linhas não combinadas.
● É possível efetuar junções externas em ambos os lados

### LEFT JOIN
● Exemplo:
```SQL 
SELECT categoria.nome as "Tipo", produto.nome as "Produto", produto.valor 
FROM Categoria LEFT JOIN Produto
ON Categoria.Id = Produto.Id_Categoria;
```
| Tipo				| Produto 				|	Valor	|
|	DVD					| Hancock     		|	89.99	|
|	Livro				| Código da vinci	|	39.99	|
|	Informatica	| Null 						|	Null	|

### RIGHT JOIN
● Exemplo:
```SQL
SELECT categoria.nome as "Tipo", produto.nome as "Produto", produto.valor
FROM Categoria RIGHT JOIN Produto
ON Categoria.Id = Produto.Id_Categoria;
```
|	Tipo	|	Produto					|	Valor	|
|	Livro	|	Código da vinci	|	39.99	|
|	DVD		|	Hancock					|	89.99	|

## U3A2 - Funções de Agregação
***
### GROUP BY
● Funções de agregação em SQL: desenvolver consultas utilizando
	valores das colunas como parâmetro de pesquisa (SELECT).
● Os resultados das seleções podem ser organizados em grupos,
	baseados no conteúdo existente em uma ou mais colunas.
> SELECT [coluna] FROM [tabela]
	WHERE [condição]
	GROUP BY [coluna];
	
### Funções de agregação
● Funções agregadas operam sobre conjuntos de valores,
	retornando um único resultado.
● SQL oferece cinco funções de agregação nativas: AVG, MIN,
	MAX, SUM e COUNT.
● Estrutura básica para utilizar funções de agregação:
	> SELECT função_de_agregação(coluna) AS
		nome_da_coluna_agregada
		FROM tabela
		[WHERE condição]
		[GROUP BY coluna]

## U3A3 - Sub-consultas aninhadas
***
### Subconsultas com IN e NOT IN
- É considerada uma subconsulta uma expressão em SQL, composta por SELECT-FROM-WHERE, aninhada dentro de outra consulta, permitindo fazer comparações entre os conjuntos de dados.
- Conectivos IN e NOT IN
> SELECT [campo]
		FROM [tabela]
		WHERE [campo] IN / NOT IN ( SELECT [campo] FROM [tabela] );

- Tabela Aluno

| RA  | nome  | telefone  |
| --- | ----- | --------- |
| 11  | Maria | 119999999 |
| 22  | Joao  | 119988888 |
| 33  | Jose  | 119777777 |
| 44  | Jonas | 119666666 |
- Tabela Emprestimo

| numero | retirada   | devolucao  | aluno_RA | funcionario_mat | libro_isbn |
| ------ | ---------- | ---------- | -------- | --------------- | ---------- |
| 1      | 2018-01-15 | 2018-02-01 | 11       | 1               | 11111      |
| 2      | 2018-04-05 | 2018-04-20 | 22       | 1               | 22222      |
- Tabela Restricao

| id  | aluno_RA | libro_isbn |
| --- | -------- | ---------- |
| 1   | 33       | 44444      |
```SQL
SELECT aluno.nome FROM aluno
WHERE aluno.RA NOT IN
(SELECT aluno_RA FROM restricao);
```
- Resultado:

| nome  |
| ----- |
| Maria |
| Joao  |
| Jonas |
```SQL
SELECT aluno.nome AS 'ALUNO' FROM
aluno WHERE aluno.RA NOT IN
(SELECT aluno_RA FROM emprestimo);
```
- Resultado:

| ALUNO |
| ----- |
| Jose  |
| Jonas |
### Comparação de Conjuntos
- O SQL permite desenvolver subconsultas aninhadas utilizando condições (WHERE)

| Operador Matemático | SELECT com WHERE (SQL)  | Subconsulta (SQL)               |
| :-----------------: | ----------------------- | ------------------------------- |
|          =          | WHERE campo = condição  | WHERE campo = SOME (SELECT...)  |
|         !=          | WHERE campo <> condição | WHERE campo <> SOME (SELECT...) |
|          >          | WHERE campo > condição  | WHERE campo > SOME (SELECT...)  |
|         >=          | WHERE campo >= condição | WHERE campo >= SOME (SELECT...) |
|          <          | WHERE campo < condição  | WHERE campo < SOME (SELECT...)  |
|         <=          | WHERE campo <= condição | WHERE campo <= SOME (SELECT...) |
- Exemplo: Listar os nomes do empregados que têm salário superior a algum empregado do departamento B
```SQL
SELECT nome, salario, dpto FROM colaborador;
```

| nome  | salario | dpto |
| ----- | ------- | ---- |
| joao  | 3000.00 | B    |
| maria | 6000.00 | A    |
| zé    | 2000.00 | A    |
| bil   | 3000.00 | B    |
| ana   | 5000.00 | C    |
```SQL
SELECT salario FROM colaborador WHERE dpto = "B";
```

| salario |
| ------- |
| 3000.00 |
| 3000.00 |
```SQL
SELECT nome, salario, dpto FROM colaborador
WHERE salario > SOME (SELECT salario FROM colaborador WHERE dpto = 'B');
```

| nome  | salario | dpto |
| ----- | ------- | ---- |
| maria | 6000.00 | A    |
| ana   | 5000.00 | C    |
## U3A4 - Visões (View), índices (Index) e Fulltext
***
### Introdução
- Necessidade de técnicas que proporcionem um maior aproveitamento dos recursos disponíveis
- Considere o exemplo:
![[PBD_U3A4_exemplo_tabela.png]]

### Visões (VIEW)
- O recurso SQL para gerar visões é uma alternativa para visualizar os dados de uma ou mais tabelas de um BD (tabela virtual)
- A técnica de VIEW encapsula uma seleção de dados (SELECT)
- Torna as consultas mais rápidas
- Quando há alterações, o SGBD atualiza a VIEW automaticamente.
- Sintaxe e operações com uma VIEW:
> CREATE VIEW [nome_da_VIEW] AS
> SELECT [coluna]
> FROM [tabela]
> WHERE [condições];

> SELECT * FROM [nome_da_VIEW];

> DROP VIEW [nome_da_VIEW];

- Exemplo:
```SQL
CREATE VIEW v_select1 AS
SELECT veiculo.nome as “Veiculo”, fabricante.marca as “Marca”, veiculo.cor as “Cor”,
veiculo.preco as “Valor”
FROM veiculo INNER JOIN fabricante
WHERE veiculo.fabricante_Codigo = fabricante.Codigo AND veiculo.preco <= 50000;
```

- Vantagens:
	+ Economia de tempo: diminuição na carga de criação de comandos SELECT
	+ Velocidade de acesso: devido às VIEWs estarem pré armazenadas
	+ Ocultação da complexidade: o usuário não necessita saber dos campos, nem das seleções.

### Índice (INDEX)
- Problema do Table Scan: tempo de verificação tende a ser muito grande.
- A utilização dos índices é opcional para a seleção de dados → estruturas redundantes.
- Não era admitido até a versão SQL:1999

- Declarar um índice, no desenvolvimento da tabela:
	> CREATE TABLE [nomeDaTabela] (
	> 	Campo1 tipo(tamanho),
	> 	Campo2 tipo(tamanho),
	> 	INDEX(Campo1)
>	);

- Declarar um índice em tabela existente no BD:
> CREATE INDEX [nomeDoIndice] ON [nomeDaTabela](Campo);

- Exemplo:
```SQL
CREATE INDEX idx_Renavam
ON veiculo(RENAVAN);

SHOW INDEX FROM veiculo;
```
- Resultado:

| Table   | Non_unique | Key_name          | Seq_in_index | Column_name       |
| ------- | ---------- | ----------------- | ------------ | ----------------- |
| veiculo | 0          | PRIMARY           | 1            | RENAVAN           |
| veiculo | 1          | Fabricante_Codigo | 1            | Fabricante_Codigo |
| veiculo | 1          | idx_Renavam       | 1            | RENAVAN           |


- Sintaxe para utilizar um índice:
> SELECT [coluna] FROM [nomeDaTabela]
> USE INDEX (nomeDoIndice)
> WHERE [condições];

- Exemplo:
```SQL 
SELECT nome AS “Veiculo”, cor AS “Cor”, Preço AS “Valor” 
FROM veiculo
USE INDEX(idx_Renavam)
WHERE preco<= 50000;
```
### FULLTEXT em banco de dados relacional
- Buscar um trecho dentro de várias strings / ativa fulltext na tabela
> ALTER TABLE [nome_tabela] ADD FULLTEXT (nome_da_coluna);

- Buscar palavras dentro de longos textos:
> SELECT [coluna] FROM nome_da_tabela 
> WHERE MATCH(coluna)
> AGAINST(‘palavra_desejada’);

