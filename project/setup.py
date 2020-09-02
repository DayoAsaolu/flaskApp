from setuptools import setup

setup(
    name='project',
    version="0.2",
    packages=['project'],

    install_requires=['flask>=0.12'],

    package_data={
        '': ['*.txt', '*.pdf', '*.db', '*.py'],
        'project': ['docs/*', 'tests/*', 'static/*', 'templates/*'],
    },

    author="Brandon Drake-Goobie, Robin White, Dayo Asaolu, Rashed Ferdous, Alberto Briceno"
    description="This is our project file",
    url="http://127.0.0.1:5000",
)