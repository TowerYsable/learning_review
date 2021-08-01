# -*- coding: utf-8 -*-



class LSTM_NP():
    def __init__(self):
        # hyper-params
        self.H = 256 # LSTM 隐藏层维度
        self.D = 1000 # 输入数据的维度 == 词表的大小
        self.O = 10 # 输出层类别数目
        self.Z = H + D # 因为需要把LSTM的状态与输入数据拼接


        self.var = dict(
            Wf=np.random.randn(self.Z, self.H) / np.sqrt(self.Z / 2.),
            Wi=np.random.randn(self.Z, self.H) / np.sqrt(self.Z / 2.),
            Wc=np.random.randn(self.Z, self.H) / np.sqrt(self.Z / 2.),
            Wo=np.random.randn(self.Z, self.H) / np.sqrt(self.Z / 2.),
            Wy=np.random.randn(self.H, self.O) / np.sqrt(self.O / 2.),
            bf=np.zeros((1, self.H)),
            bi=np.zeros((1, self.H)),
            bc=np.zeros((1, self.H)),
            bo=np.zeros((1, self.H)),
            by=np.zeros((1, self.D))
        )


    def lstm_forward(self, X, state):
        m = self.var
        Wf, Wi, Wc, Wo, Wy = m['Wf'], m['Wi'], m['Wc'], m['Wo'], m['Wy']
        bf, bi, bc, bo, by = m['bf'], m['bi'], m['bc'], m['bo'], m['by']

        h_old, c_old = state

        # One-hot 编码
        X_one_hot = np.zeros(D)
        X_one_hot[X] = 1.
        X_one_hot = X_one_hot.reshape(1, -1)

        # 上一步状态与当前输入值连接
        X = np.column_stack((h_old, X_one_hot))
    　　hf = sigmoid(X @ Wf + bf)
        hi = sigmoid(X @ Wi + bi)
        ho = sigmoid(X @ Wo + bo)
        hc = tanh(X @ Wc + bc)

        c = hf * c_old + hi * hc
        h = ho * tanh(c)

        y = h @ Wy + by
        prob = softmax(y)

        cache = ... # 存储所有的中间变量结果

        return prob, (h, c), cache


    def lstm_backward(self, prob, y_train, state, cache):
        # 取出前向传播步骤中存储的中间状态变量
        ... = cache
        dh_next, dc_next = state

        # Softmax loss gradient
        dy = prob.copy()
        dy[0, y_train] -= 1.

        # 隐藏层到输出层的导数
        dWy = h.T @ dy
        dby = dy
        # 注意加上dh_next这一项
        dh = dy @ Wy.T + dh_next

        # h = ho * tanh(c)，计算ho的偏导数
        dho = tanh(c) * dh
        dho = dsigmoid(ho) * dho

        # h = ho * tanh(c), 计算c的偏导数
        dc = ho * dh * dtanh(c)
        dc = dc + dc_next

        # c = hf * c_old + hi * hc，计算hf的偏导数
        dhf = c_old * dc
        dhf = dsigmoid(hf) * dhf

        # c = hf * c_old + hi * hc，计算hi的偏导数
        dhi = hc * dc
        dhi = dsigmoid(hi) * dhi

        # c = hf * c_old + hi * hc，计算hc的偏导数
        dhc = hi * dc
        dhc = dtanh(hc) * dhc

        # 各个门的偏导数
        dWf = X.T @ dhf
        dbf = dhf
        dXf = dhf @ Wf.T

        dWi = X.T @ dhi
        dbi = dhi
        dXi = dhi @ Wi.T

        dWo = X.T @ dho
        dbo = dho
        dXo = dho @ Wo.T

        dWc = X.T @ dhc
        dbc = dhc
        dXc = dhc @ Wc.T

        # 由于X参与多个门的计算，因此偏导数需要累加
        dX = dXo + dXc + dXi + dXf
        # 计算h_old的偏导数
        dh_next = dX[:, :H]
        # c = hf * c_old + hi * hc，计算dc_next的偏导数
        dc_next = hf * dc

        grad = dict(Wf=dWf, Wi=dWi, Wc=dWc, Wo=dWo, Wy=dWy, bf=dbf, bi=dbi, bc=dbc, bo=dbo, by=dby)

        state_old = (dh_next, dc_next)

        return grad, state_old


    def train_step(self, X_train, y_train, state):
        probs = []
        caches = []
        loss = 0.
        h, c = state

        # 正向计算

        for x, y_true in zip(X_train, y_train):
            prob, state, cache = self.lstm_forward(x, state)
            loss += cross_entropy(prob, y_true)

            # 保存正向计算的结果
            probs.append(prob)
            caches.append(cache)

        # 损失值采用交叉熵
        loss /= X_train.shape[0]

        # 反向过程

        # 在最后一步， dh_next 和 dc_next 的值等于0
        state = (np.zeros_like(h), np.zeros_like(c))
        grads = {k: np.zeros_like(v) for k, v in self.var.items()}

        # 按照从后到前的时间顺序
        for prob, y_true, cache in reversed(list(zip(probs, y_train, caches))):
            grad, state = self.lstm_backward(prob, y_true, state, cache)

            # 累加各个步骤的梯度值
            for k in grads.keys():
                grads[k] += grad[k]

        return grads, loss, state