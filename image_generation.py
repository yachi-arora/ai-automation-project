import pollinations.ai as ai
from PIL import Image

def generate_image(text_promp) -> None:
    model = ai.Image()
    image = model.generate(
        prompt=text_promp,
    )

    image.save("pollinations-Image.png")
    img = Image.open('/Users/yachiarora/Documents/Programming/Pyhton/pollinations-Image.png')
    img.show()



