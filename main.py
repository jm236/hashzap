

# Front (usuário -> site) e Back (oq rola por tras)
# Título do site
# Botao p iniciar o site
# Pop up (Bem vindo ao hashzap, digite seu nome, iniciar chat...)
# Chat
    # Usuario entrou no chat
    # Envie uma mensagem

import flet as ft

def main(pagina):
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    def enviar_mensagem(evento):
        # inserção da mensagem no chat
        mensagem = f"{nome_usuario.value}: " + campo_mensagem.value
        pagina.pubsub.send_all(mensagem) # envio da mensagem para o chat geral

        # limpeza do campo da mensagem
        campo_mensagem.value = ''

        # impressao da msg na tela
        pagina.update()



    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    chat = ft.Column()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    def entrar_chat(evento):
        pop_up.open = False # fechando o poup
        pagina.remove(botao_inicio) # tirando o botao de iniciar o chat
        pagina.pubsub.send_all(f'{nome_usuario.value} entrou no chat.')
        
        pagina.add(chat)
        linha_msg = ft.Row([campo_mensagem, botao_enviar])

        pagina.add(linha_msg) # imprimindo a linha da mensagem na tela
        pagina.update()



    nome_usuario =ft.TextField(label="Escreva seu nome") # campo de texto pro usuario adicionar o nome dele
    pop_up = ft.AlertDialog(open=False, # nao vai estar aberto inicialmente
                            modal=True, 
                            title=ft.Text("Bem vindo ao Hashzap!"),
                            content=nome_usuario, # conteudo do botao
                            actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]) # botao p entrar no chat

    def iniciar_chat(evento):
        pagina.dialog = pop_up
        pop_up.open = True
        pagina.update()

    texto = ft.Text("Hashzap") # Criação do texto
    pagina.add(texto) # Impressao do texto na pagina

    botao_inicio = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    pagina.add(botao_inicio)

#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)
