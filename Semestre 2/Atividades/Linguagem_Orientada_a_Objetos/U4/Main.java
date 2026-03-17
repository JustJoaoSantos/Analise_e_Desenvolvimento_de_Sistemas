
public class Main {
    public static void main(String[] args) {
        Livro[] livros = new Livro[5];
        livros[0] = new Livro("Head First Java", "Kathy Sierra & Bert Bates", 2003);
        livros[1] = new Livro("I Have No Mouth, and I Must Scream", "Harlan Ellison", 1967);
        livros[2] = new Livro("Do Androids Dream of Electric Sheep?", "Philip K. Dick", 1968);
        livros[3] = new Livro("Annihilation ", "Jeff VanderMeer", 2014);
        livros[4] = new Livro("The Colour Out of Space", "H. P. Lovecraft", 1927);

        System.out.println("Livros Registrados");
        for (int i = 0; i < 5; i++) {
            livros[i].exibirInformacoes();
        }

        System.out.println("\nLivros que possuem a palavra 'Java'");
        System.out.println("=======================================");
        for (int i = 0; i < 5; i++) {
            if (livros[i].titulo.contains("Java")) {
                livros[i].exibirInformacoes();
            }
        }
        
    }
}
