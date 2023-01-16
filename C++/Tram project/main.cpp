/* Jimi Niemi
 *
 * Program reads a file with information about tramlines and stops.
 * Program can be used to inspect and modify lines and stops using different commands
 *
 * */

#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <set>

using namespace std;

//Splits a given string to many strings
//Returns a vector that has the strings
vector<string> split_a_string(string given_string, char delimiter)
{
    string s = given_string;
    vector<string> result;
    string str = "";

    for (auto character : s)
    {
        if(character == delimiter)
        {
            if (str.size() == 0)
            {
                cout << "Error: Invalid format in file." << endl;
                exit(EXIT_FAILURE);
            }
            else if (str.at(0) == '"' and str.at(str.size() - 1) != '"')
            {
                str += character;
            }
            else
            {
                if (str.at(0) == '"' and str.at(str.size() - 2) == '"')
                {
                    result.push_back(str);
                    str = "";
                }
                else
                {
                    result.push_back(str);
                    str = "";
                }
            }
        }
        else
        {
            str += character;
        }
    }

    result.push_back(str);

    //Erases quotation marks
    for (unsigned int i = 0; i < result.size(); ++i)
    {
        string str = "";

        for (char character : result.at(i))
        {
            if (character != '"')
            {
                str += character;
            }
        }
        result.at(i) = str;
    }

    return result;
}

//Adds line or a stop to database
//lines, map: tramway lines
//stops, map: tramway line stops
//line, string: line to be added to lines
//stop, string: stop to be added to stops
//distance, double: distance to be added to stops
//Returns the map "Lines"
map<string, map <string, double>> add_to_database(map<string, map<string, double>> &lines,
                                                  map<string, double> &stops, string line = "",
                                                  string stop = "", double distance = 0.0)
{
    stops.clear();

    if (lines.find(line) != lines.end())
    {
        lines.at(line).insert({stop, distance});
    }
    else
    {
        lines.insert({line, stops});
        lines.at(line).insert({stop, distance});
    }
    return lines;
}

//Takes map of the lines and name of stop as string
//Removes the given stop from all of the lines
void remove_stop(map <string, map<string, double>> &lines, string stop_name)
{
    for (auto line : lines)
    {
        for (auto stop : line.second)
        {
            if (stop.first == stop_name)
            {
                lines.at(line.first).erase(stop_name);
            }
        }
    }
    cout << "Stop was removed from all lines." << endl;
}

//Takes map of the lines and name of the line as string
//Adds the given line to the map
void addline(map <string, map<string, double>> &lines, string line_name)
{
    if (lines.find(line_name) != lines.end())
    {
        cout << "Error: Stop/line already exists." << endl;
    }

    else
    {
        map<string, double> stops;
        add_to_database(lines, stops, line_name);
        cout << "Line was added." << endl;
    }
}

//Takes map of theline, stop as string and distance as double
//Adds a stop to the given line
void add_stop(map<string, double> &line, string stop, double distance)
{
    if (line.find(stop) != line.end())
    {
        cout << "Error: Stop/line already exists" << endl;
    }
    else
    {
        for (auto it : line)
        {
            if (it.second == distance)
            {
                if (it.first != "")
                {
                    cout << "Error: Stop/line already exists" << endl;
                    return;
                }
                else
                {
                    line.erase(it.first);
                    line.insert({stop, distance});
                }
            }
        }
        line.insert({stop, distance});
        cout << "Stop was added." << endl;
    }
}

//Takes line and 2 stops
//Prints out the distance between the given stops
void calculate_distance(map <string, map<string, double>> lines, string line_name,
                        string stop1, string stop2)
{

    if (lines.find(line_name) == lines.end())
    {
        cout << "Error: Line could not be found." << endl;
    }
    else
    {
        if (lines.at(line_name).find(stop1) == lines.at(line_name).end()
                or lines.at(line_name).find(stop2) == lines.at(line_name).end())
        {
            cout << "Error: Stop could not be found." << endl;
        }
        else
        {
            double stop1_distance = lines.at(line_name).at(stop1);
            double stop2_distance = lines.at(line_name).at(stop2);
            double distance = 0.0;

            if (stop1_distance > stop2_distance)
            {
                distance = stop1_distance - stop2_distance;
            }
            else if (stop2_distance > stop1_distance)
            {
                distance = stop2_distance - stop1_distance;
            }
            else
            {
                distance = 0.0;
            }

            cout << "Distance between " << stop1 << " and "
                 << stop2 << " is " << distance << endl;
        }
    }
}

//Takes map of the lines and name of a stop as string
//Prints all lines that have the given stop
void print_lines_for_stop(map<string, map<string, double>> lines, string stop_name)
{
    cout << "Stop " << stop_name <<
            " can be found on the following lines: " << endl;

    for (auto line : lines)
    {
        if (lines.at(line.first).find(stop_name) != lines.at(line.first).end())
        {
            cout << " - " << line.first << endl;
        }
    }
}
//Takes map of the lines
//Prints all stops
void print_all_stops(map<string, map<string, double>> lines)
{
    set<string> stops;

    for (auto line : lines)
    {
        for (auto stop : lines.at(line.first))
        {
            stops.insert(stop.first);
        }
    }
    cout << "All stops in alphabetical order:" << endl;

    for (auto stop : stops)
    {
        cout << stop << endl;
    }
}

//Takes map of the line and name of the line as string
//Prints stops of a given line
void print_lines_with_stops(map<string, double> line, string line_name)
{
    cout << "Line " << line_name <<
            " goes through these stops in the order they are listed:" << endl;

    map<double, string> inverted_map;

    for (auto it : line)
    {
        inverted_map.insert({it.second, it.first});
    }

    for (auto stop : inverted_map)
    {
        if (stop.second != "")
        {
            cout << " - " << stop.second << " : " << stop.first << endl;
        }
    }
}

//Takes a map of the lines
//Prints the lines in alphabetical order
void print_lines(map<string, map<string, double>> lines)
{
    cout << "All tramlines in alphabetical order: " << endl;
    for (auto it : lines)
    {
        cout << it.first << endl;
    }

}

//Takes map of the lines
//Asks the user for command then acts accordingly
void commands(map<string, map<string, double>> &lines)
{
    while(true)
    {

        cout << "tramway> ";
        string command;
        getline(cin, command);

        vector<string> parts_of_command = split_a_string(command, ' ');

        string primary = parts_of_command.at(0);
        string str = "";

        for (char character : primary)
        {
            str += toupper(character);
        }
        primary = str;

        if(primary == "QUIT")
        {
            exit(EXIT_SUCCESS);
        }
        else if(primary == "LINES")
        {
            print_lines(lines);
        }
        else if(primary == "LINE")
        {
            if (parts_of_command.size() == 1 or parts_of_command.at(1) == "")
            {
                cout << "Error: Invalid input." << endl;
            }
            else
            {
                string line_name;
                line_name = parts_of_command.at(1);

                if (lines.find(line_name) == lines.end())
                {
                    cout << "Error: Line could not be found." << endl;
                }
                else
                {
                print_lines_with_stops(lines.at(line_name), line_name);
                }
            }
        }
        else if (primary == "STOPS")
        {
            print_all_stops(lines);
        }
        else if (primary == "STOP")
        {
            if (parts_of_command.size() == 1 or parts_of_command.at(1) == "")
            {
                cout << "Error: Invalid input." << endl;
            }
            else
            {
                string stop_name;
                stop_name = parts_of_command.at(1);

                for (auto line : lines)
                {
                    if (lines.at(line.first).find(stop_name) != lines.at(line.first).end())
                    {
                        print_lines_for_stop(lines, stop_name);
                        commands(lines);
                    }
                }
                cout << "Error: Stop could not be found." << endl;                
            }
        }
        else if (primary == "DISTANCE")
        {
            if (parts_of_command.size() < 4)
            {
                cout << "Error: Invalid input." << endl;
            }
            else
            {
                string line_name = parts_of_command.at(1);
                string stop1 = parts_of_command.at(2);
                string stop2 = parts_of_command.at(3);
                calculate_distance(lines, line_name, stop1, stop2);
            }
        }
        else if (primary == "ADDLINE")
        {
            if (parts_of_command.size() < 2)
            {
                cout << "Error: Invalid input." << endl;
            }
            else
            {
                string line_name = parts_of_command.at(1);
                addline(lines, line_name);
            }
        }
        else if(primary == "ADDSTOP")
        {
            if (parts_of_command.size() < 4)
            {
                cout << "Error: Invalid input." << endl;
            }
            else
            {
                string line_name = parts_of_command.at(1);

                if (lines.find(line_name) == lines.end())
                {
                    cout << "Error: Line could not be found." << endl;
                }
                else
                {
                    string stop = parts_of_command.at(2);
                    double distance = stod(parts_of_command.at(3));

                    add_stop(lines.at(line_name), stop, distance);
                }
            }
        }
        else if (primary == "REMOVE")
        {
            if (parts_of_command.size() < 2)
            {
                cout << "Error: Invalid input." << endl;
            }
            else
            {
                string stop_name = parts_of_command.at(1);

                for (auto line : lines)
                {
                    if (line.second.find(stop_name) != line.second.end())
                    {
                        remove_stop(lines, stop_name);
                        commands(lines);
                    }
                }
                cout << "Error: Stop could not be found." << endl;
            }
        }
        else
        {
            cout << "Error: Invalid input." << endl;
        }
    }
}

//Asks for file name and tries to open the file
//stops: map of the stops, stop name and distance
//lines: map of the lines, line name and stops
//Return database with contents of the file
map<string, map<string, double>> input_file(map<string, double> stops, map<string, map<string, double>> lines)
{
    cout << "Give a name for input file: ";
    string file_name = "";
    cin >> file_name;

    ifstream file(file_name);

    if (not file)
    {
        cout << "Error: File could not be read." << endl;
        exit(EXIT_FAILURE);
    }

    else

    {
        string row;
        while(getline(file, row))
        {
            vector<string> parts = split_a_string(row, ';');

            if (parts.size() < 2 or parts.size() > 3 or parts.at(0) == "" or parts.at(1) == "")

            {
                cout << "Error: invalid format in file." << endl;
                exit(EXIT_FAILURE);
            }

            else

            {
                string line = "";
                string stop = "";
                line = parts.at(0);
                stop = parts.at(1);
                double distance = 0.0;

                if (parts.size() == 2 or parts.at(2) == "")
                {
                    distance = 0.0;
                }

                else
                {
                    distance = stod(parts.at(2));
                }

                add_to_database(lines, stops, line, stop, distance);

            }
        }

        file.close();

    }
    return lines;
}

// The most magnificent function in this whole program.
// Prints a RASSE
void print_rasse()
{
    std::cout <<
                 "=====//==================//===\n"
                 "  __<<__________________<<__   \n"
                 " | ____ ____ ____ ____ ____ |  \n"
                 " | |  | |  | |  | |  | |  | |  \n"
                 " |_|__|_|__|_|__|_|__|_|__|_|  \n"
                 ".|                  RASSE   |. \n"
                 ":|__________________________|: \n"
                 "___(o)(o)___(o)(o)___(o)(o)____\n"
                 "-------------------------------" << std::endl;
}

// Short and sweet main.
int main()
{
    map<string, double> stops;
    map<string, map<string, double>> lines;

    print_rasse();
    lines = input_file(stops, lines);
    cin.ignore();
    commands(lines);

    return EXIT_SUCCESS;
}
