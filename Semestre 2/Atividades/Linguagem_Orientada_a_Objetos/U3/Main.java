    public class Main {
        public static void main(String[] args) {
        Soma soma = new Soma();
        Divisao divisao = new Divisao();

        System.out.println(soma.calcular(2.1, 3.4));

        try {
            System.out.println(divisao.calcular(2, 3));
            System.out.println(divisao.calcular(2, 0));
        } catch (DivisaoPorZeroException e) {
            System.out.println(e.getMessage());
        }
    }

}
