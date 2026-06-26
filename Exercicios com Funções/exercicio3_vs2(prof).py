def desenha_linha(limite, preenchimento, largura):
    print(limite + (preenchimento * (largura - 2)) + limite)

def montar_menu(itens, largura):
    desenha_linha('+','_',largura)
    for item in itens:
        print(f'| {item:<16} |')
        desenha_linha('+', '-',largura)

itens = ['Usuários', 'Clientes', 'Fornecedores','Relatórios']
item_largura = 20
montar_menu(itens, item_largura)