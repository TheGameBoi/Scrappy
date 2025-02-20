import customtkinter
from customtkinter import *

#Window Settings
root = CTk()
root.title("Scrappy")
root.iconbitmap('C:/Users/GameBoi/PycharmProjects/Scrappy 2.0/imgs/recycler.ico')
root.geometry("1020x520")
customtkinter.set_appearance_mode('dark')


# Frames
frame = CTkFrame(master=root, height=500, width=1000, corner_radius=10)
frame.grid(row=0, column=1, padx=10, pady=10)

# Button Group 1
def comps():
    trash = CTkButton(root, text="Tech Trash")
    trash.place(relx=0.3, rely=0.2, anchor=CENTER)
    laptop = CTkButton(root, text="Computer")
    laptop.place(relx=0.45, rely=0.2, anchor=CENTER)
    sheet = CTkButton(root, text="Sheet Metal")
    sheet.place(relx=0.6, rely=0.2, anchor=CENTER)
    metal_blade = CTkButton(root, text="Blade")
    metal_blade.place(relx=0.3, rely=0.3, anchor=CENTER)
    metal_pipe = CTkButton(root, text="Metal Pipe")
    metal_pipe.place(relx=0.45, rely=0.3, anchor=CENTER)
    gears = CTkButton(root, text="Gear")
    gears.place(relx=0.6, rely=0.3, anchor=CENTER)
    springs = CTkButton(root, text="Spring")
    springs.place(relx=0.3, rely=0.4, anchor=CENTER)
    smg = CTkButton(root, text="SMG Body")
    smg.place(relx=0.45, rely=0.4, anchor=CENTER)
    rfl = CTkButton(root, text="Rifle Body")
    rfl.place(relx=0.6, rely=0.4, anchor=CENTER)
    fse = CTkButton(root, text="Fuse")
    fse.place(relx=0.3, rely=0.5, anchor=CENTER)
    trp = CTkButton(root, text="Tarp")
    trp.place(relx=0.45, rely=0.5, anchor=CENTER)
    cam = CTkButton(root, text="Camera")
    cam.place(relx=0.6, rely=0.5, anchor=CENTER)
    rpe = CTkButton(root, text="Rope")
    rpe.place(relx=0.3, rely=0.6, anchor=CENTER)
    semi = CTkButton(root, text="Semi Body")
    semi.place(relx=0.45, rely=0.6, anchor=CENTER)
    kit = CTkButton(root, text="Sewing Kit")
    kit.place(relx=0.6, rely=0.6, anchor=CENTER)
    tank = CTkButton(root, text="Propane Tank")
    tank.place(relx=0.45, rely=0.7, anchor=CENTER)

#Button Group 2
def tools():
    pick = CTkButton(root, text="Ice Pick")
    pick.place(relx=0.3, rely=0.2, anchor=CENTER)
    hammer = CTkButton(root, text="Salvaged Hammer")
    hammer.place(relx=0.45, rely=0.2, anchor=CENTER)
    salvage = CTkButton(root, text="Salvaged Axe")
    salvage.place(relx=0.6, rely=0.2, anchor=CENTER)
    hatchet = CTkButton(root, text="Metal Hatchet")
    hatchet.place(relx=0.3, rely=0.3, anchor=CENTER)
    pickaxe = CTkButton(root, text="Metal Pickaxe")
    pickaxe.place(relx=0.45, rely=0.3, anchor=CENTER)
    prim_pick = CTkButton(root, text="Stone Pickaxe")
    prim_pick.place(relx=0.6, rely=0.3, anchor=CENTER)
    prim_axe = CTkButton(root, text="Stone Axe")
    prim_axe.place(relx=0.3, rely=0.4, anchor=CENTER)
    jack = CTkButton(root, text="Jackhammer")
    jack.place(relx=0.45, rely=0.4, anchor=CENTER)
    chain = CTkButton(root, text="Chainsaw")
    chain.place(relx=0.6, rely=0.4, anchor=CENTER)
    shove = CTkButton(root, text="Shovel")
    shove.place(relx=0.3, rely=0.5, anchor=CENTER)
    light = CTkButton(root, text="Flashlight")
    light.place(relx=0.45, rely=0.5, anchor=CENTER)

#Button Group 3
def melee():
    swrd = CTkButton(root, text="Sword")
    swrd.place(relx=0.3, rely=0.2, anchor=CENTER)
    long = CTkButton(root, text="Longsword")
    long.place(relx=0.45, rely=0.2, anchor=CENTER)
    salv = CTkButton(root, text="Salvaged Cleaver")
    salv.place(relx=0.6, rely=0.2, anchor=CENTER)
    combat = CTkButton(root, text="Combat Knife")
    combat.place(relx=0.3, rely=0.3, anchor=CENTER)
    bone = CTkButton(root, text="Bone Club")
    bone.place(relx=0.45, rely=0.3, anchor=CENTER)
    knife = CTkButton(root, text="Bone Knife")
    knife.place(relx=0.6, rely=0.3, anchor=CENTER)
    pad = CTkButton(root, text="Paddle")
    pad.place(relx=0.3, rely=0.4, anchor=CENTER)
    mce = CTkButton(root, text="Mace")
    mce.place(relx=0.6, rely=0.4, anchor=CENTER)
    skin = CTkButton(root, text="Skinning Knife")
    skin.place(relx=0.3, rely=0.5, anchor=CENTER)
    sspear = CTkButton(root, text="Stone Spear")
    sspear.place(relx=0.45, rely=0.5, anchor=CENTER)
    wspear = CTkButton(root, text="Wood Spear")
    wspear.place(relx=0.6, rely=0.5, anchor=CENTER)

# Tier Buttons
Comps = CTkButton(frame, text="Comps", command=comps)
Comps.place(relx=0.35, anchor=N)
Melee = CTkButton(frame, text="Melee", command=melee)
Melee.place(relx=0.50, anchor=N)
Tools = CTkButton(frame, text="Tools", command=tools)
Tools.place(relx=0.65, anchor=N)

# Exit
def exiting():
    root.destroy()

stop = CTkButton(root, text="Exit", command=exit)
stop.place(relx=0.8, rely=0.9)


# Run Init
root.mainloop()