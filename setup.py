from setuptools import setup, find_packages

def listify(filename):
    return filter(None, open(filename,'r').read().split('\n'))

setup(
    name = "vumi-client",
    version = "0.1.0",
    url = 'http://github.com/smn/vumi-client',
    license = 'BSD',
    description = 'Client for Vumi API',
    author = 'Praekelt Foundation',
    author_email = 'dev@praekeltfoundation.org',
    packages = find_packages(),
    install_requires = ['setuptools'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking'
    ]
)

