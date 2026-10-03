# Unidade 1
***
## U1A1 - Fundamentos da Web com HTML5
***
### Linguagens me marcação x programação
- Marcação: Organiza e apresenta informações com ênfase na 
	estrutura e semântica
- Programação: Executa tarefas e implementa lógica

### HTML 
- HTML: HyperText Markup Language
- Criação: Tim Berners-Lee (CERN, início dos anos 90)
- Objetivo inicial: estruturar documentos acadêmicos e 
	compartilhar informções.
	
- Evolução do HTML:
	- Versões iniciais: formatações de texto e links;
	- W3C (World Wide Web Consortium): padronização e incorporação
		de recursos.
	- HTML5: multimídia e semântica avançada
	
### Estrutura Básica do Documento HTML 
- <html> : raiz do documento -contêiner principal
- <head> : meta-informações -título, estilos, metadados, scripts
- <title> : título da aba do navegador -importante para SEO
- <body> : conteúdo visível da página -textos, imagens, links

```HTML
<html>
	<head>
		<title>Minha Página</title>
	</head>
	<body>
	</body>
</html>
```

### Elementos Fundamentais Semântica 
- Semântica: significado dos elementos além da aprensetação
	visual.
- Elementos semânticos descrevem o conteúdo para navegadores 
	e desenvolvedores.
	
- Importância:
	+ Acessibilidade: leitores de tela interpretam o conteúdo
		logicamente (ex: <nav>, <article>, <aside>)
		
	+ Otimização para mecanismos de busca(SEO): buscadores
		entendem a relevância do conteúdo (ex: <article>, <h1>)
	
	+ Manutenção e organização do código: código mais legível e
		intuitivo

	+ Benefícios para o desenvolvimento: frameworks e
		ferramentas utilizam a estrutura semântica
		
### Elementos Fundamentais - Cabeçalho e Parágrafos
- Tags de Cabeçalho (<h1> a <h6>):
	+ Definem títulos e subtítulos
	+ Hierarquia de importância (<h1> é o título principal)
	+ Importante para estrutura semântica e mecanismos de busca
	
- Parágrafos (<p>):
	+ Agrupam blocos de texto com significado completo
	+ Navegadores adicionam espaçamento automático
	
### Elementos Fundamentais - Quebras de Linha e Listas
- Quebras de Linha (<br>):
	+ Insere uma quebra de linha forçada
	+ Usar com moderação (para conteúdo específico, 
		não para espaçamento)
		
- Listas: apresentam informações de forma organizada
	+ Listas Ordenadas (<ol>): sequência numerada 
		(<li> para cada item)
	+ Listas Não Ordenadas (<ul>): itens marcados com símbolos 
		(<li> para cada item)
	+ Listas de Definição (<dl>): termos e suas definições 
		(<dt> para o termo, <dd> para a descrição)
		
## U1A2 - 
***
### Definição de Tags
• Tags: "Etiquetas" do conteúdo
• Abertura (<tag>) e fechamento (</tag>)
• Exemplo: <p>Meu parágrafo</p>

### Tipos de Tags
• Tags parEs: início e fim
• Tags vazias: apenas início (<img src="">)
• Atributos: detalhes da tag
• Exemplo de atributo: <a href="">

### Hierarquia
• Organização do conteúdo
• Elementos pai e filho
• <html>, <head>, <body> (Estrutura Básica)

### Aninhamento
• Tags dentro de tags
• Ordem correta de fechamento
• Exemplo:
	+ <div><p></p></div> (Correto)
	+ <div><p></div></p> (Incorreto)
	
### Semântica
• Significado, não só aparência
• Ajuda navegadores e buscadores
• Exemplo Ruim: <div> para Tudo
• Exemplo Bom: <article>, <nav>, etc.

### Semântica e Hierarquia
• Combinando conceitos
• Títulos (<h1> - <h6>) = hierarquia semântica
• <article> + <section> + <p> = conteúdo organizado

### Elementos Fundamentais - Cabeçalho e Parágrafos
• Tags de Cabeçalho (<h1> a <h6>):
	+ Definem títulos e subtítulos
	+ Hierarquia de importância (<h1> é o título principal)
	+ Importante para estrutura semântica e mecanismos de busca
• Parágrafos (<p>):
	+ Agrupam blocos de texto com significado completo
	+ Navegadores adicionam espaçamento automático
	
## U1A3 - Semântica e Organização de Conteúdo 
***
### Formulários: interação com o usuário
• Coleta de dados (nome, e-mail, etc.)
• Tags HTML para formulários

### Elementos de formulário
• Campos de texto: <input type="text">
• Campos de e-mail: <input type="email">
• Áreas de texto: <textarea>
• Botões: <button type="submit">

Rótulos e atributos
• Rótulos: <label for="campo">
• Atributo name (identificação dos dados)
• Atributo id (associação com <label>)
• Atributo required (campo obrigatório)
• Atributo placeholder (texto de dica)

### Ação e método
• Atributo action (para onde enviar os dados)
• Atributo method="post"

### Exemplo de formulário de contato
````HTML
<form action="/enviar-contato" method="post">
	<label for="nome">Nome:</label><br>
	<input type="text" id="nome" name="nome" required placeholder="Seu nome"><br><br>
	
	<label for="email">E-mail:</label><br>
	<input type="email" id="email" name="email" required placeholder="Seu e-mail"><br><br>
	
	<label for="mensagem">Mensagem:</label><br>
	<textarea id="mensagem" name="mensagem" rows="4" cols="50"></textarea><br><br>
	
	<button type="submit">Enviar</button>
</form>
````

### Tabelas: organização de dados
• Organizar dados em linhas e colunas

### Estrutura da tabela
• <table> (tabela completa)
• <tr> (linha da tabela)
• <th> (célula de cabeçalho)
• <td> (célula de dados)
````HTML
<table>
	<tr>
		<th>Cabeçalho 1</th>
		<th>Cabeçalho 2</th>
	</tr>
	<tr>
		<td>Dado 1</td>
		<td>Dado 2</td>
	</tr>
</table>
````

### Mais elementos de tabela
• <caption> (título da tabela)
• <thead> (cabeçalho da tabela)
• <tbody> (corpo da tabela)
• <tfoot> (rodapé da tabela)

### Exemplo de tabela de preços
````HTML
<table>
	<caption>Tabela de Preços</caption>
	<thead>
		<tr>
			<th>Produto</th>
			<th>Preço</th>
		</tr>
	</thead>
	
	<tbody>
		<tr>
			<td>Produto A</td>
			<td>R$ 10,00</td>
		</tr>
		<tr>
			<td>Produto B</td>
			<td>R$ 20,00</td>
		</tr>
	</tbody>
	
	<tfoot>
		<tr>
			<td>Total</td>
			<td>R$ 30,00</td>
		</tr>
	</tfoot>
</table>
````

### Validação de dados
• Por que validar dados?
• Validação no lado do cliente (HTML5)
• Atributo required (obrigatório)
• Atributo type="email" (formato de e-mail)
• minlength e maxlength (tamanho do texto)
• min e max (valores numéricos)
• pattern (expressões regulares)

### Exemplo de validação
````HTML
<form action="/processar-formulario" method="post">
	<label for="nome">Nome:</label><br>
	<input type="text" id="nome" name="nome" required minlength="3" maxlength="50"><br><br>
	
	<label for="email">E-mail:</label><br>
	<input type="email" id="email" name="email" required><br><br>
	
	<label for="idade">Idade:</label><br>
	<input type="number" id="idade" name="idade" min="18" max="120"><br><br>
	
	<label for="senha">Senha:</label><br>
	<input type="password" id="senha" name="senha" required pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"><br><br>
	
	<button type="submit">Enviar</button>
</form>
````

## U1A4 - Exercícios Práticos com HTML 
***
### Mídias e Links
• Mídias e Links: elementos essenciais
• Mídias: tornar o conteúdo visual
• Links: navegação e interatividade

### Inserção de imagens
• Tag <img> (inserir imagem)
• Atributo src (caminho da imagem)
• Atributo alt (texto alternativo - acessibilidade)

### Inserção de vídeos
• Tag <video> (inserir vídeo)
• Tag <source> (múltiplos formatos)
• Atributo controls (controles de reprodução)

### URI e URL
• URI: identificador de recurso
• URL: localizador de recurso
• URL é um tipo de URI
• Variáveis em URLs
	+ Passar informações para o servidor
	+ ?nome=valor&nome2=valor2

### Criação de hiperlinks
• Tag <a> (criar link)
• Atributo href (destino do link)
• Tipos de links:
	+ Absolutos (para fora do site)
	+ Relativos (dentro do site)
	+ Âncora (na mesma página)
	+ E-mail (mailto:)

### Acessibilidade em imagens
• Atributo alt é essencial
• Descrições concisas e relevantes
• alt="" para imagens decorativas

### Acessibilidade em vídeos
• Legendas (tag <track>)
• Transcrições (texto completo)
• Controles de vídeo acessíveis (teclado)

# Unidade 2
***
## U2A1 - Introdução ao CSS e Seletores
***
### O Que é CSS?
• CSS = Cascading Style Sheets (Folhas de Estilo em Cascata).
• Linguagem para descrever a apresentação de documentos HTML.
• HTML: Estrutura e Conteúdo.
• CSS: Aparência e Layout.
• O termo "Cascata": como as regras são aplicadas e resolvidas.

### Por que o CSS é essencial?
• Separação: Conteúdo (HTML) vs. Apresentação (CSS).
• Consistência: Manutenção e atualização simplificadas.
• Flexibilidade: Criatividade ilimitada no design.
• Responsividade: Adaptação a diferentes dispositivos (desktops, 
	tablets, mobiles).
• Experiência do Usuário (UX): Sites mais agradáveis e intuitivos.
• SEO (Indireto): Código mais limpo e melhor engajamento.

### Selecionando elementos para estilizar
• Definição: como "mirar" elementos HTML.
• Seletor de Tipo (Elemento): p, h1, div.
• Seletor de ID: #meuId (único na página).
• Seletor de Classe: .minhaClasse (reutilizável para múltiplos 
	elementos).
• Seletores de atributo: a[target="_blank"].
• Seletores combinadores: div p, ul > li.

### Estilizando elementos selecionados
• Definição: atributos de estilo a serem aplicados.
• Sintaxe: propriedade: valor.

### Estrutura do Código CSS
• Sintaxe Básica: seletor { propriedade: valor; 
	propriedade2: valor2; }
• Seletor: o alvo do estilo.
• Bloco de Declaração: envolto por { }.
• Declaração: propriedade: valor; (finalizado com ;).
• Pontos Cruciais: Espaços em branco, ponto e vírgula.

### Comentários CSS
• Sintaxe: /* Seu comentário aqui */
• Propósito: documentação, colaboração, depuração.

## U2A2 - Design com o Box Model
***
### O Modelo de Caixa (Box Model): a fundação de tudo
• Conceito: cada elemento HTML é uma caixa retangular com camadas
	concêntricas.
• Camadas do Box Model:
	+ Conteúdo: área do texto/imagem (definido por width/height).
	+ Padding (Preenchimento): espaço transparente entre conteúdo e
		borda (empurra conteúdo para dentro).
	+ Border (Borda): linha que envolve padding e conteúdo.
	+ Margin (Margem): espaço transparente fora da borda (empurra
		outros elementos para longe).
• box-sizing:
	+ content-box (padrão): width/height aplicam-se ao conteúdo;
		padding e borda são adicionados.
	+ border-box: width/height incluem padding e borda (mais 
		previsível, recomendado).
• Importância: essencial para controlar tamanho e espaçamento dos
	elementos.

### Técnicas de posicionamento: mova seus elementos com precisão
• Definição: controla a localização de um elemento na tela.
• Tipos de posicionamento:
	+ Static: padrão; no fluxo normal do documento;
		top/bottom/left/right não funcionam.
	+ Relative: posicionado em relação à sua posição normal; mantém
		espaço original; top/bottom/left/right o deslocam.
	+ Absolute: removido do fluxo normal (não ocupa espaço);
		posicionado em relação ao ancestral posicionado mais próximo 
		(ou <body>).
	+ Fixed: removido do fluxo; posicionado em relação à viewport
		(janela do navegador); permanece visível ao rolar.
	+ Sticky: híbrido relative/fixed; comporta-se como relative até
		atingir um limite de rolagem (top/bottom/etc.), então "cola" 
		como fixed.
• Aplicações: menus fixos, pop-ups, tooltips, elementos 
	sobrepostos, barras de rolagem.

### Utilização de Flexbox: otimizando layouts modernos
• Conceito: Módulo unidimensional para distribuir e alinhar 
	itens dentro de um contêiner.
• Principais Elementos:
	+ Contêiner flex: elemento pai com display: flex ou display: inline-flex.
	+ Itens flex: filhos diretos do contêiner flex.
• Propriedades do Contêiner Flex:
	+ Flex-direction: define o eixo principal (linha ou coluna).
	+ Justify-content: alinha itens ao longo do eixo principal.
	+ Align-items: alinha itens ao longo do eixo transversal 
		(perpendicular).
	+ Flex-wrap: controla a quebra de linha dos itens.
	+ Gap: espaçamento entre os itens.
• Propriedades dos Itens Flex:
	+ Flex-grow: define capacidade de crescer.
	+ Flex-shrink: define capacidade de encolher.
	+ Order: define a ordem visual.
	+ Align-self: sobrescreve align-items para um item específico.
• Benefícios: centralização fácil, colunas de mesma altura, 
	distribuição de espaço, layouts responsivos com menos código.
• Aplicações: barras de navegação, galerias, cards, formulários.

### Conclusão: seu domínio do layout
• Compreensão do Box Model permite controle do espaço.
• Domínio das Técnicas de Posicionamento oferece precisão no
	posicionamento.
• Uso do Flexbox simplifica alinhamento, distribuição e 
	responsividade.
• Resultado: você, agora, pode resolver problemas de layout,
	criar designs complexos e ter total controle visual sobre suas
	páginas web.
	
## U2A3 - Layouts Flexíveis
***
### Estilizaçãa Avançada com CSS
• Problema: sites estáticos, monótonos e que não se adaptam a
	diferentes telas. Experiência do usuário fragmentada e 
	frustrante.
• Solução: CSS avançado para criar interfaces dinâmicas, 
	interativas e responsivas.
• Objetivo: transformar designs comuns em experiências digitais
	espetaculares e universalmente acessíveis

### Animações e transições
• O que são: técnicas para mudar propriedades CSS suavemente ao 
	longo do tempo, dando vida aos elementos.
• Por que usar: criam interfaces intuitivas, dinâmicas e 
	envolventes; fornecem feedback visual e guiam a atenção do 
	usuário.
• Transições CSS:
	+ Para efeitos simples, desencadeados por interações (hover, 
	focus, click).
	+ Propriedades principais: transition-property, 
		ransition-duration, transition-timing-function, 
		transition-delay.
	+ Exemplo: botão que muda de cor e escala suavemente ao passar 
		o mouse.

• Animações CSS (@keyframes):
	+ Para sequências de movimento complexas e independentes de
		interação.
	+ Definidas em "estágios" (0%, 50%, 100% ou from/to).
	+ Propriedades principais: animation-name, animation-duration,
		animation-iteration-count, animation-direction, animation-
		fill-mode.
	+ Exemplo: Spinner de carregamento que gira continuamente.

### Media Queries
• O que são: regras CSS que aplicam estilos diferentes com base 
	nas características do dispositivo (largura, altura, 
	orientação, resolução).
• Por que usar: essenciais para o design responsivo, permitindo 
	que seu site se adapte a qualquer tamanho de tela.
• Sintaxe: @media media-type and (media-feature) { /* estilos */ }

• Características comuns:
	+ min-width: se a tela for maior ou igual a X.
	+ max-width: se a tela for menor ou igual a X.
	+ orientation: portrait ou landscape.
	
• Exemplos de uso:
	+ Mudar layout de colunas para empilhamento em telas menores.
	+ Ocultar/mostrar elementos dependendo do tamanho da tela.
	+ Alterar tamanhos de fonte para melhor legibilidade

### Estratégias para design responsivo
• O que é: criar sites que se adaptam e oferecem uma ótima 
	experiência de usuário em qualquer dispositivo.
• Abordagem Mobile-First:
	+ Projetar e codificar primeiramente para dispositivos móveis 
		(telas pequenas).
	+ Usar min-width nas media queries para adicionar estilos e 
		complexidade para telas maiores.
	+ Vantagens: Performance otimizada, foco no conteúdo essencial, 
		melhor manutenibilidade.

• Grids Flexíveis:
	+ Usar unidades relativas (%, fr) com Flexbox ou CSS Grid.
	+ Permitem que os layouts se ajustem automaticamente ao tamanho 
		da tela.
	+ Exemplo: itens de grid que se reorganizam de uma coluna para 
		várias.

• Imagens Flexíveis:
	+ Garantir que imagens e mídias se ajustem ao contêiner.
	+ Sempre usar max-width: 100%; e height: auto; para manter 
		proporção e evitar transbordamento.
	
• Unidades Relativas:
	+ Preferir em, rem, vw, vh para tipografia e espaçamento.
	+ Adaptam-se dinamicamente ao tamanho da fonte raiz ou da 
		viewport, melhorando a acessibilidade e responsividade.
		
## U2A4 - Personalização e Temas
*** 
### Criação de Temas Customizados
• Definição: construção de uma identidade visual coesa (cores,
	fontes, espaçamento, sombras, etc.) para o projeto.
• Propósito: ir além do básico, criando uma "personalidade" única
	para o site/aplicação.
• Ferramenta essencial: variáveis CSS (--) para definir valores
	reutilizáveis e dinâmicos.
• Vantagens:
	+ Consistência: garante uniformidade visual em todo o projeto.
	+ Manutenção: facilita alterações globais (mude um valor,
		atualize tudo).
	+ Reusabilidade: aplique o mesmo tema em diferentes elementos 
		ou até em outros projetos.
	+ Flexibilidade: permite criar variações (ex: modo claro/escuro)
		facilmente.
• Impacto: acelera o desenvolvimento e melhora a experiência do
	usuário com um design profissional e impactante.

### Hierarquia de Estilos (A Cascata do CSS)
• Definição: como o navegador decide qual regra CSS aplicar 
	quando há múltiplos estilos para um elemento.
• Pilares Principais:
	+ Cascata: processo de combinação de estilos de diferentes 
		fontes (navegador, usuário, autor).
	+ Especificidade: peso de um seletor (ID > Classe > Elemento).
		Seletores mais específicos vencem.
	+ Ordem de origem: em caso de mesma especificidade, a última 
		regra declarada (ou importada) prevalece.

• Problemas resolvidos:
	+ Estilos que "não pegam" ou se comportam inesperadamente.
	+ Sobrescrita indesejada de regras.
• Boas práticas:
	+ Entender a dança entre os pilares para depurar eficientemente.
	+ Evitar o uso excessivo de !important (quebra a cascata e 
		dificulta a manutenção).
	+ Impacto: permite escrever CSS preditivo, ter controle total 
		sobre o design e depurar problemas de forma eficaz.

### Modularização de CSS
• Definição: Dividir a folha de estilos em arquivos menores e
	gerenciáveis, cada um para uma parte específica (componente, 
	seção, funcionalidade).
• Problema resolvido: o "monstro monolítico" CSS em projetos 
	grandes, que se torna difícil de navegar e manter.

• Benefícios:
	+ Organização: código mais legível e fácil de encontrar.
	+ Manutenção: simplifica atualizações e correções.
	+ Reutilização: facilita o uso de componentes em diferentes 
		partes do projeto ou em novos projetos.
	+ Colaboração: permite que vários desenvolvedores trabalhem em
		paralelo sem conflitos.
	+ Escalabilidade: prepara o código para o crescimento do projeto.
• Metodologias (Exemplos): BEM, SMACSS, ITCSS (oferecem 
	estruturas e convenções).
• Implementação: utilização de @import no CSS principal para 
	reunir os módulos.
• Impacto: Transforma o caos em um sistema organizado, eficiente 
	e colaborativo.
	
# Unidade 3
***
## U3A1 - Variáveis, Operadores e Decisão
***
### importação de javascript no html 
````HTML
<head>
<script src"index.js" defer type="module"></script>
</head>
````
- defer: espera o HTML ser carregado para carregar o js 
	torna desnecessario colocar o <script> no final do <body>
	
- type="module": prepara para a utilização de varios arquivos .js 

### Funções
- Função seta
````JS 
const saudacao = (nome) => `Olá, ${nome}!`;
````
- Função anônima
````JS
const saudacao = function(nome) {
	return `Olá, ${nome}!`;
};
````

## U3A2 - Funções e Eventos DOM 
***
### Manipulando dados do HTML pelo JS 
````JS 
const btn_calcular = document.getElementById('btn_calcular')

btn_calcular.addEventListener('click', function() {
	let peso = document.getElementById('peso')
	let altura = document.getElementById('altura')
	let valor_IMC = calcularIMC(peso.value, altura.value)
	
	document.getElementById('resultado_valor_imc').innerText = valor_IMC
}
````