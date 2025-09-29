from typing import List
import heapq


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.tq = []
        self.curr_prios = {}
        self.task_user_mapping = {}

        for userId, taskId, priority in tasks:
            self.tq.append((-priority, -taskId, userId))
            self.curr_prios[taskId] = priority
            self.task_user_mapping[taskId] = userId

        heapq.heapify(self.tq)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.tq, (-priority, -taskId, userId))
        self.curr_prios[taskId] = priority
        self.task_user_mapping[taskId] = userId
        return None

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.tq, (-newPriority, -taskId, self.task_user_mapping[taskId]))
        self.curr_prios[taskId] = newPriority
        return None

    def rmv(self, taskId: int) -> None:
        # Lazy removal!!!
        if taskId in self.curr_prios:
            del self.curr_prios[taskId]
            del self.task_user_mapping[taskId]
        return None

    def execTop(self) -> int:
        if len(self.tq) == 0:
            return -1
        cur_prio, cur_task_id, cur_user_id = heapq.heappop(self.tq)
        cur_task_id = -cur_task_id
        print(
            cur_prio,
            cur_task_id,
            cur_user_id,
            "\n",
            self.curr_prios,
            "\n",
            self.task_user_mapping,
            "\n",
        )
        if (
            cur_task_id not in self.curr_prios
            or self.curr_prios[cur_task_id] != -cur_prio
            or self.task_user_mapping[cur_task_id] != cur_user_id
        ):
            return self.execTop()
        else:
            self.curr_prios.pop(cur_task_id)
            self.task_user_mapping.pop(cur_task_id)
            return cur_user_id


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()


def t1():
    instr = ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
    tasks = [
        [[[1, 101, 8], [2, 102, 20], [3, 103, 5]]],
        [4, 104, 5],
        [102, 9],
        [],
        [101],
        [50, 101, 8],
        [],
    ]
    obj = None
    for i, cmd in enumerate(instr):
        if obj is not None:
            print()
            print(obj.tq)
            None
        if cmd == "TaskManager":
            obj = TaskManager(*tasks[i])
            print(None)
        elif cmd == "add":
            param_1 = obj.add(*tasks[i])
            print(param_1)
        elif cmd == "edit":
            param_2 = obj.edit(*tasks[i])
            print(param_2)
        elif cmd == "rmv":
            param_3 = obj.rmv(*tasks[i])
            print(param_3)
        elif cmd == "execTop":
            param_4 = obj.execTop()
            print(param_4)


def t2():
    instr = ["TaskManager", "execTop"]
    tasks = [[[[4, 15, 33]]], []]
    obj = None
    for i, cmd in enumerate(instr):
        if obj is not None:
            print()
            print(obj.tq)
            None
        if cmd == "TaskManager":
            obj = TaskManager(*tasks[i])
            print(None)
        elif cmd == "add":
            param_1 = obj.add(*tasks[i])
            print(param_1)
        elif cmd == "edit":
            param_2 = obj.edit(*tasks[i])
            print(param_2)
        elif cmd == "rmv":
            param_3 = obj.rmv(*tasks[i])
            print(param_3)
        elif cmd == "execTop":
            param_4 = obj.execTop()
            print(param_4)


if __name__ == "__main__":
    t2()
