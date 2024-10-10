# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autodub', 'autodub.audio', 'autodub.video']

package_data = \
{'': ['*']}

install_requires = \
['hmmlearn @ git+https://github.com/hmmlearn/hmmlearn.git',
 'jinja2>=3.1.4,<4.0.0',
 'moviepy>=1.0.3,<2.0.0',
 'pyannote-audio @ git+https://github.com/pyannote/pyannote-audio.git@develop',
 'pybind11>=2.8.0',
 'sympy @ git+https://github.com/sympy/sympy.git']

setup_kwargs = {
    'name': 'autodub',
    'version': '0.0.1',
    'description': 'Dub your movies.',
    'long_description': '',
    'author': 'Youval Vanlaer',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
