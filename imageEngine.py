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
        if arr is None : 
            plt.imsave(output_path, self.imgArray)
        elif len(arr.shape) == 2: 
            plt.imsave(output_path, arr, cmap='gray')
        else : 
            plt.imsave(output_path, arr)
    def to_grayScale(self) -> np.ndarray : 
        red = self.imgArray[:, :, 0]
        green = self.imgArray[:, :, 1]
        blue = self.imgArray[:, :, 2]
        luminance = (0.299 * red) + (0.587 * green) + (0.114 * blue)
        return luminance.astype(np.uint8)
    def extractChannel(self, input : str) -> np.ndarray :
        tempArr = self.imgArray.copy()
        if not isinstance(input, str) : 
            raise TypeError("Only Strings Allowed")
        elif (input == "R") :
            tempArr[:, :, 1] = 0
            tempArr[:, :, 2] = 0
        elif (input == "B") : 
            tempArr[:, :, 0] = 0
            tempArr[:, :, 1] = 0
        elif (input == "G") : 
            tempArr[:, :, 0] = 0
            tempArr[:, :, 2] = 0
        else : 
            raise ValueError(f"Invalid channel '{input}'. Allowed values are 'R', 'G', 'B'.")
        return tempArr
    def flip(self, direction : str) -> np.ndarray : 
        temp = None
        if not isinstance(direction, str) : 
            raise TypeError("Only Strings Allowed !")
        elif(direction.capitalize() == 'Horizontal') :
            temp = self.imgArray[:, ::-1, :]
        elif(direction.capitalize() == 'Vertical') : 
            temp = self.imgArray[::-1, :, :]
        else : 
            raise ValueError(f"Invalid Input '{direction}. Allowed Values Are : 'Horizontal', 'Vertical'")
        return temp
    def rotate90(self, direction : str) -> np.ndarray :
        if not isinstance(direction, str) : 
            raise TypeError("Only Strings Allowed !")
        elif(direction.lower() == 'clockwise') :
            temp = self.imgArray.swapaxes(0, 1)
            return temp[::, ::-1]
        elif(direction.lower() == 'counterclockwise') :
            temp = self.imgArray.swapaxes(0, 1)
            return temp[::-1, ::]
        else : 
            raise ValueError(f"Invalid Input '{direction}. Allowed Values Are : 'Clockwise''Counterclockwise'")