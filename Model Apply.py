import cv2
from ultralytics import YOLO
#for writing video
from cv2 import VideoWriter, VideoWriter_fourcc

writer=VideoWriter("newVideos\\fifth.mp4",VideoWriter_fourcc(*'mp4v'), 20, (1280,720))

# Load the YOLOv8 model
model = YOLO('best.pt')

# Open the video file
video_path = "newVideos\\video5.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame,conf=0.6,iou=0.5)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        pic=cv2.putText(annotated_frame, f'boxes: {len(results[0].boxes)}', (50, 50) , cv2.FONT_HERSHEY_SIMPLEX ,  
                   1, (255, 0, 0) , 2, cv2.LINE_AA) 
        
        

        # Display the annotated frame
        #cv2.imshow("YOLOv8 Inference", pic)
        pic=cv2.resize(pic,(1280,720))
        writer.write(pic)
        # Break the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#release
writer.release()
cap.release()
cv2.destroyAllWindows()

