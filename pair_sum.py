'''find all distinct pairs of numbers from a list that sum up to a given number'''


def get_pairs(k, num_list):
    '''get pairs of numbers from num_list that sum up to k
    input: k = number that we are summing to, num_list = list of numbers
    output:  list of pairs of numbers from num_list that sum up to k'''

    out_list = []
    # loop over first half of num_list
    for num1 in num_list[ : len(num_list)/2]:
        # loop over each number in num_list to get sums
        for num2 in num_list:   
            # check to see if sum = k and that they are not the same number
            if (num1 + num2 == k) and (num1 != num2):
                out_list.append([num1, num2])

    return out_list


my_list = [3, 4, 5, 6, 7]
print get_pairs(10, my_list)
