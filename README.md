This is an object detection ML model for USB icons built using Yolov8. 

You can access its API via Roboflow: https://universe.roboflow.com/ronan-takizawa-c6iem/usbicon 

The USB icon, a symbol represented with an arrow branching to three subarrows with a circle, triangle, and square, is used in modern tech products to indicate if a product has a USB port or a USB connector. 
![usb-symbol2269](https://github.com/ronantakizawa/usbicondetection/assets/71115970/fbf6af28-aa97-49dc-b390-416fe3bd35b9)

Using this model, anyone can upload an image of a product and the model could detect if the product has USB connection by looking for the USB icon. This object detection model is useful for ecommerce product scanning to classify products as USB chargeable or not.  

The dataset includes 295 images.
Photos are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of vertical flip
* Random rotation of between -11 and +11 degrees
* Random Gaussian blur of between 0 and 1.5 pixels
