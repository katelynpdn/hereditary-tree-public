import csv
import argparse

# TODO HINT Workshop 4
def arg_parser():
    parser = argparse.ArgumentParser(
        prog='Hereditary Tree',
        description='Finds probabilities of inheriting trait for every person in a family'
    )
    # Define the command-line arguments.
    parser.add_argument('i', type=str, help="csv file")
    return parser.parse_args()


# TODO IMPLEMENT. HINT: Workshop 4
def file_type_checker(extension):
    return (extension == "csv")


def main():
    # Parse the command-line arguments.
    ARGS = arg_parser()

    people = load_data(ARGS.i)
    # print("people")
    # print(people)

    # Keep track of gene and trait probabilities for each person
    probabilities = dict()

    for person, data in people.items():

        '''
        TODO: iterate over the 'trait' value of 'data' to assign the 
            correct value in probabilities. 
        
            probabilities should be structured as such:
            probabilities = {
                "person": {
                    "gene": {
                        2: 1,
                        1: 1, 
                        0: 0
                    }, 
                    "trait": 1
                }, 
                "person2": ...
            }
        '''
        print("data['trait']")
        print(data['trait'])
        personDict = dict()
        if (data['trait'] == '1'):
            print("true")
            personDict["gene"] = {
                2: 1,
                1: 0, 
                0: 0
            }
        else:  #Trait is 0
            print("false")
            personDict["gene"] = {
                2: 0,
                1: 0, 
                0: 1
            }
        
        personDict["trait"] = data['trait']
        probabilities[person] = personDict

    # print("probabilities")
    # print(probabilities)
    
    # calculate_trait will determine the phenotype('trait') based on genotype
    calculate_trait(probabilities, people)

    # Print results
    # print("people")
    # print(people)
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            if field.capitalize() == "Trait":
                print(f"  {field.capitalize()}: {probabilities[person][field]}")
                continue
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")

# This method will determine the phenotype('trait') based on genotype
def calculate_trait(probabilities, people):
    for person, data in probabilities.items():
        # we only want to calculate the trait when it is set to None
        # print("Right now trait is ")
        # print(data['trait'])
        if data['trait'] == '':
            '''
            TODO: fetch the father and mother genotypes from the 'person' we're looking at
                    using the people dictionary. Then assign the appropriate value in the
                    probabilities dictionary using the trait_helper() function.
            '''
            father = people[person]["father"]
            fatherGenotype = int(people[father]['trait'])
            mother = people[person]["mother"]
            motherGenotype = int(people[mother]['trait'])
            # print("motherGenotype")
            # print(motherGenotype)
            # print("fatherGenotype")
            # print(fatherGenotype)

            data['trait'] = trait_helper(fatherGenotype, motherGenotype)["trait"]
            data['gene'] = trait_helper(fatherGenotype, motherGenotype)["gene"]
            # print("Updated trait to ")
            # print(data['trait'])

# Note: This method will only work for beginners part of the project.
# Here we just walk through the gene and check what genotype the parent has
# Since it is only 0 or 2 for the beginner case, we can just return true
# Whenever one of the values of the dictionary is 1
def parent_genotype(gene):
    for key, val in gene.items():
        if val == 1:
            return key

# calculates probability of a child having a trait given parent's trait & genotype information
# genes1, genes2 will be 0, 1, or 2
# TRAIT IS RECESSIVE
#returns to_return dictionary
def trait_helper(genes1, genes2):
    to_return = {
        "gene": {
            2: 0,
            1: 0,
            0: 0
        },
        "trait": 0
    }
    '''
    TODO: Given the two genotypes passed in to this function, 
            determine the correct possible genotypes and traits 
            to return. 

            For example, if we had an example_dict that we wanted
            to return, we would fill it with the possibility it could
            have 0, 1, or 2 of the alleles of interest by labelling it with
            example_dict['gene'][0] = ? ; example_dict['gene'][1] = ? ;
            example_dict['gene'][2] = ?. We could also determine the probability
            that it could inherit the trait and store it in example_dict['trait]
            with values such as 1, 0.5, 0.25, etc.
    '''
    # Possibiliites: AA & Aa, AA & aa, Aa & Aa, Aa & aa, 0 & 0
    if ((genes1 == 2 and genes2 == 1) or (genes1 == 1 and genes2 == 2)): #AA & Aa
        to_return['gene'][1] = .50
        to_return['gene'][2] = .50
    elif ((genes1 == 2 and genes2 == 0) or (genes1 == 0 and genes2 == 2)): #AA & aa
        to_return['gene'][1] = 1
    elif (genes1 == 1 and genes2 == 1): #Aa & Aa
        to_return['gene'][0] = .25
        to_return['gene'][1] = .50
        to_return['gene'][2] = .25
    elif ((genes1 == 1 and genes2 == 0) or (genes1 == 0 and genes2 == 1)): #Aa & aa
        to_return['gene'][0] = .50
        to_return['gene'][1] = .50
    elif (genes1 == 2 and genes2 == 2): #AA and AA
        to_return['gene'][2] = 1
    else: #aa & aa
        to_return['gene'][0] = 1
    
    to_return['trait'] = (to_return['gene'][2])
    # print("to_return")
    # print(to_return)
    return to_return



def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data2 = dict()
            # TODO: load data from each row into the dictionary data here
            data2['mother'] = row['mother']
            data2['father'] = row['father']
            data2['trait'] = row['trait']
            data[row['name']] = data2
    return data

# runs when we call the python file
if __name__ == "__main__":
    main()
