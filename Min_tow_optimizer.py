import numpy as np
import re
import matplotlib.pyplot as plt

# global variables
tow_width = 5
tow_length = 50


def makeset(setline, fem_lines):
    j = 0
    set_eles = []
    while re.match('[+]', fem_lines[setline + j + 1]):
        j = j+1
        if re.search('THRU', fem_lines[setline + j]):
            [ele_1, ele_2] = [int(s) for s in fem_lines[setline + j].split() if s.isdigit()]
            set_eles.append(np.arange(ele_1, ele_2+1, 1))
        else:
            set_eles.append(np.array([int(s) for s in fem_lines[setline + j].split() if s.isdigit()]))

    return np.concatenate(set_eles)


def ele_props(ele_line):
    el_nums = [int(s) for s in ele_line.split() if s.isdigit()]
    elID = el_nums[0]
    elnodes = el_nums[2:6]
    return elID, elnodes


def node_props(nodeline):
    nodenum = float(nodeline[9:16])

    xstr = nodeline[24:31]
    if xstr.find('.') < xstr.find('-'):
        nodex = 0

    elif xstr.count('-') > 1:
        nodex = 0

    else:
        nodex = float(xstr)

    ystr = nodeline[32:39]
    if ystr.find('.') < ystr.find('-'):
        nodey = 0
        #print(nodeline)
    elif ystr.count('-') > 1:
        nodey = 0
        #print([2, nodeline])
    else:
        nodey = float(ystr)

    return nodenum, nodex, nodey


def build_eles(elelines):
    el_list = []
    for j in range(len(elelines)):
        el_list.append(ele_props(lines[elelines[j]]))
    return el_list


def build_nodes(nodelines):
    listnodes = []
    for j in range(len(nodelines)):
        listnodes.append(node_props(lines[nodelines[j]]))
    return listnodes


def ele_to_point(element):
    elenodes = element_list[element-1][1]

    n0 = node_list[elenodes[0]-1][1:3]
    n1 = node_list[elenodes[1]-1][1:3]
    n2 = node_list[elenodes[2]-1][1:3]
    n3 = node_list[elenodes[3]-1][1:3]

    return [(n0[0]+n1[0]+n2[0]+n3[0])/4, (n0[1]+n1[1]+n2[1]+n3[1])/4]


def ply_to_points(plyset):
    ply_xy = []
    for j in range(len(plyset)):
        if element_list[plyset[j]-1][0] is not None:
            ply_xy.append(ele_to_point(plyset[j]))
        else:
            ply_xy.append([None, None])

    return ply_xy


def ply_rotate(plypts, pangle):
    rotated_pts = []

    for j in range(len(plypts)):
        x = plypts[j][0]
        y = plypts[j][1]
        if x is not None:
            rotated_pts.append([x * np.cos(np.radians(pangle)) - y * np.sin(np.radians(pangle)),
                                y * np.cos(np.radians(pangle)) + x * np.sin(np.radians(pangle))])
        else:
            rotated_pts.append([x, y])

    return rotated_pts


def build_tows(plypts):

    plypts = np.array(plypts)
    plypts = np.reshape(plypts[plypts != np.array(None)], (-1, 2))

    ymin = min(plypts[:, 1])
    ymax = max(plypts[:, 1])

    n_tows = int(np.ceil((ymax-ymin)/tow_width))

    tow_table = []

    for j in range(n_tows):
        tow_eles = []
        for k in range(len(plypts)):
            if ymin + (j*tow_width) <= plypts[k, 1] < ymin + (tow_width * (j+1)):
                tow_eles.append([k, plypts[k]])

        tow_table.append(tow_eles)

    return tow_table


def tow_score(tow_ele_list):
    tow_xvals = []
    for j in range(len(tow_ele_list)):
        tow_xvals.append(tow_ele_list[j][1][0])


    minx = min(tow_xvals)
    maxx = max(tow_xvals)

    score = max(0, tow_length - abs(maxx-minx))

    return score


def lam_score():
    ply_scores = []
    for j in range(len(ply_table)):
        ply_penalty = 0
        xyply = ply_to_points(ply_table[j])
        rotply = ply_rotate(xyply, ply_angles[j])

        plt.scatter(*zip(*rotply))
        plt.show()

        tow_list = build_tows(rotply)
        for k in range(len(tow_list)):
            if len(tow_list[k]) > 0:
                ply_penalty = ply_penalty + tow_score(tow_list[k])
        ply_scores.append(ply_penalty)
    return ply_scores





# load the file to memory
fem_file = open("Boeing Window narrow_shuffling.8.fem")
lines = fem_file.readlines()

# initialize line collectors
ele_lines = []
node_lines = []
ply_angles = []
ply_names = []
set_lines = []
ply_table = []
stack = 0


# parse through the full .fem file and sort out which lines pertain to what
for i in range(len(lines)):
    femline = lines[i]

    if re.match('GRID', femline):
        node_lines.append(i)
    elif re.match('CQUAD4', femline):
        ele_lines.append(i)
    elif re.match('SET', femline):
        set_lines.append(i)
# catch only the laminate of interest
    elif re.match('DSHUFFLE', femline):
        stack = stack + 1
# directly save the ply angles, since its only 1 line
    elif re.match('PLY', femline) and stack == 1:
        ply_angles.append(float(femline[35:40]))
        ply_names.append(float(lines[i+1][12:16]))


# build the element sets for the plies of interest
i = 0
while i < len(set_lines):
    set_line = set_lines[i]
    if [int(s) for s in lines[set_line].split() if s.isdigit()][0] in ply_names:
        ply_table.append(makeset(set_line, lines))
    i = i+1

# build the elements, assign nodes
elist = build_eles(ele_lines)
element_list = []
for i in range(len(elist)):
    if (elist[i][0]-1) == len(element_list):
        element_list.append(elist[i])
    else:
        while elist[i][0] != len(element_list):
            element_list.append([None, [None, None, None, None]])

# build nodes, assign x/y coordinates
nlist = build_nodes(node_lines)
node_list = []
for i in range(len(nlist)):
    if (nlist[i][0]) == len(node_list)+1:
        node_list.append(nlist[i])
    else:
        while nlist[i][0] != len(node_list)+1:
            node_list.append([None, None, None])
        node_list.append(nlist[i])




print(lam_score())






























