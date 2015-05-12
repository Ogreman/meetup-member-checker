from setuptools import setup

setup(
    name="meetup-members",
    version='1.0',
    py_modules=['member_checker'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        meetup-members=member_checker:cli
    ''',
)

