''' used to download images '''

# from simple_image_download import simple_image_download as simp

# response = simp.simple_image_download

# keywords = ["shoes"]

# for k in keywords:
#     response().download(k,200)

""" used to train """

# from ultralytics import YOLO

# model = YOLO('yolov8s.pt')

# output = model.train(data = "custom_data.yaml",epochs = 3 , imgsz = 640)

# print(output)
# print(output[0].numpy())

from ultralytics import YOLO
model=YOLO("best.pt")
model.predict(source="c.jpg",show=True,conf=0.5,save=True)



