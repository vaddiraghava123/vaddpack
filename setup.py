from setuptools import setup, find_packages

setup(
    name='vaddpack',  # Package name
    version='0.1.0',   # Initial version
    description='A simple vaddpack package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Raghava Vaddi',
    author_email='vaddiraghava123@gmail.com',
    url='https://github.com/vaddiraghava123/vaddpack',
    license='MIT',
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        # Add dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
 )
