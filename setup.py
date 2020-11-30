from setuptools import setup


SHORT_DESCRIPTION = 'Rename output documentation files to transliterated names'

try:
    with open('README.md', encoding='utf8') as readme:
        LONG_DESCRIPTION = readme.read()

except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION


setup(
    name='foliantcontrib.transliterate',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    version='20.11.1',
    author='Maksim Lapshin',
    author_email='max@flussonic.com',
    packages=['foliant.preprocessors.transliterate'],
    license='MIT',
    platforms='any',
    install_requires=[
        'foliant>=1.0.8',
        'foliantcontrib.utils.combined_options>=1.0.7',
        'foliantcontrib.utils.preprocessor_ext>=1.0.4',
        'foliantcontrib.utils>=1.0.0',
        'transliterate>=1.10.0',
        'python-slugify>=4.0.1',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ]
)
