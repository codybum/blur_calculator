# applying fast fourier transform to fin d the blur images , taken threshold to be 100 but it can vary
import argparse
import cv2

parser = argparse.ArgumentParser(description='Blurr Parser')

#general args
parser.add_argument('--frame_path', type=str, help='name of project')

args = parser.parse_args()

def variance_of_laplacian(frame_path):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    image = cv2.imread(frame_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    if args.frame_path is not None:
        value = variance_of_laplacian(args.frame_path)
    else:
        print('provide frame path --frame_path')

