def minmeetingrooms( intervals):
    meeting_room = []
    for i in range(len(intervals)):
        for j in range(len(intervals[i])):
            print(intervals[j])

minmeetingrooms([[15, 20], [5, 10], [0,30]])