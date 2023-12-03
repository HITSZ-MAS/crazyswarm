function min_distance = ob_distance(file1, obstacle)
    % 步骤 1: 导入 CSV 文件
    data1 = readtable(file1);

    % 步骤 2: 分离 X 和 Y 轴数据
    X1 = data1.x;
    Y1 = data1.y;

    % 初始化距离数组
    n1 = length(X1); % drone1 的点的总数
    distances = zeros(n1, 1); % 初始化距离数组，长度为 n1

    % 计算无人机和障碍物之间的距离
    for i = 1:n1
        dx = obstacle(1) - X1(i);
        dy = obstacle(2) - Y1(i);
        distances(i) = sqrt(dx^2 + dy^2);
    end

    % 输出距离数组的最小值
    min_distance = min(distances);
end