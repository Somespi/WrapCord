from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme_file: 
    LONG_DESC = readme_file.read()

setup(
    name='wrapcord',
    version='0.1.2',
    author='Someone',
    author_email='',
    description='Helpful tools for Discord.',
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=["API","wrapper","discord","tools","wrapcord"],
    url='https://github.com/Somespi/Wrapcord/',
    packages=find_packages(),
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
)
