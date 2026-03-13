class Divisao extends OperacaoMatematica {
    @Override
    public double calcular(double a, double b) throws DivisaoPorZeroException {
        if (a == 0 || b == 0) {
            throw new DivisaoPorZeroException("Erro: Parametro nao pode ser zero!");
        }
        
        return a / b;
        
    }
}