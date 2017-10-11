from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='reclib',
      version='0.1',
      description='A package for recommender systems based on latent factor models',
      long_description='This is unique in that we exclusively include our Weighted-SVD model.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      keywords='svd svd++ wsvd weighted-svd mf matrix-factorization',
      url='https://github.com/ncu-dart/reclib',
      author='Hung-Hsuan Chen',
      author_email='hhchen@ncu.edu.tw',
      license='MIT',
      packages=['reclib'],
      install_requires=[
            'numpy',
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=[
            'bin/wsvd-train.py',
            'bin/svd-train.py',
            'bin/rec-predict.py',
      ],
)
