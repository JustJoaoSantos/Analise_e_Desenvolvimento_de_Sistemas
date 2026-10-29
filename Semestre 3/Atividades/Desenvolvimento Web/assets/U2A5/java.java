import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculadoraTest {
    Calculadora calc = new Calculadora();

    @Test
    void somar() {
        assertEquals(5, calc.somar(2, 3));
        assertEquals(-5, calc.somar(-2, -3));
        assertEquals(0, calc.somar(-2, 2));
    }

    @Test
    void dividir() {
        assertEquals(2, calc.dividir(4, 2));
        assertEquals(1, calc.dividir(5, 5));
        assertThrows(ArithmeticException.class, ()-> calc.dividir(10, 0));
    }
}