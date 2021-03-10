import discord
import random
from discord.ext import commands
from discord.utils import get
import asyncio
import time

bot = commands.Bot(command_prefix='>')


@bot.event
async def on_ready():
    bot.remove_command("help")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    while True:
        game = discord.Game("테스트")
        await bot.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(">도움")
        await bot.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("개발자 : Kaizer#7037")


@bot.command()
async def 도움(ctx):
    embed = discord.Embed(title="카이저봇 도움말", description="접두사 : > \n주인 : Kaizer#7037", colour=808000)
    # embed.set_thumbnail(url="")
    # embed.set_image(url="")
    embed.add_field(name="ping", value="`>ping`", inline=False)
    embed.add_field(name="안녕", value="`>안녕`", inline=False)
    embed.add_field(name="문의", value="`버그나 오류를 제보하세요!`", inline=False)
    embed.add_field(name="up", value="`대문자 변환`", inline=False)
    embed.add_field(name="slap", value="`>slap (member)`", inline=False)
    embed.add_field(name="random", value="`>random`", inline=False)
    embed.add_field(name="프사", value="`자신의 프사를 확인하세요!`", inline=False)
    embed.set_footer(text="하단 설명")
    # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다 embed.set_footer(text="하단 설명") # 하단에 들어가는 조그마한 설명을 잡아줍니다 await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다. await message.channel.send("할 말", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    await ctx.send(embed=embed)


'''@commands.has_permissions(administrator=True)
@bot.command()
async def 인증(ctx, member: discord.Member = None, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{}님, 당신은 이 명령을 실행하실 권한이 없습니다.".format(ctx.message.author))
    else:
        member = ctx.author
        role = discord.utils.get(ctx.guild.roles, name="멤버")
        await member.add_roles(role)
        # await ctx.channel.send(str(member)+"에게 역할이 적용되었습니다.")'''

#@commands.has_permissions(administrator=True)

@bot.command()
async def 인증(ctx, member: discord.Member=None):
    embed = discord.Embed(title = '인증 완료!', description = '5초 후에 역할이 지급됩니다!' colour=65ff00)
    embed.set_footer(text=f"{ctx.author.name} - 인증됨", icon_url=ctx.author.avatar_url) 
    msg = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(title = '인증 완료!', description = '4초 후에 역할이 지급됩니다!' colour=65ff00)
    embed.set_footer(text=f"{ctx.author.name} - 인증됨", icon_url=ctx.author.avatar_url)
    await msg.edit(embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(title = '인증 완료!', description = '3초 후에 역할이 지급됩니다!' colour=65ff00)
    embed.set_footer(text=f"{ctx.author.name} - 인증됨", icon_url=ctx.author.avatar_url)
    await msg.edit(embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(title = '인증 완료!', description = '2초 후에 역할이 지급됩니다!' colour=65ff00)
    embed.set_footer(text=f"{ctx.author.name} - 인증됨", icon_url=ctx.author.avatar_url)
    await msg.edit(embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(title = '인증 완료!', description = '1초 후에 역할이 지급됩니다!' colour=65ff00)
    embed.set_footer(text=f"{ctx.author.name} - 인증됨", icon_url=ctx.author.avatar_url)
    await msg.edit(embed=embed)
    await asyncio.sleep(1)
    member = ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="멤버"))
    await member.remove_roles(get(ctx.guild.roles, name="인증되지 않은 멤버"))
    #await ctx.channel.send(str(member)+"님 인증이 완료되었습니다!")

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4) * 1000)}ms')  # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다.

'''@_kick.error
async def _kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{}님, 당신은 이 명령을 실행하실 권한이 없습니다.".format(ctx.message.author))'''

@bot.command(name="추방", pass_context=True)
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+"을(를) 추방하였습니다.")

@bot.command(name="밴", pass_context=True)
async def _ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send(str(user_name) + "을(를) 영원히 매장시켰습니다.")

@bot.command(name="언밴", pass_context=True)
async def _unban(ctx, *, user_name):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention}을(를) 회생시켰습니다.")
            return

@bot.command(name="1234")
async def _1234(ctx):
    await ctx.send("5678")


@bot.command()
async def 안녕(ctx):
    await ctx.send(ctx.author.mention + ' ' + "님, 안녕하세요!")


@bot.command()
async def 반응(ctx):
    await ctx.message.add_reaction('✅')


@bot.command()
async def 문의(ctx, *, naeyong):
    owner = 723329000705097813
    ch = bot.get_user(owner)
    embed = discord.Embed(title='문의 도착', description='~~관리자 일해라~~', color=00000)
    embed.add_field(name='문의 내용', value=(naeyong))
    await ch.send(embed=embed)
    await ctx.send(f"문의를 성공적으로 보냈어요! 내용: {naeyong} \n||**장난 문의는 처벌 대상입니다^^**||")


def to_upper(argument):
    return argument.upper()


@bot.command()
async def up(ctx, *, content: to_upper):
    await ctx.send(content)


@bot.command()
@commands.has_guild_permissions(manage_messages=True)  # 권한설정
async def 타임뮤트(ctx, user: discord.Member, time: int, *, reason=None):  # time: int int = 숫자라 생각하셈
    guild = ctx.guild  # guild = 길드 객체로 돌리기
    muted = discord.utils.get(guild.roles, name="Muted 뮤트")  # 뮤트역할 정해주기

    await user.add_roles(muted)  # 뮤트 역할 추가 해주기
    embed = discord.Embed(title="사용자 뮤트", description=f"{user.mention}님이 {reason}이란 이유로 {time}초의 뮤트를 받았습니다")
    await ctx.send(embed=embed)

    await asyncio.sleep(time)  # 정수의 초를 기다리고

    await user.remove_roles(muted)  # 뮤트 역할 제거 해주기
    embed = discord.Embed(title="사용자 언뮤트", description=f"{user.mention}님이 뮤트에서 해방되었습니다")
    await ctx.send(embed=embed)


'''@bot.command()
async def slapp(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped because {}'.format(slapped, reason))'''


@bot.command()
async def slap(ctx, user: discord.Member, *, reason='no reason'):
    slapped = user.mention
    human = ctx.author.mention
    await ctx.send('{} just got slapped by {} because {}'.format(slapped, human, reason))


@bot.command()
async def 룰렛(ctx):
    channel = message.channel
    choice = message.content.split(" ")
    choicenumber = random.randint(1, len(choice) - 1)
    choiceresult = choice[choicenumber]
    await channel.send("**" + choiceresult + "을(를)고를래요!**")


@bot.command(name="random")
async def _random(ctx):
    embed = discord.Embed(title="Random Number", description=(random.randrange(1, 101)), color=(0xF85252))
    await ctx.send(embed=embed)


'''@bot.event
async def on_raw_reaction_add(payload):
    with open('reactrole.json') as react_file:

        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])

                await bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)


@bot.command()
async def reactrole(ctx, emoji: discord.Emoji, role: discord.Role, *, message):
    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name': role.name,
            'role_id': role.id,
            'emoji': emoji,
            'message_id': msg.id
        }

        data.append(new_react_role)

    with open('reactrole.json', 'w') as j:
        json.dump(data, j, indent=4)
'''


@bot.command()
async def 프사(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    embed = discord.Embed(title=f"{member}님의 프사", description="")  # member = mention당한 유저
    embed.set_image(url=member.avatar_url)  # 유저 프사따기
    await ctx.send(embed=embed)


# @bot.command()
# async def set_reaction(ctx, role: discord.Role, msg: discord.Message, emoji):


bot.run("NzgzNjI5MjY4MDAwODMzNTU3.X8dhoA.UbN0Cmk5Qu4kNbwv2x1ern2S5DM")
