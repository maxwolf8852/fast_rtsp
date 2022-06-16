import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

requirements = ["av>=9.2.0"]

setuptools.setup(
	name="fast_rtsp_maxwolf8852",
	version="0.0.1",
	author="Maxim Volkovskiy",
	author_email="maxwolf8852@gmail.com",
	description="Fast rtsp capture package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/maxwolf8852/fast_rtsp.git",
	packages=setuptools.find_packages(),
	install_requires=requirements,
	classifiers=[
		"Programming Language :: Python :: 3.9",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)