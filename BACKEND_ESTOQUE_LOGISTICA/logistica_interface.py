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

        autor = ft.TextField(
            label = "Nome do Livro"
        )

        sinopse = ft.TextField(
            label = "Adicione a Sinopse do Livro"
        )



        #-------------------------------------------------------------------------------------------------------------------------------
        #O código a seguir é faz parte do cadastro da capa de um livro, onde a foto da capa vai ser selecionada do arquivo do compuitador e inserido na pasta local do projeto
        file_picker = ft.FilePicker()
        page.overlay.append(file_picker)

        capa = ft.ElevatedButton(
        text="Selecionar imagem",  # texto exibido no botão
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=False,  # impede que vários arquivos sejam escolhidos
            allowed_extensions=["jpg", "jpeg", "png"]  # restringe a tipos de imagem
        ))
        #capa = ft.Image()
        #-------------------------------------------------------------------------------------------------------------------------------

        
        #A função enviar_livros vai pegar todos os valores digitados e coletar ele e enviar via json para o backend, Observação, toda função que realiza algo, como um "evento", necessita de um parametro para isso, nesse caso foi o "e", enviar_livros(e), mas pode ser qualquer um, futuramente devo atualizar e escrever evento em todas as funões de evento
        def enviar_livros(e):
            livros = {
                "nome": nome_livro.value
            }

            requests.post("http://127.0.0.1:5000/BACKEND_ESTOQUE_LOGISTICA", json=livros)

        btn_enviar = ft.ElevatedButton(
            text = "CADASTRAR LIVRO",
            on_click = enviar_livros
        )

        page.add(nome_livro, autor, sinopse, capa, btn_enviar)

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