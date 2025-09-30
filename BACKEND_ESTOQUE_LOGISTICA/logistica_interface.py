import flet as ft
import requests

#Comando que cria a primeira página da interface
def main(page: ft.Page):
    #Comando que exclui os elementos da página anterior permitindo que os novos elementos apareção na págiona atual
    page.controls.clear()
    #titulo que aparece no topo superior da página
    page.title = "Antunes_Logistica"
    
    #Página onde será feito o cadastro dos livros
    def cadastro_livros(e):
        
        #Comando que exclui os elementos da página anterior permitindo que os novos elementos apareção na págiona atual
        page.controls.clear()
        
        #Sessão onde irá se criar uma tabela de preenchimento para cadastrar livros novos, os livros cadastrados aqui vão ser enviados para o banco de dados e exibido no site
        nome_livro = ft.TextField(
            label = "Nome do Livro"
        )

        '''#Rever o qrcode pois creio que ele pode ser inserido automaticamente'''
        
        qrcode = ft.TextField(
            label = "Ensira nome do QRcode"
        )
        

        preco_livro = ft.TextField(
            label = "Digite o preço do livro"
        )

        '''Fora esses itens ainda tem a capa, preciso ver como adicionar ela, já quie será através de um 'url' '''

        descricao_livro = ft.TextField(
            label = "Descrição do livro"
        )

        btn_enviar = ft.ElevatedButton(
            text = "CADASTRAR LIVRO",
            on_click = enviar_livros
        )

        def enviar_livros():
            livros = {
                "nome":nome_livro.value
            }
        

        #Sessão onde os dados coletados serão coletados e mandados via json para o sistema

        page.add(nome_livro, qrcode, preco_livro, descricao_livro, btn_enviar)

    #Botão que leva até a aba de cadastro de novos livros (Essa aba vai ficar dentro da parte de manipulação dos livros, onde se visualiza o estoque geral, entretanto vou deixar por aqui temporariamente apenas para facilitar a criação do sistema, posteriormente ele vai mudar para outro lugar)
    btn_cadastro_de_livros = ft.ElevatedButton(
        text="Cadastro de Livros",
        on_click=cadastro_livros)
    
    

    #Sessão onde fica armazenados os elementos da página
    page.add(btn_cadastro_de_livros)

    #Atualiza a pagina com os itens novos
    page.update()

#Comando que inicia a interface
ft.app(target=main, view=ft.AppView.FLET_APP)