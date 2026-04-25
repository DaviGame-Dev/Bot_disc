# 🤖 Bot Diário para Discord (Daily GIF Bot)

Um bot simples e automatizado para Discord, construído em Python. Ele foi projetado para enviar uma mensagem diária contendo um texto personalizado e um GIF para um usuário específico através de Mensagens Diretas (DM). 

Ideal para automatizar lembretes, brincadeiras diárias ou mensagens de bom dia para amigos.

## ✨ Funcionalidades

* **Rotina Automatizada:** Envia uma mensagem programada a cada 24 horas usando a extensão `tasks` do discord.py.
* **Entrega Direta:** Focado no envio via DM (Direct Message) pelo ID do usuário, sem poluir os canais do servidor.
* **Comando de Interrupção (Opt-out):** Respeita a privacidade permitindo que o destinatário pare o envio das mensagens a qualquer momento digitando `!parar`.
* **Inicialização Segura:** O ciclo de mensagens só inicia após a confirmação de que o bot está 100% conectado aos servidores do Discord.

## 🛠️ Tecnologias Utilizadas

* [Python 3.8+](https://www.python.org/)
* [discord.py](https://discordpy.readthedocs.io/en/stable/) - Biblioteca oficial para integração com a API do Discord.

## ⚙️ Pré-requisitos

Antes de rodar o bot, você precisará de:
1. Uma conta no [Discord Developer Portal](https://discord.com/developers/applications).
2. Um "Application" criado e configurado como Bot.
3. O **Token** de acesso do seu Bot.
4. O **Message Content Intent** ativado na aba "Bot" do Developer Portal (necessário para o bot ler o comando `!parar`).
5. O ID numérico do usuário que receberá as mensagens (obtido ativando o Modo Desenvolvedor no Discord).

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/DaviGame-Dev/Bot_disc
   cd Bot_disc
   ```

2. **Instale as dependências:**
   É recomendado o uso de um ambiente virtual (venv), mas você pode instalar a biblioteca diretamente via pip:
   ```bash
   pip install discord.py
   ```

3. **Configure as variáveis:**
   Abra o arquivo `bot.py` em seu editor de código e substitua as variáveis no bloco de configurações com as suas informações reais:
   ```python
   # --- CONFIGURAÇÕES DO BOT ---
   TOKEN = 'COLE_SEU_TOKEN_AQUI'
   ID_DO_AMIGO = 123456789012345678  # Substitua pelo ID numérico real
   PREFIXO = '!'
   ```

4. **Inicie o bot:**
   No terminal, execute o script:
   ```bash
   python bot.py
   ```
   *Se tudo estiver correto, você verá a mensagem "Logado como [Nome do Seu Bot]!" no terminal.*

## 📝 Personalização

Para alterar a frase ou o GIF enviado, basta modificar estas duas linhas no arquivo `bot.py`:

```python
FRASE_DIARIA = "Sua frase personalizada aqui!"
LINK_GIF = "[https://link-do-seu-gif.com/imagem.gif](https://link-do-seu-gif.com/imagem.gif)"
```

## ⚠️ Avisos Legais e Privacidade

Este bot foi criado para fins de estudo e interação amigável. De acordo com a [Política de Desenvolvedores do Discord](https://discord.com/developers/docs/policies-and-agreements/developer-policy), o envio de DMs não solicitadas (Spam) pode resultar no banimento da sua conta e do seu bot. 

**Sempre obtenha o consentimento** do usuário antes de configurar o ID dele para receber as mensagens diárias e nunca remova o comando `!parar` do código.

Utilize serviços de hospedagem para manter o bot 24/7
