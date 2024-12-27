from setuptools import find_packages
from setuptools import setup


version = '0.0'

setup(
    name='SiblingPackage',
    version=version,
    description="",
    long_description="""\
""",
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='GPL',
    package_data={'': ['*.zcml']},
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['F'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'TestDirective',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
