# Deep-Learning based clothing design program 

_Clothing design program improving StarGAN and Mask R-CNN_

<br><br>


__Attributes (temporary)__<br>
: check, dot, flower, stripe, leopard, red, blue 


<br><br>

## Dependencies
* [Python 3.5+](https://www.continuum.io/downloads)
* [PyTorch 0.4.0+](http://pytorch.org/)
* [TensorFlow 2.0+](https://www.tensorflow.org/)

<br><br>



## Downloading datasets
You can download the clothing dataset from [this link](https://drive.google.com/drive/folders/12zLjMI1XY0Tl_QK2Gwb8P8V-yLsNvoFU?usp=sharing).
<br>
__'data' folder should be located under 'StarGAN' folder.__ (-> StarGAN/data)


(The folder structure follows what is shown [here](https://github.com/yunjey/StarGAN/blob/master/jpg/RaFD.md).)


<br><br>

## Training networks 
-> 'StarGAN' 폴더 위치에서 수행!<br><br>

```
!python main.py --mode train --dataset RaFD --rafd_crop_size 256 --image_size 128 --c_dim 7 \
                --num_iters 50000 \
                --rafd_image_dir data/custom/train \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --model_save_step 10000
```
(_c_dim : number of attributes, num_iters : number of training iterations_)

<br><br>

## Test networks
-> 'StarGAN' 폴더 위치에서 수행!<br><br>
```
!python main.py --mode test --dataset RaFD --image_size 128 --c_dim 7 \
                --rafd_image_dir data/custom/test \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --test_iters 50000
```
