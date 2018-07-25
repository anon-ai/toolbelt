from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    with open('README.md') as f:
        long_description = f.read().strip()

with open('VERSION') as f:
    version = f.read().strip()

setup(
    name='hazy',
    description='Hazy command line interface (CLI) toolbelt.',
    long_description=long_description,
    url='https://github.com/hazy/toolbelt',
    author='Hazy',
    author_email='info@hazy.com',
    version=version,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
      'click>=5',
      'pycrypto>=2',
      'requests>=2',
    ],
    python_requires='>=3',
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'hazy = hazy.main:cli',
        ],
    },
)
