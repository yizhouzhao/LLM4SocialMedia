import base64
import requests

def converter(image_path):
    # Open and read the image file in binary mode
    with open(image_path, "rb") as image_file:
        # Convert the binary data to base64
        base64_data = base64.b64encode(image_file.read()).decode('utf-8')
        # Format as data:image/png;base64,{base64_data}
        formatted_data = f"data:image/png;base64,{base64_data}"
    return formatted_data

def Use_VQA(VQA, png):
    right_format = converter(png)
    response = requests.post(VQA, json={
        "data": [
            right_format,
            "Is there a cat in the picture?",
        ]
    }).json()
    answer = response["data"][0]

    return answer

# Example usage
VQA_url = "https://ofa-sys-ofa-vqa.hf.space/run/predict"
image_path = "specified_area_screenshot.png"
answer = Use_VQA(VQA_url, image_path)

if "yes" in answer.lower():
    print("图像中有猫！")
else:
    print("图像中没有猫。")
#     print(f"Failed to retrieve data. Status code: {response.status_code}")

