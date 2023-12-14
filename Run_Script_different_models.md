# How to Set-up different multi-modeality models

## 1. Download different models like [llava model](https://huggingface.co/TheBloke/llava-v1.5-13B-GPTQ) [Vicuna v0 13B](https://huggingface.co/anon8231489123/vicuna-13b-GPTQ-4bit-128g) [Vicuna v1 13B](https://huggingface.co/TheBloke/Vicuna-13B-1.1-GPTQ?text=Hey+my+name+is+Julien%21+How+are+you%3F)

with follwing model tags:

`TheBloke/llava-v1.5-13B-GPTQ:gptq-4bit-32g-actorder_True`
`anon8231489123/vicuna-13b-GPTQ-4bit-128g`
`TheBloke/Vicuna-13B-1.1-GPTQ`

## 2. Using different piplines for each models to test different multi-modelity models performance on TikTok[reference](https://github.com/oobabooga/text-generation-webui/blob/main/extensions/multimodal/README.md)
As of now, the following multimodal pipelines are supported:
|Pipeline|`--multimodal-pipeline`|Default LLM|LLM info(for the linked model)|Pipeline repository|
|-|-|-|-|-|
|[LLaVA 13B](https://github.com/haotian-liu/LLaVA)|`llava-13b`|[LLaVA 13B](https://huggingface.co/wojtab/llava-13b-v0-4bit-128g)|GPTQ 4-bit quant, old CUDA|built-in|
|[LLaVA 7B](https://github.com/haotian-liu/LLaVA)|`llava-7b`|[LLaVA 7B](https://huggingface.co/wojtab/llava-7b-v0-4bit-128g)|GPTQ 4-bit quant, old CUDA|built-in|
|[MiniGPT-4 7B](https://github.com/Vision-CAIR/MiniGPT-4)|`minigpt4-7b`|[Vicuna v0 7B](https://huggingface.co/TheBloke/vicuna-7B-GPTQ-4bit-128g)|GPTQ 4-bit quant, new format|[Wojtab/minigpt-4-pipeline](https://github.com/Wojtab/minigpt-4-pipeline)|
|[MiniGPT-4 13B](https://github.com/Vision-CAIR/MiniGPT-4)|`minigpt4-13b`|[Vicuna v0 13B](https://huggingface.co/anon8231489123/vicuna-13b-GPTQ-4bit-128g)|GPTQ 4-bit quant, old CUDA|[Wojtab/minigpt-4-pipeline](https://github.com/Wojtab/minigpt-4-pipeline)|
|[InstructBLIP 7B](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip)|`instructblip-7b`|[Vicuna v1.1 7B](https://huggingface.co/TheBloke/vicuna-7B-1.1-GPTQ-4bit-128g)|GPTQ 4-bit quant|[kjerk/instructblip-pipeline](https://github.com/kjerk/instructblip-pipeline)|
|[InstructBLIP 13B](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip)|`instructblip-13b`|[Vicuna v1.1 13B](https://huggingface.co/TheBloke/vicuna-13B-1.1-GPTQ-4bit-128g)|GPTQ 4-bit quant|[kjerk/instructblip-pipeline](https://github.com/kjerk/instructblip-pipeline)|

## 3. Start the server using the following command for different models

Remember to install the openAI API

```bash
python server.py --model TheBloke_llava-v1.5-13B-GPTQ_gptq-4bit-32g-actorder_True --multimodal-pipeline llava-v1.5-13b --disable_exllama --loader autogptq --api --extensions multimodal --listen
```

## 3. Now run the take_screen_shot script in the example folder to play TikTok with multimodality model

```bash
cd examples
python take_screen_shot.py
```


## 4. One example of script by looking [CAT](https://www.tiktok.com/@fasincat), 
(text2) C:\Users\madis\Desktop\LLM4Social_Yuning\LLM4SocialMedia\examples>python take_screen_shot.py
'在您的计算机屏幕上，有一张由一只可爱的猫编写的Nyan Cat (also known as the Grumpy Cat) GIF，他措手势，显示轻蔑服装。他并不是真正的狮子，而是一只模拟狮子！🐆🤣💨'
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about '在您的计算机屏幕上，有一张 由一只可爱的猫编写的Nyan Cat (also known as the Grumpy Cat) GIF，他措手势，显示轻蔑服装。他并不是真正的狮子，而是一只模 拟狮子！🐆🤣💨', If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
No
"\nYes, there is a cat in the image, and it is sitting on the woman's lap. The woman is petting the cat while touching her nails while sitting on her sofa."
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about "\nYes, there is a cat in the image, and it is sitting on the woman's lap. The woman is petting the cat while touching her nails while sitting on her sofa.", If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
Yes
sleeping... #######                                          18%
' Yes, there is a cat in the image. The cat is resting on a bed next to a green blanket.'
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about ' Yes, there is a cat in the image. The cat is resting on a bed next to a green blanket.', If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
Yes
sleeping... #######                                          18%
"\n\nThe image is of a young woman who is interacting with an orange and white cat. It appears the woman is either trying to tickle the cat or playing with it, as the cat is hanging by its tail and swatting a string behind her. The woman is holding the cat's tail, and there is a chair visible in the background. The scene is quite playful and lighthearted."
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about "\n\nThe image is of a young woman who is interacting with an orange and white cat. It appears the woman is either trying to tickle the cat or playing with it, as the cat is hanging by its tail and swatting a string behind her. The woman is holding the cat's tail, and there is a chair visible in the background. The scene is quite playful and lighthearted.", If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
Yes
sleeping... #######                                          18%
'\nThe image shows a snowy outdoor scene featuring a snow-covered patch of ground with a cat starting to walk across it. The cat seems to be peaking over the snow towards the camera. In the background, a car is parked or driving by, and a snowboard is laying on the snow with its tip pointed upward. The windows of a building can be seen in the distance, depending on the angle and perspective of the picture. The combination of these elements suggests that this scene takes place in a winter setting where various outdoor activities are possible.'
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about '\nThe image shows a snowy outdoor scene featuring a snow-covered patch of ground with a cat starting to walk across it. The cat seems to be peaking over the snow towards the camera. In the background, a car is parked or driving by, and a snowboard is laying on the snow with its tip pointed upward. The windows of a building can be seen in the distance, depending on the angle and perspective of the picture. The combination of these elements suggests that this scene takes place in a winter setting where various outdoor activities are possible.', If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
Yes
sleeping... #######                                          18%
"\nBased on the image, the cat appears to be sitting on a counter or table and looking at something outside of the capture. A person in the room is showing something to the cat or pointing at something, as indicated by their pointing finger. The cat's pretty brown whiskers and gray hair make for an attractive color combination.\n\nFurthermore, a pack of cigarettes and a cell phone are also visible in the image, which might suggest that this scene takes place in a living space where various activities are happening. Overall, the image portrays a person engaging with a cat, pointing towards something that seems to have captured the cat's attention."
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about "\nBased on the image, the cat appears to be sitting on a counter or table and looking at something outside of the capture. A person in the room is showing something to the cat or pointing at something, as indicated by their pointing finger. The cat's pretty brown whiskers and gray hair make for an attractive color combination.\n\nFurthermore, a pack of cigarettes and a cell phone are also visible in the image, which might suggest that this scene takes place in a living space where various activities are happening. Overall, the image portrays a person engaging with a cat, pointing towards something that seems to have captured the cat's attention.", If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
Yes
sleeping... #######                                          18%
"\nI can see that a small part of a room with a couch and a teddy bear on it is visible in the image. The couch is large, situated on the room's wall. The cats are laying close to each other, one of them is grooming the other. This suggests that everyone in the room with the two cats has a pet. One of the cats seems to be slightly older than the other, so they could be siblings or a parent and its offspring."
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about "\nI can see that a small part of a room with a couch and a teddy bear on it is visible in the image. The couch is large, situated on the room's wall. The cats are laying close to each other, one of them is grooming the other. This suggests that everyone in the room with the two cats has a pet. One of the cats seems to be slightly older than the other, so they could be siblings or a parent and its offspring.", If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
Yes
sleeping... #######                                          18%
'在这个照片中，我可以看到一只小型猫被引导着走着，并且它正在捕捉一个小型螺丝，用零件的形式在猫前。此事情发生在一个默暗的 房间内。猫本身是没有固定形的，而是像一条贵甲，突兀直出一条螺丝。'
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about '在这个照片中，我可以看到一 只小型猫被引导着走着，并且它正在捕捉一个小型螺丝，用零件的形式在猫前。此事情发生在一个默暗的房间内。猫本身是没有固定形的，而是像一条贵甲，突兀直出一条螺丝。', If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
No
'\nThe image captures a lively scene where three Chihuahuas are playing together in a house. Yes, there are three dogs in the scene as indicated by reference to the multiple "Chi."\n\nTwo of the dogs are actively playing with a red frisbee in the wood flooring living room, while a third dog is watching the play unfold. A couch can be seen in the background of the scene, completing the cozy yet playful atmosphere of the room. The presence of the frisbee adds a fun aspect to the image as the dogs enjoy their playtime together. The overall scene embodies a heartwarming moment between the pets and their environment.'
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about '\nThe image captures a lively scene where three Chihuahuas are playing together in a house. Yes, there are three dogs in the scene as indicated by reference to the multiple "Chi."\n\nTwo of the dogs are actively playing with a red frisbee in the wood flooring living room, while a third dog is watching the play unfold. A couch can be seen in the background of the scene, completing the cozy yet playful atmosphere of the room. The presence of the frisbee adds a fun aspect to the image as the dogs enjoy their playtime together. The overall scene embodies a heartwarming moment between the pets and their environment.', If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
No
' I see an image of a cat standing on a kitchen counter next to a sink. The cat appears to be looking somewhat concerned, as it situates itself in the middle of the scene. The surrounding environment includes a sink and a flattened metal oven further down the counter. This view also includes a large portion of a computer screen, indicating that the photo might have been captured from a digital image rather than in mere reality.'
I am a cat lover, and I am scrolling on tik_tok to find cat videos, and this video is about ' I see an image of a cat standing on a kitchen counter next to a sink. The cat appears to be looking somewhat concerned, as it situates itself in the middle of the scene. The surrounding environment includes a sink and a flattened metal oven further down the counter. This view also includes a large portion of a computer screen, indicating that the photo might have been captured from a digital image rather than in mere reality.', If video includes cat, I will stay at this video otherwise will not stay. Please help me decide whether to stay on the video or not. Please include yes or no in your answer, just respond in one word.
Yes
sleeping... #######                                          18%
[0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
Precision: 1.0
Recall: 0.7
F1 Score: 0.8235294117647058