# U1A1 - Fundamentos de Orientacao a objetos
- Competencia ENADE: analisar, projetar, documentar, implemetar, testar, implantar e manter sistemas computacionais para diferentes plataformas/comceber, especificar, projetar, construir, testar, verificar e validar sistemas de computacao
- Evolucao da programacao
	- Evoluiu de abordagem lineares e sequenciais para paradigmas mais complexos.
	- Na decada de 1960 as tentativas de estruturar melhor as aplicacoes levou ao desenvolvimento do POO
	
- Objeto: conceitos do mundo real que podem ser sistematizados em um programa.

- Linguagems pioneiras
	- Simula foi a primeira linguagem a introduzir o conceito de classses. 
	- Smalltalk e C++ posteriormente popularizaram este paradigma.
	
- Vantagens da OO 
	- Modularidade que facilita a manutencao 
	- escalabilidade 
	
- Pilares da OO 
	- Abstracao: processo de simplificar um sistema ao ocultar detalhes complexos e mostrar apenas as características essenciais de um objeto
	- Encapsulamento: consiste em proteger os dados de um objeto, permitindo o acesso somente através de métodos específicos, garantindo que os atributos internos de um objeto não sejam alterados de maneira incorreta.
	- Heranca: permite que uma classe derive de outra, herdando seus atributos e métodos.
	- Polimorfismo:  é a capacidade de um método ou função de assumir diferentes formas com base no objeto em que é aplicado
	
# U1A2 - Conceitos Basicos de Orientacao a Objetos em Programacao 
- Linguagem de programacao OO 
	- Java 
	- Python 
	- C++
	
- Ambientes de desenvolvimentos (IDE)
	- Eclipse
	- PyCharm
	- NetBeans
	
- Frameworks
	- fornecem um conjunto de ferramentas, bibliotecas e praticas recomendadas que facilitam o desenvolvimento.
	- Spring (java): simplifica o desenvolvimento de aplicações empresariais e promove o uso de componentes modulares.
	- Django (python): facilita o desenvolvimento de aplicações web.
	- Qt (C++): Framework multiplataforma para desenvolvimento de interfaces gráficas.
	
- Atributos e operacoes
	- atributos sao variáveis que armazenam as propriedades de um objeto e descrevem o estado do objeto em um dado momento.
	- Operacoes descrevem o comportamento que os objetos podem ter.
	- atributos (attributes / variables)
	- metodos (methods / functions)
	
- Visibilidade e modificadores de acesso 
	- permite controlar como e de onde eles podem ser acessados dentro do codigo
	- publico (public)
	- protegido (protected)
	- privado (private)
	
# U1A3 - Introducao as Aplicaçoes Orientadas a objetos
- beneficios
	- Reusabilidade de Codigo
	- Manutencao Simplificada
	- Flexibilidade
	- Seguranca e Controle
	
- Principios de design da OO 
	- Principio da Responsabilidade Unica: 
		- SRP ou Single Responsability Principle 
		- Afirma que cada classe deve ter apenas uma unica razao para mudar. 
		- Ou seja cada classe deve ser responsavel or uma unica funcionalidade dentro do sistema.
	
	- Principio Aberto/Fechado:
		- OCP ou Open/Close Principle
		- Afirma que uma classe deve sera aberta para extensao, mas fechada para modificacao. 
		- Ou seja, ao criar novas funcionalidades nao devemos modificar as existentes.
	
	- Principio da substituicao de liskov:
		- LSP ou Liskov Substitution Principle
		- afirma que objeatos de uma classe derivada devem ser capazes de substituir objetos da classe base sem alterar a corretude do sistema.
		- Ou seja, uma subclasse deve poder ser usada no lugar da classe pai sem causar problemas de comportamento.
		
	- Principio da segregacao de interfaces:
		- ISP ou Interface Segregation Principle
		- afirma que uma classe nao deve ser forcada a implementar interfaces que ela nao usa.
		- Ou seja, em vez de criar interfaces grandes e genericas, e melhor criar interfaces pequenas e especificas para diferentes comportamentos.

# U1A4 - Classe, Objeto e Instancia
- Classe 
	- 'Molde' para criar objetos, este conceito permite criar modelos que representam elementos do mundo real, organizando e encapsulando caracteristicas e comportamentos 
	- Exemplo UML:
	``` UML diagram de classe
			Pessoa
		- id : int 
		- nome : string
		- endereco : Endereco 
		--------------------
		+ getNome() : string 
		+ getIdade() : int 
		+ setEndereco(e : Endereco) : void
	```
- Componentes principais de uma classe:
	- Nome
	- Atributos
	- Operacoes/Metodos
	
- Criacao e instanciacao de objetos 
	- Instanciar significar criar uma instancia especifica de uma classe, ou seja objeto 
	- exemplo:
		- Livro livro1 = new Livro("Dom Quixote", "Miguel de Cervantes", 1605);
		- Instancia de classe 'Livro' chamada 'livro1'
		
- Relacao entre classes, objetos e instancias 
	- Classe: nao ocupa espcao de memoria, pois e um templete, mas ao compilar a definicao ira ser armazenada para uso posterior 
	- Objeto: cadas instancia ocupa um espaco na memoria.
	
#U2A1 - Construtores e Sobrecarga
- contrutores
	- Na programação orientada a objetos, um construtor é um método especial dentro de uma classe cuja função é inicializar objetos dessa classe.
	- nao possui tipo de retorno, nem void
	- nome sera o mesmo da classe
	
- sobrecarga 
	- permite criar multiplas versoes de um construtor (ou de um metodo) com diferentes conjuntos de parametros.
	- em java, ela funciona porque a linguagem permite ter metodos com o mesmo metodo se forem diferenciados pelos parametros.

#U2A2 - Estrutura de Decisao
- If 
	- verifica se a variavel e verdadeira, se o valor logico for TRUE, o block if() sera executado, caso contrario o bloco else() sera executado.
	- exemplo:
	```java 
	public void aumentarVolume(){
		if (ligado) {
			//bloco true
		} else {
			//bloco false
		}
	}
	
	```
- Switch case
	- alternativa ao if para casos em que existem muitas condicoes possiveis.
	```
	int i = 1;
	switch (i) {
		case 1:
			//bloco 1
			break;
		case 2:
			//bloco 2
			break;
		default:
			//bloco executado quando todos os cases for falso
			break;
	}
	```
	
- operadores relacionais
	- == : igual a 
	- != 
	- > 
	- < 
	- >= 
	- <= 
	- ! : nao 
	- && : e 
	- || : ou
	
# U2A3 - Estruturas de Repetição
- while
	- Ausada quando não sabemos exatamente quantas vezes o laço será repetido, mas sabemos a condição que deve ser satisfeita para continuar o loop
	```
	int i = 1;
	while (i <= 100) {
		System.out.println(i + " vezes");
	}
	```

- for
	- usado quando sabemos de antemão quantas vezes queremos repetir o bloco de código
	```
	for (int i = 1; i <= 100; i++) {
		System.out.println(i + " vezes");
	}
	```
	
- do while
	- O laço “do-while” é similar ao “while”, com a diferença de que ele garante que o bloco de código seja executado pelo menos uma vez, mesmo que a condição seja falsa.
	```
	int i = 1;
	do {
		i++;
		System.out.println(i + " vezes");
	} while (i <= 100);
	```
	
- break 
	- interrompe a execucao e sai do loop

- continue 
	- interrompe a execucao e pula para o proximo loop, ignorando o codigo restante.
	
- for-each
	- Prefira “for-each” para percorrer listas e arrays: a estrutura “for-each” é mais eficiente e legível quando precisamos apenas acessar os elementos de uma lista.
	```
	int[] numeros = {1, 2, 3, 4, 5};
	
	for (int num : numeros) {  //para cada numero salve em num.
		System.out.println(num);
	}
	```
	
# U2A4 - Reutilizacao de classes 
- Heranca, interface e polimorfismo
	```java em Treinavel.java
	public interface Treinavel {
		void executarComando(String comando);
	}
	```
	
	```java em Animal.java
	public class Animal {
		public void falar() {
			System.out.println("animal faz um som");
		}
	}
	```
	- herdando da classe Animal e implementando a interface Treinavel.
	```java em Cachorro.java
	public class Cachorro extends Animal implements Treinavel {
		@Override
		public void falar() {
			System.out.println("au au");
		}
		
		@Override 
		public void executarComando(String comando) {
			System.out.println("executando o comando: " + comando);
		}
	}
	```
	
	- driver function 
	```java em HerancaInterface.java 
	public class HerancaInterface {
		public static void main(String[] args) {
			Cachorro cachorro = new Cachorro();
			cachorro.falar();
			cachorro.executarComando("Sente");
		}
	}
	```
	
	- compilando e executando arquivo
	```terminal
	javac HerancaInterface.java 
	java HerancaInterface
	```

# U3A2 - Definicao e uso de interfaces
- interface e herança
```
public class AlunoGraduacao extends Aluno implements Avaliacao {
	public AlunoGraduacao(String nome, int matricula, double nota) {
		super(nome, matricula, nota); //passando input do construtor para classe pai 
	}
	
	@Override 
	public double calcularMedia() { //sobrecarga da interface
		return getNota() * 1.2;
	}
}
```

# U3A3 - Classes Abstratas
- ao contrario das interfaces classes concretaas podem herdar apenas uma classa abstrata
- classe abstrata 
```
abstract class Pessoa { //nao para ser instanciada apenas herdada
	protected String nome;
	
	public Pessoa(String nome) {
		this.nome = nome;
	}
	
	public abstract void apresentar();
}

class Aluno extends Pessoa {
	private int matricula;
	
	public Aluno (String nome, int matricula) {
		super(nome)
		this.matricula = matricula;
	}
	
	@Override 
	public void apresentar() {
		System.out.println("Eu sou o aluno " + nome + " e minha matricula " + matricula);
	}
}

public class Main {
	public static void main(String[] args) {
		Aluno aluno1 = new Aluno("Joao", 16);
		aluno1.apresentar();
	}
}
```

# U4A4 - Tratamento de excessoes
- o try-catch imperirar que o sistema quebre e exibirar uma mensagem de erro amigavel
- o finally garantira que o sistema sempre finalize corretamente
```
try {

    // Código que pode gerar uma exceção

} catch (TipoDeExcecao e) {

    // Código para tratar a exceção

} finally {

    // Código que será executado sempre

}
```

- tipos de excessoes 
Em Java, as exceções podem ser classificadas em duas categorias principais:

1.    Checked Exceptions:

    São verificadas pelo compilador e devem ser tratadas obrigatoriamente. Exemplos:
    IOException”: Erros relacionados à entrada e saída de dados.
    “SQLException”: Erros relacionados ao banco de dados.

2.    Unchecked Exceptions:

    Não são verificadas pelo compilador e podem ou não ser tratadas pelo programador. Exemplos:
    “ArithmeticException”: Como no caso de divisão por zero.
    “NullPointerException”: Tentativa de acessar métodos ou atributos de um objeto nulo.
	
# U4A1 - Conceito e Aplicacao
- Ciclo de vida 
	- Analise
	- design
	- Implementacao 
	- Teste e manutenca
	
- Design Patterns
	- Singleton: Garantir que uma classe tenha apenas uma instancia e fornecer um ponto global de acesso.
	- Factory Method: Criar objetos sem expor a logica de criacao ao cliente. 
	- Observer: permitir que objetos sejam notificados sobre mudancas em outro metodos.
	
# U4A2 - Arrays 
- os arrays, ou vetores, sao estruturas de dados fundamentais para organizacao e manipulacao de informacoes.

- Vetor unidimensional
	```
	int[] notas = new int[5]; //declaracao de array de 5 elementos 
	notas[0] = 902;
	notas[1] = 200;
	
	for (int i = 0; i < notas.length; i++) {
		System.out.println(notas[i]);
	}
	
	Arrays.sort(notas);
	```
	
- array multidimensional ou matriz
	```
	int[][] matriz = {
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9}
	}
	
	for (int linha = 0; linha < matriz.lenght; linha++) {
		for (int coluna = 0; coluna < matriz[linha].length; coluna++) {
			System.out.println(matriz[linha][coluna]);
		}
	}
	```
	
- array list 
	```
	import java.util.ArrayList;

	public class ExemploArrayList {
		public static void main(String[] args) {
			ArrayList<String> nomes = new ArrayList<>();
			nomes.add("João");
			nomes.add("Maria");
			nomes.add("Carlos");

			for (String nome : nomes) {
				System.out.println(nome);
			}
		}
	}
	```

# U4A3 - Colecoes e Arquivos
- O framework 'java.util.collection' define a base para diversas implementacoes de colecoes, como listas, conjuntos, filas e mapas.
- tipos e characteristicas
	- list: permite duplicatas, mantem ordem, acesso por indice
	- Set: nao permite duplicata, nao mantem ordem, acesso por iteracao
	- Map: chaves unicas, valores repetem, nao mantem ordem, acesso por chave.

- Lista dinamica ou ArrayList 
	- Uma lista dinâmica é um tipo de coleção que armazena elementos de maneira sequencial e ajusta seu tamanho automaticamente
	```
	import java.util.ArrayList;
	
	ArrayList<String> nomes = new ArrayList<>();
	nomes.add("Ana");
	nomes.add("anderson");
	nomes.add("clara");
	
	int i = 1;
	for (String nome : nomes) {
		System.out.println(i + "-" + nome);
		i++;
	}
	```
	
- Conjuntos ou Sets
	- Conjuntos garantem que cada elemento seja único, sendo ideais em cenários que requerem eliminação de duplicatas.
	```
	import java.util.HashSet;

	public class ExemploHashSet {
		public static void main(String[] args) {
			HashSet<String> linguagens = new HashSet<>();
			linguagens.add("Java");
			linguagens.add("Python");
			linguagens.add("Java"); // Não será adicionado novamente

			for (String linguagem : linguagens) {
				System.out.println(linguagem);
			}
		}
	}
	```

- Filas ou Queue
	- Filas operam no sistema FIFO (First In, First Out), aplicáveis em gerenciamento de tarefas ou mensagens
	```
	import java.util.LinkedList;
	import java.util.Queue;

	public class ExemploQueue {
		public static void main(String[] args) {
			Queue<String> fila = new LinkedList<>();
			fila.add("Pedido 1");
			fila.add("Pedido 2");
			fila.add("Pedido 3");

			while (!fila.isEmpty()) {
				System.out.println("Processando: " + fila.poll());
			}
		}
	}
	```
	
- Mapas ou Maps
	- Os mapas armazenam dados no formato chave-valor, permitindo acesso eficiente baseado na chave.
	```
	import java.util.HashMap;

	public class ExemploHashMap {
		public static void main(String[] args) {
			HashMap<Integer, String> alunos = new HashMap<>();
			alunos.put(1, "Carlos");
			alunos.put(2, "Marina");

			for (int chave : alunos.keySet()) {
				System.out.println("ID: " + chave + ", Nome: " + alunos.get(chave));
			}
		}
	}
	```
	
	
- Classe para usar listas
 ```
 class ListaNomes {
	private ArrayList<String> nomes = new ArrayList<>();
	
	public void adicionarNome(String lnome) {
		nomes.add(lnome);
	}
	
	public void removerNome(String lnome) {
		nomes.remove(lnome);
	}
	
	public void listarNomes() {
		for (String nome : nomes) {
			System.out.println(nome);
		}
	}
 }
 
 public class main {
	public static void main(String[] args) {
		ListaNomes lista = new ListaNomes();
		
		lista.adicionarNome("Anderson");
		lista.adicionarNome("Roberto");
		lista.adicionarNome("Clara");
		
		lista.listarNomes();
		
		lista.removerNome("Clara");
		
		lista.listarNomes();
	}
 }
 ```
 
- Leitura de arquivos 
	- realizado por classes como FileReader ou BufferedReader que permite ler arquivos linha por linha
	```
	import java.io.BufferedReader;
	import java.io.FileReader;
	import java.io.IOException;

	public class LeituraArquivo {
		public static void main(String[] args) {
			try (BufferedReader br = new BufferedReader(new FileReader("dados.txt"))) {
				String linha;
				while ((linha = br.readLine()) != null) {
					System.out.println(linha);
				}

			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	```
	
- Gravacao em arquivos 
	- A gravação é feita com “BufferedWriter” e “FileWriter”.
	```
	import java.io.BufferedWriter;
	import java.io.FileWriter;
	import java.io.IOException;

	public class GravacaoArquivo {
		public static void main(String[] args) {
			try (BufferedWriter bw = new BufferedWriter(new FileWriter("saida.txt"))) {
				bw.write("Primeira linha.");
				bw.newLine();

			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	```
	

- Organização e serialização de dados em aplicações
	- Serialização é o processo de converter objetos em um formato que pode ser armazenado ou transmitido, permitindo sua recuperação posterior
	- Em Java, a serialização é feita com a interface “Serializable”. Objetos serializados podem ser salvos em arquivos ou enviados pela rede.
	```
	import java.io.*;

	class Pessoa implements Serializable {
		private String nome;
		private int idade;

		public Pessoa(String nome, int idade) {
			this.nome = nome;
			this.idade = idade;
		}

		@Override
		public String toString() {
			return nome + ", " + idade + " anos";
		}
	}

	public class SerializacaoExemplo {
		public static void main(String[] args) {
			try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("pessoa.dat"))) {
				Pessoa p = new Pessoa("Ana", 25);
				oos.writeObject(p);

			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	```
	

- Recuperação de dados serializados
	- Objetos serializados podem ser lidos com “ObjectInputStream”. A seguir, pode ser observado uma implementação em Java utilizando este tipo de objeto.
	```
	try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("pessoa.dat"))) {
		Pessoa p = (Pessoa) ois.readObject();
		System.out.println("Dados: " + p);

	} catch (IOException | ClassNotFoundException e) {
		e.printStackTrace();
	}
	```

# U4A4 - Banco de dados relacional
- MySQL
	```
	-- criando banco de dados 
	CREATE DATABASE gerenciamento_clientes;
	USE gerenciamento_clientes;
	
	-- criar tabela
	CREATE TABLE cliente (
		id int primary key,
		nome varchar(100),
		email varchar(100),
		telefone varchar(15),
		cidade varchar(50),
		uf varchar(2)
	);
	
	-- inserir dados em tabela cliente 
	INSERT INTO cliente VALUES (1, 'Anderson', 'anderson@hotmail.com', '43 99999-9999', 'Londrinas' , 'PR');
	INSERT INTO cliente VALUES (2, 'Anderson', 'anderson@hotmail.com', '43 99999-9999', 'Londrinas' , 'PR');
	INSERT INTO cliente VALUES (3, 'Anderson', 'anderson@hotmail.com', '43 99999-9999', 'Londrinas' , 'PR');
	
	-- busca das informacoes
	SELECT * FROM cliente;
	
	-- update de informacoes 
	UPDATE cliente 
		SET nome = 'Dorival', 
			uf = 'SP'
		WHERE id = 2;
		
	-- busca selecionada
	SELECT id, nome, cidade, uf FROM cliente;
	
	-- delecao selecionada
	DELETE FROM cliente WHERE id = 3;
	```
- conexao java -> sql
	```
	import mysql.connector
	
	conexao = mysql.connector.connect(
	host="localhost",
	user="root",
	password="sua_senha",
	database="gerenciamento_loja"
	)

	cursor = conexao.cursor()
	 
	# Consultar produtos de uma categoria específica
	categoria = 1
	cursor.execute(f"SELECT nome_produto, preco, estoque FROM produtos WHERE id_categoria = {categoria}")
	 
	for produto in cursor.fetchall():
			print(produto)
	conexao.close()
	```
- usando java para conectar com o banco de dados 
	```
	import java.sql.Connection;
	import java.sql.DriverManager;
	import java.sql.SQLException;
	 
	public class DatabaseConnection {
		private static final String URL = "jdbc:mysql://localhost:3306/meubanco";
		private static final String USER = "usuario";
		private static final String PASSWORD = "senha";
	 
		public static Connection getConnection() throws SQLException {
			return DriverManager.getConnection(URL, USER, PASSWORD);
		}
	}
	```
	
- usando java para realizar consultas
	```
	import java.sql.Connection;
	import java.sql.ResultSet;
	import java.sql.SQLException;
	import java.sql.Statement;
	 
	public class QueryExample {
		public static void main(String[] args) {
			try (Connection connection = DatabaseConnection.getConnection();
				 Statement statement = connection.createStatement();
				 ResultSet resultSet = statement.executeQuery("SELECT * FROM Clientes")) {
	 
				while (resultSet.next()) {
					int id = resultSet.getInt("ID");
					String nome = resultSet.getString("Nome");
					String email = resultSet.getString("Email");
					String dataNascimento = resultSet.getString("DataNascimento");
	 
					System.out.println("ID: " + id + ", Nome: " + nome + ", Email: " + email + ", Data de Nascimento: " + dataNascimento);
				}
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	```
	
- usando java para inserir dados 
	```
	import java.sql.Connection;
	import java.sql.PreparedStatement;
	import java.sql.SQLException;
	 
	public class InsertExample {
		public static void main(String[] args) {
			String sql = "INSERT INTO Clientes (ID, Nome, Email, DataNascimento) VALUES (?, ?, ?, ?)";
	 
			try (Connection connection = DatabaseConnection.getConnection();
			PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
				preparedStatement.setInt(1, 2);
				preparedStatement.setString(2, "Maria Oliveira");
				preparedStatement.setString(3, "maria.oliveira@example.com");
				preparedStatement.setDate(4, java.sql.Date.valueOf("1990-08-25"));

				int rowsAffected = preparedStatement.executeUpdate();
				System.out.println("Linhas afetadas: " + rowsAffected);

			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	```
	
- usando java para atualizar os dados 
	```
	import java.sql.Connection;
	import java.sql.PreparedStatement;
	import java.sql.SQLException;
	 
	public class UpdateExample {
		public static void main(String[] args) {
			String sql = "UPDATE Clientes SET Email = ? WHERE ID = ?";
	 
			try (Connection connection = DatabaseConnection.getConnection();
			PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
	 
				preparedStatement.setString(1, "maria.novoemail@example.com");
				preparedStatement.setInt(2, 2);
				int rowsAffected = preparedStatement.executeUpdate();
				System.out.println("Linhas afetadas: " + rowsAffected);
				
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	```
	
- usando java para excluir dados 
	```
	import java.sql.Connection;
	import java.sql.PreparedStatement;
	import java.sql.SQLException;
	 
	public class DeleteExample {
		public static void main(String[] args) {
			String sql = "DELETE FROM Clientes WHERE ID = ?";
	 
			try (Connection connection = DatabaseConnection.getConnection();
			PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
	 
				preparedStatement.setInt(1, 2);
				int rowsAffected = preparedStatement.executeUpdate();
				System.out.println("Linhas afetadas: " + rowsAffected);

			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	```