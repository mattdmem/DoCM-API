from distutils.core import setup
import os
import uuid
from pip.req import parse_requirements
install_reqs = parse_requirements(os.path.join(os.path.dirname(__file__), "requirements.txt"), session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs if ir.req is not None]
setup(
    name='DoCM-API',
    version='0.0.1',
    packages=['pyDoCM'],
    url='',
    license='',
    author='mparker',
    author_email='',
    description='A python wrapper for the Database of Curated Mutations API',
    install_requires=reqs
)
