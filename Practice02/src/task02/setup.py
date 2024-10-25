from setuptools import find_packages, setup

package_name = 'task02'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/task02.yaml']),
        ('share/' + package_name + '/launch', ['launch/task02.launch']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='slava233',
    maintainer_email='harik10346@gmail.com',
    description='ROS2 Message Publisher',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = task02.publisher:main',
        ],
    },
)
