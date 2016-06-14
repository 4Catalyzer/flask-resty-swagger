from setuptools import setup

setup(
    name='flask_resty_swagger',
    version='0.1.1',
    description="Generate swagger documentation from flask-resty service",
    author="Giacomo Tagliabue",
    author_email="giacomo.tag@gmail.com",
    license="MIT",
    keywords="rest flask swagger",
    packages=['flask_resty_swagger'],
    zip_safe=False,
    install_requires=[
        'apispec >= 0.6.0',
        'flask-resty >= 0.6.0',
        'marshmallow >= 2.4.2',
    ],
    scripts=['bin/flask-resty-swagger'],
)
