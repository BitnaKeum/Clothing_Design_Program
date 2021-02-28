# Deep-Learning based Clothing Design Program 

_Clothing design program improving StarGAN and Mask R-CNN_

<br><br>


__Attributes (temporary)__<br>
: blue, check, dot, red, stripe


<br><br>

## Dependencies
* [Python 3.5+](https://www.continuum.io/downloads)
* [PyTorch 0.4.0+](http://pytorch.org/)
* [TensorFlow 2.0+](https://www.tensorflow.org/)

<br><br>



## Downloading datasets
You can download the clothing dataset [here](https://drive.google.com/drive/folders/12zLjMI1XY0Tl_QK2Gwb8P8V-yLsNvoFU?usp=sharing)!
<br>

The folder should be located like `StarGAN/data`.


(_The folder structure follows what is shown [here](https://github.com/yunjey/StarGAN/blob/master/jpg/RaFD.md)._)


<br><br>


## Training networks 
('StarGAN' 폴더 위치에서 수행하기!)<br><br>
(_c_dim : number of attributes, num_iters : number of training iterations_)

```
# Train
!python main.py --mode train --dataset RaFD --rafd_crop_size 256 --image_size 128 --c_dim 5 \
                --num_iters 140000 \
                --rafd_image_dir data/custom/train \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --model_save_step 10000
```
```
# Test
!python main.py --mode test --dataset RaFD --image_size 128 --c_dim 5 \
                --rafd_image_dir data/custom/test \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --test_iters 140000
```

The result images are saved in `StarGAN/stargan_custom/results`.

<br><br>

## ~~Using pre-trained networks~~
~~You can download pre-trained model [here](https://drive.google.com/drive/folders/1YA8Ju_UAwqj8HBe-G6bPw0F3nXCaUl_J?usp=sharing).~~<br>

The folder should be located like `StarGAN/stargan_custom/models`.
<br>

('StarGAN' 폴더 위치에서 수행하기!)
```
# Test
!python main.py --mode test --dataset RaFD --image_size 128 --c_dim 5 \
                --rafd_image_dir data/custom/test \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --test_iters 140000
```

The result images are saved in `StarGAN/stargan_custom/results`.

<br><br>


## Result examples
__Sequence__ : original - blue - check - dot - red - stripe<br>
(140000 iterations training, No Skip-connection)
<br><br>

![image](https://user-images.githubusercontent.com/37769713/109409571-3a6bb980-79d7-11eb-84fe-9e761272e6cc.png)

![image](https://user-images.githubusercontent.com/37769713/109409581-50797a00-79d7-11eb-99dc-6bf4b406101a.png)

![image](https://user-images.githubusercontent.com/37769713/109409596-70a93900-79d7-11eb-8ad2-e9444d2b3374.png)

![image](https://user-images.githubusercontent.com/37769713/109409609-874f9000-79d7-11eb-8759-f14080ca0bac.png)

![image](https://user-images.githubusercontent.com/37769713/109409616-a2220480-79d7-11eb-87da-cc15b944aaf8.png)

![image](https://user-images.githubusercontent.com/37769713/109409636-ce3d8580-79d7-11eb-9abb-f2da5568994a.png)

![image](https://user-images.githubusercontent.com/37769713/109409643-d990b100-79d7-11eb-96f6-4364aeba521c.png)

