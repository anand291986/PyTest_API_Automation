from setuptools import setup, find_packages

setup(name='API',
      version='1.0',
      description="API Test Automation",
      author='Anand Ganapathy',
      author_email='anand.ganapathy@mindtree.com',
      url='https://test.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==6.2.1",
          "pytest-html-reporter==0.2.3",
          "requests==2.23.0",
          "requests-oauthlib==1.3.0",
          "xmlschema==1.4.1",
          "SQLAlchemy==1.3.22",
          "pytest-sugar==0.9.4",
          "pytest-xdist==2.2.0",
          "PyHamcrest==2.0.2",
          "json-schema-matchers==0.1.2",
          "cx-Oracle==8.1.0",
      ]
      )