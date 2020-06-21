import sqlite3,discord,random,os
from discord.ext import commands


class Moderator(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
	@commands.command(aliases=["Hammer","hammer","poop","Poop"])
	@commands.has_any_role("Mod","Reyter")
	async def ban(self,ctx,member:discord.Member,	reason=None):
		if reason == None:
			reason = "Undefined"
		await member.ban(reason=reason,delete_message_days=0)
		card = discord.Embed(
		colour=ctx.author.color,
		title=f"Haha now go meow!",
		description=f"{ctx.author.name} has banned {member.name}, Reason: {reason}"
	)
		await ctx.send(embed=card)

	@commands.command(aliases=["Stroke","bite","Bite","stroke"])
	@commands.has_any_role("Mod","Reyter")
	async def strike(self,ctx,member:discord.Member,	strike=1):
   	 db = sqlite3.connect("data.db")
   	 cursor = db.cursor()
   	 cursor.execute("SELECT * FROM info WHERE id = ?",(member.id,))
   	 db.commit()
   	 user = cursor.fetchone()
   	 print(user)
   	 if user[0] == ctx.author.id:
   	 	await ctx.send("You cant strike yourself lol")
   	 	db.close()
   	 else:
   	 	userStrike = user[2]+strike
   	 	cursor.execute("""
    			UPDATE info
    				SET strike = ?
    				WHERE name = ?
    		""",(userStrike,member.name,))
    		db.commit()
    		db.close()
    		card = discord.Embed(
    		colour=discord.Colour.from_rgb(255,20,20),
    		title=f"{member.name} has been given {strike} strikes by {ctx.author.name}"
    	)
    		await ctx.send(embed=card)
    
	@commands.command()
	@commands.has_any_role("Mod","Reyter")
	async def clear(self,ctx,msg:int):
		channel = ctx.channel
		deleted = await channel.purge(limit=msg)
		card = discord.Embed(
		colour=discord.Colour.from_rgb(20,255,20),
		title=f"Deleted {len(deleted)} messages"
		)
		await ctx.send(embed=card,delete_after=4)
	
	@commands.command()
	@commands.has_role("Reyter")
	async def dc(self,ctx):
		card = discord.Embed(
		colour=discord.Colour.from_rgb(20,255,20),
		title="Successfully disconnected meow!"
		)
		await ctx.send(embed=card)
		await bot.logout()

def setup(bot):
	bot.add_cog(Moderator(bot))