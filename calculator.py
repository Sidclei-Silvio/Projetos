import tkinter as tk

def calcular():
    try:
        resultado = eval(entrada.get())
        label_resultado.config(text="Resultado: " + str(resultado))
    except Exception as e:
        label_resultado.config(text="Erro: " + str(e))

root = tk.Tk()
root.iconbitmap(r'C:\Projetos\calc.ico')
root.title("Calculadora")

entrada = tk.Entry(root, width=30)
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

linha = 1
coluna = 0
for botao in botoes:
    tk.Button(root, text=botao, width=5, command=lambda b=botao: entrada.insert(tk.END, b)).grid(row=linha, column=coluna)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

tk.Button(root, text="Calcular", width=20, command=calcular).grid(row=6, column=0, columnspan=4)
label_resultado = tk.Label(root, text="", width=30)
label_resultado.grid(row=7, column=0, columnspan=4)

