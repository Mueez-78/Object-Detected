from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.predict(source=0, show=True, classes=[0, 2, 3, 5, 67, 39, 56, 73, 64, 63, 40], 
            # save=True,
              #project = "completed",
              #name = "detected",
              #save_txt=True
              )
            #[0, 2, 3, 5, 67, 39, 56, 73, 64, 63, 40]       