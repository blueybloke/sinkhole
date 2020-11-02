from setuptools import setup


setup(
    name='sinkhole',
    version='0.1',
    py_modules=['sinkhole'],
    install_requires=[
        'Click',
        'requests',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        sinkhole=app:cli
    ''',
)
