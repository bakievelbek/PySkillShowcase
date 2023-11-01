"""

SQL joins are essential for querying data from multiple tables. They define how to combine rows from two or
 more tables based on related columns between them.

"""

# INNER JOIN (or JOIN)
#     - Combines rows from two tables based on a related column.
#     - It fetches rows from both tables where there is a match.


"""

SELECT Project.ID, Project.Name, Device.ID
from Project
Inner join Device on Project.ID = Device.ProjectID

"""

"""
Result:

ID      Name                        Device.ID
8,      OSM Trial,                  0
1,      CyMon8 Debugging on PC,     1
2,      CyMon8 on rbglle0041,       3
5,      CyMon at PCP,               4
7,      Cooking Tryout,             5
0,      No Project,                 6
4,      Test_for_Berlin,            7
4,      Test_for_Berlin,            8
8,      OSM Trial,                  9
8,      OSM Trial,                  10

"""

# LEFT (OUTER) JOIN (or LEFT JOIN)
#
#     Returns all rows from the left table, and the matched rows from the right table.
#     Unmatched rows from the right table will have NULL.


"""

SELECT Project.ID, Project.Name, Device.ID
from Project
Left join Device on Project.ID = Device.ProjectID

"""

"""
Result:

ID      Name                        Device.ID
0,      No Project,                 6
1,      CyMon8 Debugging on PC,     1
2,      CyMon8 on rbglle0041,       3
3,      Tryout,                     <null>
4,      Test_for_Berlin,            7
4,      Test_for_Berlin,            8
5,      CyMon at PCP,               4
6,      "",                         <null>
7,      Cooking Tryout,             5
8,      OSM Trial,                  0
8,      OSM Trial,                  9
8,      OSM Trial,                  10

"""

# RIGHT (OUTER) JOIN (or RIGHT JOIN)

#     Similar to the LEFT JOIN but returns all rows from the right table.
#     Note: Not all databases support RIGHT JOIN, but you can achieve similar
#     results by reversing table positions in LEFT JOIN.


"""

SELECT Project.ID, Project.Name, Device.ID
from Project
RIGHT JOIN Device on Project.ID = Device.ProjectID

"""

"""
Result:

ID      Name                        Device.ID
8,      OSM Trial,                  0
1,      CyMon8 Debugging on PC,     1
2,      CyMon8 on rbglle0041,       3
5,      CyMon at PCP,               4
7,      Cooking Tryout,             5
0,      No Project,                 6
4,      Test_for_Berlin,            7
4,      Test_for_Berlin,            8
8,      OSM Trial,                  9
8,      OSM Trial,                  10

"""

# FULL (OUTER) JOIN

# Returns all rows when there is a match in one of the tables. Unmatched rows will have NULL values
# for every column of the table that lacks a match.


"""

SELECT Project.ID, Project.Name, Device.ID
from Project
FULL JOIN Device on Project.ID = Device.ProjectID

"""

"""
Result:

ID      Name                        Device.ID
0,      No Project,                 6
1,      CyMon8 Debugging on PC,     1
2,      CyMon8 on rbglle0041,       3
3,      Tryout,                     <null>
4,      Test_for_Berlin,            7
4,      Test_for_Berlin,            8
5,      CyMon at PCP,               4
6,      "",                         <null>
7,      Cooking Tryout,             5
8,      OSM Trial,                  0
8,      OSM Trial,                  9
8,      OSM Trial,                  10

"""

# SELF JOIN

# Useful to represent a tree hierarchy
# A self join is a regular join but involves joining a table with itself.
# Useful for finding related data within the same table.

"""

SELECT dc1.ID as ParentID, dc1.Name as Parent,
       dc2.ID as ChildID, dc2.Name as Child

FROM DevClass dc1
JOIN DevClass dc2 on dc1.ID = dc2.Parent
Order by
    dc1.ID
    
"""

"""
Result:

ParentID        Parent          ChildID         Child
0,              CyMon,          1,              CyMon8_Dev
0,              CyMon,          3,              FAEM SM
0,              CyMon,          6,              FAEM
0,              CyMon,          10,             Cooking
0,              CyMon,          16,             Fridge
0,              CyMon,          19,             MT_PLUS
0,              CyMon,          20,             MT_PLUS_2
1,              CyMon8_Dev,     2,              CyMon8_Washer
3,              FAEM SM,        4,              ES900
3,              FAEM SM,        5,              ES600
3,              FAEM SM,        14,             EOX6021
4,              ES900,          18,             ES900 High
6,              FAEM,           7,              TI900
6,              FAEM,           8,              TE300
6,              FAEM,           9,              ES400
10,             Cooking,        11,             EOX6021
11,             EOX6021,        12,             Siemens
12,             Siemens,        13,             AV3
15,             SBS,            15,             SBS
16,             Fridge,         17,             SBS


"""

# CROSS JOIN

# In SQL returns the Cartesian product of the two tables, which means that it returns every combination of rows
# from the two tables.
# Useful when you want to see all combinations of queried items

"""

SELECT Project.Name as ProjectName, Device.name as DeviceName
FROM Project
CROSS JOIN Device

"""


"""
Result:

ProjectName                     DeviceName
No Project,                     No 9
No Project,                     Debugging on PC
No Project,                     Debugging on rbglle0041
No Project,                     ES900 Tim
No Project,                     Herd 1
No Project,                     Herd 2
No Project,                     Test WM
No Project,                     WaschMachine
No Project,                     MT_Plus_0001
No Project,                     MT_Plus_0002
CyMon8 Debugging on PC,         No 9
CyMon8 Debugging on PC,         Debugging on PC
CyMon8 Debugging on PC,         Debugging on rbglle0041
CyMon8 Debugging on PC,         ES900 Tim
CyMon8 Debugging on PC,         Herd 1
CyMon8 Debugging on PC,         Herd 2
CyMon8 Debugging on PC,         Test WM
CyMon8 Debugging on PC,         WaschMachine
CyMon8 Debugging on PC,         MT_Plus_0001
CyMon8 Debugging on PC,         MT_Plus_0002
CyMon8 on rbglle0041,           No 9
CyMon8 on rbglle0041,           Debugging on PC
CyMon8 on rbglle0041,           Debugging on rbglle0041
CyMon8 on rbglle0041,           ES900 Tim
CyMon8 on rbglle0041,           Herd 1
CyMon8 on rbglle0041,           Herd 2
CyMon8 on rbglle0041,           Test WM
CyMon8 on rbglle0041,           WaschMachine
CyMon8 on rbglle0041,           MT_Plus_0001
CyMon8 on rbglle0041,           MT_Plus_0002
Tryout,                         No 9
Tryout,                         Debugging on PC
Tryout,                         Debugging on rbglle0041
Tryout,                         ES900 Tim
Tryout,                         Herd 1
Tryout,                         Herd 2
Tryout,                         Test WM
Tryout,                         WaschMachine
Tryout,                         MT_Plus_0001
Tryout,                         MT_Plus_0002
Test_for_Berlin,                No 9
Test_for_Berlin,                Debugging on PC
Test_for_Berlin,                Debugging on rbglle0041
Test_for_Berlin,                ES900 Tim
Test_for_Berlin,                Herd 1
Test_for_Berlin,                Herd 2
Test_for_Berlin,                Test WM
Test_for_Berlin,                WaschMachine
Test_for_Berlin,                MT_Plus_0001
Test_for_Berlin,                MT_Plus_0002
CyMon at PCP,                   No 9
CyMon at PCP,                   Debugging on PC
CyMon at PCP,                   Debugging on rbglle0041
CyMon at PCP,                   ES900 Tim
CyMon at PCP,                   Herd 1
CyMon at PCP,                   Herd 2
CyMon at PCP,                   Test WM
CyMon at PCP,                   WaschMachine
CyMon at PCP,                   MT_Plus_0001
CyMon at PCP,                   MT_Plus_0002
"",                             No 9
"",                             Debugging on PC
"",                             Debugging on rbglle0041
"",                             ES900 Tim
"",                             Herd 1
"",                             Herd 2
"",                             Test WM
"",                             WaschMachine
"",                             MT_Plus_0001
"",                             MT_Plus_0002
Cooking Tryout,                 No 9
Cooking Tryout,                 Debugging on PC
Cooking Tryout,                 Debugging on rbglle0041
Cooking Tryout,                 ES900 Tim
Cooking Tryout,                 Herd 1
Cooking Tryout,                 Herd 2
Cooking Tryout,                 Test WM
Cooking Tryout,                 WaschMachine
Cooking Tryout,                 MT_Plus_0001
Cooking Tryout,                 MT_Plus_0002
OSM Trial,                      No 9
OSM Trial,                      Debugging on PC
OSM Trial,                      Debugging on rbglle0041
OSM Trial,                      ES900 Tim
OSM Trial,                      Herd 1
OSM Trial,                      Herd 2
OSM Trial,                      Test WM
OSM Trial,                      WaschMachine
OSM Trial,                      MT_Plus_0001
OSM Trial,                      MT_Plus_0002


"""