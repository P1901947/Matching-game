import os

def loadImages():
    images = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(".gif"):
                images.append(filename)
    return images
