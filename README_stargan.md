# GAN based Clothing Design Program 

_Clothing design program improving StarGAN and Mask R-CNN_

<br><br>




## Result examples
_(U-net model, 140000 iterations training)_
<br><br>

![image](https://user-images.githubusercontent.com/37769713/120093837-c963ab80-c157-11eb-9a32-f4e348e4b727.png)





<br><br>

## Dependencies
* [Python 3.5+](https://www.continuum.io/downloads)
* [PyTorch 1.8.0+](http://pytorch.org/)
* [TensorFlow 2.0+](https://www.tensorflow.org/)

<br><br>



## Downloading datasets

You can download the clothing dataset [here](https://drive.google.com/drive/folders/12zLjMI1XY0Tl_QK2Gwb8P8V-yLsNvoFU?usp=sharing)!
<br>

The folder should be located like `StarGAN/data`.
<br>

The folder structure should be like this.

![image](https://user-images.githubusercontent.com/37769713/118932307-daa3ff80-b982-11eb-93da-0f3ad8c50c66.png)

All of the test images can be located in just one folder. (don't need to split the images.)<br>
But the other folders should exist even if they are empty.<br>

_Dataset Attributes : check, dot, leopard, stripe, tiedye, blue, green, purple, red_



<br><br>


## Training networks 
Run it from `StarGAN` path.<br>

```
# Train
!python main.py --mode train --dataset RaFD --rafd_crop_size 256 --image_size 256 --c_dim 9 \
                --num_iters 140000 \
                --rafd_image_dir data/custom/train --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --model_save_step 20000 \
                --model_name 'U-net'
```

```
# Test
!python main.py --mode test --dataset RaFD --image_size 256 --batch_size 1 --c_dim 9 \
                --rafd_image_dir data/custom/test \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --test_iters 140000
```

The result images are saved in `StarGAN/stargan_custom/results`.

(_c_dim: number of attributes<br>num_iters: number of training iterations<br>model_name: 'U-net' (default) / 'Original' / 'Reconstruction'_)
<br>

<br><br>


## Using pre-trained networks
You can download pre-trained models [here](https://drive.google.com/drive/folders/1YA8Ju_UAwqj8HBe-G6bPw0F3nXCaUl_J?usp=sharing).<br>

`140000-G.ckpt`, `140000-D.ckpt` : U-net model (good-performance) &nbsp; __<- Use this !__<br>
`140000-G_origin.ckpt`, `140000-D_origin.ckpt` : Original StarGAN model<br>
`140000-G_reconstruction.ckpt`, `140000-D_reconstruction.ckpt` : Reconstruction loss changed model (poor-performance) <br>

<br>

The folder should be located like `StarGAN/stargan_custom/models`.<br>
Please set the name of model file that you want to use as _'140000-G.ckpt'_ and _'140000-D.ckpt'_.

<br>

Run it from `StarGAN` path.<br>
```
# Test
!python main.py --mode test --dataset RaFD --image_size 256 --batch_size 1 --c_dim 9 \
                --rafd_image_dir data/custom/test \
                --sample_dir stargan_custom/samples --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models --result_dir stargan_custom/results \
                --test_iters 140000
```



The result images are saved in `StarGAN/stargan_custom/results`.


<br><br><br>



_We referenced this [paper](https://arxiv.org/abs/1711.09020). Thanks._
```
@inproceedings{choi2018stargan,
author={Yunjey Choi and Minje Choi and Munyoung Kim and Jung-Woo Ha and Sunghun Kim and Jaegul Choo},
title={StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation},
booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
year={2018}
}
```
