def printArray(x):
	print("{", end = "")
	for a in range(len(x)-1):
		print("\"" + x[a].replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n").replace("\t", "\\t") + "\", ", end = "")
	print("\"" + x[len(x)-1].replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n").replace("\t", "\\t") + "\"", end = "")
	print("};", end = "")

varC = ["def printArray(x):\n\tprint(\"{\", end = \"\")\n\tfor a in range(len(x)-1):\n\t\tprint(\"\\\"\" + x[a].replace(\"\\\\\", \"\\\\\\\\\").replace(\"\\\"\", \"\\\\\\\"\").replace(\"\\n\", \"\\\\n\").replace(\"\\t\", \"\\\\t\") + \"\\\", \", end = \"\")\n\tprint(\"\\\"\" + x[len(x)-1].replace(\"\\\\\", \"\\\\\\\\\").replace(\"\\\"\", \"\\\\\\\"\").replace(\"\\n\", \"\\\\n\").replace(\"\\t\", \"\\\\t\") + \"\\\"\", end = \"\")\n\tprint(\"};\", end = \"\")\n\nvarC = ", "\nvarP = ", "\n\nprint(varP[0], end=\"\")\nprintArray(varC)\nprint(varP[1], end=\"\")\nprintArray(varP)\nprint(varP[2], end=\"\")\n"]
varP = ["#include<iostream>\n\nusing namespace std;\n\nvoid printArray(string x[], int count);\n\nstring sanitizeString(string x);\n\nint main() {\n\tstring varC[] = ", "\n\tstring varP[] = ", "\n\n\tcout << varC[0];\n\tprintArray(varC, sizeof(varC)/sizeof(varC[0]));\n\tcout << varC[1];\n\tprintArray(varP, sizeof(varP)/sizeof(varP[0]));\n\tcout << varC[2];\n\n\treturn 0;\n}\n\nvoid printArray(string x[], int count) {\n\tcout << \"[\";\n\tfor (int i=0; i < count-1; i++) {\n\t\tcout << \"\\\"\" << sanitizeString(x[i]) << \"\\\"\" << \", \";\n\t}\n\n\tcout << \"\\\"\" << sanitizeString(x[count-1]) << \"\\\"\";\n\tcout << \"]\";\n}\n\nstring sanitizeString(string x) {\n\tfor (int i=0; i<x.length(); i++) {\n\t\tswitch(x[i]) {\n\t\t\tcase('\\\\'):\n\t\t\t\tx.replace(i, 1, \"\\\\\\\\\");\n\t\t\t\ti++;\n\t\t\t\tbreak;\n\t\t\tcase('\\\"'):\n\t\t\t\tx.replace(i, 1, \"\\\\\\\"\");\n\t\t\t\ti++;\n\t\t\t\tbreak;\n\t\t\tcase('\\n'):\n\t\t\t\tx.replace(i, 1, \"\\\\n\");\n\t\t\t\ti++;\n\t\t\t\tbreak;\n\t\t\tcase('\\t'):\n\t\t\t\tx.replace(i, 1, \"\\\\t\");\n\t\t\t\ti++;\n\t\t\t\tbreak;\n\t\t}\n\t}\n\n\treturn x;\n}\n"]

print(varP[0], end="")
printArray(varC)
print(varP[1], end="")
printArray(varP)
print(varP[2], end="")
