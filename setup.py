from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('crmp', 'theme', 'docs', 'index.rst'))

setup(name='crmp.theme',
      version='1.0',
      description="CRMP theme",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Upfront Systems',
      author_email='rijk@upfrontsystems.co.za',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['crmp'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'hexagonit.testing',
          'manuel',
          'plone.app.testing',
          'plone.app.theming',
          'plone.browserlayer',
          'setuptools',
          'zope.i18nmessageid',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
