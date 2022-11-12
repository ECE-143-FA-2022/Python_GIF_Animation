import os
import imageio


def make_gif(folder_path,gif_path):
    """
    Imageio function that allows a user to make a gif out of a folder of images
    :param folder_path: path to a folder of images
    :type folder_path: str
    :param gif_path: output path for the final rendered gif
    :type gif_path: str
    :returns: None
    """

    # Initialize a list of images
    images = []
    # loop through all items in the input folder
    for image in sorted(os.listdir(folder_path)):
        # skipping any non-image items
        if image.endswith('.png') or image.endswith('.jpeg'):
            # add image to image list
            full_image_path = os.path.join(folder_path,image)
            images.append(imageio.imread(full_image_path))
    # render gif
    imageio.mimsave(gif_path,images,duration=0.35)

# Example Function Call
#path = "path/to/folder/with/images"                                                
#gif_file = 'filename.gif'
#make_gif(path,gif_file)

# code for the demo gif provided on the repository
#path = "/home/jacob/Fall2022/ECE143/Final_Project/Import_Export_demo/animation_test"
#gif_name = "demo.gif"
#make_gif(path,gif_name)
