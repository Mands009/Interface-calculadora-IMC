import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC e sua classificação
def calcular_imc():
    try:
        # Obtém os valores de peso e altura
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        # Verifica se a altura é maior que 0 para evitar divisão por 0
        if altura <= 0:
            messagebox.showerror("Erro", "A altura deve ser maior que zero.")
            return

        # Calcula o IMC
        imc = peso / (altura ** 2)

        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 35:
            classificacao = "Obesidade grau 1"
        elif 35 <= imc < 40:
            classificacao = "Obesidade grau 2"
        else:
            classificacao = "Obesidade grau 3 (mórbida)"

        # Exibe o resultado do IMC e a classificação
        label_resultado.config(text=f"IMC: {imc:.2f} - {classificacao}")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

# Função para reiniciar os campos
def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado.config(text="IMC: ")

# Função para sair da aplicação
def sair():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Cálculo do IMC - Índice de Massa Corporal")

# Definindo o tamanho da janela
janela.geometry("400x400")

# Título na parte superior com cor de fundo cinza claro
titulo = tk.Label(janela, text="Cálculo do IMC - Índice de Massa Corporal", font=("Arial", 16), pady=10)
titulo.pack(fill="both", padx=10, pady=10)
titulo.config(bg="#d3d3d3")  # Cor de fundo cinza claro

# Campo para o nome do paciente
label_nome = tk.Label(janela, text="Nome do paciente:")
label_nome.pack()
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)

# Campo para o endereço
label_endereco = tk.Label(janela, text="Endereço:")
label_endereco.pack()
entry_endereco = tk.Entry(janela, width=40)
entry_endereco.pack(pady=5)

# Campo para a altura
label_altura = tk.Label(janela, text="Altura (em metros):")
label_altura.pack()
entry_altura = tk.Entry(janela, width=40)
entry_altura.pack(pady=5)

# Campo para o peso
label_peso = tk.Label(janela, text="Peso (em kg):")
label_peso.pack()
entry_peso = tk.Entry(janela, width=40)
entry_peso.pack(pady=5)

# Botão para calcular o IMC com cor de fundo cinza claro
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack(pady=10)
botao_calcular.config(bg="#d3d3d3")  # Cor de fundo cinza claro

# Label para exibir o resultado do IMC
label_resultado = tk.Label(janela, text="IMC: ", font=("Arial", 14), fg="blue")
label_resultado.pack(pady=10)

# Frame para os botões "Reiniciar" e "Sair"
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

# Botão para reiniciar com cor de fundo cinza claro
botao_reiniciar = tk.Button(frame_botoes, text="Reiniciar", command=reiniciar)
botao_reiniciar.pack(side="left", padx=10)
botao_reiniciar.config(bg="#d3d3d3")  # Cor de fundo cinza claro

# Botão para sair com cor de fundo cinza claro
botao_sair = tk.Button(frame_botoes, text="Sair", command=sair)
botao_sair.pack(side="left", padx=10)
botao_sair.config(bg="#d3d3d3")  # Cor de fundo cinza claro

# Rodapé da página
rodape = tk.Label(janela, text="Calculadora IMC - 2024", font=("Arial", 8))
rodape.pack(side="bottom", pady=10)

# Inicia o loop da interface
janela.mainloop()