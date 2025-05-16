import discord
from discord.ext import commands
# Botun Komut İsteklerini Ayarla
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot Başlatıldığında Mesaj Gönder
@bot.event
async def on_ready():
    print(f"Bot giriş yaptı: {bot.user}")
    await bot.change_presence(activity=discord.Game(name="İklim Habercisi"))

# Geri dönüşüm rehberi komutu
@bot.command()
async def iklim_video(ctx):
    rehber = (
        "*Geri Dönüşüm Rehberi*\n"
        "💡 *iklim değişikliği nedir*: https://www.youtube.com/watch?v=aGYjEyHBUTA .\n"
        "💡 *iklim değişikliğine neden olan faktörler*: https://www.youtube.com/watch?v=gUX2x3Y_BJA .\n"
        "💡 *iklim değişikliği nasıl önlenir*: https://www.youtube.com/watch?v=sY3KFvPW7z0 .\n"
    )
    await ctx.send(rehber)

@bot.command()
async def iklim_haber(ctx):
    mesaj1 = (
        "💡 *İklim değişikliği nedir*: \n"
        "İklim değişikliğini; ısıyı tutan sera gazlarının atmosferde artması ile ortalama sıcaklıkların yükselmesi ve sonucunda iklimin beklenmeyen değişimlere uğraması olarak açıklayabiliriz. "
        "Kuraklık, seller, kasırgalar gibi aşırı hava olaylarının sıklığında ve etkisinde artış görülüyor. Okyanus seviyeleri yükseliyor, buzullar eriyor ve bu durum tüm canlıları etkiliyor.\n"
    )

    mesaj2 = (
        "💡 *İklim değişikliğine neden olan faktörler*: \n"
        "- Fosil yakıt kullanımı (kömür, petrol, doğalgaz)\n"
        "- Ormansızlaşma ve doğa tahribatı\n"
        "- Tarımsal faaliyetlerden çıkan gazlar (metan, CO2)\n"
        "- Ozon tabakasının incelmesi, partikül artışı\n"
        "- Doğal nedenler: volkanik patlamalar, güneş lekeleri vs.\n"
    )

    mesaj3 = (
        "💡 *İklim değişikliği nasıl önlenir*: \n"
        "- Enerji tasarruflu cihazlar kullan\n"
        "- Gereksiz elektronik aletleri fişten çek\n"
        "- LED ampuller tercih et\n"
        "- Isı yalıtımına önem ver\n"
        "- Geri dönüşüm yap, karbon ayak izini azalt\n"
    )

    await ctx.send(mesaj1)
    await ctx.send(mesaj2)
    await ctx.send(mesaj3)


# Kullanıcının sorusuna yanıt verme komutu
@bot.command()
async def soru(ctx, *, soru_metni):
    yanit = (
        f"*Sorunuz:* {soru_metni}\n"
        "♻ Genel geri dönüşüm kurallarını kontrol edin. Belirli bir malzeme için detay isterseniz !iklim_haber komutu veya !iklim_video komutunu kullanabilirsiniz."
    )
    await ctx.send(yanit)

# Hataları yönetmek için bir hata mesajı
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("⚠ Geçersiz komut. Lütfen !iklim_haber veya !soru komutunu kullanın.")
    else:
        await ctx.send("❌ Bir hata oluştu!")

# Botun Tokenini Yazın
bot.run("")
