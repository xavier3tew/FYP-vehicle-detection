Below are the model codes used for the final year project
SSD Model : https://bham-my.sharepoint.com/personal/jwt057_student_bham_ac_uk/_layouts/15/guestaccess.aspx?guestaccesstoken=KPZh0FNHH606IN9KrrMFIjhEQPDs5eB6HGQ1HNhTh5Q%3D&docid=2_0dfab7d640e14464fbda763dac7d68772&rev=1&e=HfCIe7

YOLOv3 :https://bham-my.sharepoint.com/personal/jwt057_student_bham_ac_uk/_layouts/15/guestaccess.aspx?guestaccesstoken=G8jcBQMkIjmS9omTjAwYYzV2JwTXoGNznAdidbnOEfg%3D&docid=2_0f2c72778fb5c44509f9ed81748b0efac&rev=1&e=lBoL3q

YOLOv5 : https://bham-my.sharepoint.com/personal/jwt057_student_bham_ac_uk/_layouts/15/guestaccess.aspx?guestaccesstoken=DgE0uCgi6jpYN%2Fd0OcLIj6xzZDyeZk%2BhbyU1e7r7YVg%3D&docid=2_033a4c02bc5584d7b8f9985fc58fdcc19&rev=1&e=9eXa2Q

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

SHA256
SSD.zip: aed343c689cdf5cb4b14a85811343a1f95dee4077de92db1b8d89d3687b65e65
YOLOv3.zip:056ea285df9a98a0e9017c396a90a30ecc8a9546a17f916501c9750da9b81690
YOLOv5.zip:7d49adb20fdee3f1ecaf61d8936fb4b1309612aaa3de379e2d2ddfd2c128539b