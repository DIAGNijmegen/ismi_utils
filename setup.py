import setuptools

if __name__ == '__main__':
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        version='0.1.0',
        author_email='Joeran.Bosma@radboudumc.nl',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/DIAGNijmegen/ismi',
        project_urls={
            "Bug Tracker": "https://github.com/DIAGNijmegen/ismi/issues"
        },
        license='Apache 2.0',
        packages=['ismi'],
    )
