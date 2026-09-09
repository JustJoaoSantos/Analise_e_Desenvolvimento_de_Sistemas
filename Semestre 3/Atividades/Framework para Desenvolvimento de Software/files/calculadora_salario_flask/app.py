from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        salario_bruto = float(request.form['salario'])
        dependentes = int(request.form['dependentes'])

    except ValueError:
        return "Erro: Insira valores válidos."

    imposto_inss = salario_bruto * (8/100)
    imposto_ir = (salario_bruto - imposto_inss) * (15/100)
    desconto_dependentes = dependentes * 200
  
    salario_liquido = salario_bruto - imposto_inss

    if salario_bruto > 2500:
        salario_liquido -= imposto_ir
        imposto_ir = f"R${imposto_ir:.2f}"
    else:
        imposto_ir = "Não Considerado."

    if desconto_dependentes > 0:
        salario_liquido += desconto_dependentes
        desconto_dependentes = f"R${desconto_dependentes:.2f}"
    else:
        desconto_dependentes = "Não Considerado"

    resultado = f'''
        <div style="max-width: fit-content; margin-left: auto; margin-right: auto; margin-top: 200px">
            <p> Imposto INSS (8%): R${imposto_inss:.2f} </p> 
            <p> Imposto de Renda (15%): {imposto_ir} </p>
            <p> Adicionais de Dependentes: {desconto_dependentes} </p>
            <hr>
            <p> Salário líquido: R${salario_liquido:.2f} </p>
        </div>
    '''

    return resultado

if __name__ == '__main__':
    app.run(debug=True)

    