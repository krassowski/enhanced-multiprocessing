from setuptools import setup
from setuptools import find_packages


try:
    from pypandoc import convert

    def get_long_description(file_name):
        return convert(file_name, 'rst', 'md')

except ImportError:

    def get_long_description(file_name):
        with open(file_name) as f:
            return f.read()


if __name__ == '__main__':
    setup(
        name='enhanced_multiprocessing',
        packages=find_packages(),
        version='1.0',
        license='MIT',
        description='A wrapper around Python\'s multiprocessing, providing support for tqdm progress bars and shared arguments',
        long_description=get_long_description('README.md'),
        author='Michal Krassowski',
        author_email='krassowski.michal+pypi@gmail.com',
        url='https://github.com/krassowski/enhanced-multiprocessing',
        keywords=['multiprocessing', 'multiprocess', 'progress', 'progressbar', 'bar', 'enhanced'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Topic :: Utilities',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 3.7'
        ],
        install_requires=['tqdm'],
    )
