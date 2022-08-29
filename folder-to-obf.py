import os
from PIL import Image
import json

path = "SANTE"
outPath = "SANTE.obf"

buttons = []
images = []
id = 0
images_id = 0
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(".png"):
            imagePath = os.path.join(root, name)
            print(imagePath)
            img = Image.open(imagePath)
            label = name.split(".")[0]
            print(id)
            print("image_id: " + str(images_id))
            print("label: " + label)


            # get width and height
            width = img.width
            height = img.height
            
            # display width and height
            print("The height of the image is: ", height)
            print("The width of the image is: ", width)


            id += 1
            images_id = id


            images.append({
                "id": str(id),
                "url": "https://dummyimage.com/"+str(width)+"x"+str(height)+"/000/"+name+"&text="+label,
                "width": width,
                "height": height,
                "content_type": "image/png"
            })
            buttons.append({
                "id": str(id),
                "image_id": str(id),
                "label": label,
            })

        else:
            print("not a png")

# Create obf file
obf = {
    "format": "open-board-0.1",
    "id": "1",
    "locale": "en",
    "url": "http://www.myaacapp.com/boards/123",
    "name": "Example Board",
    "description_html": "This is just a <b>simple</b> example board I put together.",
    "buttons": buttons,
    "grid": {
        "rows": 1,
        "columns": 2,
        "order": [
            ["1","2"]
        ]
    },
    "images": images
}

# Write obf file
with open(outPath, 'w') as outfile:
    json.dump(obf, outfile)
    print("done")
