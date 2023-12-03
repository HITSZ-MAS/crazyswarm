function min_distance = drone_distance(file1, file2)
    % 步骤 1: 导入 CSV 文件
    data1 = readtable(file1);
    data2 = readtable(file2);

    % 步骤 2: 分离 X、Y 和 Z 轴数据
    X1 = data1.x;
    Y1 = data1.y;
    Z1 = data1.z;

    X2 = data2.x;
    Y2 = data2.y;
    Z2 = data2.z;

    % 初始化距离数组
    n1 = length(X1); % drone1 的点的总数
    n2 = length(X2); % drone2 的点的总数
    distances = zeros(min(n1, n2), 1); % 初始化距离数组，长度为 n1 和 n2 中的较小值

    % 计算两个无人机之间的距离
    for i = 1:min(n1, n2)
        dx = X2(i) - X1(i);
        dy = Y2(i) - Y1(i);
        dz = Z2(i) - Z1(i);
        distances(i) = sqrt(dx^2 + dy^2 + dz^2);
    end

    % 输出距离数组的最小值
    min_distance = min(distances);
end