from setuptools import setup, find_packages

setup(
    name='gnome-battery-notifier',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'notify2',
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'gnome-battery-notifier=main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='An application that notifies when battery level exceeds 75%',
    license='MIT',
    keywords='GNOME battery notifier',
    url='https://github.com/yourusername/gnome-battery-notifier',
)