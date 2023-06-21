import numpy as np
import cv2 
from matplotlib import pyplot as plt
import os

video= cv2.VideoCapture('traffic1.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('processedTraffic1.mp4',fourcc,30,(width,height))

matrix=[]

for i in range(100):
    ret, image= video.read()
    matrix.append(image)

matrix = np.array(matrix) 

video.set(cv2.CAP_PROP_POS_FRAMES, 0)

t = 1  
plt.imshow(matrix[t,:,:], cmap = "gray")
plt.axis('off')
plt.show()

b = np.median(matrix,axis=0) 
b = b.astype(np.uint8)
plt.imshow(b)
plt.axis('off')
plt.show()
dst = cv2.GaussianBlur(b,(15,15),0)

dst = cv2.pyrMeanShiftFiltering(dst, 28, 28)

plt.imshow(dst,cmap="gray")
plt.axis('off')
plt.show()

mask = np.zeros((dst.shape[0]+2, dst.shape[1]+2), np.uint8)

seed_point = (int((dst.shape[1])/2),int(dst.shape[0]/1.6))
seed_point2 = (int(150),int(735))
#seed_point3 = (int(1076),int(1000))
new_val = 255

cv2.floodFill(dst, mask, seed_point, new_val,(1,1,1),(1,1,1),4)
cv2.floodFill(dst, mask, seed_point2, new_val,(1,1,1),(1,1,1),4)
#cv2.floodFill(dst, mask, seed_point3, new_val,(1,1,1),(1,1,1),4)
rows, cols = mask.shape[:2]
mask[0, :] = 0
mask[rows-1, :] = 0
mask[:, 0] = 0
mask[:, cols-1] = 0
# showing the result
plt.imshow(dst,cmap="gray")
plt.axis('off')
plt.show()


mask= cv2.resize(mask, (b.shape[1], b.shape[0]), cv2.INTER_NEAREST)
print("this is the mask: ")
print(mask.dtype,mask.shape)
plt.imshow(mask,cmap="gray")
plt.axis('off')
plt.show()

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60,60))
mask_dilation = cv2.dilate(mask, kernel, iterations=1)

plt.imshow(mask_dilation,cmap="gray")
plt.axis('off')
plt.show()
#mask_dilation = cv2.resize(mask_dilation, (b.shape[1], b.shape[0]), cv2.INTER_NEAREST)

while True:
    success,frame =video.read()
    if not success:
        break
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask_dilation)
    out.write(masked_frame)

video.release()
out.release()

processed=cv2.VideoCapture('processedTraffic5.mp4')
output_path = "processed3"
if not os.path.exists(output_path):
    os.makedirs(output_path)
count = 1
while True:
    success, frame=processed.read()
    if not success:
        break
    top_row = 0
    for i in range(frame.shape[0]):
        if not np.all(frame[i] == 0):
            top_row = i
            break
    frame=frame[top_row:]

    height, width, _ = frame.shape

    remote_height= int(height/5)
    near_height=height -remote_height

    remote=frame[:remote_height+100,:]
    near=frame[remote_height:near_height,:]

    remote_width= remote.shape[1]

    for x in range (remote_width):
        col=remote[:,x]
        if np.any(col!=0):
            break

    copy=np.fliplr(remote)
    for y in range(copy.shape[1]):
        col=copy[:,y]
        if np.any(col!=0):
            break

    cropped_remote=remote[:, x:remote_width-y]

    remote_output=os.path.join(output_path, str(count) + 'r.jpg')
    near_output=os.path.join(output_path, str(count)+'.jpg')
    cv2.imwrite(near_output, near)
    cv2.imwrite(remote_output,cropped_remote)
    count +=1
processed.release()

