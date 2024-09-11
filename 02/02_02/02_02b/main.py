''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

students_pet_cound_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

ITEM_AT_INDEX_THREE = students_pet_cound_list[3]
#print(students_pet_cound_list[100])
ITEM_THREE_FROM_BACK = students_pet_cound_list[-3]
print(ITEM_THREE_FROM_BACK)

NUM_OF_STUDENTS = len(students_pet_cound_list)
print(NUM_OF_STUDENTS)
SUM = 0

for INDIVIDUAL_PET_COUNT in students_pet_cound_list:
  SUM += INDIVIDUAL_PET_COUNT
print(SUM)

AVERAGE = SUM / len(students_pet_cound_list)
print(AVERAGE)

