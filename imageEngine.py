import numpy as np
import matplotlib.pyplot as plt

class ImageEngine : 
    def __init__(self, image_path : str):
        self.imgArray = plt.imread('assets/sample.jpg')
        if not isinstance(self.imgArray, np.ndarray):
            raise TypeError("Loaded image is not a valid NumPy array")
        
    def getMetaData(self) -> dict :
        pass
    def saveImage(self, output_path : str, arr : np.ndarray = None) : 
        pass
