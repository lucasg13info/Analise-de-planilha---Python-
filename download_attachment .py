########################################################################
#                                                                      #
#                                                                      #
#                 Download de anexo de e-mail v1                       #
#                                                                      #
#                                                                      #
########################################################################

import os
from imbox import Imbox # pip install imbox
import traceback
import pandas as pd

# habilite aplicativos menos seguros em sua conta do Google
# https://myaccount.google.com/lesssecureapps


FROM_EMAIL = "lucccasestefano1@gmail.com"
FROM_PWD = "xxxx"
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

def download_anexo():
    download_folder = "/path/to" #Salva nesse diretório 

    #Cria a pasta se não existir
    if not os.path.isdir(download_folder):
         os.makedirs(download_folder, exist_ok=True)
        
    mail = Imbox(SMTP_SERVER, username=FROM_EMAIL, password=FROM_PWD, ssl=True, ssl_context=None, starttls=False)
    # messages = mail.messages() # Busca pelos e-mails da pasta Inbox
    messages = mail.messages(folder='Teste') #Busca pelos e-mails da pasta Testes
    #messages = mail.messages(subject='Planilha de nomes') #Busca pelo assunto específico

    for (uid, message) in messages:
        mail.mark_seen(uid) # marcar a mensagem como lida

        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')
                download_path = f"{download_folder}/{att_fn}"
                print(f'O arquivo baixado foi: {download_path}')
                print(f'Salvo nas pasta: {download_folder}')
                
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())
            except:
                print(traceback.print_exc())
    mail.logout()
    # def leitura_planilha():
    #     x = pd.read_excel(att_fn)
    #     print(x)


    # leitura_planilha()
download_anexo()

"""
Filtros de mensagem disponíveis: 

# Recebe todas as mensagens da caixa de entrada
messages = mail.messages()

# Mensagens não lidas
messages = mail.messages(unread=True)

# Mensagens sinalizadas
messages = mail.messages(flagged=True)

# Mensagens não sinalizadas
messages = mail.messages(unflagged=True)


# Mensagens enviadas de
messages = mail.messages(sent_from='sender@example.org')

# Mensagens enviadas PARA
messages = mail.messages(sent_to='receiver@example.org')

# Mensagens recebidas antes da data específica
messages = mail.messages(date__lt=datetime.date(2018, 7, 31))

# Mensagens recebidas após uma data específica
messages = mail.messages(date__gt=datetime.date(2018, 7, 30))

# Mensagens recebidas em uma data específica
messages = mail.messages(date__on=datetime.date(2018, 7, 30))

# Mensagens cujos assuntos contêm uma string
messages = mail.messages(subject='Christmas')

# Mensagens de uma pasta específica - esse está em uso!
messages = mail.messages(folder='Social')
"""