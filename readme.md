# Machine Learning Udacity

This is a repo with my personal notes from Udacity's Machine Learning Nanodegree.

You can use any information on this repo, but if you are taking the course please abide to the [Udacity Honor Code](https://udacity.zendesk.com/hc/en-us/articles/210667103-What-is-the-Udacity-Honor-Code-)

- - -

## Links

- [Get Anaconda here](https://www.continuum.io/downloads)
- [MLND Projects Repo](https://github.com/udacity/machine-learning)

## Setting up a python environment

After you install anaconda (choose the one for python 2.7), make sure that `which conda` returns a version. If it doesn't, you might have to `source ~/.bash_profile` (if you are on a Mac).

You can then create an environment with `conda create -n <env_name> python=2 anaconda` (then `y`) to create an environment with all the packages of anaconda. If you prefer, you can just create an bare environment (lose the `anacoda` param) and install only the necessary packages with `conda install <pkg_name>`.

Then activate it with `source activate <env_name>`.
