from setuptools import Command, setup
import subprocess

# -----------------------------------------------------------------------------


def system(command):
    class SystemCommand(Command):
        user_options = []

        def initialize_options(self):
            pass

        def finalize_options(self):
            pass

        def run(self):
            subprocess.check_call(command, shell=True)

    return SystemCommand


# -----------------------------------------------------------------------------

setup(
    name='flask_resty_swagger',
    version='0.2.0',
    description="Generate swagger documentation from flask-resty service",
    author="Giacomo Tagliabue",
    author_email="giacomo.tag@gmail.com",
    license="MIT",
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ),
    keywords="rest flask swagger",
    packages=['flask_resty_swagger'],
    zip_safe=False,
    install_requires=[
        'apispec >= 0.14.0',
        'flask-resty >= 0.19.0',
        'marshmallow >= 2.4.2',
    ],
    scripts=['bin/flask-resty-swagger'],
    cmdclass={
        'clean': system('rm -rf build dist *.egg-info'),
        'package': system('python setup.py sdist bdist_wheel'),
        'publish': system('twine upload dist/*'),
        'release': system('python setup.py clean package publish'),
    },
)
