from setuptools import setup

setup(
    name='flask_resty_swagger',
    version='0.1.3',
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
        'flask-resty >= 0.6.0',
        'marshmallow >= 2.4.2',
    ],
    scripts=['bin/flask-resty-swagger'],
)
