from transformers import pipeline

# Your code here
# classifier = pipeline("sentiment-analysis")

# print(classifier("I've been waiting for a HuggingFace course my whole life."))

# cl = pipeline("zero-shot-classification")

# print (cl("I don't want cheese.", candidate_labels=["eductaion","restaurant","milk"],))

tran = pipeline("translation", model= "FlagAlpha/Llama2-Chinese-13b-Chat")

a = tran("this is a translation task")

print(a)