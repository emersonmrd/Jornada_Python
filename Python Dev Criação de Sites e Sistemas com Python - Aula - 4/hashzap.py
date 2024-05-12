# Título: Hashzap
#Botão de iniciar Chat
    # popup (janela na frente da tela)
    # Título: Bem vindo ao Hashzap
    # Campo de texto -> Esreve seu nome no chat
    # Botão: Entrar no chat
        # Sumir com o título Hashzap
        # Sumir com o botão  "Iniciar chat"
        # Fechar a janela (popup)
        # Carregar o chat
            # As mensagens que já foram enviadas (Chat)
            #  Campo: digite sua mensagem 
            # Botão: enviar

# pip install flet 

# importar o flet
import flet as ft

# Criar a função principal do seu aplicativo
def main(pagina):
    # criar todas as funcionalidades

    # cria o elemento
    titulo = ft.Text("Hashzap")

    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    chat = ft.Column()
    
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()


    botao_entrar = ft.ElevatedButton("Entrar no chat",on_click=entrar_chat)
    janela = ft.AlertDialog(
        title=titulo_janela, 
        content=campo_nome_usuario,
        actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

    # adiciona o elemtno na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# rodar o seu aplicativo
ft.app(main,view=ft.WEB_BROWSER)
