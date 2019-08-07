from setuptools import setup

testing_requirements = [
    'pytest-cov==2.5.1',
    'tox==2.7.0',
]

setup(
    name='python_production_script_recipe',
    version='1.0.0',
    author='Adam Burns',
    author_email='adam@operatingops.org',
    description='Recipe of best practices for Python scripts in production.',
    packages=['sample_scripts'],
    entry_points={
        'console_scripts': [
            'sample-script-good=sample_scripts.good:entry_point',
        ],
    },
    extras_require={
        'testing': testing_requirements
    }
)
