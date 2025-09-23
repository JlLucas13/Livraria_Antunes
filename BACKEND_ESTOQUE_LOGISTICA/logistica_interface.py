import flet as ft

#Comando que cria a primeira página da interface
def main(page: ft.Page):
    #Comando que exclui os elementos da página anterior permitindo que os novos elementos apareção na págiona atual
    page.controls.clear()
    #titulo que aparece no topo superior da página
    page.title = "Antunes_Logistica"
    
    #Página onde será feito o cadastro dos livros
    def cadastro_livros(e):
        pass

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