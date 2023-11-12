# LLM4SocialMedia

## Keep top

[Overleaf Paper](https://www.overleaf.com/3926568544nvdtkxktjptn#b091bd)

# TODO: 11/08/2023

## Set up a server for Llama2 server.

For Madison:

- (1)  Get familiar with AWS.

  EC2 -> us-west-2 -> Ubuntu -> g5.2xlarge -> 100GB
  
- (1) Get familiar with Ubuntu command line

  Install ubuntu on windows

For Yizhou:

- API call for the text-generation-webui [`Done`] (See SETUP_API.md)


For both: 

- See paper writing

```bash
ssh -i ov6.pem ubuntu@54.245.65.14
```

# TODO 10/23/23

## idea: prompt to decide whether to stay on this video or not

Strategies: 
  - (1) Questionnaire [Spatial], structured QA questions -> whether to stay on this video or not
  - (2) Hierarchical [Temporal], time-depending QA questions
  - (3)* [Causal] Reason you like or not?

Technologies （get the answers from the questions）:
  - [Option one] VQA models: ViLT(1.a),  OFA(1.b), MiniGPT-4(1.c = 2.a + ViT)
  - [Option two] Image/Video captioning e.g. BLIP-2 (2.d) [Search some Video captioning modules]) + QA, *llama2(2.a)*, ChatGPT(2.b), GPT-4*(2.c) [Please help me apply for an API for this.]

Task: 
  - Please help me construct a llama2 server?\

---------------------------------------------

# 11/07/2023: [Video: How To Install LLaMA 2 Locally](https://www.youtube.com/watch?v=k2FHUP0krqg)

## Install Environment

### 1. Download and create a [anaconda environment](https://www.anaconda.com/download)

### 2. Go to your anaconda navigator and launch the powershell

### [Optional] 3. Download [cuda and cudnn](https://blog.csdn.net/anmin8888/article/details/127910084) on website, Here is instruction.

## 4.Create a new environment using your anaconda powershell

```bash
conda create --name type_in_your_env_name python=3.10
conda activate type_in_your_env_name
```


### 5.Install the gpu version pytorch with cuda support(PLEASE REPLACE UDA toolkit version (e.g., cu111, cu110, cu102, etc.) based on your CUDA installation.)

        THE VEDIO USED ANOTHER COMMAND YOU COULD CHECK IF THERE IS A DIFFERENCE!!
        (pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117)
        This may be used (I THINK!)
        pip install torch==1.10.0+cu111 torchvision==0.11.1+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

### 6.Check if you are using the gpu version torch(ensure you are using the right environment when using this!!)

```python
import torch

print(torch.cuda.is_available()) 

print(torch.backends.cudnn.version())

print(torch.__version__)

print(torch.cuda.current_device())

print(torch.cuda.get_device_name(torch.cuda.current_device()))
```


### 7.if you get THIS then you are alset for the environment

```
        (try) PS C:\Users\madis\Desktop\llm> python .\TORCH.py
        True
        8801
        2.1.0+cu121
        0
        NVIDIA GeForce RTX 4090
```

  - Please help me apply for an API for GPT-4?

## Server Set-up

### 8. Start the setting up of server(please navigate to the corresponding directory using cd)
```bash
conda install -c anaconda git
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
pip install -r requirements.txt

# start the server
python server.py
```


## 9. You will get a message saying 

      (textgen2) C:\Users\madis\Desktop\llm\text-generation-webui>python server.py
      2023-10-30 13:22:47 INFO:Loading the extension "gallery"...
      Running on local URL:  http://127.0.0.1:7860
      
      To create a public link, set `share=True` in `launch()`.
      
## 10.copy the url, paste into browser,click the upper parameter model

## 11.get a model: test :https://huggingface.co/TheBloke/Llama-2-13B-Chat-fp16 

    paste TheBloke/Llama-2-13B-Chat-fp16 into download model square and press download
    will take a while
    go to left up and choose the model name in the dropdown menu of model, the click load
    will take a while
    go to upper parameter session and press apply flags

  YOU ARE DONE!

# TODO for Madison 10/05/23

## 1. Design your own desktop

4090 GPU + supported by Yizhou 
CPU[Compatible with Graphic Card] + Cooler + Motherboard [WIFI, Compatible with CPU + GPU] + RAM + M.2 SSD + CASE

 1.buy parts (✅）
 2.research mechanism（✅）
 3.build harware （✅）
 4.install software(✅) 


## 2. Learn to use Github and VScode

 1.establish ssh keygen
(git config EMAIL AND USER NAME)

## 3. Related work

 1.ucla library
 2.online resources
 3.watch koko
 4.learn transformer


## TODO: Start Research (Next week)

- 1. Research Title: Can LLMs Play Video Shorts
- 2. Research Questions: 
    - a. Can short video providers (P) find the Pattern of LLMs
    - b. Can we guide P (e.g. Tiktok, youtube, Snapchat, Ins) to some pattern by shaping LLMs with Prompts
    - c. What is the speed and efficiency?

- 3. Dataset:
    - Collect: Tiktok, youtube, Snapchat, Ins

- 4. Propose our framework: 
    `Faster`: improve the model response speed. 
    `Cloud computing/Acceleration` speed up inference.
    `Better`: pipelines

- 5. Eval metrics: 
    Evaluate your pipelines (GPT-4V)


## 4. Presentation
    - Paper: IJCAI (Jan 2024) / ACL (Dec 2023) 8 pages
    - Website: 


