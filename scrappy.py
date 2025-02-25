from customtkinter import *
import functions
import customtkinter

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
    trash = CTkButton(frame, text="Tech Trash", command=functions.tech_btn)
    trash.place(relx=0.3, rely=0.2, anchor=CENTER)
    laptop = CTkButton(frame, text="Computer", command=functions.computer_btn)
    laptop.place(relx=0.45, rely=0.2, anchor=CENTER)
    sheet = CTkButton(frame, text="Sheet Metal", command=functions.sheet_btn)
    sheet.place(relx=0.6, rely=0.2, anchor=CENTER)
    metal_blade = CTkButton(frame, text="Blade", command=functions.blade_btn)
    metal_blade.place(relx=0.3, rely=0.3, anchor=CENTER)
    metal_pipe = CTkButton(frame, text="Metal Pipe", command=functions.pipe_btn)
    metal_pipe.place(relx=0.45, rely=0.3, anchor=CENTER)
    gears = CTkButton(frame, text="Gear", command=functions.gear_btn)
    gears.place(relx=0.6, rely=0.3, anchor=CENTER)
    springs = CTkButton(frame, text="Spring", command=functions.spring_btn)
    springs.place(relx=0.3, rely=0.4, anchor=CENTER)
    smg = CTkButton(frame, text="SMG Body", command=functions.smg_btn)
    smg.place(relx=0.45, rely=0.4, anchor=CENTER)
    rfl = CTkButton(frame, text="Rifle Body", command=functions.rifle_btn())
    rfl.place(relx=0.6, rely=0.4, anchor=CENTER)
    fse = CTkButton(frame, text="Fuse", command=functions.fuse_btn)
    fse.place(relx=0.3, rely=0.5, anchor=CENTER)
    trp = CTkButton(frame, text="Tarp", command=functions.tarp_btn)
    trp.place(relx=0.45, rely=0.5, anchor=CENTER)
    cam = CTkButton(frame, text="Camera", command=functions.camera_btn)
    cam.place(relx=0.6, rely=0.5, anchor=CENTER)
    rpe = CTkButton(frame, text="Rope", command=functions.ropes)
    rpe.place(relx=0.3, rely=0.6, anchor=CENTER)
    semi = CTkButton(frame, text="Semi Body", command=functions.semi_btn)
    semi.place(relx=0.45, rely=0.6, anchor=CENTER)
    kit = CTkButton(frame, text="Sewing Kit", command=functions.sewing_btn)
    kit.place(relx=0.6, rely=0.6, anchor=CENTER)
    tank = CTkButton(frame, text="Propane Tank", command=functions.propane_btn)
    tank.place(relx=0.45, rely=0.7, anchor=CENTER)


#Button Group 2
def tools():
    pick = CTkButton(frame, text="Ice Pick", command=functions.icepick)
    pick.place(relx=0.3, rely=0.2, anchor=CENTER)
    hammer = CTkButton(frame, text="Salvaged Hammer", command=functions.salham)
    hammer.place(relx=0.45, rely=0.2, anchor=CENTER)
    salvage = CTkButton(frame, text="Salvaged Axe", command=functions.salhat)
    salvage.place(relx=0.6, rely=0.2, anchor=CENTER)
    hatchet = CTkButton(frame, text="Metal Hatchet", command=functions.hatchet)
    hatchet.place(relx=0.3, rely=0.3, anchor=CENTER)
    pickaxe = CTkButton(frame, text="Metal Pickaxe", command=functions.pickaxe)
    pickaxe.place(relx=0.45, rely=0.3, anchor=CENTER)
    prim_pick = CTkButton(frame, text="Stone Pickaxe", command=functions.stonepick)
    prim_pick.place(relx=0.6, rely=0.3, anchor=CENTER)
    prim_axe = CTkButton(frame, text="Stone Axe", command=functions.stonehat)
    prim_axe.place(relx=0.3, rely=0.4, anchor=CENTER)
    jack = CTkButton(frame, text="Jackhammer", command=functions.jackie)
    jack.place(relx=0.45, rely=0.4, anchor=CENTER)
    chain = CTkButton(frame, text="Chainsaw", command=functions.chain)
    chain.place(relx=0.6, rely=0.4, anchor=CENTER)
    light = CTkButton(frame, text="Flashlight", command=functions.light)
    light.place(relx=0.3, rely=0.5, anchor=CENTER)


#Button Group 3
def melees():
    swrd = CTkButton(frame, text="Sword", command=functions.sword)
    swrd.place(relx=0.3, rely=0.2, anchor=CENTER)
    long = CTkButton(frame, text="Longsword", command=functions.longsword)
    long.place(relx=0.45, rely=0.2, anchor=CENTER)
    salv = CTkButton(frame, text="Salvaged Cleaver", command=functions.cleaver)
    salv.place(relx=0.6, rely=0.2, anchor=CENTER)
    combat = CTkButton(frame, text="Combat Knife", command=functions.comknife)
    combat.place(relx=0.3, rely=0.3, anchor=CENTER)
    bone = CTkButton(frame, text="Bone Club", command=functions.boneclub)
    bone.place(relx=0.45, rely=0.3, anchor=CENTER)
    knife = CTkButton(frame, text="Bone Knife", command=functions.boneknife)
    knife.place(relx=0.6, rely=0.3, anchor=CENTER)
    pad = CTkButton(frame, text="Paddle", command=functions.paddle)
    pad.place(relx=0.3, rely=0.4, anchor=CENTER)
    mce = CTkButton(frame, text="Mace", command=functions.mace)
    mce.place(relx=0.45, rely=0.4, anchor=CENTER)
    sspear = CTkButton(frame, text="Stone Spear", command=functions.stonespear)
    sspear.place(relx=0.6, rely=0.4, anchor=CENTER)
    wspear = CTkButton(frame, text="Wood Spear", command=functions.woodspear)
    wspear.place(relx=0.3, rely=0.5, anchor=CENTER)


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
Comps.place(relx=0.3, rely=0.02, anchor=N)
Melee = CTkButton(root, text="Melee", command=melee)
Melee.place(relx=0.45, rely=0.02, anchor=N)
Tools = CTkButton(root, text="Tools", command=tools)
Tools.place(relx=0.6, rely=0.02, anchor=N)


# Entry
amount = CTkEntry(root, width=175, height=5, placeholder_text="   Amount of items to scrap.")
amount.place(relx=0.35, rely=0.82, anchor=S)


# Outputs
output = CTkTextbox(master=root, width=535, height=50)
output.place(relx=0.25, rely=0.85)


# How the Recyclers process the rates and user inputs
def recycle_safe():
    output.delete("0.0", END)
    output.insert("0.0", f"Please select a resource or component to recycle!")
    match functions.selections:
        case 1:
            rec_scrap = float(int(amount.get()) * functions.scrap * 0.8)
            rec_armor = float(int(amount.get()) * functions.high_quality_metal * 1)
            rec_frags = float(int(amount.get()) * functions.metal_frags * 0.8)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {amount.get()} {functions.Items} for {rec_scrap} {functions.Resources}, {rec_armor} {functions.Armors}, and {rec_frags} {functions.M_Fragments}!")
        case 2:
            rec_rope = float(int(amount.get()) * functions.rope * 0.8)
            rec_cloth = float(int(amount.get()) * functions.cloth * 1)
            output.delete("0.0", END)
            output.insert("0.0", f"You recycled {amount.get()} {functions.Items} for {rec_rope} and {rec_cloth} Cloth!")
        case 3:
            rec_comp = float(int(amount.get()) * functions.components * 0.8)
            rec_armor2 = float(int(amount.get()) * functions.high_quality_metal * 1)
            rec_frags2 = float(int(amount.get()) * functions.metal_frags * 0.8)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {amount.get()} {functions.Items} for {rec_comp} {functions.Resources}, {rec_armor2} {functions.Armors}, and {rec_frags2} {functions.M_Fragments}!")
        case 4:
            rec_trash = float(int(amount.get()) * functions.components * 0.8)
            rec_armor = float(int(amount.get()) * functions.high_quality_metal * 0.8)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {amount.get()} {functions.Items} for {rec_trash} {functions.Resources} and {rec_armor} {functions.Armors}!")
        case 5:
            rec_wood = float(int(amount.get()) * functions.wood * 0.8)
            rec_frags = float(int(amount.get()) * functions.metal_frags * 0.8)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {amount.get()} {functions.Items} for {rec_wood} {functions.M_Fragments} and {rec_frags} {functions.Armors}!")


        case ValueError:
            output.delete("0.0", END)
            output.insert("0.0", f"Please enter a valid amount of items to recycle!")


def recycle_monument():
    output.delete("0.0", END)
    output.insert("0.0", f"Please select a resource or component to recycle!")
    match functions.selections:
        case 1:
            rec_scrap1 = float(int(amount.get()) * functions.scrap * 1.2)
            rec_armor1 = float(int(amount.get()) * functions.high_quality_metal * 1)
            rec_frags1 = float(int(amount.get()) * functions.metal_frags * 1.2)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {str(amount.get())} {functions.Items} for {rec_scrap1} {functions.Resources}, {rec_armor1} {functions.Armors}, and {rec_frags1} {functions.M_Fragments}!")
        case 2:
            rec_rope1 = float(int(amount.get()) * functions.rope * 1.2)
            rec_cloth1 = float(int(amount.get()) * functions.cloth * 1.2)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {str(amount.get())} Tech Trash for {rec_rope1} Rope and {rec_cloth1} Cloth!")
        case 3:
            rec_comp = float(int(amount.get()) * functions.components * 1.2)
            rec_armor2 = float(int(amount.get()) * functions.high_quality_metal * 1)
            rec_frags2 = float(int(amount.get()) * functions.metal_frags * 1.2)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {str(amount.get())} {functions.Items} for {rec_comp} {functions.Resources}, {rec_armor2} {functions.Armors}, and {rec_frags2} {functions.M_Fragments}!")
        case 4:
            rec_trash = float(int(amount.get()) * functions.components * 1.2)
            rec_armor = float(int(amount.get()) * functions.high_quality_metal * 1.2)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {amount.get()} {functions.Items} for {rec_trash} {functions.Resources} and {rec_armor} {functions.Armors}!")
        case 5:
            rec_wood = float(int(amount.get()) * functions.wood * 1.2)
            rec_frags = float(int(amount.get()) * functions.metal_frags * 1.2)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {int(amount.get())} {functions.Items} for {rec_wood} {functions.M_Fragments} and {rec_frags} {functions.Armors}!")
        case 6:
            rec_blade = float(int(amount.get()) * functions.blade * 1.2)
            output.delete("0.0", END)
            output.insert("0.0",
                          f"You recycled {int(amount.get())} {functions.Items} for {rec_blade} {functions.M_Fragments}")

        case ValueError:
            output.delete("0.0", END)
            output.insert("0.0", f"Please enter a valid amount of items to recycle!")



# Recycle Buttons
monument = CTkButton(root, text="Recycle at Monument", command=recycle_monument)
monument.place(relx=0.55, rely=0.82, anchor=S)
safe = CTkButton(root, text="Recycle at Safezone", command=recycle_safe)
safe.place(relx=0.7, rely=0.82, anchor=S)


# Exit
def exiting():
    root.destroy()

stop = CTkButton(root, text="Exit", command=exit)
stop.place(relx=0.8, rely=0.9)


# Run Init
root.mainloop()