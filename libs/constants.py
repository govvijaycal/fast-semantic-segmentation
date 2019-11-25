r"""Cityscapes train IDs to label IDs or label colors."""

# pylint: skip-file
# flake8: noqa

CITYSCAPES_LABEL_COLORS = [
    (128,  64, 128),        # road
    (244,  35, 231),        # sidewalk
    ( 69,  69,  69),        # building
    (102, 102, 156),        # wall
    (190, 153, 153),        # fence
    (153, 153, 153),        # pole
    (250, 170,  29),        # traffic light
    (219, 219,   0),        # traffic sign
    (106, 142,   3),        # vegetation
    (152, 250, 152),        # terrain
    ( 69, 129, 180),        # sky
    (219,  19,  60),        # person
    (255,   0,   0),        # rider
    (  0,   0, 142),        # car
    (  0,   0,  69),        # truck
    (  0,  60, 100),        # bus
    (  0,  79, 100),        # train
    (  0,   0, 230),        # motocycle
    (119,  10,   3)]        # bicycle

CITYSCAPES_LABEL_IDS = [
    (7,     ),              # 0
    (8,     ),              # 1
    (11,    ),              # 2
    (12,    ),              # 3
    (13,    ),              # 4
    (17,    ),              # 5
    (19,    ),              # 6
    (20,    ),              # 7
    (21,    ),              # 8
    (22,    ),              # 9
    (23,    ),              # 10
    (24,    ),              # 11
    (25,    ),              # 12
    (26,    ),              # 13
    (27,    ),              # 14
    (28,    ),              # 15
    (31,    ),              # 16
    (32,    ),              # 17
    (33,    ),              # 18
]

CARLA_LABEL_COLORS = [
    (0, 0, 0),         # None
    (70, 70, 70),      # Buildings
    (190, 153, 153),   # Fences
    (72, 0, 90),       # Other
    (220, 20, 60),     # Pedestrians
    (153, 153, 153),   # Poles
    (157, 234, 50),    # RoadLines
    (128, 64, 128),    # Roads
    (244, 35, 232),    # Sidewalks
    (107, 142, 35),    # Vegetation
    (0, 0, 255),      # Vehicles
    (102, 102, 156),  # Walls
    (220, 220, 0)     # TrafficSigns
]

CARLA_LABEL_IDS = [
    (0,     ),            
    (1,     ),            
    (2,    ),             
    (3,    ),             
    (4,    ),             
    (5,    ),             
    (6,    ),             
    (7,    ),             
    (8,    ),             
    (9,    ),             
    (10,    ),            
    (11,    ),             
    (12,    ),              
]