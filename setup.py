from setuptools import setup
from setuptools import find_packages

version = '0.1.0.dev0'

# Please update tox.ini when modifying dependency version requirements
install_requires = [
    'acme>=0.31.0',
    'certbot>=0.34.0',
    'dns-lexicon>=3.2.9',
    'mock',
    'setuptools',
    'zope.interface',
]

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='certbot-dns-dreamhost',
    version=version,
    description="Dreamhost DNS Authenticator plugin for Certbot",
    url='https://github.com/chhsiao1981/certbot-dns-dreamhost',
    author="Chuan-Heng Hsiao",
    author_email='hsiao.chuanheng@gmail.com',
    license='Apache License 2.0',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-dreamhost = certbot_dns_dreamhost.dns_dreamhost:Authenticator',
        ],
    },
    test_suite='certbot_dns_dreamhost',
)
