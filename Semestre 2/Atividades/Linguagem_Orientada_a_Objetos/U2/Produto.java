class Produto {
    //ATRIBUTOS
    String nome;
    double preco;
    static int quantidadeTotal = 0;

    //CONSTRUTORES
    public Produto() {
        quantidadeTotal++;
    }

    public Produto(String nome, double preco) {
        quantidadeTotal++;
        this.nome = nome;
        this.preco = preco;
    }

    //FUNCOES
    public void exibirDados() {
        System.out.println("Nome: " + nome);
        System.out.println("Preço: " + preco);
    }

    public static void exibirQuantidadeTotal() {
        System.out.println("Quantidade total de items cadastrado: " + quantidadeTotal);
    }
}
