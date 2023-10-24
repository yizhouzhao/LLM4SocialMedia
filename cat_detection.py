import requests
import base64

def convert_url_image(url):
	image_response = requests.get(url)
	conversion = base64.b64encode(image_response.content).decode('utf-8')
	return f"data:image/png;base64,{conversion}"

def Use_VQA(url,VQA):
	right_format= convert_url_image(url)
	response = requests.post(VQA, json={
		"data": [
			right_format,
			"Is there a cat in the picture?",
		]
	}).json()
	answer = response["data"][0]

	return answer

pic = "https://plus.unsplash.com/premium_photo-1669997804173-1cf7003d0664?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2371&q=80"

answer= Use_VQA(pic,"https://ofa-sys-ofa-vqa.hf.space/run/predict")

# 判断模型的回答是否包含"yes"，如果包含则表示图像中有猫，否则表示图像中没有猫
if "yes" in answer.lower():
    print("图像中有猫！")
else:
    print("图像中没有猫。")
#     print(f"Failed to retrieve data. Status code: {response.status_code}")
