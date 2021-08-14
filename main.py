import discord
from discord.ext import commands


TOKEN = 'ODc2MTEyNTE2MjE0ODE2NzY4.YRfVXQ.2T5R5MOYa0ygFLGjlV3gI5aCaCM'

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))


# pings bot to make sure it works
@client.command()
async def ping(ctx):
	await ctx.send('Hello Budios!')

# start command
@client.command()
async def start(ctx):
	embed = discord.Embed(
		title = 'Color Pallet',
		description = 'A Pallet of colors for the rainbow bot',
		colour = discord.Colour.green()
	)

	embed.set_footer(text="Pallete")
	embed.set_image(url='https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/815/cached.offlinehbpl.hbpl.co.uk/news/SUC/color1-20191204062437970.jpg')
	embed.set_thumbnail(url='https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/815/cached.offlinehbpl.hbpl.co.uk/news/SUC/color1-20191204062437970.jpg')
	embed.set_author(name='Nafiz Bot', icon_url='https://cdn.discordapp.com/avatars/873757065829576704/fb5685b0e332b1fe4ea2e92eefe329f2.png?size=256')
	embed.add_field(name='Choose Color Pallet', value='use ```-colors``` command for colors', inline=False)
	
	

	
	await ctx.send(embed=embed)


@client.command()
async def defualt(ctx):
	chose = discord.Embed(
		title = 'Chosen Pallet',
		description = 'The Color Pallet you have chosen is: ',
		colour = discord.Colour.blue()
	)

	chose.set_footer(text='defualt pallet')
	chose.set_image(url='https://media.tarkett-image.com/large/TH_24567080_24594080_24596080_24601080_24563080_24565080_24588080_001.jpg')
	chose.set_thumbnail(url='https://cdn.discordapp.com/avatars/873757065829576704/fb5685b0e332b1fe4ea2e92eefe329f2.png?size=256')
	chose.set_author(name='Phoenix Bot', icon_url='https://cdn.discordapp.com/avatars/873757065829576704/fb5685b0e332b1fe4ea2e92eefe329f2.png?size=256')
	chose.add_field(name='defualt', value='You have chosen the defualt color pallet.')


	await ctx.send(embed=chose)

@client.command()
async def matte(ctx):
	embed = discord.Embed(
		title = 'Chosen Pallet',
		description = 'The Color Pallet you have chosen is: ',
		colour = discord.Colour.blue()
	)

	embed.set_footer(text='matte pallet')
	embed.set_image(url='https://www.schemecolor.com/wallpaper?i=24692&desktop')
	embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/873757065829576704/fb5685b0e332b1fe4ea2e92eefe329f2.png?size=256')
	embed.set_author(name='Phoenix Bot', icon_url='https://cdn.discordapp.com/avatars/873757065829576704/fb5685b0e332b1fe4ea2e92eefe329f2.png?size=256')
	embed.add_field(name='matte', value='You have chosen the matte color pallet.')

	await ctx.send(embed=embed)

# create command ( creates color pallet)
@client.command()
async def create(ctx):
	await ctx.send('Still in development :weary:')


# colors command (sees the colors)
@client.command()
async def colors(ctx):
	embed = discord.Embed(
		title = 'Color Pallet',
		description = 'A Pallet of colors for the rainbow bot',
		colour = discord.Colour.red()
	)

	embed.set_footer(text="Pallete")
	embed.set_image(url='https://miuc.org/wp-content/uploads/2018/02/How-can-colours-help-you-in-your-everyday-life.jpg')
	embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/873757065829576704/fb5685b0e332b1fe4ea2e92eefe329f2.png?size=256')
	embed.set_author(name='Phoenix Bot', icon_url='https://cdn.discordapp.com/avatars/873757065829576704/fb5685b0e332b1fe4ea2e92eefe329f2.png?size=256')
	embed.add_field(name='Choose Color Pallet', value='defualt \n matte', inline=False)
	
	

	
	await ctx.send(embed=embed)



# delete color command
@client.command()
async def delete(ctx):
	await ctx.send("deleting created colors")


# finish (stops creating color process)
@client.command()
async def finish(ctx):
	await ctx.send("Ending Process")







client.run(TOKEN)