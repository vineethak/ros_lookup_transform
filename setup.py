from setuptools import find_packages, setup

package_name = 'my_tf2_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dheeraj',
    maintainer_email='vineetha.iisc@gmail.com',
    description='ROS2 TF2 Transform Lookup Example',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'transform_lookup = ros_lookup_transform.transform_lookup:main'
        ],
    },
)
