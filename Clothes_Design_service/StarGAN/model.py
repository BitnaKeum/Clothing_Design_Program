########## skip connection ###########

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class Generator(nn.Module):
    """Generator network."""

    def __init__(self, conv_dim=64, c_dim=5, repeat_num=6):
        super(Generator, self).__init__()

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.layer1 = nn.Sequential(
            nn.Conv2d(3 + c_dim, conv_dim, kernel_size=7, stride=1, padding=3, bias=False),
            nn.InstanceNorm2d(conv_dim, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True))

        # Down-sampling layers.

        curr_dim = conv_dim
        self.layer2 = nn.Sequential(
            nn.Conv2d(curr_dim, curr_dim * 2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.InstanceNorm2d(curr_dim * 2, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True))
        curr_dim = curr_dim * 2

        self.layer3 = nn.Sequential(
            nn.Conv2d(curr_dim, curr_dim * 2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.InstanceNorm2d(curr_dim * 2, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True))
        curr_dim = curr_dim * 2

        self.layer4 = nn.Sequential(
            nn.Conv2d(curr_dim, curr_dim * 2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.InstanceNorm2d(curr_dim * 2, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True))
        curr_dim = curr_dim * 2

        # Up-sampling layers.

        self.layer5 = nn.Sequential(
            nn.ConvTranspose2d(curr_dim, curr_dim // 2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.InstanceNorm2d(curr_dim // 2, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True))
        curr_dim = curr_dim // 2

        self.layer6 = nn.Sequential(
            nn.ConvTranspose2d(curr_dim, curr_dim // 2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.InstanceNorm2d(curr_dim // 2, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True))
        curr_dim = curr_dim // 2

        self.layer7 = nn.Sequential(
            nn.ConvTranspose2d(curr_dim, curr_dim // 2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.InstanceNorm2d(curr_dim // 2, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True))
        curr_dim = curr_dim // 2

        self.layer8 = nn.Sequential(
            nn.Conv2d(curr_dim, 3, kernel_size=7, stride=1, padding=3, bias=False),
            nn.Tanh())

    def forward(self, x, c):  # x_real, c_target
        # Replicate spatially and concatenate domain information.
        # Note that this type of label conditioning does not work at all if we use reflection padding in Conv2d.
        # This is because instance normalization ignores the shifting (or bias) effect.
        c = c.view(c.size(0), c.size(1), 1, 1)
        c = c.repeat(1, 1, x.size(2), x.size(3))
        c = c.to(self.device)
        x = x.to(self.device)
        x = torch.cat([x, c], dim=1)  # concatenate

        l1 = self.layer1(x)
        l2 = self.layer2(l1)
        l3 = self.layer3(l2)
        l4 = self.layer4(l3)
        l5 = self.layer5(l4)
        l5 = l3.clone() + l5.clone()  # Skip-connection
        l6 = self.layer6(l5)
        l6 = l2.clone() + l6.clone()  # Skip-connection
        l7 = self.layer7(l6)
        l8 = self.layer8(l7)
        return l8


class Discriminator(nn.Module):
    """Discriminator network with PatchGAN."""

    def __init__(self, image_size=128, conv_dim=64, c_dim=5, repeat_num=6):
        super(Discriminator, self).__init__()
        layers = []
        layers.append(nn.Conv2d(3, conv_dim, kernel_size=4, stride=2, padding=1))
        layers.append(nn.LeakyReLU(0.01))

        curr_dim = conv_dim
        for i in range(1, repeat_num):
            layers.append(nn.Conv2d(curr_dim, curr_dim * 2, kernel_size=4, stride=2, padding=1))
            layers.append(nn.LeakyReLU(0.01))
            curr_dim = curr_dim * 2

        kernel_size = int(image_size / np.power(2, repeat_num))
        self.main = nn.Sequential(*layers)
        self.conv1 = nn.Conv2d(curr_dim, 1, kernel_size=3, stride=1, padding=1, bias=False)
        self.conv2 = nn.Conv2d(curr_dim, c_dim, kernel_size=kernel_size, bias=False)

    def forward(self, x):
        h = self.main(x)
        out_src = self.conv1(h)
        out_cls = self.conv2(h)
        return out_src, out_cls.view(out_cls.size(0), out_cls.size(1))

