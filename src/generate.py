import argparse
import logging
import os
from pathlib import Path
from PIL import Image, ImageDraw
from slugify import slugify
from typing import List, Optional, Tuple
import uuid

import Layout


class Gutter:
    def __init__(self, Vertical: int, Horizontal: int) -> None:
        self.Vertical = Vertical
        self.Horizontal = Horizontal


class Margin:
    def __init__(self, Top: float, Right: float, Bottom: float, Left: float) -> None:
        self.Top = Top
        self.Right = Right
        self.Bottom = Bottom
        self.Left = Left


class BookType:
    def __init__(self, Name: str, Width: int, Height: int) -> None:
        self.Name = Name
        self.Width = Width
        self.Height = Height

    def GetDimensions(self) -> Tuple[int, int]:
        return (self.Width, self.Height)


BookTypes = {
    # Blurb Photo Book
    'Small Square': BookType('7x7-blurb', 495, 495),
    'Standard Portrait': BookType('8x10-blurb', 567, 720),
    'Standard Landscape': BookType('10x8-blurb', 693, 594),
    'Large Landscape': BookType('12x12-blurb', 855, 864),
    'Large Square': BookType('13x11-blurb', 909, 783),

    # Blurb Magazine
    'Blurb Magazine': BookType('8.5x11-blurb', 621, 810),

    # Blurb Trade Book
    'Trade Book 8x10': BookType('8x10_true-blurb', 585, 738),
    'Trade Book 6x9': BookType('6x9-blurb', 441, 666),
    'Trade Book 5x8': BookType('5x8-blurb', 369, 594),
}


def Slugify(Text: str) -> str:
    return slugify(Text, to_lower=True)


def GetThumbnailRatio(Dimensions: Tuple[int, int]) -> float:
    return max(Dimensions[0] / 185, Dimensions[1] / 100)


def GetThumbnailDimensions(Dimensions: Tuple[int, int]) -> Tuple[int, int]:
    Ratio = GetThumbnailRatio(Dimensions)
    return (int(Dimensions[0] / Ratio), int(Dimensions[1] / Ratio))


def GetThumbnailCoordinate(Dimensions: Tuple[int, int], Coordinate: int) -> int:
    Ratio = GetThumbnailRatio(Dimensions)
    return int(Coordinate / Ratio)


def GenerateCells(Thumbnail: Image, Grid: List[List[Optional[Tuple[int, int]]]], Dimensions: Tuple[int, int], PageMargin: Margin, Gutter: Gutter) -> str:
    RowCount = len(Grid)
    assert 0 < RowCount
    ColCount = len(Grid[0])

    CellHeight = (Dimensions[1] - PageMargin.Top - PageMargin.Bottom - (RowCount-1) * Gutter.Vertical) / RowCount
    CellWidth = (Dimensions[0] - PageMargin.Left - PageMargin.Right - (ColCount-1) * Gutter.Horizontal) / ColCount

    Cells = ''
    CellIdx = 0
    PosY = Dimensions[1] - PageMargin.Top
    for RowIdx, Row in enumerate(Grid):
        assert len(Row) == ColCount
        PosX = PageMargin.Left
        for ColIdx, Cell in enumerate(Row):
            if Cell is not None:
                assert 0 < Cell[0]
                assert 0 < Cell[1]
                assert ColIdx + Cell[0] <= ColCount
                assert RowIdx + Cell[1] <= RowCount

                Padding = Margin(0, 0, 0, 0)

                if 0 < RowIdx:
                    Padding.Top = Gutter.Vertical / 2
                if ColIdx + Cell[0] < ColCount:
                    Padding.Right = Gutter.Horizontal / 2
                if RowIdx + Cell[1] < RowCount:
                    Padding.Bottom = Gutter.Vertical / 2
                if 0 < ColIdx:
                    Padding.Left = Gutter.Horizontal / 2

                Width = Padding.Left + CellWidth + Padding.Right + (CellWidth + Gutter.Horizontal) * (Cell[0] - 1)
                Height = Padding.Bottom + CellHeight + Padding.Top + (CellHeight + Gutter.Vertical) * (Cell[1] - 1)
                if Height < 0:
                    logging.error('Cell height is negative.')
                elif Width < 0:
                    logging.error('Cell width is negative.')

                Draw = ImageDraw.Draw(Thumbnail)
                Left = GetThumbnailCoordinate(Dimensions, int(PosX + Padding.Left))
                Top = GetThumbnailCoordinate(Dimensions, int(Dimensions[1] - PosY + Padding.Top))
                Right = GetThumbnailCoordinate(Dimensions, int(PosX + Width - Padding.Right))
                Bottom = GetThumbnailCoordinate(Dimensions, int(Dimensions[1] - PosY + Height - Padding.Bottom))
                Draw.rectangle([Left, Top, Right, Bottom], fill='#8C8C8C', outline='#959595', width=1)
                HorizontalCenter = int((Right - Left) / 2 + Left)
                VerticalCenter = int((Bottom - Top) / 2 + Top)
                CrosshairSize = 3
                Draw.line([HorizontalCenter, VerticalCenter - CrosshairSize, HorizontalCenter, VerticalCenter + CrosshairSize], fill='#333333', width=1)
                Draw.line([HorizontalCenter - CrosshairSize, VerticalCenter, HorizontalCenter + CrosshairSize, VerticalCenter], fill='#333333', width=1)

                CellIdx += 1
                Cells += f'''\
                {{
                    bottomPad = {Padding.Bottom},
                    dynamicCellAlignWithPhoto = true,
                    dynamicCellAutoText = "{{{{custom_token}}}}",
                    dynamicCellPlacement = "below",
                    dynamicCellSpacing = 9,
                    height = 9,
                    hints = {{
                        photoIndex = {CellIdx},
                    }},
                    leftPad = {Padding.Left},
                    placeholderType = "photo",
                    rightPad = {Padding.Right},
                    topPad = {Padding.Top},
                    transform = {{
                        angle = 0,
                        height = {Height},
                        width = {Width},
                        x = {PosX},
                        y = {PosY - Height},
                    }},
                    transformFromCustomPage = {{
                        angle = 0,
                        height = {Height},
                        width = {Width},
                        x = {PosX},
                        y = {PosY - Height},
                    }},
                    type = "PDEImage",
                    width = 9,
                }},
'''
            if 0 < ColIdx:
                PosX += Gutter.Horizontal / 2
            PosX += CellWidth + Gutter.Horizontal / 2
        if 0 < RowIdx:
            PosY -= Gutter.Vertical / 2
        PosY -= CellHeight + Gutter.Vertical / 2
    return Cells


def GenerateTemplate(OutDir: Path, Book: BookType, LayoutName: str, PageUuid: str, Grid: List[List[Optional[Tuple[int, int]]]], Margin: Margin, Gutter: Gutter, IsDoublePage: bool = False) -> str:
    Dimensions = Book.GetDimensions()
    if IsDoublePage:
        Dimensions = (Dimensions[0] * 2, Dimensions[1])

    Thumbnail = Image.new('RGB', GetThumbnailDimensions(Dimensions), 'white')

    Cells = GenerateCells(Thumbnail, Grid, Dimensions, Margin, Gutter)

    Thumbnail.save(f'{OutDir}/{Book.Name}/{Slugify(LayoutName)}/{PageUuid}_preview.png')

    return f'''\
		{{
			{{
				bottomPad = 0,
				children = {{
{Cells}
				}},
				leftPad = 0,
				rightPad = 0,
				topPad = 0,
				type = "PDEContainer",
			}},
			hints = {{
				hintType = "pageOptions",
				pageKey = "{Book.Name}_{Slugify(LayoutName)}_{PageUuid}",
			}},
			isSpread = {str(IsDoublePage).lower()},
			name = "{LayoutName}_{PageUuid}",
			pageHeight = {Dimensions[1]},
			pageId = "{Book.Name}_{Slugify(LayoutName)}_{PageUuid}",
			pageWidth = {Dimensions[0]},
			previewName = "{PageUuid}_preview.png",
			title = "{LayoutName}_{PageUuid}",
		}},
'''


def OutputTemplateFiles(OutDir: Path, Book: BookType, LayoutName: str, Margin: Margin, Gutter: Gutter) -> None:
    Path(f'{OutDir}/{Book.Name}/{Slugify(LayoutName)}').mkdir(exist_ok=True)
    File = open(f'{OutDir}/{Book.Name}/{Slugify(LayoutName)}/templatePages.lua', 'w')

    PaperUuid = uuid.uuid4()

    Templates = ''
    for PageUuid, Grid in Layout.GetSinglePages():
        Templates += GenerateTemplate(OutDir, Book, LayoutName, PageUuid, Grid, Margin, Gutter)
    for PageUuid, Grid in Layout.GetDoublePages():
        Templates += GenerateTemplate(OutDir, Book, LayoutName, PageUuid, Grid, Margin, Gutter, IsDoublePage=True)

    File.write(f'''\
pages = {{
	actualBookHeight = {Book.GetDimensions()[1]},
	actualBookWidth = {Book.GetDimensions()[0]},
	backgrounds = {{
	}},
	bookHeight = {Book.GetDimensions()[1]},
	bookWidth = {Book.GetDimensions()[0]},
	covers = {{
		hardcover_imagewrap = {{
		}},
		hardcover_jacket = {{
		}},
		softcover = {{
		}},
	}},
	hints = {{
		bookTitle = "{LayoutName}",
		hintType = "bookOptions",
		paperId = "{Book.Name}",
		styleName = "{Slugify(LayoutName)}",
	}},
	pages = {{
{Templates}
	}},
	paperId = "{PaperUuid}",
}}
''')


def OutputLayoutFile(OutDir: Path, Book: BookType, LayoutName: str) -> None:
    LayoutUuid = uuid.uuid4()
    TemplateUuid = uuid.uuid4()
    Path(f'{OutDir}/{Book.Name}').mkdir(exist_ok=True)
    File = open(f'{OutDir}/{Book.Name}/{Slugify(LayoutName)}.lrtemplate', 'w')
    File.write(f'''\
s = {{
	id = "{LayoutUuid}",
	internalName = "{Book.Name}_{Slugify(LayoutName)}",
	title = "{LayoutName}",
	type = "layoutStyle",
	value = {{
		paperId = "{Book.Name}",
		resources = "{Slugify(LayoutName)}",
		styleName = "{Slugify(LayoutName)}",
		templateId = "{TemplateUuid}",
	}},
	version = 0,
}}
''')


def GetLengthValidator(Min: int, Max: int):
    class LengthValidator(argparse.Action):
        def __call__(self, Parser, Namespace, Values, OptionString=None):
            if not Min <= len(Values) <= Max:
                raise argparse.ArgumentTypeError(f'argument "{self.dest}" requires between {Min} and {Max} arguments')
            setattr(Namespace, self.dest, Values)
    return LengthValidator


class DirValidator(argparse.Action):
    def __call__(self, Parser, Namespace, Value, OptionString=None):
        if not Value.is_dir():
            raise argparse.ArgumentTypeError(f'argument "{self.dest}" must be an existing directory')
        setattr(Namespace, self.dest, Value)


def ListToCsv(Values: List[str]) -> str:
    Csv = ''
    for Value in Values:
        Csv += f'{Value},'
    return Csv[:-1]


def main() -> None:
    Parser = argparse.ArgumentParser(description='Generate layout templates for the Lightroom Book module.')
    Parser.add_argument('book', choices=BookTypes.keys(), help='Book to generate layout templates for.')
    Parser.add_argument('-o', '--outdir', type=Path, default=os.getcwd(), action=DirValidator, help='Output directory for the template files. Default: current working directory.')
    Parser.add_argument('-n', '--name', type=str, help='Name for the generated set of layout templates.')
    Parser.add_argument('-m', '--margin', type=int, nargs='+', default=[0], action=GetLengthValidator(1, 4), help='Margin on pages. Two numbers set vertical and horizontal margins separately. Three numbers set top, horizontal, and bottom margins separately. Four numbers set top, right, bottom, and left margins separately.')
    Parser.add_argument('-g', '--gutter', type=int, nargs='+', default=[0], action=GetLengthValidator(1, 2), help='Gutter between images. Two numbers set vertical and horizontal gutters separately.')
    Parser.add_argument('-r', '--ratio', type=float, help='Desired ratio between width and height of content on page.')
    Parser.add_argument('-l', '--log', default='info', choices=['debug', 'info', 'warning', 'error', 'critical'], help='Set the logging level.')

    Args = Parser.parse_args()

    logging.basicConfig(format='%(levelname)s: %(message)s', level=Args.log.upper())

    Book = BookTypes[Args.book]

    if Args.name is None:
        Args.name = f'Margin {ListToCsv(Args.margin)}, gutter {ListToCsv(Args.gutter)}'
        if Args.ratio is not None:
            Args.name += f', ratio {Args.ratio}'

    if 1 == len(Args.margin):
        Args.margin.append(Args.margin[0])
    if 2 == len(Args.margin):
        Args.margin.append(Args.margin[0])
    if 3 == len(Args.margin):
        Args.margin.append(Args.margin[1])
    PageMargin = Margin(Args.margin[0], Args.margin[1], Args.margin[2], Args.margin[3])

    if Args.ratio is not None:
        Width = Book.GetDimensions()[0] - PageMargin.Left - PageMargin.Right
        Height = Book.GetDimensions()[1] - PageMargin.Top - PageMargin.Bottom
        if Width / Height < Args.ratio:
            Diff = Height - Width / Args.ratio
            PageMargin.Top += Diff / 2
            PageMargin.Bottom += Diff / 2
        else:
            Diff = Width - Height * Args.ratio
            PageMargin.Left += Diff / 2
            PageMargin.Right += Diff / 2

    if 1 == len(Args.gutter):
        Args.gutter.append(Args.gutter[0])
    ImageGutter = Gutter(Args.gutter[0], Args.gutter[1])

    OutputLayoutFile(Args.outdir, Book, Args.name)
    OutputTemplateFiles(Args.outdir, Book, Args.name, PageMargin, ImageGutter)


if __name__ == '__main__':
    main()
