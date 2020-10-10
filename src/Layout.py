from typing import List, Optional, Tuple

def GetSinglePages() -> List[Tuple[str, List[List[Optional[Tuple[int, int]]]]]]:
    """
    Get single page layouts.
    A page layout is represented as a two-dimensional list (spreadsheet) of None or pair of
    int. The size of the first dimension gives the number of rows, and the size of the second
    dimension gives the number of columns. The rows are equallys sized, and the columns are
    equally sized. A pair (X,Y) in cell (A,B) means that the layout should contain an image
    covering X columns and Y rows, and the upper left corner should be placed in cell (A,B).
    So the image will cover the rectangular area having cell (A,B) in the upper left corner
    and cell (A+X-1,B+Y-1) in the lower right corner.

    Example 1:
        There are three rows and two columns.
        Three images:
        - One image covers the upper left half of the page width (1 column) and 1/3 of the page height (1 row).
        - One image covers the upper right half of the page width (1 column) and 1/3 of the page height (1 row).
        - One image covers the lower full width of the page (2 columns) and 2/3 of the page height (2 rows).
        [
            [   (1,1),  (1,1)   ],
            [   (2,2),  None    ],
            [   None,   None    ],
        ]

    Example 2:
        There are five rows and five columns.
        Four images:
        - One image covers the upper left 3/5 of the page width and 2/5 of the page height.
        - One image covers the upper right 2/5 or the page width and 3/5 the page height.
        - One image covers the lower left 2/5 of the page width and 3/5 of the page height.
        - One image covers the lower right 3/5 or the page width and 2/5 the page height.
        - The center of the page (1/5 of height and width) is empty.
        [
            [   (3,2),  None,   None,   (2,3),  None   ],
            [   None,   None,   None,   None,   None   ],
            [   (2,3),  None,   None,   None,   None   ],
            [   None,   None,   (3,2),  None,   None   ],
            [   None,   None,   None,   None,   None   ],
        ]
    """
    return [
        (
            '79053d41-34a2-4f09-8899-652681e2a157',
            [
                [   (1,1)   ],
            ],
        ),
        (
            'babbd34e-d5c4-490a-ae34-bd2bdde03f6f',
            [
                [   (1,1),  (1,1)   ],
            ],
        ),
        (
            '7156e4b0-eea7-48a7-b5da-aa1fa1720570',
            [
                [   (1,1)   ],
                [   (1,1)   ],
            ],
        ),
        (
            '2d76fc61-58b4-4003-b27f-d152b4578725',
            [
                [   (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            '20e35112-4b69-48e7-90b9-4e095e42bbd7',
            [
                [   (1,1)   ],
                [   (1,1)   ],
                [   (1,1)   ],
            ],
        ),
        (
            'edeab5bc-29b7-405d-95a1-9567f165eb1b',
            [
                [   (1,1),  (1,1)   ],
                [   (2,1),  None    ],
            ],
        ),
        (
            '13ab3b2d-10ff-4ba7-92bb-370759348883',
            [
                [   (1,2),  (1,2)   ],
                [   None,   None    ],
                [   (2,3),  None    ],
                [   None,   None    ],
                [   None,   None    ],
            ],
        ),
        (
            '01d3e3eb-d872-498f-9914-732126469d7a',
            [
                [   (1,1),  (1,1)   ],
                [   (2,2),  None    ],
                [   None,   None    ],
            ],
        ),
        (
            '3f4de4a0-07ea-4ba5-8f8f-1523aec9b0f6',
            [
                [   (2,1),  None    ],
                [   (1,1),  (1,1)   ],
            ],
        ),
        (
            'a1803db3-cfc6-4952-89ab-6ea69d79ebd0',
            [
                [   (2,3),  None    ],
                [   None,   None    ],
                [   None,   None    ],
                [   (1,2),  (1,2)   ],
                [   None,   None    ],
            ],
        ),
        (
            '4819269d-a9fe-4554-b55d-edee84f8496a',
            [
                [   (2,2),  None    ],
                [   None,   None    ],
                [   (1,1),  (1,1)   ],
            ],
        ),
        (
            '7a208ea3-26b1-4e2a-8df9-104ab72ab46a',
            [
                [   (1,1),  (1,2)   ],
                [   (1,1),  None    ],
            ],
        ),
        (
            '198e2b09-ba66-453b-ad15-fbcac9ac9270',
            [
                [   (2,1),  None,   (3,2),  None,   None    ],
                [   (2,1),  None,   None,   None,   None    ],
            ],
        ),
        (
            'a38cac06-475a-431f-9b8c-c231b9cddcd6',
            [
                [   (1,1),  (2,2),  None    ],
                [   (1,1),  None,   None    ],
            ],
        ),
        (
            'ea90e905-f942-4f89-9782-6c81e9c219c2',
            [
                [   (1,2),  (1,1)   ],
                [   None,   (1,1)   ],
            ],
        ),
        (
            '48d26ed3-9afc-4544-82d9-82960d62edf6',
            [
                [   (5,2),  None,   None,   None,   None,   (4,1),  None,   None,   None    ],
                [   None,   None,   None,   None,   None,   (4,1),  None,   None,   None    ],
            ],
        ),
        (
            '37008be5-acae-409e-a1aa-675594ac27b6',
            [
                [   (4,2),  None,   None,   None,   (3,1),  None,   None    ],
                [   None,   None,   None,   None,   (3,1),  None,   None    ],
            ],
        ),
        (
            '796c0b95-4134-46a7-8f9b-e481cd03e711',
            [
                [   (3,2),  None,   None,   (2,1),  None    ],
                [   None,   None,   None,   (2,1),  None    ],
            ],
        ),
        (
            'bc5f0b98-ce05-4a99-a609-37d80ce2a68a',
            [
                [   (2,2),  None,   (1,1)   ],
                [   None,   None,   (1,1)   ],
            ],
        ),
        (
            '02bff2e2-3807-4baf-8bc4-232a657569d4',
            [
                [   (1,1),  (1,1)   ],
                [   (1,1),  (1,1)   ],
            ],
        ),
        (
            '21da4cb3-b616-4bc2-b70d-174d029901a0',
            [
                [   (3,1),  None,   None,   (2,1),  None   ],
                [   (2,1),  None,   (3,1),  None,   None   ],
            ],
        ),
        (
            '9b98235f-ddab-4afd-a9f4-9694fc4a7ed2',
            [
                [   (2,1),  None,   (1,1)   ],
                [   (1,1),  (2,1),  None    ],
            ],
        ),
        (
            '10069c06-9dbf-41b4-ae22-46d6d62a130e',
            [
                [   (2,1),  None,   (3,1),  None,   None   ],
                [   (3,1),  None,   None,   (2,1),  None   ],
            ],
        ),
        (
            'acdfea46-b5c5-465a-b074-3ca7f7bdf8ab',
            [
                [   (1,1),  (2,1),  None    ],
                [   (2,1),  None,   (1,1)   ],
            ],
        ),
        (
            '78f5352e-5890-4a14-bbb8-172ee938eacd',
            [
                [   (1,2),  (1,3)   ],
                [   None,   None    ],
                [   (1,3),  None    ],
                [   None,   (1,2)   ],
                [   None,   None    ],
            ],
        ),
        (
            '049b71ed-88ab-46f9-8fa8-839bad919a2e',
            [
                [   (1,3),  (1,2)   ],
                [   None,   None    ],
                [   None,   (1,3)   ],
                [   (1,2),  None    ],
                [   None,   None    ],
            ],
        ),
        (
            'fefb8886-f4fc-4244-8b02-52d6c99f3c7c',
            [
                [   (3,2),  None,   None,   (2,3),  None   ],
                [   None,   None,   None,   None,   None   ],
                [   (2,3),  None,   None,   None,   None   ],
                [   None,   None,   (3,2),  None,   None   ],
                [   None,   None,   None,   None,   None   ],
            ],
        ),
        (
            'adf7f3fb-9c8a-4b7c-a758-0b4ff3065e8f',
            [
                [   None,   None,   None,   (2,3),  None,   None   ],
                [   (3,2),  None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None   ],
                [   None,   (2,3),  None,   (3,2),  None,   None   ],
                [   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None   ],
            ],
        ),
        (
            '7dc0caa3-9a09-49b4-b3d4-f7d67e93f37a',
            [
                [   (1,1),  (1,1),  (1,1)   ],
                [   (3,1),  None,   None    ],
            ],
        ),
        (
            '8227fd3b-e9d9-4b47-b4ab-8545aa2da432',
            [
                [   (1,2),  (1,2),  (1,2)   ],
                [   None,   None,   None    ],
                [   (3,3),  None,   None    ],
                [   None,   None,   None    ],
                [   None,   None,   None    ],
            ],
        ),
        (
            'ee1305d1-69a4-4b3a-9358-54897b33a651',
            [
                [   (1,1),  (1,1),  (1,1)   ],
                [   (3,2),  None,   None    ],
                [   None,   None,   None    ],
            ],
        ),
        (
            '75552e19-91e8-496b-a9cb-e60e36cf9956',
            [
                [   (3,1),  None,   None    ],
                [   (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            '0d9f0c05-8cbe-4d99-b27f-c73dcfdf4f34',
            [
                [   (3,3),  None,   None    ],
                [   None,   None,   None    ],
                [   None,   None,   None    ],
                [   (1,2),  (1,2),  (1,2)   ],
                [   None,   None,   None    ],
            ],
        ),
        (
            'dd1f6ffe-c2ad-44e8-9e8b-50d4f74ad37a',
            [
                [   (3,2),  None,   None    ],
                [   None,   None,   None    ],
                [   (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            '31873322-bc4a-44cf-9d64-504bf85b41ca',
            [
                [   (1,1),  (1,3)   ],
                [   (1,1),  None    ],
                [   (1,1),  None    ],
            ],
        ),
        (
            'a5e0bc76-be1c-431c-9640-966d4bd3fccc',
            [
                [   (2,1),  None,   (3,3),  None,   None    ],
                [   (2,1),  None,   None,   None,   None    ],
                [   (2,1),  None,   None,   None,   None    ],
            ],
        ),
        (
            '8e7afc55-dd9f-48af-8048-c14ccb1d9219',
            [
                [   (1,1),  (2,3),  None    ],
                [   (1,1),  None,   None    ],
                [   (1,1),  None,   None    ],
            ],
        ),
        (
            'e3bdc07f-0add-412b-b87a-211d1a6a288e',
            [
                [   (1,3),  (1,1)   ],
                [   None,   (1,1)   ],
                [   None,   (1,1)   ],
            ],
        ),
        (
            'a3d4875f-f213-44af-aeb7-5189f9cf000d',
            [
                [   (3,3),  None,   None,   (2,1),  None    ],
                [   None,   None,   None,   (2,1),  None    ],
                [   None,   None,   None,   (2,1),  None    ],
            ],
        ),
        (
            '8695db6f-80a4-4932-9070-2eab33d4f8fd',
            [
                [   (2,3),  None,   (1,1)   ],
                [   None,   None,   (1,1)   ],
                [   None,   None,   (1,1)   ],
            ],
        ),
        (
            '25e099ea-f874-4cd2-a86f-d248a99cb834',
            [
                [   (2,1),  None,   (2,1),  None,   (2,1),  None    ],
                [   (3,1),  None,   None,   (3,1),  None,   None    ],
            ],
        ),
        (
            '2d20121b-d81b-4843-a6e2-48b12610e707',
            [
                [   (3,1),  None,   None,   (3,1),  None,   None    ],
                [   (2,1),  None,   (2,1),  None,   (2,1),  None    ],
            ],
        ),
        (
            '1bb6e568-f69b-4187-85f8-447d9e1261cc',
            [
                [   (1,2),  (1,3)   ],
                [   None,   None    ],
                [   (1,2),  None    ],
                [   None,   (1,3)   ],
                [   (1,2),  None    ],
                [   None,   None    ],
            ],
        ),
        (
            '1bde33d6-45d0-48de-9a00-10fc32f0509e',
            [
                [   (1,3),  (1,2)   ],
                [   None,   None    ],
                [   None,   (1,2)   ],
                [   (1,3),  None    ],
                [   None,   (1,2)   ],
                [   None,   None    ],
            ],
        ),
        (
            '8c61d51e-8201-4be1-b0a1-b17c16bde175',
            [
                [   (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            '1ca611a4-329c-416a-b6fc-c69fe5c09240',
            [
                [   (1,4),  (1,3),  (1,4)   ],
                [   None,   None,   None    ],
                [   None,   None,   None    ],
                [   None,   (1,4),  None    ],
                [   (1,3),  None,   (1,3)   ],
                [   None,   None,   None    ],
                [   None,   None,   None    ],
            ],
        ),
        (
            '7eb400e8-8962-401a-a890-b9f72a36ca93',
            [
                [   (1,1),  (1,1)   ],
                [   (1,1),  (1,1)   ],
                [   (1,1),  (1,1)   ],
            ],
        ),
        (
            '7b410ff2-672c-4776-b65c-e92bbb5990af',
            [
                [   (4,1),  None,   None,   None,   (3,1),  None,   None   ],
                [   (3,1),  None,   None,   (4,1),  None,   None,   None   ],
                [   (4,1),  None,   None,   None,   (3,1),  None,   None   ],
            ],
        ),
        (
            'f7f04420-de86-4a06-a30d-3153c1529c17',
            [
                [   (2,2),  None,   (1,1)   ],
                [   None,   None,   (1,1)   ],
                [   (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            'c1267516-5169-4ed8-b606-0f740ac1ee13',
            [
                [   (1,1),  (2,2),  None    ],
                [   (1,1),  None,   None    ],
                [   (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            '5bad17b7-3605-422d-8dc4-ba2c16a68e3e',
            [
                [   (1,1),  (1,1),  (1,1)   ],
                [   (2,2),  None,   (1,1)   ],
                [   None,   None,   (1,1)   ],
            ],
        ),
        (
            '832659be-f72a-4520-a667-3c3cb0afe65e',
            [
                [   (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (2,2),  None    ],
                [   (1,1),  None,   None    ],
            ],
        ),
        (
            '7fd056f7-072c-4f35-ab7c-b8392e71901b',
            [
                [   (1,1),  (1,2),  (1,1)   ],
                [   (1,1),  None,   (1,1)   ],
                [   (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            '427b3d49-7b03-4163-9296-19c46d757d54',
            [
                [   (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (1,2),  (1,1)   ],
                [   (1,1),  None,   (1,1)   ],
            ],
        ),
        (
            '2cda05c9-3d8d-4b01-9a82-120bdbdc9991',
            [
                [   (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            '7fa56168-a36d-4200-b32a-0095802dd323',
            [
                [   (7,5),  None,   None,   None,   None,   None,   None,   (4,5),  None,   None,   None,   (5,7),  None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   (5,4),  None,   None,   None,   None,   (6,6),  None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   (5,4),  None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   (5,7),  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   (4,5),  None,   None,   None,   (7,5),  None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
                [   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None   ],
            ],
        ),
        (
            'd4f24591-b2ad-43bc-bc5b-d18da4ca8c55',
            [
                [   (1,1),  (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (2,2),  None,   (1,1)   ],
                [   (1,1),  None,   None,   (1,1)   ],
                [   (1,1),  (1,1),  (1,1),  (1,1)   ],
            ],
        ),
        (
            'b1452d73-0a96-4c20-b889-790b8e71cbc1',
            [
                [   (1,1),  (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (1,1),  (1,1),  (1,1)   ],
                [   (1,1),  (1,1),  (1,1),  (1,1)   ],
            ],
        ),
    ]



def GetDoublePages() -> List[Tuple[str, List[List[Optional[Tuple[int, int]]]]]]:
    """
    Get double page layouts.
    See GetSinglePages.
    """
    return [
        (
            'cece3329-05d3-4847-8d9d-1966cabd4d1c',
            [
                [   (1,1)   ],
            ],
        ),
        (
            'dde3bdc0-652e-4ec8-a695-e4223a71c129',
            [
                [   (2,1),  None,   (5,1),  None,   None,   None,   None    ],
            ],
        ),
        (
            '85dc4f2b-4b18-48cb-88e7-2b2ca7057255',
            [
                [   (5,1),  None,   None,   None,   None,   (2,1),  None    ],
            ],
        ),
        (
            'aaace444-5d52-4378-bf07-2b82d6502a71',
            [
                [   (2,1),  None,   (5,2),  None,   None,   None,   None    ],
                [   (2,1),  None,   None,   None,   None,   None,   None    ],
            ],
        ),
        (
            '5e8a43bd-4581-45ed-9048-903d7875f6d6',
            [
                [   (5,2),  None,   None,   None,   None,   (2,1),  None    ],
                [   None,   None,   None,   None,   None,   (2,1),  None    ],
            ],
        ),
        (
            'af8ec509-feb9-4216-8dcf-293dabdcc2d3',
            [
                [   (2,1),  None,  (5,1),  None,   None,   None,   None,   (2,1),   None    ],
            ],
        ),
        (
            '9349792d-c04c-4627-86bd-fd92bf1691fd',
            [
                [   (5,2),  None,   None,   None,   None,   (1,1),  (1,1)   ],
                [   None,   None,   None,   None,   None,   (2,1),  None    ],
            ],
        ),
        (
            '273100fb-557e-41ca-aaf3-f9e9d19fe241',
            [
                [   (2,1),  None,  (5,2),  None,   None,   None,   None,   (2,1),   None    ],
                [   (2,1),  None,  None,   None,   None,   None,   None,   (2,1),   None    ],
            ],
        ),
    ]
