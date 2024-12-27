from setuptools import find_packages
from setuptools import setup


version = '0.0'

setup(
    name='base2_plug',
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
    packages=find_packages(),
    namespace_packages=['base2'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'TestDirective'],
    entry_points="""
      [z3c.autoinclude.plugin]
      target = base2
      """,
)
