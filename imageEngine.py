import numpy as np
import matplotlib.pyplot as plt

class ImageEngine : 
    def __init__(self, image_path : str):
        self.imgArray = plt.imread(image_path)
        if not isinstance(self.imgArray, np.ndarray):
            raise TypeError("Loaded image is not a valid NumPy array")
        
    def getMetaData(self) -> dict :
        height , width = self.imgArray.shape[:2]
        metadata = {
            "shape" : self.imgArray.shape,
            "dtype" : self.imgArray.dtype,
            "min_val" : self.imgArray.min(),
            "max_val" : self.imgArray.max(),
            "total_pixel" : height * width
        }
        return metadata
    def saveImage(self, output_path : str, arr : np.ndarray = None) : 
        pass
o = ImageEngine('assets/sample.jpg')
print(o.getMetaData())