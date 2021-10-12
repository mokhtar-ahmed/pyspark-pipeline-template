import setuptools

dist = "release"
setuptools.setup(
    name=f'pyspark-pipeline-{dist}',
    version='1.0',
    author='Mokhtar Ahmed',
    description='Pyspark generic pipeline template.',
    install_requires=[],
    packages=setuptools.find_packages(where='.'),
    include_package_data=True
)
