import os
import cv2
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='edit result image')
    parser.add_argument('--image', required=True,
                        metavar="original image name"
                      )

    args = parser.parse_args()

    INPUT_DIR = os.path.abspath(".\\public\\uploads")
    input_image = os.path.join(INPUT_DIR, 're'+args.image)
    print('WHAT is your NAME? : ' + input_image)
    n_input_image = cv2.imread(input_image, cv2.IMREAD_COLOR)
    cv2.imwrite(".\\StarGAN\\data\\custom\\test\\a\\input.jpg", n_input_image)
    print('save success!')