
from exp_classes import Bot, Spatial_Bot
from pl_classes import TikTok, Youtube, Snap, Instagram
from md_classes import Llava, Gemini, GPT4


Bot.run_experiment("Pet",TikTok(), Gemini(), 100)
# Spatial_Bot.run_experiment("Pet", TikTok(), Gemini(),3)