import copy


# 进行初始环境的创建生成
class CliffWalkingEnv:

    # 定义行数和列数，以及一个转移矩阵
    def __init__(self, n_col=12, n_row=4):
        self.n_col = n_col
        self.n_row = n_row
        self.P = self.create_p()

    def create_p(self):
        # 列表为4 * 12 * 4的大小
        P = [[[] for j in range(4)] for i in range(self.n_row * self.n_col)]
        # 0是往上，2是往左
        change = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for i in range(self.n_row):
            for j in range(self.n_col):
                for a in range(4):
                    # 位置在悬崖边或者目标状态，将任何奖励都设为0
                    if i == self.n_row - 1 and j > 0:
                        P[i * self.n_col + j][a] = [(1, i * self.n_col + j, 0, True)]
                        continue
                    # 其余位置
                    next_x = min(self.n_col - 1, max(0, j + change[a][0]))
                    next_y = min(self.n_row - 1, max(0, i + change[a][1]))
                    next_state = next_y * self.n_col + next_x
                    reward = -1
                    done = False
                    # 下一个位置在悬崖边或者终点
                    if next_y == self.n_row - 1 and next_x > 0:
                        done = True
                        # 下一个位置在悬崖或者终点
                        if next_x != self.n_col - 1:
                            reward = -100
                    P[i * self.n_col + j][a] = [(1, next_state, reward, done)]
        return P


class PolicyIteration:
    def __init__(self, env, theta, gamma):
        self.env = env
        self.v = [0] * self.env.n_col * self.env.n_row  # 初始化价值为0
        # 初始化为均匀随机策略
        self.pi = [[0.25, 0.25, 0.25, 0.25] for i in range(self.env.n_col * self.env.n_row)]
        # 收敛
        self.theta = theta
        # 折扣因子
        self.gamma = gamma

    def policy_evaluation(self):  # 策略评估
        cnt = 1
        while 1:
            max_diff = 0
            new_v = [0] * self.env.n_col * self.env.n_row
            for s in range(self.env.n_col * self.env.n_row):
                qsa_list = []  # 开始计算状态下所有Q(s, a)价值
                for a in range(4):
                    qsa = 0
                    for res in self.env.P[s][a]:
                        p, next_state, r, done = res
                        # 计算奖励值
                        qsa += p * (r + self.gamma * self.v[next_state] * (1 - done))
                    qsa_list.append(self.pi[s][a] * qsa)
                new_v[s] = sum(qsa_list)
                max_diff = max(max_diff, abs(new_v[s] - self.v[s]))
            self.v = new_v
            if max_diff < self.theta:
                break
            cnt += 1
        print("策略评估进行%d轮后完成" % cnt)

    def policy_iteration(self):
        while 1:
            self.policy_evaluation()
            # 深拷贝
            old_pi = copy.deepcopy(self.pi)
            # 决策更新
            new_pi = self.policy_improvement()
            if old_pi == new_pi:
                break

    def policy_improvement(self):
        improvement(self)
        print("策略提升完成")
        return self.pi


# 用于策略提升
def improvement(agent):
    for s in range(agent.env.n_col * agent.env.n_row):
        qsa_list = qsa_list_append(agent, s)
        max_q = max(qsa_list)
        cnt_q = qsa_list.count(max_q)  # 计算达到最大q值的动作数量
        agent.pi[s] = [1 / cnt_q if q == max_q else 0 for q in qsa_list]


# 完善qsa_list填充方法
def qsa_list_append(agent, s):
    qsa_list = []
    for a in range(4):
        qsa = 0
        for res in agent.env.P[s][a]:
            p, next_state, r, done = res
            qsa += p * (r + agent.gamma * agent.v[next_state] * (1 - done))
        qsa_list.append(qsa)
    return qsa_list


class ValueIteration:
    def __init__(self, env, theta, gamma):
        self.env = env
        self.v = [0] * self.env.n_col * self.env.n_row
        self.theta = theta
        self.gamma = gamma
        self.pi = [None for i in range(self.env.n_col * self.env.n_row)]

    def value_iteration(self):
        cnt = 0
        while 1:
            max_diff = 0
            new_v = [0] * self.env.n_col * self.env.n_row
            for s in range(self.env.n_col * self.env.n_row):
                qsa_list = qsa_list_append(self, s)
                new_v[s] = max(qsa_list)
                max_diff = max(max_diff, abs(new_v[s] - self.v[s]))
            self.v = new_v
            if max_diff < self.theta:
                break
            cnt += 1
        print("价值迭代一共进行%d轮" % cnt)
        self.get_policy()

    def get_policy(self):
        improvement(self)


def print_agent(agent, action_meaning, disaster=None, end=None):
    if end is None:
        end = []
    if disaster is None:
        disaster = []
    print("状态价值： ")
    for i in range(agent.env.n_row):
        for j in range(agent.env.n_col):
            # 为了输出美观，保持输出6个字符
            print('%6.6s' % ('%.3f' % agent.v[i * agent.env.n_col + j]), end=' ')
        print()

    print("策略： ")
    for i in range(agent.env.n_row):
        for j in range(agent.env.n_col):
            # 特殊状态
            if (i * agent.env.n_col + j) in disaster:
                print("****", end=' ')
            elif (i * agent.env.n_col + j) in end:  # 目标状态
                print('EEEE', end=' ')
            else:
                a = agent.pi[i * agent.env.n_col + j]
                pi_str = ''
                for k in range(len(action_meaning)):
                    pi_str += action_meaning[k] if a[k] > 0 else 'o'
                print(pi_str, end=' ')
        print()


if __name__ == '__main__':
    env = CliffWalkingEnv()
    action_meaning = ['^', 'v', '<', '>']
    theta = 0.001
    gamma = 0.9
    agent = PolicyIteration(env, theta, gamma)
    agent.policy_iteration()
    # agent = ValueIteration(env, theta, gamma)
    # agent.value_iteration()
    print_agent(agent, action_meaning, list(range(37, 47)), [47])
