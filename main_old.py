import os
import copy

def process(base, max, menu, menu_length):
    results = {}
    current_slices = base;
    for slice_type in reversed(range(menu_length)):
        next_count = current_slices + menu[slice_type]
        if next_count <= max:
            results.update({slice_type : menu[slice_type]})
            current_slices = next_count
    
    return results, current_slices

def outputFile(results, originfile):
    if not os.path.exists("submission"):
        os.mkdir("submission")
    mainFolder = ""
    newName = ("submission/results_%s.out" % (originfile))
    with open(newName, 'w') as the_file:
        the_file.write("%s\n" % (str(len(results))))
        values = ' '.join(reversed([str(elem) for elem in list(results.keys())]))
        the_file.write(values)

    print("Successful! File is located at %s" % (newName))
    print("No. of pizza types:", len(results))
    #print("Pizza Type List:", values)

def main():
    totalPoints = 0
    while True:
        target_file = ""
        max_slices = 0
        no_type = 0
        type_menu = []
        target_file = input("Filepath: ")
        filename = os.path.basename(target_file).split(".")[0]
        base = 0
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
                    base = type_menu[-1]
                    currentPoints = 0
                    for entry in range(0, no_type-2):
                        current_menu = copy.deepcopy(type_menu)
                        current_menu[entry] = 0
                        results, newPoints = process(base, max_slices, current_menu[0:len(current_menu)-1], len(current_menu)-1)
                        if newPoints > currentPoints:
                            currentPoints = newPoints
                            outputFile(results, filename)
                            totalPoints += newPoints
                        else:
                            print("New Points: %d is lower than previous points: %d" % (newPoints, currentPoints))
                        
                    print("New Points:", newPoints, "/", max_slices, "\n")
                    print("Current Total Points:", totalPoints)

                else:
                    print('ERROR: Menu is incomplete.\n')

            except FileNotFoundError as error:
                print('ERROR: File does not exist.\n')

main()