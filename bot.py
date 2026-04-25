import discord
from discord.ext import commands, tasks

# --- CONFIGURAÇÕES DO BOT ---
TOKEN = 'SEU_TOKEN_AQUI'
ID_DO_AMIGO = 123456789  # Substitua pelo ID real
PREFIXO = '!'

# Conteúdo da mensagem
FRASE_DIARIA = "Ei!"
LINK_GIF = "https://tenor.com/view/sao-sword-art-online-kirito-asuna-gif-12345"

# --- INICIALIZAÇÃO ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIXO, intents=intents)

# --- TAREFAS AUTOMÁTICAS ---
@tasks.loop(hours=24)
async def enviar_gif_diario():
    """Tarefa que roda a cada 24 horas enviando a DM."""
    print("Iniciando tentativa de envio...")
    try:
        usuario = await bot.fetch_user(ID_DO_AMIGO)
        mensagem_completa = f"{FRASE_DIARIA}\n{LINK_GIF}"
        await usuario.send(mensagem_completa)
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar: {e}")

# --- EVENTOS ---
@bot.event
async def on_ready():
    """Executado quando o bot liga com sucesso."""
    print(f'Logado como {bot.user.name}!')
    if not enviar_gif_diario.is_running():
        enviar_gif_diario.start()

# --- COMANDOS ---
@bot.command(name="parar")
async def parar(ctx):
    """Comando para encerrar o loop de mensagens."""
    enviar_gif_diario.stop()
    await ctx.send("Entendido! As mensagens diárias foram desativadas. 🛑")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    bot.run(TOKEN)
