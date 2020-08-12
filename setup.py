from setuptools import setup, find_packages
import os
import os.path
import sys

if sys.version[0] == "2":
    from pipes import quote
else:
    from shlex import quote

# Bumped version
version = '1.3.6'

# Require
install_requires = [
    "python-dateutil",
    "arrow",
    "requests==2.20.0",
    "pyfiglet",
    "twitter",
    "Pillow",
    "PySocks",
    "pocket"
]

# Default user (considers non virtualenv method)
user = os.environ.get('SUDO_USER', os.environ.get('USER', None))

# Copy default config if not exists
default = os.path.expanduser("~") + os.sep + '.rainbow_config.json'
if not os.path.isfile(default):
    cmd = 'cp rainbowstream/colorset/config ' + default
    os.system(cmd)
    if user:
        cmd = 'chown ' + quote(user) + ' ' + default
        os.system(cmd)
    cmd = 'chmod 777 ' + default
    os.system(cmd)

# Setup
setup(name='rainbowstream',
      version=version,
      description="A smart and nice Twitter client on terminal.",
      long_description=open("./README.rst", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
      ],
      keywords='twitter, command-line tools, stream API',
      author='Vu Nhat Minh',
      author_email='nhatminh179@gmail.com',
      url='http://www.rainbowstream.org/',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      rainbowstream=rainbowstream.rainbow:fly
      """,
      )
