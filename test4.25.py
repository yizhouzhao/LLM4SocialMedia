
from exp_classes import Simple_Bot, Spatial_Bot, Plain_bot
from pl_classes import TikTok, Youtube, Snap, Instagram
from md_classes import Llava, Gemini, GPT4

Simple_Bot.run_experiment("Pet",TikTok(), GPT4(), 5, 5)
# Spatial_Bot.run_experiment("Pet", TikTok(), Gemini(),100)
# Plain_bot.run_experiment(TikTok(), Gemini(), 3, 4)