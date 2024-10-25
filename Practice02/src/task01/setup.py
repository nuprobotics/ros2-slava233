from setuptools import find_packages, setup

package_name = 'task01'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + "/launch", ['launch/task01.launch'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='slava233',
    maintainer_email='harik10346@gmail.com',
    description='Message Receiver',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'receiver = task01.receiver:main',
        ],
    },
)
