import os
import copy
import itertools

def getRepeatIndex(target, item_list):
    new_list = {}
    repeat_list = [i for i,d in enumerate(item_list) if d==target]

    for item in repeat_list:
        if item not in new_list.keys():
            return item
            
def process(max, menu):
    results = []
    current_slices = menu[0];
    results.append(current_slices)
    for index, slice_type in enumerate(menu):
        if index > 0:
            next_count = current_slices + slice_type
            if next_count > max:
                return results, current_slices
            else:
                results.append(slice_type)
                current_slices = next_count
            

def outputFile(results, originfile):
    if not os.path.exists("submission"):
        os.mkdir("submission")
    mainFolder = ""
    newName = ("submission/results_%s.out" % (originfile))
    with open(newName, 'w') as the_file:
        the_file.write("%s\n" % (str(len(results))))
        values = ' '.join([str(elem) for elem in list(results)])
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
                    best_results = []
                    best_slices = 0
                    for combo in set(itertools.permutations(type_menu)):
                        new_results, new_slices = process(max_slices, list(combo))
                        if new_slices > best_slices:
                            best_results = new_results
                            best_slices = new_slices
                    
                    pizza_list = []
                    for pizza_type in best_results:
                        pizza_list.append(getRepeatIndex(pizza_type, type_menu))

                    outputFile(sorted(pizza_list), filename)

                    print("Total Slices: %d" % (sum(best_results)))
                else:
                    print('ERROR: Menu is incomplete.\n')

            except FileNotFoundError as error:
                print('ERROR: File does not exist.\n')

main()