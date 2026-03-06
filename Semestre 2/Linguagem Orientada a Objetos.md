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