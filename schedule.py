import numpy as np


class Schedule:
    """Class Schedule.
    """
    def __init__(self, courseId, classId, teacherId):
        """Init
        Arguments:
            courseId: int, unique course id.
            classId: int, unique class id.
            teacherId: int, unique teacher id.
        """
        self.courseId = courseId
        self.classId = classId
        self.teacherId = teacherId

        self.roomId = 0
        self.weekDay = 0
        self.slot = 0

    def random_init(self, roomRange):
        """random init.

        Arguments:
            roomSize: int, number of classrooms.
        """
        self.roomId = np.random.randint(1, roomRange + 1, 1)[0]
        self.weekDay = np.random.randint(1, 6, 1)[0]
        self.slot = np.random.randint(1, 6, 1)[0]


def schedule_cost(population, elite):
    """calculate conflict of class schedules.

    Arguments:
        population: List, population of class schedules.
        elite: int, number of best result.

    Returns:
        index of best result.
        best conflict score.
    """
    conflicts = []
    n = len(population[0])

    for p in population:
        conflict = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                # 硬约束条件3: 同一时间,一个教室只能上一门课程
                # if p[i].roomId == p[j].roomId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                #     conflict += 1

                # 硬约束条件1: 同一时间,一个班级只能上一门课程
                if p[i].classId == p[j].classId and p[i].courseId == p[j].courseId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # 硬约束条件2: 同一时间,一个教师只能上一门课程
                if p[i].teacherId == p[j].teacherId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # # check same course for one class in same day
                # if p[i].classId == p[j].classId and p[i].courseId == p[j].courseId and p[i].weekDay == p[j].weekDay:
                #     conflict += 1

                # todo 软约束条件1: 满足个别教师的特殊上课时间需求

                # todo 软约束条件2: 同一门课程尽量平均分散在一周里

                # todo 软约束条件3: 同一个教师的课不能排满一整天

                # todo 软约束条件4: 同一个教师的课不能排满一整天(师生都很累)

        conflicts.append(conflict)

    index = np.array(conflicts).argsort()

    return index[: elite], conflicts[index[0]]
