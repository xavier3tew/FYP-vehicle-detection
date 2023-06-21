Below are the model codes used for the final year project
https://drive.google.com/drive/folders/1wR5mRSLIYmqZzVmZO7UZhVNlJ4f_YDJa?usp=sharing

TO RUN extract.py (road surface segmentation):
1) capture video of traffic1.mp4
2) run it 
3) close all the pop out windows, those are to visualise the steps
4) wait for your segmented road  
* if you want to run other traffic scenes, the seed points have to be reconfigured in line 43 and 48
* all you need to do is run the first pop out window , select the road and memorise the (x,y) coordinates
* replace numeric values in line 43 with (x,y) cooridnates

TO RUN DETECTION CODE:

1) open notebook and upload corresponding zip files ,unzip files 
    SSD Model -> ssdmobilenet.ipynb
    YOLOv3 -> 
    YOLOv5 ->
2) replace all the filename location of '/content/drive/MyDrive' to unzipped filename location 

'/content/drive/MyDrive/models/research' ->'/unzippedfile/models/research'


2) Depending on which model you are running, the setup is different 

IF SSD:
1) start from 2nd cell and run everything till initilisation 
2) change PATH_TO_VIDEO to path of your video
3)  run pipeline testing 
* if tflite_dectect_video_sort fails, restart runtime and it should work again

IF YOLOv5:
1)start from 2nd cell and run everything till training code
2) run detection code with your own video 
3) outputted video would be in the latest /runs/exp

IF YOLOv3:
(MUST RUN AFTER EXTRACT)
1)open detection_custom.py
2)change folder directory to folder of the processed frames (/processed1/) from extract.py
3) run cell
*video functionality does not work 
