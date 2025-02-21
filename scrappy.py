import customtkinter
from customtkinter import *


#Window Settings
root = CTk()
root.title("Scrappy")
root.iconbitmap('C:/Users/GameBoi/PycharmProjects/Scrappy 2.0/imgs/recycler.ico')
root.geometry("1000x500")
customtkinter.set_appearance_mode('dark')


# Frames
frame = CTkFrame(master=root, height=500, width=1000)
frame.grid(row=0, column=1)


# Button Group 1
def comps():
    trash = CTkButton(frame, text="Tech Trash")
    trash.place(relx=0.3, rely=0.2, anchor=CENTER)
    laptop = CTkButton(frame, text="Computer")
    laptop.place(relx=0.45, rely=0.2, anchor=CENTER)
    sheet = CTkButton(frame, text="Sheet Metal")
    sheet.place(relx=0.6, rely=0.2, anchor=CENTER)
    metal_blade = CTkButton(frame, text="Blade")
    metal_blade.place(relx=0.3, rely=0.3, anchor=CENTER)
    metal_pipe = CTkButton(frame, text="Metal Pipe")
    metal_pipe.place(relx=0.45, rely=0.3, anchor=CENTER)
    gears = CTkButton(frame, text="Gear")
    gears.place(relx=0.6, rely=0.3, anchor=CENTER)
    springs = CTkButton(frame, text="Spring")
    springs.place(relx=0.3, rely=0.4, anchor=CENTER)
    smg = CTkButton(frame, text="SMG Body")
    smg.place(relx=0.45, rely=0.4, anchor=CENTER)
    rfl = CTkButton(frame, text="Rifle Body")
    rfl.place(relx=0.6, rely=0.4, anchor=CENTER)
    fse = CTkButton(frame, text="Fuse")
    fse.place(relx=0.3, rely=0.5, anchor=CENTER)
    trp = CTkButton(frame, text="Tarp")
    trp.place(relx=0.45, rely=0.5, anchor=CENTER)
    cam = CTkButton(frame, text="Camera")
    cam.place(relx=0.6, rely=0.5, anchor=CENTER)
    rpe = CTkButton(frame, text="Rope")
    rpe.place(relx=0.3, rely=0.6, anchor=CENTER)
    semi = CTkButton(frame, text="Semi Body")
    semi.place(relx=0.45, rely=0.6, anchor=CENTER)
    kit = CTkButton(frame, text="Sewing Kit")
    kit.place(relx=0.6, rely=0.6, anchor=CENTER)
    tank = CTkButton(frame, text="Propane Tank")
    tank.place(relx=0.45, rely=0.7, anchor=CENTER)


#Button Group 2
def tools():
    pick = CTkButton(frame, text="Ice Pick")
    pick.place(relx=0.3, rely=0.2, anchor=CENTER)
    hammer = CTkButton(frame, text="Salvaged Hammer")
    hammer.place(relx=0.45, rely=0.2, anchor=CENTER)
    salvage = CTkButton(frame, text="Salvaged Axe")
    salvage.place(relx=0.6, rely=0.2, anchor=CENTER)
    hatchet = CTkButton(frame, text="Metal Hatchet")
    hatchet.place(relx=0.3, rely=0.3, anchor=CENTER)
    pickaxe = CTkButton(frame, text="Metal Pickaxe")
    pickaxe.place(relx=0.45, rely=0.3, anchor=CENTER)
    prim_pick = CTkButton(frame, text="Stone Pickaxe")
    prim_pick.place(relx=0.6, rely=0.3, anchor=CENTER)
    prim_axe = CTkButton(frame, text="Stone Axe")
    prim_axe.place(relx=0.3, rely=0.4, anchor=CENTER)
    jack = CTkButton(frame, text="Jackhammer")
    jack.place(relx=0.45, rely=0.4, anchor=CENTER)
    chain = CTkButton(frame, text="Chainsaw")
    chain.place(relx=0.6, rely=0.4, anchor=CENTER)
    shove = CTkButton(frame, text="Shovel")
    shove.place(relx=0.3, rely=0.5, anchor=CENTER)
    light = CTkButton(frame, text="Flashlight")
    light.place(relx=0.45, rely=0.5, anchor=CENTER)


#Button Group 3
def melees():
    swrd = CTkButton(frame, text="Sword")
    swrd.place(relx=0.3, rely=0.2, anchor=CENTER)
    long = CTkButton(frame, text="Longsword")
    long.place(relx=0.45, rely=0.2, anchor=CENTER)
    salv = CTkButton(frame, text="Salvaged Cleaver")
    salv.place(relx=0.6, rely=0.2, anchor=CENTER)
    combat = CTkButton(frame, text="Combat Knife")
    combat.place(relx=0.3, rely=0.3, anchor=CENTER)
    bone = CTkButton(frame, text="Bone Club")
    bone.place(relx=0.45, rely=0.3, anchor=CENTER)
    knife = CTkButton(frame, text="Bone Knife")
    knife.place(relx=0.6, rely=0.3, anchor=CENTER)
    pad = CTkButton(frame, text="Paddle")
    pad.place(relx=0.3, rely=0.4, anchor=CENTER)
    mce = CTkButton(frame, text="Mace")
    mce.place(relx=0.45, rely=0.4, anchor=CENTER)
    skin = CTkButton(frame, text="Skinning Knife")
    skin.place(relx=0.6, rely=0.4, anchor=CENTER)
    sspear = CTkButton(frame, text="Stone Spear")
    sspear.place(relx=0.3, rely=0.5, anchor=CENTER)
    wspear = CTkButton(frame, text="Wood Spear")
    wspear.place(relx=0.45, rely=0.5, anchor=CENTER)


# Clear Frame
def comp():
    for item in frame.winfo_children():
        item.place_forget()
    comps()
def melee():
    for item in frame.winfo_children():
        item.place_forget()
    melees()
def tool():
    for item in frame.winfo_children():
        item.place_forget()
    tools()


# Tier Buttons
Comps = CTkButton(root, text="Comps", command=comp)
Comps.place(relx=0.3, anchor=N)
Melee = CTkButton(root, text="Melee", command=melee)
Melee.place(relx=0.45, anchor=N)
Tools = CTkButton(root, text="Tools", command=tools)
Tools.place(relx=0.60, anchor=N)


# Recycle Buttons
monument = CTkButton(root, text="Monument")
monument.place(relx=0.55, rely=0.82, anchor=S)
safe = CTkButton(root, text="Safe")
safe.place(relx=0.7, rely=0.82, anchor=S)


# Entry
entry = CTkEntry(root, width=200, height=5)
entry.place(relx=0.35, rely=0.82, anchor=S)


# Outputs
output = CTkTextbox(master=root, width=520, height=50)
output.place(relx=0.25, rely=0.85)

# Exit
def exiting():
    root.destroy()

stop = CTkButton(root, text="Exit", command=exit)
stop.place(relx=0.8, rely=0.9)


# Run Init
root.mainloop()