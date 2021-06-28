import prettytable 

from schedule import Schedule
from genetic import GeneticOptimize


def vis(schedule):
    """visualization Class Schedule.

    Arguments:
        schedule: List, Class Schedule
    """
    col_labels = ['week/slot', '1', '2', '3', '4', '5']
    table_vals = [[i + 1, '', '', '', '', ''] for i in range(5)]

    table = prettytable.PrettyTable(col_labels, hrules=prettytable.ALL)

    for s in schedule:
        weekDay = s.weekDay
        slot = s.slot
        text = 'course: {} \n class: {} \n room: {} \n teacher: {}'.format(s.courseId, s.classId, s.roomId, s.teacherId)
        table_vals[weekDay - 1][slot] = text

    for row in table_vals:
        table.add_row(row)

    print(table)


if __name__ == '__main__':
    schedules = []

    # add schedule
    schedules.append(Schedule("语文", "立言班", 11101))
    schedules.append(Schedule("语文", "立言班", 11101))
    schedules.append(Schedule("语文", "立言班", 11101))
    schedules.append(Schedule("语文", "立言班", 11101))
    schedules.append(Schedule("数学", "立言班", 11102))
    schedules.append(Schedule("数学", "立言班", 11102))
    schedules.append(Schedule("数学", "立言班", 11102))
    schedules.append(Schedule("数学", "立言班", 11102))
    schedules.append(Schedule("英语", "立言班", 11103))
    schedules.append(Schedule("英语", "立言班", 11103))
    schedules.append(Schedule("英语", "立言班", 11103))
    schedules.append(Schedule("英语", "立言班", 11103))
    schedules.append(Schedule("体育", "立言班", 11104))
    schedules.append(Schedule("体育", "立言班", 11104))
    schedules.append(Schedule("相声", "立言班", 11105))
    schedules.append(Schedule("相声", "立言班", 11105))
    schedules.append(Schedule("机器", "立言班", 11106))
    schedules.append(Schedule("机器", "立言班", 11106))
    schedules.append(Schedule("美术", "立言班", 11107))
    schedules.append(Schedule("美术", "立言班", 11107))
    schedules.append(Schedule("音乐", "立言班", 11108))
    schedules.append(Schedule("音乐", "立言班", 11108))
    schedules.append(Schedule("手工", "立言班", 11109))
    schedules.append(Schedule("手工", "立言班", 11109))

    schedules.append(Schedule("语文", "立德班", 11101))
    schedules.append(Schedule("语文", "立德班", 11101))
    schedules.append(Schedule("语文", "立德班", 11101))
    schedules.append(Schedule("语文", "立德班", 11101))
    schedules.append(Schedule("数学", "立德班", 11102))
    schedules.append(Schedule("数学", "立德班", 11102))
    schedules.append(Schedule("数学", "立德班", 11102))
    schedules.append(Schedule("数学", "立德班", 11102))
    schedules.append(Schedule("英语", "立德班", 11103))
    schedules.append(Schedule("英语", "立德班", 11103))
    schedules.append(Schedule("英语", "立德班", 11103))
    schedules.append(Schedule("英语", "立德班", 11103))
    schedules.append(Schedule("体育", "立德班", 11104))
    schedules.append(Schedule("体育", "立德班", 11104))
    schedules.append(Schedule("相声", "立德班", 11105))
    schedules.append(Schedule("相声", "立德班", 11105))
    schedules.append(Schedule("机器", "立德班", 11106))
    schedules.append(Schedule("机器", "立德班", 11106))
    schedules.append(Schedule("美术", "立德班", 11107))
    schedules.append(Schedule("美术", "立德班", 11107))
    schedules.append(Schedule("音乐", "立德班", 11108))
    schedules.append(Schedule("音乐", "立德班", 11108))
    schedules.append(Schedule("手工", "立德班", 11109))
    schedules.append(Schedule("手工", "立德班", 11109))

    schedules.append(Schedule("语文", "立行班", 11101))
    schedules.append(Schedule("语文", "立行班", 11101))
    schedules.append(Schedule("语文", "立行班", 11101))
    schedules.append(Schedule("语文", "立行班", 11101))
    schedules.append(Schedule("数学", "立行班", 11102))
    schedules.append(Schedule("数学", "立行班", 11102))
    schedules.append(Schedule("数学", "立行班", 11102))
    schedules.append(Schedule("数学", "立行班", 11102))
    schedules.append(Schedule("英语", "立行班", 11103))
    schedules.append(Schedule("英语", "立行班", 11103))
    schedules.append(Schedule("英语", "立行班", 11103))
    schedules.append(Schedule("英语", "立行班", 11103))
    schedules.append(Schedule("体育", "立行班", 11104))
    schedules.append(Schedule("体育", "立行班", 11104))
    schedules.append(Schedule("相声", "立行班", 11105))
    schedules.append(Schedule("相声", "立行班", 11105))
    schedules.append(Schedule("机器", "立行班", 11106))
    schedules.append(Schedule("机器", "立行班", 11106))
    schedules.append(Schedule("美术", "立行班", 11107))
    schedules.append(Schedule("美术", "立行班", 11107))
    schedules.append(Schedule("音乐", "立行班", 11108))
    schedules.append(Schedule("音乐", "立行班", 11108))
    schedules.append(Schedule("手工", "立行班", 11109))
    schedules.append(Schedule("手工", "立行班", 11109))

    # optimization
    ga = GeneticOptimize(popsize=50, elite=10, maxiter=9999)
    res = ga.evolution(schedules, 3)

    # visualization
    vis_res = []
    for r in res:
        if r.classId == "立行班":
            vis_res.append(r)
    vis(vis_res)
