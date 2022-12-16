bpm = [122, 136, 150, 123, 138, 157, 165, 142, 132, 148, 162, 146, 170,  187, 185, 158, 165, 182, 193, 167, 158, 167, 182, 169]
total = len(bpm)

half_way = int(total / 2)
first_half = bpm[:half_way]
second_half = bpm[half_way:]

first_avg = sum(first_half) / half_way
second_avg = sum(second_half) / half_way

print('First half average: ' + str(first_avg))
print('Second half average: ' + str(second_avg))

final_mins = bpm[2::4]
breaks = bpm[3::4]
print('During breaks: ' + str(breaks))
print('During final minutes: ' + str(final_mins))

max_index = bpm.index(max(bpm))
print('Recovery from maximim: ' + str(bpm[max_index:]))
