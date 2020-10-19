#include<iostream>

using namespace std;

void printArray(string x[], int count);

string sanitizeString(string x);

int main() {
	string varC[] = {"def printArray(x):\n\tprint(\"{\", end = \"\")\n\tfor a in range(len(x)-1):\n\t\tprint(\"\\\"\" + x[a].replace(\"\\\\\", \"\\\\\\\\\").replace(\"\\\"\", \"\\\\\\\"\").replace(\"\\n\", \"\\\\n\").replace(\"\\t\", \"\\\\t\") + \"\\\", \", end = \"\")\n\tprint(\"\\\"\" + x[len(x)-1].replace(\"\\\\\", \"\\\\\\\\\").replace(\"\\\"\", \"\\\\\\\"\").replace(\"\\n\", \"\\\\n\").replace(\"\\t\", \"\\\\t\") + \"\\\"\", end = \"\")\n\tprint(\"};\", end = \"\")\n\nvarC = ", "\nvarP = ", "\n\nprint(varP[0], end=\"\")\nprintArray(varC)\nprint(varP[1], end=\"\")\nprintArray(varP)\nprint(varP[2], end=\"\")\n"};
	string varP[] = {"#include<iostream>\n\nusing namespace std;\n\nvoid printArray(string x[], int count);\n\nstring sanitizeString(string x);\n\nint main() {\n\tstring varC[] = ", "\n\tstring varP[] = ", "\n\n\tcout << varC[0];\n\tprintArray(varC, sizeof(varC)/sizeof(varC[0]));\n\tcout << varC[1];\n\tprintArray(varP, sizeof(varP)/sizeof(varP[0]));\n\tcout << varC[2];\n\n\treturn 0;\n}\n\nvoid printArray(string x[], int count) {\n\tcout << \"[\";\n\tfor (int i=0; i < count-1; i++) {\n\t\tcout << \"\\\"\" << sanitizeString(x[i]) << \"\\\"\" << \", \";\n\t}\n\n\tcout << \"\\\"\" << sanitizeString(x[count-1]) << \"\\\"\";\n\tcout << \"]\";\n}\n\nstring sanitizeString(string x) {\n\tfor (int i=0; i<x.length(); i++) {\n\t\tswitch(x[i]) {\n\t\t\tcase('\\\\'):\n\t\t\t\tx.replace(i, 1, \"\\\\\\\\\");\n\t\t\t\ti++;\n\t\t\t\tbreak;\n\t\t\tcase('\\\"'):\n\t\t\t\tx.replace(i, 1, \"\\\\\\\"\");\n\t\t\t\ti++;\n\t\t\t\tbreak;\n\t\t\tcase('\\n'):\n\t\t\t\tx.replace(i, 1, \"\\\\n\");\n\t\t\t\ti++;\n\t\t\t\tbreak;\n\t\t\tcase('\\t'):\n\t\t\t\tx.replace(i, 1, \"\\\\t\");\n\t\t\t\ti++;\n\t\t\t\tbreak;\n\t\t}\n\t}\n\n\treturn x;\n}\n"};

	cout << varC[0];
	printArray(varC, sizeof(varC)/sizeof(varC[0]));
	cout << varC[1];
	printArray(varP, sizeof(varP)/sizeof(varP[0]));
	cout << varC[2];

	return 0;
}

void printArray(string x[], int count) {
	cout << "[";
	for (int i=0; i < count-1; i++) {
		cout << "\"" << sanitizeString(x[i]) << "\"" << ", ";
	}

	cout << "\"" << sanitizeString(x[count-1]) << "\"";
	cout << "]";
}

string sanitizeString(string x) {
	for (int i=0; i<x.length(); i++) {
		switch(x[i]) {
			case('\\'):
				x.replace(i, 1, "\\\\");
				i++;
				break;
			case('\"'):
				x.replace(i, 1, "\\\"");
				i++;
				break;
			case('\n'):
				x.replace(i, 1, "\\n");
				i++;
				break;
			case('\t'):
				x.replace(i, 1, "\\t");
				i++;
				break;
		}
	}

	return x;
}
