import setuptools

setuptools.setup(
    name='django-sberbank',
    version='0.2.30',
    description='Django app for Sberbank payments',
    url='http://github.com/madprogrammer/django-sberbank',
    author='Sergey Anufrienko',
    author_email='sergey.anoufrienko@gmail.com',
    license='BSD',
    packages=setuptools.find_packages(),
    platforms='any',
    zip_safe=False,
    install_requires=[
        'django',
        'django-jsonfield',
        'djangorestframework',
        'celery',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
