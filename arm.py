class register():
    def __init__(self, name):
        self.name = name
        self.available = True

    def change_availability(self):
        self.available = not(self.available)


REGISTERS = ["R15",
             "R14",
             "R13",
             "R12",
             "R11",
             "R10",
             "R9",
             "R8",
             "R7",
             "R6",
             "R5",
             "R4",
             "R3",
             "R2",
             "R1",
             "R0"]

OPERATORS = ["+", "-", "*", "/", "%"]

TRUE_REGIS = []


def read_line(line):
    arm = ""
    sections = line.split(" ")

    for section in sections:
        if len(section) > 0:
            if section == "main":
                arm += "_start:\n"
            if section[-1] == ":":
                arm += section + "\n"
                arm += "stmfd sp!, {lr}" +"\n"

            if section == "+":
                r1 = REGISTERS.pop()
                r2 = REGISTERS.pop()
                arm += "MOV " + r2 + ", " + "#" + sections[sections.index(section)-1] + "\n"
                arm += "ADD " + r1 + ", " + r2 + ", " + "#" + sections[sections.index(section) + 1] + "\n"

            if section == "-":
                r1 = REGISTERS.pop()
                r2 = REGISTERS.pop()
                arm += "MOV " + r2 + ", " + "#" + sections[sections.index(section) - 1] + "\n"
                arm += "SUB " + r1 + ", " + "#" + ", " + "#" + sections[sections.index(section) + 1] + "\n"

            if section == "*":
                r1 = REGISTERS.pop()
                arm += "MUL " + r1 + ", " + "#" + sections[sections.index(section)-1] + ", " + "#" + sections[sections.index(section) + 1] + "\n"

            if section == "==":
                r1 = REGISTERS.pop()
                indi = sections[sections.index(section)-1].find("=")
                registro1 = sections[sections.index(section)-1][indi+1::]
                arm += "LDR " + r1 + ", " + "= " + registro1 + "\n"
                arm += "CMP " + r1 + ", " + "#" +sections[sections.index(section)+1] + "\n"
                arm += "BLT " + "true" + "\n"
                arm += "B " + "fin"+"\n"

            if section == ">":
                r1 = REGISTERS.pop()
                indi = sections[sections.index(section)-1].find("=")
                registro1 = sections[sections.index(section)-1][indi+1::]
                arm += "LDR " + r1 + ", " + "= " + registro1 + "\n"
                arm += "CMP " + r1 + ", " + "#" +sections[sections.index(section)+1] + "\n"
                arm += "BLT " + "true" + "\n"
                arm += "B " + "fin"+"\n"

            if section == "<":
                r1 = REGISTERS.pop()
                indi = sections[sections.index(section)-1].find("=")
                registro1 = sections[sections.index(section)-1][indi+1::]
                arm += "LDR " + r1 + ", " + "= " + registro1 + "\n"
                arm += "CMP " + r1 + ", " + "#" + sections[sections.index(section)+1] + "\n"
                arm += "BLT " + "true" + "\n"
                arm += "B " + "fin"+"\n"

    if sections[0] == "func":
        if "end" in sections[1]:
            pass

    return arm



def compose_arm(inte, scopes):
    inte = inte.split("\n")
    num = 15
    arm = ".text" + "\n" + ".align 2" + "\n" + ".global main" + "\n" + ".type main, %function\n"
    while num > 0:
        r = register("R" + str(num))
        TRUE_REGIS.append(r)
        num -= 1
    for line in inte:
        arm += read_line(line)
    arm += "MOV R0 , #0\nMOV R3 , #0\nldmfd sp!, {lr}" + "\n" + "bx lr" + "\n" + ".data" + "\n" + ".align 2"
    print(arm)