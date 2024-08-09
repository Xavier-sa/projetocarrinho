import tkinter as tk
from tkinter import messagebox, simpledialog

# testando com Tk para ver andamento
def exibir_cliente(cliente):
    return f'Cliente (nome: {cliente["nome"]})'

def exibir_produto(produto):
    return f'Produto (nome: {produto["nome"]}, quantidade: {produto["quantidade"]})'

def exibir_carrinho(cliente, carrinho):
    mensagem = f'CARRINHO DE {cliente["nome"]}\n'
    for produto in carrinho:
        mensagem += f'{exibir_produto(produto)}\n'
    return mensagem


def mensagem_cliente_encontrado():
    messagebox.showinfo("Info", "Cliente encontrado!")

def mensagem_cliente_nao_encontrado():
    messagebox.showerror("Erro", "Cliente não encontrado!")

def mensagem_excluido_cliente(tipo):
    if tipo == 'sucesso':
        messagebox.showinfo("Info", "Cliente removido com sucesso!")
    elif tipo == 'erro':
        messagebox.showerror("Erro", "Cliente não encontrado!")

def mensagem_encerrar_programa():
    messagebox.showinfo("Info", "Finalizando programa.")
    root.destroy()


def cadastrar_cliente():
    nome = simpledialog.askstring("Cadastrar Cliente", "Nome do cliente:")
    if nome:
        clientes.append({"nome": nome})
        mensagem_cliente_encontrado()
        atualizar_lista_clientes()

def listar_clientes():
    texto_clientes = '\n'.join([exibir_cliente(cliente) for cliente in clientes])
    texto_clientes_label.config(text=texto_clientes)

def editar_cliente():
    nome_atual = simpledialog.askstring("Editar Cliente", "Nome atual do cliente:")
    novo_nome = simpledialog.askstring("Editar Cliente", "Novo nome do cliente:")
    for cliente in clientes:
        if cliente["nome"] == nome_atual:
            cliente["nome"] = novo_nome
            mensagem_cliente_encontrado()
            atualizar_lista_clientes()
            return
    mensagem_cliente_nao_encontrado()

def excluir_cliente():
    nome = simpledialog.askstring("Excluir Cliente", "Nome do cliente a ser excluído:")
    global clientes
    clientes = [cliente for cliente in clientes if cliente["nome"] != nome]
    mensagem_excluido_cliente('sucesso' if any(cliente["nome"] == nome for cliente in clientes) else 'erro')
    atualizar_lista_clientes()

def adicionar_no_carrinho():
    nome_cliente = simpledialog.askstring("Adicionar ao Carrinho", "Nome do cliente:")
    nome_produto = simpledialog.askstring("Adicionar ao Carrinho", "Nome do produto:")
    for cliente in clientes:
        if cliente["nome"] == nome_cliente:
            for produto in produtos:
                if produto["nome"] == nome_produto:
                    carrinhos[cliente["nome"]].append(produto)
                    messagebox.showinfo("Info", "Produto adicionado ao carrinho!")
                    atualizar_carrinho(cliente)
                    return
    messagebox.showerror("Erro", "Cliente ou produto não encontrado!")

def remover_do_carrinho():
    nome_cliente = simpledialog.askstring("Remover do Carrinho", "Nome do cliente:")
    nome_produto = simpledialog.askstring("Remover do Carrinho", "Nome do produto:")
    for cliente in clientes:
        if cliente["nome"] == nome_cliente:
            carrinhos[cliente["nome"]] = [produto for produto in carrinhos[cliente["nome"]] if produto["nome"] != nome_produto]
            messagebox.showinfo("Info", "Produto removido do carrinho!")
            atualizar_carrinho(cliente)
            return
    messagebox.showerror("Erro", "Cliente não encontrado!")

def cadastrar_produto():
    nome = simpledialog.askstring("Cadastrar Produto", "Nome do produto:")
    quantidade = simpledialog.askinteger("Cadastrar Produto", "Quantidade do produto:")
    if nome and quantidade is not None:
        produtos.append({"nome": nome, "quantidade": quantidade})
        messagebox.showinfo("Info", "Produto cadastrado com sucesso!")
        atualizar_lista_produtos()

def listar_produtos():
    texto_produtos = '\n'.join([exibir_produto(produto) for produto in produtos])
    texto_produtos_label.config(text=texto_produtos)

def incluir_no_estoque():
    nome = simpledialog.askstring("Incluir no Estoque", "Nome do produto:")
    quantidade = simpledialog.askinteger("Incluir no Estoque", "Quantidade a ser adicionada:")
    for produto in produtos:
        if produto["nome"] == nome:
            produto["quantidade"] += quantidade
            messagebox.showinfo("Info", "Quantidade atualizada com sucesso!")
            atualizar_lista_produtos()
            return
    messagebox.showerror("Erro", "Produto não encontrado!")

def atualizar_lista_clientes():
    texto_clientes = '\n'.join([exibir_cliente(cliente) for cliente in clientes])
    texto_clientes_label.config(text=texto_clientes)

def atualizar_lista_produtos():
    texto_produtos = '\n'.join([exibir_produto(produto) for produto in produtos])
    texto_produtos_label.config(text=texto_produtos)

def atualizar_carrinho(cliente):
    texto_carrinho = exibir_carrinho(cliente, carrinhos.get(cliente["nome"], []))
    texto_carrinho_label.config(text=texto_carrinho)

def criar_botao(texto, comando, cor_fundo="#007bff", cor_texto="white"):
    return tk.Button(
        root, text=texto, command=comando, bg=cor_fundo, fg=cor_texto, 
        font=("Arial", 12, "bold"), height=2, width=20, 
        relief=tk.RAISED, bd=3, activebackground="#0056b3", activeforeground="white"
    )

def menu_principal():
    for widget in root.winfo_children():
        widget.destroy()

    criar_botao("Menu Cliente", menu_cliente).pack(pady=10)
    criar_botao("Menu Produto", menu_produto).pack(pady=10)
    criar_botao("Encerrar Programa", mensagem_encerrar_programa, "#dc3545").pack(pady=20)

def menu_cliente():
    for widget in root.winfo_children():
        widget.destroy()

    global texto_clientes_label, texto_carrinho_label
    texto_clientes_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
    texto_clientes_label.pack(pady=10)

    texto_carrinho_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
    texto_carrinho_label.pack(pady=10)

    criar_botao("Cadastrar Cliente", cadastrar_cliente).pack(pady=10)
    criar_botao("Listar Clientes", listar_clientes).pack(pady=10)
    criar_botao("Editar Cliente", editar_cliente).pack(pady=10)
    criar_botao("Excluir Cliente", excluir_cliente).pack(pady=10)
    criar_botao("Adicionar ao Carrinho", adicionar_no_carrinho).pack(pady=10)
    criar_botao("Remover do Carrinho", remover_do_carrinho).pack(pady=10)
    criar_botao("Voltar ao Menu Principal", menu_principal).pack(pady=10)

def menu_produto():
    for widget in root.winfo_children():
        widget.destroy()

    global texto_produtos_label
    texto_produtos_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
    texto_produtos_label.pack(pady=10)

    criar_botao("Cadastrar Produto", cadastrar_produto).pack(pady=10)
    criar_botao("Listar Produtos", listar_produtos).pack(pady=10)
    criar_botao("Incluir no Estoque", incluir_no_estoque).pack(pady=10)
    criar_botao("Voltar ao Menu Principal", menu_principal).pack(pady=10)

# Dados predefinidos para iniciar o programa
clientes = [{"nome": "Xavier"},{"nome": "freeza"},{"nome": "goku"},{"nome": "trunks"},{"nome": "vegeta"},]
produtos = [{"nome": "Computador", "quantidade": 10}]
carrinhos = {cliente["nome"]: [] for cliente in clientes}

# Configuração da caixa
root = tk.Tk()
root.title("Carrinho do Xavier")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

menu_principal()

root.mainloop()
