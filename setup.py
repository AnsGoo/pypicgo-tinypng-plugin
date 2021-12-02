from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
setup(
    name='pypicgo-tinypng-plugin',
    version='1.0.0',
    keywords=['python', 'pypicgo','tinypng', 'tinify'],
    description='tinypng for pypicgo',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT Licence', 
    url='https://github.com/AnsGoo/pypicgo-tinypng-plugin',
    author='ansgoo',
    author_email='haiven_123@163.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'pypicgo>=1.1.0',
        'tinify>=1.5.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Environment :: MacOS X',
     ]
)
