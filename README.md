# Real Time CNN Visualization

This is an UI application, which allows to visualize Convolutional Neural Networks in real time.
First, Activation maps of convolutional layers as well activations of fully connected layer are visualized and available for applying more advance visualization techniques.

## Visualization Algorithms

* [Grad-CAM](https://arxiv.org/abs/1610.02391 "Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization")
* [Guided Backprop](https://arxiv.org/abs/1412.6806 "Striving for Simplicity: The All Convolutional Net")

## Requirements

* [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/) (optional)
* Recent NVIDIA drivers (`nvidia-384` on Ubuntu)
* [NVIDIA Docker](https://github.com/NVIDIA/nvidia-docker )


## Usage

#### With pure Docker
```
docker build -t basecv .
docker run  --runtime nvidia --env DISPLAY=$DISPLAY --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"    -it -v  -v=$(pwd)/..:$(pwd)/.. -w=$(pwd) basecv  python3 main.py
```

### With Docker Compose

```
docker-compose build
docker-compose run vis
```

## Troubleshooting

#### Could not connect to any X display.

Run `xhost +local:docker`, also check [this](https://forums.docker.com/t/start-a-gui-application-as-root-in-a-ubuntu-container/17069)