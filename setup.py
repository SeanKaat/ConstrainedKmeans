from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='kmeansclustering',         # How you named your package folder (MyLib)
    packages=['kmeansclustering'],   # Chose the same as "name"
    version='0.3',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='kmeans constrained clustering',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sean Kaat',                   # Type in your name
    author_email='seankaat@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/SeanKaat/kmeansclustering',
    # I explain this later on
    download_url='https://github.com/SeanKaat/kmeansclustering/archive/v_03.tar.gz',
    # Keywords that define your package best
    keywords=['Kmeans', 'clustering', 'constrained'],
    install_requires=[
        'pulp',
        'argparse',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
