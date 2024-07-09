import flet as ft

def main(page: ft.Page):
    #Configurações da Página
    page.title= "App de Vendas"
    page.auto_scroll = True
    page.scroll = "auto"
    page.window.bgcolor
    page.adaptive = True
    
    #Listas
    produtos_quantidade = []
    

    
    #Funções
    def tela2(e):
        ver_compra(e)
        page.remove(cadastro_vendas)
        page.add(vizualizar_compra) 
        page.update()
    
    def tela1(e):
       
        page.remove(vizualizar_compra)
        page.add(cadastro_vendas)
        page.update()
        tabela_produtos.rows.clear()
        valor_total_venda.controls.clear()

    #Adicionando novo campo para cadastrar mais de um produto
    def add_produto(e):
        quantidade = ft.TextField(label="Quantidade", keyboard_type= ft.KeyboardType.NUMBER)
        produto = ft.Dropdown(width=100, options=[
                    ft.dropdown.Option("Picolé Comum"),
                    ft.dropdown.Option("Picolé Recheado"),
                    ft.dropdown.Option("Potes"),
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

    def fechar_modal(e):
        page.close(alert)


    #Identificando produto e passando seu valor
    def ver_compra(e):
        
        i = 0
        valores = []
        while i < len(produtos_quantidade):
            
            produto = produtos_quantidade[i]['produto'].value
            quantidade = int(produtos_quantidade[i]['quantidade'].value)

            match produto:
                case 'Potes':
                    valor_unitario = 25.00
                case 'Picolé Comum':
                    valor_unitario = 1.00
                case 'Picolé Recheado':
                    valor_unitario = 2.50
                case 'Casquinha':
                    valor_unitario = 5.00
            
            mult_produto = quantidade * valor_unitario
            valores.append(mult_produto)
            tabela_produtos.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(f"{produto}", color="black")),
                        ft.DataCell(ft.Text(f"x{quantidade}", color="black")),
                        ft.DataCell(ft.Text(f"R${mult_produto}", color="black"))
                    ]
                )
            )
            
            i = i + 1
        soma_valores = sum(valores)
        valor_total_venda.controls.append(
            ft.Text(f"Valor Total: R${soma_valores}", color="red", weight=ft.FontWeight.BOLD)
            )
       
            
        

        
      
       
       
    tabela_produtos =ft.DataTable(
                    
            columns=[
                ft.DataColumn(ft.Text("Nomes", color="black")),
                ft.DataColumn(ft.Text("Quantidade", color="black")),
                ft.DataColumn(ft.Text("Valor", color="black"))
                ],
            
            rows=[]
        )   

    valor_total_venda = ft.Row(controls=[], alignment=ft.MainAxisAlignment.CENTER)
        
    cadastro_vendas = ft.Column([
        ft.Row([
            
            ft.Container(
                content=ft.ElevatedButton(icon=ft.icons.ADD, text="Adicionar", on_click=add_produto),
                alignment=ft.alignment.center,
                padding=10  ,
                margin=ft.Margin(left=0.5,top=50, bottom=10, right=0.5)
            ),
            ft.Container(
                ft.ElevatedButton(icon=ft.icons.NAVIGATE_NEXT ,text="Continuar" ,on_click=tela2),
                alignment=ft.alignment.bottom_left,
                padding=10,
                margin=ft.Margin(left=0.5,top=50, bottom=10, right=0.5)
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        col={'xs': 12, 'sm': 6, 'md': 4, 'lg': 3},
        
        
        ),
       ],
        
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       )
    
    alert = ft.AlertDialog(
        modal=True,
        title=ft.Text('Venda Registrada com sucesso!'),
        actions=[
            ft.ElevatedButton(icon=ft.icons.CLOSE, text="Ok", on_click= fechar_modal)
        ]
    )

    vizualizar_compra = ft.ResponsiveRow(
        [
            ft.Column(
                
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls= [

                            ft.Container(
                                content=ft.Row([tabela_produtos,valor_total_venda], alignment=ft.MainAxisAlignment.CENTER, wrap=True, spacing=10),
                                margin=ft.Margin(top=10, right=0.5, left=0.5, bottom=10),
                                bgcolor="white"
                            ),
                            
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.Container(
                                    ft.ElevatedButton(icon=ft.icons.EDIT, text="Editar",on_click=tela1),
                                    alignment=ft.alignment.bottom_center,
                                    padding=10,
                                    col={'xs': 12, 'sm': 6, 'md': 4, 'lg': 3}

                                ),
                                ft.Container(
                                    ft.ElevatedButton(icon=ft.icons.SAVE,text="Salvar", on_click= lambda e: page.open(alert)),
                                    alignment= ft.alignment.top_center,
                                    padding=10,
                                    col={'xs': 12, 'sm': 6, 'md': 4, 'lg': 3}
                                    
                                )

                            ],
                                
                            )
                            
                       
                    ],
                    scroll="auto",
                    
                    
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
