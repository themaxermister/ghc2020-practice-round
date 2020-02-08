import os

def process(max, menu, menu_length):
    ordered_dict = {}
    current_slices = 0;
    for slice_type in reversed(range(menu_length)):
        next_count = current_slices + menu[slice_type]
        if next_count <= max:
            ordered_dict.update({slice_type : menu[slice_type]})
            current_slices = next_count
    
    return ordered_dict, current_slices

def outputFile(results, originfile):
    if not os.path.exists("submission"):
        os.mkdir("submission")
    mainFolder = ""
    newName = ("submission/results_%s" % (originfile))
    with open(newName, 'w') as the_file:
        the_file.write("%s\n" % (str(len(results))))
        values = ' '.join(reversed([str(elem) for elem in list(results.keys())]))
        the_file.write(values)

    print("Successful! File is located at %s" % (newName))
    print("No. of pizza types:", len(results))
    print("Pizza Type List:", values)

def main():
    totalPoints = 0
    while True:
        target_file = ""
        max_slices = 0
        no_type = 0
        type_menu = []
        target_file = input("Filepath: ")
        filename = os.path.basename(target_file)
        if target_file == "clear":
            totalPoints = 0
            print("Total points is 0.\n")
        elif target_file == "exit":
            exit()
        else: 
            try:
                openfile = open(target_file,"r")
                filetext = openfile.readlines()
                openfile.close()

                for index, line in enumerate(filetext):
                    if index == 0:
                        first = (line.replace("\n", "")).split(" ")
                        max_slices = int(first[0])
                        no_type = int(first[1])

                    else:
                        type_list = (line.replace("\n", "")).split(" ")
                        type_menu += [int(i) for i in type_list]

                if len(type_menu) == no_type:
                    # Process
                    results, newPoints = process(max_slices, type_menu ,no_type)
                    outputFile(results, filename)
                    totalPoints += newPoints
                    print("New Points:", newPoints, "/", max_slices, "\n")
                    print("Current Total Points:", totalPoints)

                else:
                    print('ERROR: Menu is incomplete.\n')

            except FileNotFoundError as error:
                print('ERROR: File does not exist.\n')

main()