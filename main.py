import flet as ft

def main(page: ft.Page):
    #Configurações da Página
    page.title= "App de Vendas"
    page.auto_scroll = True
    page.scroll = "auto"
    page.window_bgcolor
    #Listas
    produtos_quantidade = []
    
    #Funções
    def tela2(e):
        ver(e)
        page.remove(cadastro_vendas)
        page.add(vizualizar_compra) 
        page.update()
    
    def tela1(e):
        page.remove(vizualizar_compra)
        page.add(cadastro_vendas)
        page.update()
    #Adicionando novo campo para cadastrar mais de um produto
    def add_produto(e):
        quantidade = ft.TextField(label="Quantidade")
        produto = ft.Dropdown(width=100, options=[
                    ft.dropdown.Option("Picole"),
                    ft.dropdown.Option("Pote"),
                    ft.dropdown.Option("Casquinha"),
                ],
                label="Produtos"
                )
        add_Field = ft.ResponsiveRow([
            ft.Container(quantidade, col={'xs': 12, 'sm': 6, 'md': 4, 'lg': 3}),
            ft.Container(produto, col={'xs': 12, 'sm': 6, 'md': 4, 'lg': 3}),
        ])
        produtos_quantidade.append({"quantidade": quantidade, "produto": produto})
        cadastro_vendas.controls.append(add_Field)
        page.update()

    #Identificando produto e passando seu valor
    def ver(e):
        produtos = []
        for i in produtos_quantidade:
            quantidade = i['quantidade'].value
            produto = i['produto'].value
            produtos.append(produto)
            match produto:
                case "Pote":
                    valor_unitario = 25
                case "Picole":
                    valor_unitario = 2
                case "Casquinha":
                    valor_unitario = 5
            preco = int(quantidade) * valor_unitario

            coluna_produto.controls.append(
                ft.Row(controls=[ft.Text(f"{produto}", color="black")], alignment=ft.MainAxisAlignment.CENTER)                                        
            )
            coluna_quantidade.controls.append(
                ft.Row(controls=[ft.Text(f"x{quantidade}", color="black")], alignment=ft.MainAxisAlignment.CENTER)
            )
            coluna_preco.controls.append(
                ft.Row(controls=[ft.Text(f"R${preco}", color="black")], alignment=ft.MainAxisAlignment.CENTER)
            )

            

    #TELAS

    #Tela do formulario de cadastrar venda
    cadastro_vendas = ft.Column([
                
                ft.Container(
                    ft.IconButton(icon=ft.icons.NAVIGATE_NEXT , on_click=tela2),
                    alignment=ft.alignment.center,
                    padding=10  
                ),
                ft.Container(
                    content=ft.IconButton(icon=ft.icons.ADD, on_click=add_produto),
                    alignment=ft.alignment.bottom_left,
                    padding=10  
                ),
                
       ],
        
       )
    
    coluna_quantidade = ft.Column(
        controls=[ft.Row(controls=[ft.Text("Quantidade", color="black", weight=ft.FontWeight.BOLD, )])],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    coluna_produto = ft.Column(
        controls=[ft.Row(controls=[ft.Text("Nomes", color="black", weight=ft.FontWeight.BOLD)])],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    coluna_preco = ft.Column(
        controls=[ft.Row(controls=[ft.Text("Preço do Produto", color="black", weight=ft.FontWeight.BOLD)])],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    


    coluna_de_checkin = ft.Column(
        controls=[ft.Column(
            controls=[
                ft.Row(controls= [ft.Text("Produtos:", color="black", weight=ft.FontWeight.W_900, size=25)]),
                ft.Row(controls=[coluna_produto, coluna_quantidade, coluna_preco], alignment=ft.MainAxisAlignment.CENTER) 
                ])],
        width=1500,
        height=500,
        wrap=True,
        spacing=10,

        )
        



    vizualizar_compra = ft.ResponsiveRow(
        [
            ft.Column(
                controls= [
                            ft.Container(
                                ft.ElevatedButton(icon=ft.icons.SAVE,text="Salvar", on_click=''),
                                alignment=ft.alignment.bottom_center,
                                padding=10,
                                col={'xs': 12, 'sm': 6, 'md': 4, 'lg': 3}

                            ),
                            ft.Container(
                                ft.IconButton(icon=ft.icons.CANCEL, on_click=tela1),
                                alignment= ft.alignment.top_center,
                                padding=10,
                                col={'xs': 12, 'sm': 6, 'md': 4, 'lg': 3}
                            ),
                            ft.Container(                                
                                coluna_de_checkin,                                
                                bgcolor="white"
                            )
                            
                        ],
                        scroll="auto"
                    
                ),
           
    ])

    screen_login = ft.ResponsiveRow([
        ft.Column(
            alignment= ft.alignment.center,
            controls=[
                ft.Text("Login", size=30),
                ft.Dropdown(options=[
                    ft.dropdown.Option("Matheus"),
                    ft.dropdown.Option("Daimes"),
                    ft.dropdown.Option("Valdir")
                ]),
                ft.TextField(label="Senha", password=True, can_reveal_password=True)
            ],
            scroll="auto"
        )
        
    ])
    

    page.add(cadastro_vendas )
     
        

ft.app(target=main, assets_dir="assets")
