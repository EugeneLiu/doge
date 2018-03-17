# coding: utf8

import sys

from setuptools.command.test import test as TestCommand
from setuptools import setup, Extension


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(name='doge',
      version='0.1.1',
      description='A RPC Framework',
      long_description=open('README.md').read(),
      author='Timmy',
      author_email='zhu327@gmail.com',
      url='http://github.com/zhu327/doge',
      packages=['doge'],
      license=open('LICENSE').read(),
      keywords=['rpc', 'etcd', 'messagepack', 'gevent', 'microservices'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Natural Language :: Chinese',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
      ],
      install_requires=[
          'mprpc',
          'pyformance',
          'python-etcd',
      ],
      tests_require=[
          'pytest',
      ],
      cmdclass={'test': PyTest}, )