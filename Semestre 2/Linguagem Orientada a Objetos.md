# U1A1 - Fundamentos de Orientacao a objetos
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
- Heranca
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

- Interface 

- Polimorfismo 