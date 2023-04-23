# Visual Pushing and Grasping Toolbox
This is a fork of [Visual Pushing and Grasping Toolbox](https://github.com/andyzeng/visual-pushing-grasping)
I used in my university project for AI-based gripping point determination.

## Prerequisite
You will need a NVIDIA GPU with at least 10GB VRAM to run this project.

## Installation

To run the project you have to install [b5](https://github.com/team23/b5)
and [docker](https://docs.docker.com/engine/install/) with NVIDIA GPU support,
[nvidia-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker).

Afterwards, you can set up and execute the project with the following two commands:

```shell
# Setup project
b5 install

# Run project
b5 run
```

This should open vrep with the default scene.

## Commands
The following commands are available in the project. Navigate to the location of this repo in your shell and run the commands there.

`b5 train:blocks`
Will start a Training on the Dataset located in `objects/blocks`.

`b5 train:abc`
Will start a Training on the Dataset located in `objects/abc`

`b5 scenario:create`
Let you create a new Scenario. See [here](https://github.com/andyzeng/visual-pushing-grasping#evaluation) for more information.

`b5 scenario:run`
Will run the evaluations used in my work. You need to specify the assets directory and the scenario you want to run.

Since I couldn't publish my model on GitHub, you have to train your own first. See commands above on how to do so.
After training, rename your log located in `logs` to latest and rename the model you want to use to `logs/latest/models/latest.pth`

Possible arguments to run the evaluation are listed below.
You can run them with `b5 scenario:run <Dataset> <Experiment> `.

| Experiment | Dataset                |
|------------|------------------------|
| exp_1      | blocks                 |
| exp_2      | abc_exp                |
| exp_c      | abc_single/<1/2/3/4/5> |
| exp_ll     | abc_single/<1/2/3/4/5> |
| exp_lr     | abc_single/<1/2/3/4/5> |
| exp_tl     | abc_single/<1/2/3/4/5> |
| exp_tr     | abc_single/<1/2/3/4/5> |