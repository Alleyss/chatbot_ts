from setuptools import find_packages
from setuptools import setup


version = '0.0'

setup(
    name='TestDirective',
    version=version,
    description="",
    long_description="""\
""",
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    package_data={'': ['*.zcml']},
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = basepackage
      """,
)
