import imageEngine as imgEn

obj = imgEn.ImageEngine('assets/sample.jpg')

print(obj.getMetaData())
obj.saveImage("assets/gray.jpg", obj.to_grayScale())
obj.saveImage("assets/ext.jpg", obj.extractChannel('G'))
obj.saveImage("assets/flipV.jpg", obj.flip('vertical'))
obj.saveImage("assets/flipH.jpg", obj.flip('Horizontal'))
obj.saveImage("assets/rotclkw.jpg", obj.rotate90('clockwise'))
obj.saveImage("assets/rotaclkw.jpg", obj.rotate90('counterclockwise'))
obj.saveImage("assets/adj.jpg", obj.adjBriCT(70, 1.1))