import interactions
from interactions import slash_command, slash_option, SlashContext, OptionType
from utils import make_call, utils_get_news
import config

bot = interactions.Client(token=config.getConfig("bot_token"))

#This command will return the price of a stock by checking an external API, and returning the value
@slash_command(name="stonks", description="Check on the stonks")
@slash_option(
    name="stonk",
    description="Code of the stock you want",
    required=True,
    opt_type=OptionType.STRING
)
async def my_command_function(ctx: SlashContext, stonk):
    await ctx.defer()
    print(f"Requesting price for {stonk}")
    price = make_call(stonk)
    print(price)
    if price != "" and price != None:
        await ctx.send(f"The ask price for {stonk} is {price}")

#This command will return a series of news articles related to a certain stock ticker
@slash_command(name="news", description="Whats happening with the stonk")
@slash_option(
    name="stonk_news",
    description="Get the latest article",
    required=True,
    opt_type=OptionType.STRING
)
async def get_news(ctx: SlashContext, stonk_news):
    await ctx.defer()
    print(f"Requesting news for {stonk_news}")
    news = utils_get_news(stonk_news)
    print(news)
    if news != "" and news != None:
        await ctx.send(news)

bot.start()
print("Bot has been started")