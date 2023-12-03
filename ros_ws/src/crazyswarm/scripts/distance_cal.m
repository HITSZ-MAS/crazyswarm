clear;
drone_files = {'drone1.csv', 'drone2.csv', 'drone3.csv', 'drone4.csv', 'drone5.csv', 'drone6.csv', 'drone0.csv'};

% 初始化最小距离
min_distance = Inf;

min_x = Inf;
max_x = -Inf;
min_y = Inf;
max_y = -Inf;

% 计算所有无人机之间的最小距离
for i = 1:length(drone_files)
    data = readtable(drone_files{i});
    min_x = min(min_x, min(data.x));
    max_x = max(max_x, max(data.x));
    min_y = min(min_y, min(data.y));
    max_y = max(max_y, max(data.y));
    for j = i+1:length(drone_files)
        distance = drone_distance(drone_files{i}, drone_files{j});
        fprintf('无人机 %d 和无人机 %d 之间的最小距离为: %.2f\n', i, j, distance);
        if distance < min_distance
            min_distance = distance;
            min_drones = [i, j];
        end
    end
end

fprintf('X 轴的最小值为: %.2f，最大值为: %.2f\n', min_x, max_x);
fprintf('Y 轴的最小值为: %.2f，最大值为: %.2f\n', min_y, max_y);

% 输出最小距离
fprintf('无人机 %d 和无人机 %d 之间的最小距离为: %.2f\n', min_drones(1), min_drones(2), min_distance);

% 障碍物列表
obstacles = [-2.7, 6.6; -0.96, 6.6; 1.56, 5.64; 1.26, 2.7; -1.9, 2.9];

for i = 1:length(drone_files)
    % 读取无人机数据
    data = readtable(drone_files{i});

    % 获取数据点的数量
    num_points = size(data, 1);

    % 构造时间序列，间隔为0.1s
    time = (0:0.05:(num_points-1)*0.05)';

    % 提取位置数据
    position = [data.x, data.y, data.z];

    % 计算速度
    % 使用差分方法计算速度
    dt = 0.05;  % 时间间隔
    velocity = [0 0 0; diff(position) / dt];  % 第一个速度值设为0

    % 创建图形
    figure;
    
    % 绘制位置图
    subplot(2, 1, 1);
    plot(time, position, 'LineWidth', 2);  % 增加线条宽度
    xlabel('Time [s]', 'FontWeight', 'bold', 'FontSize', 14);
    ylabel('Position [m]', 'FontWeight', 'bold', 'FontSize', 14examssx);
    title(sprintf('无人机 %d 的位置', i), 'FontWeight', 'bold', 'FontSize', 14);
    legend('V_x', 'V_y', 'V_z', 'FontWeight', 'bold', 'FontSize', 14, 'Orientation', 'horizontal');


    % 绘制速度图
    subplot(2, 1, 2);
    plot(time, velocity, 'LineWidth', 2);  % 增加线条宽度
    xlabel('Time [s]', 'FontWeight', 'bold', 'FontSize', 14);
    ylabel('Velocity [m/s]', 'FontWeight', 'bold', 'FontSize', 14);
    title(sprintf('无人机 %d 的速度', i), 'FontWeight', 'bold', 'FontSize', 14);
    legend('V_x', 'V_y', 'V_z', 'FontWeight', 'bold', 'FontSize', 14, 'Orientation', 'horizontal');


    % 保存图形
    saveas(gcf, sprintf('drone_%d.png', i));
end

