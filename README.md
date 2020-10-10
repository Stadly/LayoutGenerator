# LayoutGenerator

[![Software License][ico-license]](LICENSE.md)

Generate layout templates for the Book module in Adobe Lightroom Classic.

## Introduction

It is very hard to create layouts with consistent margin and gutters in Adobe Lightroom Classic’s Book module.

`LayoutGenerator` creates layout templates with your desired margin and gutters, allowing you to design books with consistent page layouts, regardless of the number of images on each page.

## Installation

Use the following commands to set up `LayoutGenerator`.

Download `LayoutGenerator`:

``` bash
git clone --depth 1 https://github.com/Stadly/LayoutGenerator.git
```

Install dependencies:

``` bash
pip install -r LayoutGenerator/requirements.txt
```

Change working directory:

``` bash
cd LayoutGenerator/src
```

### Install in Docker container

It is also possible to set up and use `LayoutGenerator` in a docker container instead of installing it locally. See the section [Using Docker](#using-docker) for details.

## Usage

Run the python file `generate.py` to use `LayoutGenerator`.

### Book type

`LayoutGenerator` can be used to generate layout templates for 9 different book types:

- Small Square
- Standard Portrait
- Standard Landscape
- Large Landscape
- Large Square
- Blurb Magazine
- Trade Book 8x10
- Trade Book 6x9
- Trade Book 5x8

Specify your book type to generate layout templates for it:

```
python generate.py 'Standard Landscape'
```

### Storing the layout template files

By default, the template files will be stored in your current working directory. To set a different output directory, use the `-o` or `--outdir` argument.

The output directory should be set based on your operating system:

- Windows: `C:\Users\[user name]\AppData\Roaming\Adobe\Lightroom\Layout Templates`
- macOS: `/Users/[user name]/Library/Application Support/Adobe/Lightroom/Layout Templates`

``` bash
python generate.py 'Standard Landscape' -o /my/output/directory
```

### Page margins

Use the `-m` or `--margin` argument to set page margins. Specify from 1 to 4 integers to get your desired result:
- 1 number: `-m A`. All margins are set to `A`.
- 2 numbers: `-m Y X`. Top and bottom margins are set to `Y`, left and right margins are set to `X`.
- 3 numbers: `-m T X B`. Top margin is set to `T`, left and right margins are set to `X`, bottom margin is set to `B`.
- 4 numbers: `-m T R B L`. Top margin is set to `T`, right margin is set to `R`, bottom margin is set to `B`, left margin is set to `L`.

### Image gutters

Use the `-g` or `--gutter` argument to set the gutter between images. Specify 1 or 2 integers to get your desired result:
- 1 number: `-g A`. All gutters are set to `A`.
- 2 numbers: `-g V H`. Vertical gutters are set to `V`, horizontal gutters are set to `H`.

### Layout ratio

Use the `-r` or `--ratio` argument to set the ratio between the width and height of the layouts. With a ratio of 2/3, the layout width will be 2/3 of the layout height. If you specify a ratio of 1, square layouts will be generated. The page margins are automatically adjusted to account for the difference between the chosen layout ratio and the ratio of the book pages.

``` bash
python generate.py 'Standard Landscape' -r 3/2
```

### Naming the layout template collection

Inside Lightroom Classic, the generated layout templates will be available in a template collection. By default, the collection will be named based on the margins, gutters and ratio of the layout templates. To set a custom name, use the `-n` or `-name` argument:

``` bash
python generate.py 'Standard Landscape' -n 'My layout templates'
```

### Logging output

Any logging output generated by `LayoutGenerator` is written to `stderr`. There are five levels of logging:

1. debug
2. info
3. warning
4. error
5. critical

By default, `info` and higher log messages are output. Use the `-l` or `--log` argument to specify which levels of log messages to output:

``` bash
python generate.py 'Standard Landscape' -l debug
```

### Using Docker

[Docker](https://www.docker.com) makes setting up and using `LayoutGenerator` really easy. All you have to do is build the docker image, and you can use `LayoutGenerator` without installing any dependencies (even Python!) locally.

#### Build the docker image

Build the docker image using the following command.

``` bash
docker build -t generate-layout .
```

#### Run the docker container

After the image is built, just run it to use `LayoutGenerator`. The syntax when running `LayoutGenerator` inside the docker container is the same as when running it locally, except that `python generate.py` is replaced by `docker run generate-layout`.

In addition the `--output` argument should not be used. The output directory is instead specified using volume mounting. In order for the docker container to be able to access the location where the layout template files should be stored, the output directory must be mounted to the docker container. Use the `-v` or `--volume` argument and specify the absolute path of the output directory, followed by `:/output`.

For example, the following command will generate layout templates for the book type `Large Square`, with margins of 50 and gutter of 10, and store them at `/path/to/templates`:

``` bash
docker run -v /path/to/templates:/output generate-layout 'Large Square' -m 50 -g 10
```

If you want to mount a directory using a relative path, you can use `$(pwd)` to denote the current working directory:

``` bash
docker run -v "$(pwd):/output" generate-layout 'Large Square' -m 50 -g 10
```

## Change log

Please see [CHANGELOG](CHANGELOG.md) for information on what has changed recently.

## Security

If you discover any security related issues, please email magnar@myrtveit.com instead of using the issue tracker.

## Credits

- [Magnar Ovedal Myrtveit][link-author]
- [All contributors][link-contributors]

## License

The MIT License (MIT). Please see [License file](LICENSE.md) for more information.

[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square

[link-author]: https://github.com/Stadly
[link-contributors]: ../../contributors
