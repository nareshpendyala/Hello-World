'''
Neighboring pixels in images tend to have similar values, so conv layer will typically produce similar
values for neighboring pixels in output. Thus, much result from conv layer is redundant.
Pooling solve this problem, but they also reduce the size of the image. 

Perform pooling by traversing the input image in 2x2 blocks (because pool size is 2)
'''
import numpy as np

class MaxPool2:
    # A Max pooling layer using a pool size of 2

    def iterate_regions(self, image):
        '''
        Generate non-overlapping 2x2 image region to pool over
        - image is a 2d numpy array
        '''
        h, w, _ = image.shape
        new_h = h //2
        new_w = w //2

        for i in range(new_h):
            for j in range(new_w):
                im_region = image[(i * 2):(i * 2 + 2), (j * 2):(j * 2 + 2)]
                yield im_region, i, j

    def forward(self, input):
        '''
        Performs a forward pass of the maxpool layer using the given input.
        Returns a 3d numpy array with dimensions (h / 2, w / 2, num_filters).
        - input is a 3d numpy array with dimensions (h, w, num_filters)
        '''
        h, w, num_filters = input.shape
        output = np.zeros((h // 2, w // 2, num_filters))

        for im_region, i, j in self.iterate_regions(input):
            output[i, j] = np.amax(im_region, axis=(0,1))

        return output  
