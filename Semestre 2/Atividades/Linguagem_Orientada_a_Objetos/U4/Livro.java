public class Livro {
    String titulo;
    String autor;
    int ano_publicacao;

    public Livro(String titulo, String autor, int ano_publicacao) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano_publicacao = ano_publicacao;
    }

    public void exibirInformacoes() {
        System.out.println("Titulo: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Ano de Publicacao: " + ano_publicacao);
        System.out.println("------------------------");
    }
}