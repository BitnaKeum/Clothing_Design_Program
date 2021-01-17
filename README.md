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
You can download the clothing dataset [here](https://drive.google.com/drive/folders/12zLjMI1XY0Tl_QK2Gwb8P8V-yLsNvoFU?usp=sharing).
<br>

The folder should be located like `StarGAN/data`.


(The folder structure follows what is shown [here](https://github.com/yunjey/StarGAN/blob/master/jpg/RaFD.md).)


<br><br>


## Training networks 
('StarGAN' 폴더 위치에서 수행하기!)<br><br>
(_c_dim : number of attributes, num_iters : number of training iterations_)

```
# Train
!python main.py --mode train --dataset RaFD --rafd_crop_size 256 --image_size 128 --c_dim 7 \
                --num_iters 50000 \
                --rafd_image_dir data/custom/train \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --model_save_step 10000
```
```
# Test
!python main.py --mode test --dataset RaFD --image_size 128 --c_dim 7 \
                --rafd_image_dir data/custom/test \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --test_iters 50000
```

<br><br>

## Using pre-trained networks
You can download pre-trained model [here](https://drive.google.com/drive/folders/1YA8Ju_UAwqj8HBe-G6bPw0F3nXCaUl_J?usp=sharing).<br>

The folder should be located like `StarGAN/stargan_custom/models`.
<br>

('StarGAN' 폴더 위치에서 수행하기!)
```
# Test
!python main.py --mode test --dataset RaFD --image_size 128 --c_dim 7 \
                --rafd_image_dir data/custom/test \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --test_iters 50000
```

The result images are saved in `StarGAN/stargan_custom/results`.

<br><br>


## Result examples
__Sequence__ : original - blue - check - dot - flower - leopard - red - stripe<br>
(50000 iterations training)
<br><br>

![image](https://user-images.githubusercontent.com/37769713/104835211-6ed45c00-58e8-11eb-90b3-10a5a5265691.png)


![image](https://user-images.githubusercontent.com/37769713/104835237-99beb000-58e8-11eb-896f-5193a20ac592.png)

![image](https://user-images.githubusercontent.com/37769713/104835255-c5da3100-58e8-11eb-8ba7-9e74d1387e94.png)

![image](https://user-images.githubusercontent.com/37769713/104835284-edc99480-58e8-11eb-82e7-dfade9b87f9d.png)

![image](https://user-images.githubusercontent.com/37769713/104835305-0afe6300-58e9-11eb-9433-ab7e2786ac1b.png)

![image](https://user-images.githubusercontent.com/37769713/104835321-1fdaf680-58e9-11eb-84a0-e3aa1460a94f.png)

![image](https://user-images.githubusercontent.com/37769713/104835348-5b75c080-58e9-11eb-8c29-686c916240f1.png)

