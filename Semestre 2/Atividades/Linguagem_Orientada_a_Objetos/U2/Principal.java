class Principal {
    public static void main(String[] args) {
        Produto p1 = new Produto();
        Produto p2 = new Produto("Chocolate", 13.90);
        Produto p3 = new Produto("Cafe", 15.90);

        p1.exibirDados();
        System.out.println("==================");

        p2.exibirDados();
        System.out.println("==================");

        p3.exibirDados();
        System.out.println("==================");

        Produto.exibirQuantidadeTotal();
    }
}