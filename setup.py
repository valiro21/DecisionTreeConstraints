import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='DecisionTreeConstraints',
     version='0.1',
     author="Valentin Rosca",
     author_email="rosca.valentin2012@gmail.com",
     description="Building Decision Trees with Constraints",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/valiro21/DecisionTreeConstraints",
     packages=setuptools.find_packages(),
     keywords='decision trees classifier pruning constraints',
     classifiers=[
         'Development Status :: 3 - Alpha',
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
         'Intended Audience :: Science/Research',
         'Intended Audience :: Developers',
     ],
 )
