components = 0
scrap = 0
high_quality_metal = 0
metal_frags = 0
cloth = 0
rope = 0
selections = 0
tech_trash = 0
wood = 0
stone = 0
blade = 0
gears = 0
bones = 0


# Materials
Items = None
Resources = None
Armors = None
M_Fragments = None


# Frames
def clear_output():
    global scrap, high_quality_metal, metal_frags, components, rope, cloth, selections
    scrap, tech_trash, wood, stone, blade, bones, gears = 0



def tech_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Tech Trash"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 20
    high_quality_metal = 1
    metal_frags = 45


def computer_btn():
    global components, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    selections = 3
    Items = "Targeting Computer"
    Resources = "Tech Trash"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    components = 3
    high_quality_metal = 1
    metal_frags = 50


def sheet_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    selections = 1
    Items = "Sheet Metal"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    scrap = 8
    high_quality_metal = 1
    metal_frags = 100


def pipe_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Metal Pipe"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 5
    high_quality_metal = 1
    metal_frags = 0


def blade_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Metal Blade"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 2
    high_quality_metal = 0
    metal_frags = 15


def gear_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Gears"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 10
    high_quality_metal = 1
    metal_frags = 13


def spring_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Spring"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 10
    high_quality_metal = 1
    metal_frags = 0


def road_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Road Sign"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 25
    high_quality_metal = 1
    metal_frags = 0


def smg_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "SMG Body"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 15
    high_quality_metal = 2
    metal_frags = 0


def rifle_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Rifle Body"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 25
    high_quality_metal = 2
    metal_frags = 0


def sewing_btn():
    global rope, cloth, selections, Resources, Armors, Items
    Items = "Sewing Kit"
    Resources = "Rope"
    Armors = "Cloth"
    selections = 2
    rope = 2
    cloth = 10


def tarp_btn():
    global cloth, selections, Resources, Items
    Items = "Tarp"
    Resources = "Cloth"
    selections = 2
    cloth = 50

def ropes():
    global cloth, selections, Resources, Items
    Items = "Rope"
    Resources = "Cloth"
    selections = 2
    cloth = 15

def propane_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Propane Tank"
    Resources = "Scrap"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 1
    high_quality_metal = 0
    metal_frags = 50

def semi_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Semi Auto Body"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 15
    high_quality_metal = 2
    metal_frags = 75

def camera_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, components
    Items = "Camera"
    Resources = "Tech Trash"
    Armors = "High Quality Metal"
    selections = 4
    components = 2
    high_quality_metal = 2

def fuse_btn():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Fuse"
    Resources = "Scrap"
    Armors = "High Quality Metal"
    M_Fragments = "Metal Fragments"
    selections = 1
    scrap = 20
    high_quality_metal = 0
    metal_frags = 0


def pickaxe():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood
    Items = "Pickaxe"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    wood = 50
    metal_frags = 63

def hatchet():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    wood = 50
    metal_frags = 38

def icepick():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, blade
    Items = "Icepick"
    Resources = "Metal Blade"
    Armors = "Metal Pipe"
    blade = 3
    selections = 6

def salhat():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    selections = 5
    wood = 60
    metal_frags = 45

def salham():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, blade
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    selections = 5
    blade = 3

def stonepick():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood, stone
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    wood = 60
    metal_frags = 45

def stonehat():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood, stone
    Items = "Stone Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    wood = 100
    stone = 50

def jackie():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, blade
    Items = "Jackhammer"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    scrap = 30
    blade = 3

def chain():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, blade, gears
    Items = "Chainsaw"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    high_quality_metal = 3
    gears = 1
    blade = 3

def light():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Flashlight"
    M_Fragments = "Metal Fragments"
    metal_frags = 15

def sword():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    selections = 3
    metal_frags = 8

def longsword():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, blade
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    metal_frags = 50
    blade = 1

def cleaver():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    selections = 5
    metal_frags = 25

def comknife():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    selections = 5
    bones = 15

def boneclub():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    metal_frags = 15

def boneknife():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    metal_frags = 15

def paddle():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    metal_frags = 8
    wood = 100

def mace():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    metal_frags = 25
    wood = 50

def stonespear():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, stone
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    stone = 25

def woodspear():
    global scrap, high_quality_metal, metal_frags, selections, Resources, Armors, M_Fragments, Items, wood
    Items = "Hatchet"
    M_Fragments = "Metal Fragments"
    Armors = "Wood"
    selections = 5
    wood = 150