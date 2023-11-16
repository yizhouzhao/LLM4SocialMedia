# How to Set-up LLMs as a Web API Service

---

## 0. How to set up an EC2 instance

## 0.1 Start an EC2 instance

## 0.2 Configure the env for LLM on EC2

[Ignore] Install anaconda
```bash
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh
```

Activate the environment
```bash
conda env list
source activate pytorch
python
```

The python version should be 3.10, if not we have to install again


```python
#check pytorch
import torch
print(torch.__version__)
print(torch.cuda.is_available())
```

Install the `text-generation-webui`

```bash
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
pip install -r requirements.txt
```

## 1. Clone and Install the `Text-Generation-Webui` as described in `README.md`

```bash
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
pip install -r requirements.txt
python server.py --share --listen
```

## 2. Install the [OpenAI API](https://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API) extension described in the document

> **Note**: this modules doesn't need to be using OpenAI's API Key. It is just a OpenAI-API-Like module to deploy the LLM as a web-service.

```bash
pip install -r extensions/openai/requirements.txt
```

Start the server, and select the model as usual:

```bash
python server.py --extensions openai --listen
```

## 3. Now run the script in the example folder to chat

```bash
python examples/stream.py
```

## (Optional) Read more by opening the url
```
http://localhost:5000/docs
```
---

# How to Set-up Models with multi-modeality

## 1. Download [llava model](https://huggingface.co/TheBloke/llava-v1.5-13B-GPTQ)

with model tag:

`TheBloke/llava-v1.5-13B-GPTQ:gptq-4bit-32g-actorder_True`

## 2. Start the server using the following command

```bash
python server.py --model TheBloke_llava-v1.5-13B-GPTQ_gptq-4bit-32g-actorder_True --multimodal-pipeline llava-v1.5-13b --disable_exllama --loader autogptq --api --extensions multimodal
```

## 3. Now run the script in the example folder to interact with mutli-modality

```bash
cd examples
python multimodel.py
```