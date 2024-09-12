

# panoptica

[![Python Versions](https://img.shields.io/pypi/pyversions/panoptica)](https://pypi.org/project/panoptica/)
[![Stable Version](https://img.shields.io/pypi/v/panoptica?label=stable)](https://pypi.python.org/pypi/panoptica/)
[![Documentation Status](https://readthedocs.org/projects/panoptica/badge/?version=latest)](http://panoptica.readthedocs.io/?badge=latest)
[![tests](https://github.com/BrainLesion/panoptica/actions/workflows/tests.yml/badge.svg)](https://github.com/BrainLesion/panoptica/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/BrainLesion/panoptica/graph/badge.svg?token=A7FWUKO9Y4)](https://codecov.io/gh/BrainLesion/panoptica)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Computing instance-wise segmentation quality metrics for 2D and 3D semantic- and instance segmentation maps.

## Features

The package provides three core modules:

1. Instance Approximator: instance approximation algorithms to extract instances from semantic segmentation maps/model outputs.
2. Instance Matcher: matches predicted instances with reference instances.
3. Instance Evaluator: computes segmentation and detection quality metrics for pairs of predicted - and reference segmentation maps.

![workflow_figure](https://github.com/BrainLesion/panoptica/blob/main/examples/figures/workflow.png?raw=true)

## Installation

With a Python 3.10+ environment, you can install panoptica from [pypi.org](https://pypi.org/project/panoptica/)

```sh
pip install panoptica
```

## Metrics

> [!NOTE]
> Panoptica supports a large range of metrics. <br>
> An overview of the supported metrics and their formulas can be found here: [panoptica/metrics.md](https://github.com/BrainLesion/panoptica/tree/main/metrics.md)

## Use cases and tutorials

> [!TIP]
> We provide Jupyter Notebook tutorials showcasing various use cases. <br>
> You can explore them here: [BrainLesion/tutorials/panoptica](https://github.com/BrainLesion/tutorials/tree/main/panoptica)


### Semantic Segmentation Input

<img src="https://github.com/BrainLesion/panoptica/blob/main/examples/figures/semantic.png?raw=true" alt="semantic_figure" height="300"/>

Jupyter Notebook Tutorial: [NBViewer](https://nbviewer.org/github/BrainLesion/tutorials/blob/main/panoptica/example_spine_semantic.ipynb) or on [GitHub](https://github.com/BrainLesion/tutorials/tree/main/panoptica/example_spine_semantic.ipynb) 

Although an instance-wise evaluation is highly relevant and desirable for many biomedical segmentation problems, they are still addressed as semantic segmentation problems due to the lack of appropriate instance labels.

This tutorial leverages all three modules of panoptica: instance approximation, -matching and -evaluation.

### Unmatched Instances Input

<img src="https://github.com/BrainLesion/panoptica/blob/main/examples/figures/unmatched_instance.png?raw=true" alt="unmatched_instance_figure" height="300"/>

Jupyter Notebook Tutorial: [NBViewer](https://nbviewer.org/github/BrainLesion/tutorials/blob/main/panoptica/example_spine_unmatched_instance.ipynb) or on [GitHub](https://github.com/BrainLesion/tutorials/tree/main/panoptica/example_spine_unmatched_instance.ipynb) 

It is a common issue that instance segmentation outputs feature good outlines but mismatched instance labels.
For this case, the matcher module can be utilized to match instances and the evaluator to report metrics.


### Matched Instances Input

<img src="https://github.com/BrainLesion/panoptica/blob/main/examples/figures/matched_instance.png?raw=true" alt="matched_instance_figure" height="300"/>

Jupyter Notebook Tutorial: [NBViewer](https://nbviewer.org/github/BrainLesion/tutorials/blob/main/panoptica/example_spine_matched_instance.ipynb) or on [GitHub](https://github.com/BrainLesion/tutorials/tree/main/panoptica/example_spine_matched_instance.ipynb) 

If your predicted instances already match the reference instances, you can directly compute metrics using the evaluator module.

### Matching Algorithm Example
Jupyter Notebook Tutorial: [NBViewer](https://nbviewer.org/github/BrainLesion/tutorials/blob/main/panoptica/example_spine_matching_algorithm.ipynb) or on [GitHub](https://github.com/BrainLesion/tutorials/tree/main/panoptica/example_spine_matching_algorithm.ipynb) 


### Using Configs (saving and loading)

You can construct Panoptica_Evaluator (among many others) objects and save their arguments, so you can save project-specific configurations and use them later.
It uses ruamel.yaml in a readable way.

Jupyter Notebook Tutorial: [NBViewer](https://nbviewer.org/github/BrainLesion/tutorials/blob/main/panoptica/example_config.ipynb) or on [GitHub](https://github.com/BrainLesion/tutorials/tree/main/panoptica/example_config.ipynb) 



## Citation

> [!IMPORTANT]
> If you use panoptica in your research, please cite it to support the development!

Kofler, F., Möller, H., Buchner, J. A., de la Rosa, E., Ezhov, I., Rosier, M., Mekki, I., Shit, S., Negwer, M., Al-Maskari, R., Ertürk, A., Vinayahalingam, S., Isensee, F., Pati, S., Rueckert, D., Kirschke, J. S., Ehrlich, S. K., Reinke, A., Menze, B., Wiestler, B., & Piraud, M. (2023). *Panoptica -- instance-wise evaluation of 3D semantic and instance segmentation maps.* [arXiv preprint arXiv:2312.02608](https://arxiv.org/abs/2312.02608).

```
@misc{kofler2023panoptica,
      title={Panoptica -- instance-wise evaluation of 3D semantic and instance segmentation maps}, 
      author={Florian Kofler and Hendrik Möller and Josef A. Buchner and Ezequiel de la Rosa and Ivan Ezhov and Marcel Rosier and Isra Mekki and Suprosanna Shit and Moritz Negwer and Rami Al-Maskari and Ali Ertürk and Shankeeth Vinayahalingam and Fabian Isensee and Sarthak Pati and Daniel Rueckert and Jan S. Kirschke and Stefan K. Ehrlich and Annika Reinke and Bjoern Menze and Benedikt Wiestler and Marie Piraud},
      year={2023},
      eprint={2312.02608},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Contributing

We welcome all kinds of contributions from the community!

### Reporting Bugs, Feature Requests and Questions

Please open a new issue [here](https://github.com/BrainLesion/panoptica/issues).